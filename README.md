#  通讯录后端项目 - 832301219

## Git 仓库链接
* **前端仓库链接：** [https://github.com/f2x1/832301219_concacts_frontend](https://github.com/f2x1/832301219_concacts_frontend)
* **后端仓库链接：** [https://github.com/f2x1/832301219_concacts_backend]()

## 项目简介
本项目是《第一次作业——前后端分离通讯录编程》的后端实现部分。项目采用 **Python** 语言和 **Django Rest Framework (DRF)** 框架，负责提供前端所需的所有 RESTful API 接口，并管理联系人数据的持久化存储。

* **Django 项目名:** `kekeproject`
* **Django 应用名:** `tongxunlu`

## 功能实现
后端服务基于 DRF 的 `ModelViewSet` 实现了联系人资源的完整管理：

| 功能点       | 对应 DRF 操作 | 描述                                                         |
| :----------- | :------------ | :----------------------------------------------------------- |
| **创建**     | `create()`    | (`POST /api/contacts/`) 接收 POST 请求数据，创建新的联系人记录。 |
| **查询列表** | `list()`      | (`GET /api/contacts/`) 响应 GET 请求，返回所有联系人的列表。 |
| **查询详情** | `retrieve()`  | (`GET /api/contacts/{id}/`) 响应 GET 请求（带 ID），返回单个联系人数据。 |
| **修改**     | `update()`    | (`PUT /api/contacts/{id}/`) 接收 PUT 请求，根据 ID 更新数据库中的联系人信息。 |
| **删除**     | `destroy()`   | (`DELETE /api/contacts/{id}/`) 接收 DELETE 请求，根据 ID 删除对应的联系人记录。 |

## 技术栈
* **后端语言：** Python 3.12.4
* **后端框架：** Django, Django Rest Framework (DRF)
* **数据库：** SQLite3 (开发数据库 `db.sqlite3`)
* **跨域处理：** `django-cors-headers`

## 本地运行步骤
### 1. 环境依赖
* Python 3.12.4
* Pip 包管理器
* (本项目虚拟环境在 `testdjango` 文件夹，但未上传至 Git)

### 2. 数据库配置
本项目默认使用 `db.sqlite3` 数据库，已包含在项目中。

### 3. 运行步骤
1.  **克隆仓库：**
    ```bash
    git clone [https://github.com/f2x1/832301219_concacts_backend.git](https://github.com/f2x1/832301219_concacts_backend.git)
    cd 832301219_concacts_backend
    ```
2.  **安装依赖：**
    ```bash
    # (假设依赖已在本地虚拟环境安装好)
    # 如果有 requirements.txt 文件，则运行: pip install -r requirements.txt
    pip install django djangorestframework django-cors-headers
    ```
3.  **应用迁移：**
    ```bash
    # 基于 tongxunlu/models.py 创建数据库表
    python manage.py makemigrations tongxunlu
    python manage.py migrate
    ```
4.  **启动服务：**
    
    ```bash
    python manage.py runserver 127.0.0.1:8000
    ```
    服务成功启动后，前端即可通过 `http://127.0.0.1:8000/api/contacts/` 访问 API 接口。
