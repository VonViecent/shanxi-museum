# 陕西历史博物馆信息管理系统

这是一个基于Flask后端和HTML/JS前端的陕西历史博物馆信息管理系统，用于管理文物、展览和游客信息。

## 功能

- 文物管理：添加、编辑、删除、查询文物信息
- 展览管理：添加、编辑、删除、查询展览信息
- 游客管理：添加、编辑、删除、查询游客信息（API提供，但前端未完全实现）

## 技术栈

- 后端：Python Flask + SQLAlchemy + SQLite
- 前端：HTML/CSS/JavaScript (原生，无框架)

## 安装和运行

1. 确保安装Python 3.7+

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```
   python app.py
   ```

4. 打开浏览器访问 http://localhost:5000/static/index.html

## 数据库

使用SQLite数据库 `museum.db`，首次运行时自动创建表。

## API端点

- GET /api/artifacts - 获取所有文物
- POST /api/artifacts - 添加文物
- PUT /api/artifacts/<id> - 更新文物
- DELETE /api/artifacts/<id> - 删除文物

- GET /api/exhibitions - 获取所有展览
- POST /api/exhibitions - 添加展览
- PUT /api/exhibitions/<id> - 更新展览
- DELETE /api/exhibitions/<id> - 删除展览

- 类似地，/api/visitors

## 测试

运行应用后，可以通过前端界面测试CRUD操作，或使用工具如Postman测试API。