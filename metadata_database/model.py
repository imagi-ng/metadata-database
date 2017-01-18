import metadata_database.type


class Base(metadata_database.database.Model):
    __abstract__ = True

    id = metadata_database.database.Column(
        metadata_database.type.UUID,
        primary_key=True
    )


class Annotation(Base):
    __tablename__ = "annotations"

    annotator_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("annotators.id")
    )

    category_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("categories.id")
    )

    channel_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("channels.id")
    )


class Annotator(Base):
    __tablename__ = "annotators"

    annotations = metadata_database.database.relationship(
        "Annotation",
        backref="annotator"
    )

    token = metadata_database.database.Column(
        metadata_database.database.String(255)
    )


class Category(Base):
    __tablename__ = "categories"

    annotations = metadata_database.database.relationship(
        "Annotation",
        backref="category"
    )

    description = metadata_database.database.Column(
        metadata_database.database.String(255)
    )


class Channel(Base):
    __tablename__ = "channels"

    annotations = metadata_database.database.relationship(
        "Annotation",
        backref="channel"
    )

    image_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("images.id")
    )

    stains = metadata_database.database.relationship(
        "Stain",
        secondary="stainable",
        backref="channel"
    )


class Experiment(Base):
    __tablename__ = "experiments"


class Image(Base):
    __tablename__ = "images"

    imageable_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("imageable.id")
    )

    imageable = metadata_database.database.relationship(
        "Imageable",
        backref="images"
    )

    channels = metadata_database.database.relationship(
        "Channel",
        backref="image"
    )


class Imageable(Base):
    __tablename__ = "imageable"

    type = metadata_database.database.Column(
        metadata_database.database.String(36)
    )

    __mapper_args__ = {
        "polymorphic_identity": "imageable",
        "polymorphic_on": type
    }


class Plate(Base):
    __tablename__ = "plates"

    experiment_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("experiments.id")
    )

    channels = metadata_database.database.relationship(
        "Well",
        backref="plate"
    )


class Slide(Imageable):
    __tablename__ = "slides"

    id = metadata_database.database.Column(
        metadata_database.type.UUID,
        metadata_database.database.ForeignKey("imageable.id"),
        primary_key=True
    )

    experiment_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("experiments.id")
    )

    __mapper_args__ = {
        "polymorphic_identity": "slides",
    }


class Stain(Base):
    __tablename__ = "stains"

    name = metadata_database.database.Column(
        metadata_database.database.String(255)
    )


class Stainable(Base):
    __tablename__ = "stainable"

    channel_id = metadata_database.database.Column(
        metadata_database.type.UUID,
        metadata_database.database.ForeignKey("channels.id")
    )

    stain_id = metadata_database.database.Column(
        metadata_database.type.UUID,
        metadata_database.database.ForeignKey("stains.id")
    )


class Well(Imageable):
    __tablename__ = "wells"

    id = metadata_database.database.Column(
        metadata_database.type.UUID,
        metadata_database.database.ForeignKey("imageable.id"),
        primary_key=True
    )

    plate_id = metadata_database.database.Column(
        metadata_database.database.ForeignKey("plates.id")
    )

    x = metadata_database.database.Column(
        metadata_database.database.String(255)
    )

    y = metadata_database.database.Column(
        metadata_database.database.String(255)
    )

    __mapper_args__ = {
        "polymorphic_identity": "wells",
    }
