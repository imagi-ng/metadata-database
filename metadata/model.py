import metadata.type
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


@sqlalchemy.ext.declarative.as_declarative()
class Base(object):
    id = sqlalchemy.Column(metadata.type.UUID, primary_key=True)


class Annotation(Base):
    __tablename__ = "annotations"

    annotator_id = sqlalchemy.Column(sqlalchemy.ForeignKey("annotators.id"))

    category_id = sqlalchemy.Column(sqlalchemy.ForeignKey("categories.id"))

    channel_id = sqlalchemy.Column(sqlalchemy.ForeignKey("channels.id"))


class Annotator(Base):
    __tablename__ = "annotators"

    annotations = sqlalchemy.orm.relationship("Annotation", backref="annotator")

    token = sqlalchemy.Column(sqlalchemy.String(255))


class Category(Base):
    __tablename__ = "categories"

    annotations = sqlalchemy.orm.relationship("Annotation", backref="category")

    description = sqlalchemy.Column(sqlalchemy.String(255))


class Channel(Base):
    __tablename__ = "channels"

    annotations = sqlalchemy.orm.relationship("Annotation", backref="channel")

    image_id = sqlalchemy.Column(sqlalchemy.ForeignKey("images.id"))

    stains = sqlalchemy.orm.relationship("Stain", secondary="stainable", backref="channel")


class Experiment(Base):
    __tablename__ = "experiments"


class Image(Base):
    __tablename__ = "images"

    imageable_id = sqlalchemy.Column(sqlalchemy.ForeignKey("imageable.id"))

    imageable = sqlalchemy.orm.relationship("Imageable", backref="images")

    channels = sqlalchemy.orm.relationship("Channel", backref="image")


class Imageable(Base):
    __tablename__ = "imageable"

    type = sqlalchemy.Column(sqlalchemy.String(36))

    __mapper_args__ = {
        "polymorphic_identity": "imageable",
        "polymorphic_on": type
    }


class Plate(Base):
    __tablename__ = "plates"

    experiment_id = sqlalchemy.Column(sqlalchemy.ForeignKey("experiments.id"))

    channels = sqlalchemy.orm.relationship("Well", backref="plate")


class Slide(Imageable):
    __tablename__ = "slides"

    id = sqlalchemy.Column(metadata.type.UUID, sqlalchemy.ForeignKey("imageable.id"), primary_key=True)

    experiment_id = sqlalchemy.Column(sqlalchemy.ForeignKey("experiments.id"))

    __mapper_args__ = {
        "polymorphic_identity": "slides",
    }


class Stain(Base):
    __tablename__ = "stains"

    name = sqlalchemy.Column(sqlalchemy.String(255))


class Stainable(Base):
    __tablename__ = "stainable"

    channel_id = sqlalchemy.Column(metadata.type.UUID, sqlalchemy.ForeignKey("channels.id"))

    stain_id = sqlalchemy.Column(metadata.type.UUID, sqlalchemy.ForeignKey("stains.id"))


class Well(Imageable):
    __tablename__ = "wells"

    id = sqlalchemy.Column(metadata.type.UUID, sqlalchemy.ForeignKey("imageable.id"), primary_key=True)

    plate_id = sqlalchemy.Column(sqlalchemy.ForeignKey("plates.id"))

    x = sqlalchemy.Column(sqlalchemy.String(255))

    y = sqlalchemy.Column(sqlalchemy.String(255))

    __mapper_args__ = {
        "polymorphic_identity": "wells",
    }
