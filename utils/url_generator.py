def generate_url(base_url, path_params=None, query_params=None):
    """
    Generate a URL based on the provided base URL, path parameters, and query parameters.

    Parameters:
    - base_url (str): The base URL of the API.
    - path_params (dict): Dictionary of path parameters.
    - query_params (dict): Dictionary of query parameters.

    Returns:
    - The generated URL.
    """
    url = base_url.rstrip('/')  # Remove trailing slash from the base URL

    # Append path parameters to the URL
    if path_params:
        for key, value in path_params.items():
            url += f'/{value}'

    # Append query parameters to the URL
    if query_params:
        url += '?' + '&'.join([f'{key}={value}' for key, value in query_params.items()])

    return url
