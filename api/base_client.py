from config.config import API_BASE_URL
from core.logger import logger

class BaseClient:
    def __init__(self, session):
        self.base_url =  API_BASE_URL.rstrip("/")
        self.session = session
        self.timeout = 10

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        logger.info(f"{method.upper()} {url}")

        if kwargs.get("json"):
            logger.info(f"Payload: {kwargs['json']}")

        kwargs.setdefault("timeout", self.timeout)

        response = self.session.request(method, url, **kwargs)

        logger.info(f"STATUS: {response.status_code}")
        logger.info(f"TIME: {response.elapsed.total_seconds():.3f}s")

        if response.status_code >= 500:
            logger.error(f"Server error: {response.status_code}")

        return response

    def get(self, endpoint, params=None):
        return self._request(
            method = "GET", 
            endpoint = endpoint,
            params = params)

    def post(self, endpoint, json=None):
        return self._request(
            method = "POST", 
            endpoint = endpoint,
            json = json)

    def put(self, endpoint, json=None):
        return self._request(
            method = "PUT", 
            endpoint = endpoint,
            json = json)
    
    def patch(self, endpoint, json=None):
        return self._request(
            method = "PATCH", 
            endpoint = endpoint,
            json = json)

    def delete(self, endpoint, params=None):
        return self._request(
            method = "DELETE", 
            endpoint = endpoint,
            params = params)