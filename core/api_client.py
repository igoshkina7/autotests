import requests
from core.logger import logger


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        logger.info(f"{method.upper()} {url}")

        if kwargs.get("json"):
            logger.info(f"Payload: {kwargs['json']}")

        response = requests.request(method, url, **kwargs)

        logger.info(f"STATUS: {response.status_code}")
        logger.info(f"TIME: {response.elapsed.total_seconds():.3f}s")

        if response.status_code >= 500:
            logger.error(f"Server error: {response.status_code}")

        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)