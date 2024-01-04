import pytest
import utils.commonMethods as commonMethods
from utils import assertions
from resources.request_payloads import update_post_payload


@pytest.mark.usefixtures("log_test_class_name", "log_test_name")
class TestUpdateOperation:

    def test_delete_resource(self):
        post_id = update_post_payload()[1].get("id")
        response = commonMethods.delete_resource(path_param={"id": post_id})
        assertions.assert_delete_post(response=response)

    def test_invalid_invalid_resource_request(self):
        response = commonMethods.delete_resource(path_param={"id": ""})
        assertions.assert_invalid_delete_post_request(response=response)
