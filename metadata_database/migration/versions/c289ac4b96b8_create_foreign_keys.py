import alembic.op

branch_labels = None

depends_on = None

down_revision = "739d53a9c2cc"

revision = "c289ac4b96b8"


def create_foreign_key(source, destination, name):
    alembic.op.create_foreign_key(None, source, destination, [name], ["id"])


def upgrade():
    create_foreign_key("channels", "images", "image_id")

    create_foreign_key("images", "imageable", "imageable_id")

    create_foreign_key("plates", "experiments", "experiment_id")

    create_foreign_key("stainable", "channels", "channel_id")

    create_foreign_key("stainable", "stains", "stain_id")

    create_foreign_key("wells", "plates", "plate_id")


def downgrade():
    pass
