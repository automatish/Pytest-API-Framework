import pytest
from utils.logger import logger


@pytest.fixture(scope="module", autouse=True)
def log_test_class_name(request):
    # This fixture logs the test class name before the run
    logger.info(f"Running tests from: {request.node.name}")
    yield
    logger.info(f"Test Run Complete for : {request.node.name}")


@pytest.fixture(scope="function", autouse=True)
def log_test_name(request):
    # This fixture logs the test name before the test
    logger.info(f"Running test: {request.node.name}")
