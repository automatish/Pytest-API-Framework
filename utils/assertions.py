from utils.logger import logger
import json

""" Methods for assertions can be found here"""


def assert_post_creation(response, testdata):
    assert response.status_code == 201
    logger.info(f"Response is: \n {str(json.dumps(response.json(), indent=2))}")

    response_body = response.json()
    assert response_body.get("body") == testdata.get("body")
    assert response_body.get("title") == testdata.get("title")
    assert response_body.get("userId") == testdata.get("userId")
    assert response_body.get("id") is not None


def assert_invalid_post_creation(response):
    assert response.status_code == 500
    logger.info(f"Response is: {response.text}")


def assert_get_post_request(response):
    assert response.status_code == 200
    logger.info(f"Response is: \n{str(json.dumps(response.json(), indent=2))}")


def assert_invalid_get_request(response):
    assert response.status_code == 404
    logger.info("Invalid Get request")


def assert_update_post_request(response, testdata):
    assert response.status_code == 200
    logger.info(f"Response is: \n {str(json.dumps(response.json(), indent=2))}")

    response_body = response.json()
    assert response_body.get("body") == testdata.get("body")
    assert response_body.get("title") == testdata.get("title")
    assert int(response_body.get("userId")) == testdata.get("userId")


def assert_invalid_update_post_request(response):
    assert response.status_code == 404
    logger.info("Invalid Update request")


def assert_delete_post(response):
    assert response.status_code == 200
    logger.info("Post deleted successfully")


def assert_invalid_delete_post_request(response):
    assert response.status_code == 404
    logger.info("No post found to be deleted")
