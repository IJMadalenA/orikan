#!/bin/sh

start_time=$(date +%s)
rcfile_path="./compose/coverage/.coveragerc"
SQL_HOST="localhost"
SQL_PORT=5432

# Check if the database is ready
echo "Waiting for database to be ready..."

while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
  sleep 0.5
done

echo "Database is ready, running tests now."

# NORMAL TEST SCAN.
coverage run --rcfile="${rcfile_path}" manage.py test --parallel --timing --noinput --force-color --verbosity=0

# REVERSE TEST SCAN.
coverage run --rcfile="${rcfile_path}" manage.py test --failfast --reverse --timing --noinput --force-color --verbosity=0

# COMBINING THE DATA FILES.
coverage combine -q --rcfile="${rcfile_path}"

# GENERATE THE REPORT.
# coverage report --rcfile="${rcfile_path}" --skip-covered --skip-empty

# GENERATE THE HTML FILES.
rm -fr compose/coverage/html_report
coverage html --quiet --directory=tesseract-vault/coverage/html_report --rcfile="${rcfile_path}"

# ERASE THE SQLite FILES.
coverage erase

# CALCULATE AND PRINT THE TOTAL EXECUTION TIME.
end_time=$(date +%s)
duration=$((end_time - start_time))
echo "Total execution time: $duration seconds"

exec "$@"
