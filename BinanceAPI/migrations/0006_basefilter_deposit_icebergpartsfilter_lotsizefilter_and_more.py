# Generated by Django 4.2.1 on 2023-07-20 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("BinanceAPI", "0005_candlestick_avgprice_avgprice_unique_symbol_mins"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseFilter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Fecha y hora de actualización"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Fecha y hora de creación"
                    ),
                ),
                (
                    "filter_type",
                    models.CharField(
                        choices=[
                            ("PRICE_FILTER", "PRICE_FILTER"),
                            ("PERCENT_PRICE", "PERCENT_PRICE"),
                            ("PERCENT_PRICE_BY_SIDE", "PERCENT_PRICE_BY_SIDE"),
                            ("LOT_SIZE", "LOT_SIZE"),
                            ("MIN_NOTIONAL", "MIN_NOTIONAL"),
                            ("NOTIONAL", "NOTIONAL"),
                            ("ICEBERG_PARTS", "ICEBERG_PARTS"),
                            ("MARKET_LOT_SIZE", "MARKET_LOT_SIZE"),
                            ("MAX_NUM_ORDERS", "MAX_NUM_ORDERS"),
                            ("MAX_NUM_ALGO_ORDERS", "MAX_NUM_ALGO_ORDERS"),
                            ("MAX_NUM_ICEBERG_ORDERS", "MAX_NUM_ICEBERG_ORDERS"),
                            ("MAX_POSITION", "MAX_POSITION"),
                            ("TRAILING_DELTA", "TRAILING_DELTA"),
                            ("EXCHANGE_MAX_NUM_ORDERS", "EXCHANGE_MAX_NUM_ORDERS"),
                            ("EXCHANGE_MAX_ALGO_ORDERS", "EXCHANGE_MAX_ALGO_ORDERS"),
                            (
                                "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",
                                "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",
                            ),
                        ],
                        help_text="Tipo de filtro",
                        max_length=35,
                    ),
                ),
                (
                    "symbol",
                    models.ForeignKey(
                        editable=False,
                        help_text="Símbolo del par de trading",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="BinanceAPI.symbol",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Deposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Fecha y hora de actualización"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Fecha y hora de creación"
                    ),
                ),
                (
                    "deposit_id",
                    models.CharField(
                        editable=False,
                        help_text="ID de depósito",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad depositada",
                        max_digits=20,
                    ),
                ),
                (
                    "asset",
                    models.CharField(editable=False, help_text="Activo", max_length=10),
                ),
                (
                    "address",
                    models.CharField(
                        editable=False,
                        help_text="Dirección de depósito",
                        max_length=100,
                    ),
                ),
                (
                    "tx_id",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="ID de transacción",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                        ],
                        editable=False,
                        help_text="Estado del depósito",
                        max_length=10,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        editable=False, help_text="Fecha y hora del depósito"
                    ),
                ),
                (
                    "confirmations",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Número de confirmaciones",
                        null=True,
                    ),
                ),
                (
                    "fee",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Tarifa de depósito",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "tx_hash",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Hash de la transacción",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Deposit",
                "verbose_name_plural": "Deposits",
            },
        ),
        migrations.CreateModel(
            name="IcebergPartsFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "limit",
                    models.IntegerField(
                        blank=True, editable=False, help_text="Límite", null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Iceberg Parts",
                "verbose_name_plural": "Filtros de Iceberg Parts",
                "db_table": "iceberg_parts_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="LotSizeFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_qty",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad mínima",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "max_qty",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad máxima",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "step_size",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Tamaño del paso",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Tamaño de Lote",
                "verbose_name_plural": "Filtros de Tamaño de Lote",
                "db_table": "lot_size_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="MarketLotSizeFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_qty",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad mínima",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "max_qty",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Cantidad máxima",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "step_size",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Tamaño del paso",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Market Lot Size",
                "verbose_name_plural": "Filtros de Market Lot Size",
                "db_table": "market_lot_size_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="MaxNumAlgoOrdersFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "max_num_algo_orders",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Máximo número de órdenes de Algo",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Máximo Número de Órdenes de Algo",
                "verbose_name_plural": "Filtros de Máximo Número de Órdenes de Algo",
                "db_table": "max_num_algo_orders_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="MaxNumIcebergOrdersFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "max_num_iceberg_orders",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Máximo número de órdenes de Iceberg",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Máximo Número de Órdenes de Iceberg",
                "verbose_name_plural": "Filtros de Máximo Número de Órdenes de Iceberg",
                "db_table": "max_num_iceberg_orders_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="MaxPositionFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "max_position",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Posición máxima",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Posición Máxima",
                "verbose_name_plural": "Filtros de Posición Máxima",
                "db_table": "max_position_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="MinNotionalFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_notional",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Mínimo notional",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "apply_to_market",
                    models.BooleanField(
                        default=False, editable=False, help_text="Aplicar al mercado"
                    ),
                ),
                (
                    "avg_price_mins",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Minutos de precio promedio",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Mínimo Notional",
                "verbose_name_plural": "Filtros de Mínimo Notional",
                "db_table": "min_notional_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="NotionalFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_notional",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Mínimo notional",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "apply_min_to_market",
                    models.BooleanField(
                        default=False,
                        editable=False,
                        help_text="Aplicar mínimo al mercado",
                    ),
                ),
                (
                    "max_notional",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Máximo notional",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "apply_max_to_market",
                    models.BooleanField(
                        default=False, editable=False, help_text="Aplicar al mercado"
                    ),
                ),
                (
                    "avg_price_mins",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Minutos de precio promedio",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Notional",
                "verbose_name_plural": "Filtros de Notional",
                "db_table": "notional_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="PercentPriceBySideFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "bid_multiplier_up",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Multiplicador de precio hacia arriba",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "bid_multiplier_down",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Multiplicador de precio hacia abajo",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "ask_multiplier_up",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Multiplicador de precio hacia arriba",
                        null=True,
                    ),
                ),
                (
                    "ask_multiplier_down",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Multiplicador de precio hacia abajo",
                        null=True,
                    ),
                ),
                (
                    "avg_price_mins",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Minutos de precio promedio",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Porcentaje de Precio",
                "verbose_name_plural": "Filtros de Porcentaje de Precio",
                "db_table": "percent_price_by_side_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="PercentPriceFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "multiplier_up",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Multiplicador de precio hacia arriba",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "multiplier_down",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Multiplicador de precio hacia abajo",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "avg_price_mins",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Minutos de precio promedio",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Porcentaje de Precio",
                "verbose_name_plural": "Filtros de Porcentaje de Precio",
                "db_table": "percent_price_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="PriceFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Precio mínimo",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "max_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Precio máximo",
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "tick_size",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        editable=False,
                        help_text="Tamaño del tick",
                        max_digits=20,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Precio",
                "verbose_name_plural": "Filtros de Precio",
                "db_table": "price_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
        migrations.CreateModel(
            name="TrailingDeltaFilter",
            fields=[
                (
                    "basefilter_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BinanceAPI.basefilter",
                    ),
                ),
                (
                    "min_trailing_above_delta",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Mínimo trailing delta",
                        null=True,
                    ),
                ),
                (
                    "max_trailing_above_delta",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Máximo trailing delta",
                        null=True,
                    ),
                ),
                (
                    "min_trailing_below_delta",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Mínimo trailing delta",
                        null=True,
                    ),
                ),
                (
                    "max_trailing_below_delta",
                    models.IntegerField(
                        blank=True,
                        editable=False,
                        help_text="Máximo trailing delta",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Filtro de Trailing Stop Percent",
                "verbose_name_plural": "Filtros de Trailing Stop Percent",
                "db_table": "trailing_stop_percent_filter",
            },
            bases=("BinanceAPI.basefilter",),
        ),
    ]