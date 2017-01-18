import alembic.op
import csv
import metadata.type
import pkg_resources
import sqlalchemy

branch_labels = None

depends_on = None

down_revision = "294ae64fd33c"

revision = "739d53a9c2cc"


def populate(pathname, table):
    pathname = pkg_resources.resource_filename("metadata", pathname)

    with open(pathname) as data:
        records = list(csv.DictReader(data))

        alembic.op.bulk_insert(table, records, multiinsert=False)


def upgrade():
    channels = sqlalchemy.sql.table(
        "channels",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("image_id", metadata.type.UUID)
    )

    experiments = sqlalchemy.sql.table(
        "experiments",
        sqlalchemy.sql.column("id", metadata.type.UUID)
    )

    imageable = sqlalchemy.sql.table(
        "imageable",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("type", sqlalchemy.String)
    )

    images = sqlalchemy.sql.table(
        "images",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("imageable_id", metadata.type.UUID)
    )

    plates = sqlalchemy.sql.table(
        "plates",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("experiment_id", metadata.type.UUID)
    )

    stainable = sqlalchemy.sql.table(
        "stainable",
        sqlalchemy.sql.column("channel_id", metadata.type.UUID),
        sqlalchemy.sql.column("stain_id", metadata.type.UUID)
    )

    stains = sqlalchemy.sql.table(
        "stains",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("name", sqlalchemy.String)
    )

    wells = sqlalchemy.sql.table(
        "wells",
        sqlalchemy.sql.column("id", metadata.type.UUID),
        sqlalchemy.sql.column("plate_id", metadata.type.UUID),
        sqlalchemy.sql.column("x", sqlalchemy.String),
        sqlalchemy.sql.column("y", sqlalchemy.String)
    )

    populate("data/channels.csv", channels)

    populate("data/experiments.csv", experiments)

    populate("data/imageable.csv", imageable)

    populate("data/images.csv", images)

    populate("data/plates.csv", plates)

    populate("data/stainable.csv", stainable)

    populate("data/stains.csv", stains)

    populate("data/wells.csv", wells)


def downgrade():
    pass
