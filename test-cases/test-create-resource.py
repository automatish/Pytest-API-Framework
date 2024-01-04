import pytest
import utils.commonMethods as commonMethods
from utils import assertions
from resources.request_payloads import create_post_payload


@pytest.mark.usefixtures("log_test_class_name", "log_test_name")
class TestCreateOperation:

    def test_create_resource(self):
        response = commonMethods.create_resource(payload=create_post_payload())
        assertions.assert_post_creation(response=response, testdata=create_post_payload())
