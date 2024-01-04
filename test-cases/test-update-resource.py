import pytest
import utils.commonMethods as commonMethods
from utils import assertions
from resources.request_payloads import update_post_payload


@pytest.mark.usefixtures("log_test_class_name", "log_test_name")
class TestUpdateOperation:

    def test_update_resource(self):
        post_id = update_post_payload()[1].get("id")
        response = commonMethods.update_resource(path_param={"id": post_id}, payload=update_post_payload()[0])
        assertions.assert_update_post_request(response=response, testdata=update_post_payload()[0])

    def test_invalid_update_resource(self):
        response = commonMethods.update_resource(path_param={"id": ""}, payload=update_post_payload()[0])
        assertions.assert_invalid_update_post_request(response=response)
