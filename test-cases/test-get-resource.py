import pytest
import utils.commonMethods as commonMethods
from utils import assertions
from utils.read_test_data import inject_test_data


@pytest.mark.usefixtures("log_test_class_name", "log_test_name")
class TestGetOperation:
    test_data = inject_test_data(file="resources/test_data.json")

    def test_read_all_posts(self):
        response = commonMethods.get_resource()
        assertions.assert_get_post_request(response)

    @pytest.mark.parametrize("testdata", test_data.happyPath)
    def test_read_single_post_with_id(self, testdata):
        response = commonMethods.get_resource(path_param={'id': testdata.id})
        assertions.assert_get_post_request(response)

    @pytest.mark.parametrize("testdata", test_data.happyPath)
    def test_read_single_post_with_userid(self, testdata):
        response = commonMethods.get_resource(query_param={'userId': testdata.userId})
        assertions.assert_get_post_request(response)

    @pytest.mark.parametrize("testdata", test_data.happyPath)
    def test_read_single_post_with_title(self, testdata):
        response = commonMethods.get_resource(query_param={'title': testdata.title})
        assertions.assert_get_post_request(response)

    @pytest.mark.parametrize("testdata", test_data.negativeTest)
    def test_read_post_with_invalid_id(self, testdata):
        response = commonMethods.get_resource(path_param={'id': testdata.id})
        assertions.assert_invalid_get_request(response)
