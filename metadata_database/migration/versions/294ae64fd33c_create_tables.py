import alembic.op
import metadata_database.type
import sqlalchemy

branch_labels = None

depends_on = None

down_revision = None

revision = "294ae64fd33c"


def upgrade():
    alembic.op.create_table(
        "annotations",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("annotator_id", metadata_database.type.UUID),
        sqlalchemy.Column("category_id", metadata_database.type.UUID),
        sqlalchemy.Column("channel_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "annotators",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("token", sqlalchemy.String(255))
    )

    alembic.op.create_table(
        "categories",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("description", sqlalchemy.String(255))
    )

    alembic.op.create_table(
        "channels",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("image_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "experiments",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True)
    )

    alembic.op.create_table(
        "imageable",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("type", sqlalchemy.String(255))
    )

    alembic.op.create_table(
        "images",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("imageable_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "plates",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("experiment_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "slides",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("experiment_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "stainable",
        sqlalchemy.Column("channel_id", metadata_database.type.UUID),
        sqlalchemy.Column("stain_id", metadata_database.type.UUID)
    )

    alembic.op.create_table(
        "stains",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String(255))
    )

    alembic.op.create_table(
        "wells",
        sqlalchemy.Column("id", metadata_database.type.UUID, primary_key=True),
        sqlalchemy.Column("plate_id", metadata_database.type.UUID),
        sqlalchemy.Column("x", sqlalchemy.String(255)),
        sqlalchemy.Column("y", sqlalchemy.String(255))
    )


def downgrade():
    alembic.op.drop_table("annotations")

    alembic.op.drop_table("annotators")

    alembic.op.drop_table("categories")

    alembic.op.drop_table("channels")

    alembic.op.drop_table("experiments")

    alembic.op.drop_table("imageable")

    alembic.op.drop_table("images")

    alembic.op.drop_table("plates")

    alembic.op.drop_table("slides")

    alembic.op.drop_table("stainable")

    alembic.op.drop_table("stains")

    alembic.op.drop_table("wells")
