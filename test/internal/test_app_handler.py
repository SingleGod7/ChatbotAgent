from flask.testing import FlaskClient
from pkg.response import HttpCode
import pytest

class TestAppHandler:
    @pytest.mark.parametrize("query", [None, "请给我讲一个冷笑话"])
    def test_completion(self, clinet: FlaskClient, query):
        response = clinet.post("/app/completion", json={"query": query})
        print("相应内容：", response.json)
        assert response.status_code == 200
        if query == None:
            assert response.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert response.json.get("code") == HttpCode.SUCCESS
        