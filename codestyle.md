# 前端代码规范 (Code Style Guide) - 832301219

## 一、 通用原则

1.  **文件编码：** 统一使用 **UTF-8** 编码。
2.  **命名：** 统一使用英文命名，避免使用拼音，命名必须具备描述性。
3.  **注释：** 关键业务逻辑、复杂函数必须提供清晰的注释。
4.  **缩进：** 所有文件统一使用 **4 个空格** 进行缩进，禁止使用 Tab 字符。

## 二、 JavaScript 规范 (`app.js`)

### 2.1 命名约定
* **函数 / 变量：** **小驼峰命名法 (camelCase)**，例如：`fetchContacts`, `deleteContact`。
* **常量：** **全大写，下划线分隔 (UPPER_SNAKE_CASE)**，例如：`API_BASE_URL`。
* **DOM 元素引用：** 变量名应使用小驼峰命名，并与 HTML 中的 ID 保持一致，例如：`contactList`, `addForm`。

### 2.2 格式化
* **分号：** 语句末尾必须使用 **分号** 结束。
* **引号：** 字符串统一使用 **单引号** (`'`)，模板字符串 (`...`) 除外。
* **变量声明：** 优先使用 `const` 和 `let`，**禁止使用 `var`**。
* **函数定义：** 统一使用 `async function` 或 `const funcName = async function()` 形式定义异步函数。

### 2.3 API 调用和错误处理
* **异步操作：** 所有 API 调用（`fetch`）都必须使用 **`async/await`** 结构。
* **错误捕获：** 所有异步网络请求都必须包含 **`try...catch`** 块进行错误捕获和 `console.error` 输出。
* **URL 构造：** 统一使用 **模板字符串** 构造包含变量的 API URL。

## 三、 HTML/CSS 规范 (`concacts.html`)

### 3.1 HTML 规范
* **文件名：** 主文件名为 `concacts.html`。
* **语义化：** 使用正确的语义化标签结构内容，例如使用 `<ul>` 和 `<li>` 来表示列表。
* **外部资源引用：** JavaScript 文件 (`<script src="app.js"></script>`) 必须放在 `<body>` 结束标签 (`</body>`) 之前。CSS 样式应放在 `<style>` 标签内或外部 CSS 文件中，并置于 `<head>` 区域。

### 3.2 CSS 规范
* **选择器命名：** 统一使用 **小写字母和短横线** 连接（kebab-case），例如：`.contact-info`, `.delete-btn`。
* **属性顺序：** 推荐按照逻辑顺序书写：布局 (display, position) > 盒模型 (width, height, margin) > 文本 (font-size, color) > 背景和边框。