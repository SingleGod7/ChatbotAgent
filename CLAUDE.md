# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个基于 Flask 的聊天机器人代理项目，采用依赖注入设计模式，作为其他应用程序的基础框架。

## 核心架构

### 目录结构
- `app/`: 应用入口层
  - `http/`: HTTP 应用入口
- `internal/`: 内部核心组件
  - `server/`: HTTP 服务器封装
  - `router/`: 路由管理
  - `handler/`: 请求处理器
- `config/`: 配置文件（目前为空）
- `pkg/`: 可复用的包组件（目前为空）
- `test/`: 测试文件（目前为空）

### 架构特点
1. **依赖注入**: 使用 `injector` 库实现依赖注入，解耦组件依赖关系
2. **分层架构**: 清晰的职责分离，每层都有明确的职责
3. **路由集中管理**: 所有路由在 `Router` 类中统一注册和管理
4. **处理器模式**: 业务逻辑集中在 Handler 中，实现请求处理的统一入口

### 关键组件

#### Http 服务器 (`internal/server/http.py:4`)
- 继承自 Flask，封装 HTTP 服务器功能
- 在初始化时自动注册路由
- 路由器通过依赖注入传入

#### 路由管理 (`internal/router/router.py:8`)
- 使用 `@inject` 装饰器实现依赖注入
- 管理所有应用路由，使用 Blueprint 组织
- 负责将 URL 规则映射到 Handler 方法

#### 处理器 (`internal/handler/app_handler.py:1`)
- 包含具体的业务逻辑处理
- 目前提供基础的 ping 接口用于健康检查

## 开发命令

### 环境设置
```bash
# 安装依赖
pip install -r requirements.txt

# 激活虚拟环境（Windows）
venv\Scripts\activate
```

### 应用运行
```bash
# 启动开发服务器（debug 模式）
python app/http/app.py
```

### 依赖管理
```bash
# 安装新依赖
pip install package_name
pipreqs --ignore venv --force
```

## 开发规范

### 添加新路由
1. 在 `internal/handler/` 中创建对应的 Handler 方法
2. 在 `internal/router/router.py` 中注册新路由
3. 确保使用 `@inject` 装饰器注入依赖

### 添加新处理器
1. 在 `internal/handler/` 中创建新的 Handler 类或方法
2. 遵循单一职责原则，每个方法只处理一种类型的请求
3. 在 Router 中注入并注册对应的路由

### 依赖注入使用
- 使用 `@inject` 装饰器标记需要注入的依赖
- 通过 `Injector` 实例获取需要的组件
- 保持依赖关系的清晰和可维护性

## 配置说明

### Python 版本要求
- Python 3.7+

### 依赖包
- Flask==2.2.2: Web 框架
- injector==0.22.0: 依赖注入框架

### 环境变量
- 无特殊环境变量要求
- 虚拟环境目录 `venv/` 已被忽略

## 常见操作

### 添加新 API 端点
1. 在相应的 Handler 中添加处理方法
2. 在 Router 中注册新的 URL 规则
3. 确保方法签名和路由配置匹配

### 测试 API
- 使用 `GET /ping` 端点进行健康检查
- 返回格式：`{"status": "ok"}`

## 注意事项

- 项目采用严格的分层架构，避免跨层直接调用
- 所有依赖关系通过 injector 管理，避免手动实例化
- 路由注册集中在 Router 类中，保持路由配置的一致性
- Handler 方法应保持简洁，复杂的业务逻辑应拆分到服务层