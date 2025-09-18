import pytest
from dotenv import load_dotenv
from faker import Faker
from pytest_mock import MockerFixture

load_dotenv(".env.test", override=True)


def pytest_addoption(parser):
    parser.addoption(
        "--sqlecho",
        action="store_true",
        default=False,
        help="Show SQLAlchemy SQL echo",
    )

    parser.addoption(
        "--not-skip",
        action="store_true",
        default=False,
        help="Use this parameter to run skipped tests",
    )


@pytest.fixture
def faker() -> Faker:
    return Faker()


@pytest.fixture(scope="session")
def sqlecho(request) -> bool:
    return request.config.getoption("--sqlecho")
