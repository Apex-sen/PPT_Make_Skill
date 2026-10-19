# PPT Make Skill v3.2.0 — 研究生组会论文汇报

这是一个可上传到支持 Agent Skills 的工具中的独立 Skill 包。此目录根部直接包含 `SKILL.md`。

## 包含内容

- `SKILL.md`：Skill 入口、强制工作流和总体规范
- `references/`：逐页规划、标题、方法分析、完整原图、模板复用、术语、公式与验收细则
- `scripts/`：模板检查、PDF区域提取、基础PPTX生成、公式渲染、术语一致性扫描、PPTX导出和文件验证
- `docs/`：通用提示词、使用指南和版本记录
- `examples/demo_plan.json`：最小逐页计划 JSON 示例
- `requirements.txt`：可选脚本依赖

## 上传方式

1. 下载并解压 `PPT_Make_Skill_v3.2.0_完整安装包.zip`。
2. 将解压得到的 `ppt-make-skill` 文件夹上传到支持 Agent Skills 的工具，或复制到该工具要求的 Skills 目录。
3. 确认上传入口是 `ppt-make-skill/SKILL.md`。
4. 实际制作时提供论文 PDF 与需要严格复用的 PPTX 模板。

若平台只允许上传单个 Markdown 文件，可单独上传 `SKILL.md`，但将缺少 references 中的细则与辅助脚本，因此优先使用完整 ZIP。

## 推荐工作流

1. 先精读论文，建立术语表、证据表与逐页大纲。
2. 先向用户展示大纲并确认，尤其核对整体框架和核心方法。
3. 再复用模板实际页面制作可编辑 PPTX。
4. 结果页优先使用原论文完整 Figure/Table，不未经授权二次抽数重绘。
5. 导出 PDF/PNG 逐页检查图表、公式、版式与文字溢出后再交付。

## 依赖和限制

可选脚本使用 Python 3.10+。依赖见 `requirements.txt`。`render_pptx.py` 需要 LibreOffice；PDF 裁图需要 PyMuPDF。辅助脚本不能代替论文精读、学术判断和人工目视验收。

此 Skill 的许可仅适用于包内原创文档和代码，不覆盖第三方论文、数据集、机构标识或用户提供的模板。
