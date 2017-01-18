import pytest
import sqlalchemy
import sqlalchemy.orm


@pytest.fixture()
def engine():
    endpoint = "mysql+cymysql://root:@127.0.0.1/metadata"

    return sqlalchemy.create_engine(endpoint)


@pytest.fixture()
def session(engine):
    return sqlalchemy.orm.sessionmaker(engine)()
