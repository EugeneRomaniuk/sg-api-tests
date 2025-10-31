from requests import Response


class Pagination:
    def __init__(self, api_client):
        self.client = api_client

    def get_resource_list(self, endpoint: str, limit: int = None, offset: int = None) -> Response:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self.client.get(endpoint, params=params)
