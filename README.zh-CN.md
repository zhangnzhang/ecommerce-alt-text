# ecommerce-alt-text

[English](README.md) | 简体中文

一个 AI Skill 加一个 Python 小脚本，用来给网店图片写和审 alt 文案及文件名，让每张图对屏幕阅读器用户、搜索引擎和 AI 助手都「说得清楚」。

可以作为 Claude 的 Skill 使用，也可以给任何能读 Markdown 指令文件的 AI 工具用。脚本可以单独运行。

## 能得到什么

**生成模式**：给它图片、图片清单或产品链接，输出一张可以直接粘贴的表格，包括图片类型、利于搜索的文件名、alt 文案和字符数。内置 8 类图片模板：主图、使用图、五金细节、材质特写、尺寸对比、场景图、包装礼盒、买家实拍，另外还覆盖博客插图和装饰性图片。

**审计模式**：给它现有的 alt（CSV、导出文件或截图），按 6 项检查逐张标出不合格的图，每张给改写，并指出最该先改的 3 张。

**`alt_audit.py`**：只用 Python 标准库的脚本，扫描 CSV 或保存下来的 HTML 页面，找出缺 alt、把文件名当 alt、以「image of」开头、出现品牌名、用了禁用词、长度不合适、关键词堆砌和批次内重复。见[示例输出](examples/sample-output.md)。

## 遵循的规则

- **alt 里不放品牌名**（logo 本身就是图片主体时除外）。
- **术语统一**：只用你自己的产品叫法，不混用近义词。
- **不同款式不复制同一句 alt。**
- **不写「image of」「photo of」。**
- **能用数字就不用形容词。**
- **控制在大约 80–125 个字符**，最重要的词放前面。
- **纯装饰图用空 alt。**
- **不编造**图里看不到、你也没提供的规格或卖点。
- **文件名**：全小写、用连字符、能说明内容，例如 `travel-mug-navy-lid-closeup-02.jpg`，不要用 `IMG_4821.jpg`。

## 安装

**Claude：** 把 `skills/ecommerce-alt-text/` 复制到 `~/.claude/skills/`（或项目里的 `.claude/skills/`），然后说：

> 给这 6 张产品图写 alt 和文件名。
> 审一下这个 CSV 里的 alt。

**只用脚本：**

```bash
python3 skills/ecommerce-alt-text/scripts/alt_audit.py images.csv --brand "你的品牌" --banned "词1,词2"
python3 skills/ecommerce-alt-text/scripts/alt_audit.py saved-product-page.html
```

CSV 需要两列：`image` 和 `alt`。

## 文件结构

```
skills/ecommerce-alt-text/
├── SKILL.md                  # 规则、按图片类型的模板、生成与审计两种模式
└── scripts/
    └── alt_audit.py          # 扫描 CSV 或 HTML 的 alt 机械检查脚本
examples/
├── sample-images.csv         # 测试数据（虚构）
├── sample-page.html          # 测试页面（虚构）
└── sample-output.md          # 脚本的输出结果
```

## 许可证

[MIT](LICENSE)
