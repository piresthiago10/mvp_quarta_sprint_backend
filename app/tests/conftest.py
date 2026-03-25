import pytest
from main import create_app
from database.database import db
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()

        yield db

        db.session.remove()
        db.drop_all()
