import json

import requests
import resources.resource_urls as resource_urls
from utils.logger import logger
from utils import url_generator


def create_resource(payload):
    """ Method to create a Post request """
    request_url = resource_urls.BASE_URL + resource_urls.ENDPOINT
    response = requests.post(resource_urls.BASE_URL + resource_urls.ENDPOINT, json=payload)

    logger.info("URL is: {}".format(request_url))
    logger.info("Payload is: {}".format(str(json.dumps(payload, indent=2))))
    logger.info(f"Response code is: {response.status_code}")

    return response


def get_resource(path_param=None, query_param=None):
    """ Method to create a Get request """
    base_url = resource_urls.BASE_URL + resource_urls.ENDPOINT

    request_url = url_generator.generate_url(base_url=base_url, path_params=path_param, query_params=query_param)
    response = requests.get(request_url)

    logger.info("URL is: {}".format(request_url))
    logger.info(f"Response code is: {response.status_code}")

    return response


def update_resource(path_param, payload):
    """ Method to create an Update request """
    base_url = resource_urls.BASE_URL + resource_urls.ENDPOINT

    request_url = url_generator.generate_url(base_url=base_url, path_params=path_param)
    response = requests.put(request_url, payload)

    logger.info("URL is: {}".format(request_url))
    logger.info("Payload is: {}".format(str(json.dumps(payload, indent=2))))
    logger.info(f"Response code is: {response.status_code}")

    return response


def delete_resource(path_param):
    """ Method to create a delete request """
    base_url = resource_urls.BASE_URL + resource_urls.ENDPOINT

    request_url = url_generator.generate_url(base_url=base_url, path_params=path_param)
    response = requests.delete(request_url)

    logger.info("URL is: {}".format(request_url))
    logger.info(f"Response code is: {response.status_code}")

    return response
