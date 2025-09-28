from flask.testing import FlaskClient
from pkg.response import HttpCode

class TestAppHandler:

    def test_completion(self, clinet: FlaskClient):
        response = clinet.post("/app/completion", json={"query": "ni hao ni shi?"})
        print("相应内容：", response.json)
        assert response.status_code == 200
        assert response.json.get("code") == HttpCode.SUCCESS
        