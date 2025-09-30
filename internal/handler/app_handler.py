from flask import request
import os
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response.response import success_json, fail_json, validation_error_json, success_message

from internal.exception.exception import FailException

from dataclasses import dataclass
from injector import inject
from internal.service import AppService
import uuid
@inject
@dataclass
class AppHandler():
    """应用处理器"""
    app_service : AppService

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"应用创建成功，id为{app.id}")
    
    def get_app(self, id:uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用获取成功，名字为{app.name}")
    def update_app(self, id:uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用更新成功，名字为{app.name}")

    def delete_app(self, id:uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用删除成功，id为{app.id}")

    def ping(self):
        raise FailException()

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)
        query = request.json.get("query")
        client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

        response = client.chat.completions.create(
            model="glm-4.5",
            messages=[
                {"role": "system", "content": "你是智谱开发的全世界最强的ai助手"},
                {"role": "user", "content": query}
            ]
        )

        content = response.choices[0].message.content
        return success_json(data={"response": content})
