import metadata.model
import uuid


def test_image(session):
    identifier = "0e4e8d3c-95d2-4447-a912-d7e1be04a27a"

    image = session.query(metadata.model.Image).get(identifier)

    assert uuid.UUID(identifier) == image.id
