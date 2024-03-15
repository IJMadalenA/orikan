ARG PYTHON_IMAGE=python:3.13.0a4-alpine
ARG BUILD_ENVIRONMENT=production
ARG HOME_DIR=/home/orikan/

# PULL OFFICIAL PYTHON:ALPINE BASE IMAGE.
FROM ${PYTHON_IMAGE} as builder

LABEL authors="ijmadalena"

# SET WORK DIRECTORY.
# https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR /home/orikan/

# SET ENVIRONMENT VARIABLES.
# https://docs.python.org/3/using/cmdline.html#command-line-and-environment
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# UPDATE & UPGRADE PACKAGES IN THE SYSTEM.
# https://pkgs.alpinelinux.org/packages
RUN apk update && \
    apk add --no-cache -U gcc g++ libstdc++ musl-dev && \
    apk upgrade && \
    pip install poetry && \
    pip install --upgrade pip wheel

# COPY THE PROJECT REQUIREMENTS.
# https://docs.docker.com/engine/reference/builder/#copy
COPY pyproject.toml poetry.lock* ./

# GENERATE A PRECOMPILED FILE OF EACH OF THE PACKAGES REQUIRED IN THE SYSTEM.
# THAT HELP US TO SAVE SPACE AND IMPRUVE THE PERFORMANCE OF THE FINAL IMAGE.
RUN poetry lock && \
    poetry lock --check && \
    poetry self update && \
    poetry export --without-hashes -f requirements.txt > requirements.txt && \
    pip wheel --no-cache-dir --wheel-dir ./wheels -r ./requirements.txt

#######################################################################################################################
################################################## THE FINAL STAGE. ###################################################
# These are the steps that build the definitive image.
# Try to keep the image simple and light.
#######################################################################################################################

# PULL OFFICIAL PYTHON:ALPINE BASE IMAGE.
FROM ${PYTHON_IMAGE}

# CREATE DIRECTORY FOR THE NARYA USER.
RUN mkdir -p home/orikan/

# SET WORKING DIRECTORY.
WORKDIR ${HOME_DIR}

# SET ENVIRONMENT VARIABLES.
# https://docs.python.org/3/using/cmdline.html#command-line-and-environment
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 BUILD_ENV=${BUILD_ENVIRONMENT}

# CREATE THE "NARYA" USER & THE APPROPRIATE DIRECTORIES.
RUN addgroup -S orikan &&  \
    adduser -S orikan -G orikan && \
    mkdir -p /home/orikan/static && \
    mkdir -p /home/orikan/media

# UPDATE & UPGRADE PACKAGES IN THE SYSTEM.
# https://pkgs.alpinelinux.org/packages
RUN apk update && \
    apk add --no-cache -U libpq libstdc++ && \
    apk upgrade && \
    apk del --purge

COPY --from=builder home/orikan/wheels /wheels

RUN pip install --upgrade pip wheel && \
    pip cache purge && \
    pip install --no-cache -U /wheels/* && \
    rm -fR /wheels

## COPY THE ENTIRE PROJECT.
## https://docs.docker.com/engine/reference/builder/#copy
COPY ./ ./

########## RUN TESTS & Q.A. ##########
RUN python manage.py test --timing --noinput && \
#    flake8 --ignore=E501,F401 . && \
    sed -i 's/\r$//g' ./tesseract-vault/entrypoint.sh && \
    chmod +x ./tesseract-vault/entrypoint.sh && \
    chown -R orikan:orikan home/orikan/

# CHANGE TO THE NARYA USER.
USER orikan

# RUN entrypoint.sh
ENTRYPOINT ["./tesseract-vault/entrypoint.sh"]
