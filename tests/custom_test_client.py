from typing import Any

from starlette.testclient import TestClient


class CustomTestClient:
    client = None

    def __init__(self, app):
        self.client = TestClient(app)

    def request(
            self,
            method: str,
            path: str,
            **kwargs: Any,
    ):
        return self.client.request(method, path, **kwargs)

    def get(self, path: str, expected_status=200, **kwargs: Any):
        resp = self.request("GET", path, **kwargs)
        assert resp.status_code == expected_status
        return resp

    def post(self, path: str, expected_status=200, **kwargs: Any):
        resp = self.request("POST", path, **kwargs)
        assert resp.status_code == expected_status
        return resp

    def put(self, path: str, expected_status=200, **kwargs: Any):
        resp = self.request("PUT", path, **kwargs)
        assert resp.status_code == expected_status
        return resp

    def patch(self, path: str, expected_status=200, **kwargs: Any):
        resp = self.request("PATCH", path, **kwargs)
        assert resp.status_code == expected_status
        return resp

    def delete(self, path: str, expected_status=200, **kwargs: Any):
        resp = self.request("DELETE", path, **kwargs)
        assert resp.status_code == expected_status
        return resp
