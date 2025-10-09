from flask import request
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import MessagePlaceholder
from langchain.memory import ConversationWindowMemory, FileChatMessageHistory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from operator import itemgetter
from langchain.output_parsers import StrOutParser
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

    def completion(self, id:uuid.UUID):
        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)
        query = request.json.get("query")
        llm = ChatOpenAI(
                temperature=0.7,
                model="glm-4.6",
                openai_api_key=os.getenv("OPENAI_API_KEY"),
                openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
            )

        prompt = ChatPromptTemplate.from_messages([("system", "你是一个有帮助的助手，你可以根据用户问你的问题幽默的回答"),
                                                   MessagePlaceholder("history"),
                                                   ("human", "{query}")])

        
        memory = ConversationWindowMemory(k=5, 
                                          input_key='query', 
                                          output_key='output', 
                                          return_messages=True,
                                          chat_memory=FileChatMessageHistory(file_path=f"./storage/chat_history.txt"))

        parser = StrOutParser()
        chain = RunnablePassthrough.assign( history= RunnableLambda(memory.load_memory_variables) | itemgetter("history") ) | prompt | llm | parser
        response = chain.invoke({"query": query})

        content = response.content
        return success_json(data={"response": content})
