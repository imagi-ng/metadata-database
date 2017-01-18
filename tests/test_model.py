import metadata_database.model
import uuid


def test_image():
    identifier = "0e4e8d3c-95d2-4447-a912-d7e1be04a27a"

    image = metadata_database.model.Image.query.get(identifier)

    assert uuid.UUID(identifier) == image.id
