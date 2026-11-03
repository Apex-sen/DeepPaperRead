# DeepPaperNote-Explainer

**面向科研学习的论文精读教学增强层**。本项目以 `917Dhj/DeepPaperNote` 为上游工作流基础，重点升级核心方法、数学公式和算法机制的讲解质量。

## 重要定位

当前交付是一个**可应用到上游仓库的增强层（overlay）**，不是上游仓库的完整镜像。它不复制或替代上游的 PDF 获取、Zotero 解析、证据提取、图表规划、Obsidian 保存等脚本。这样做是为了避免复制一份会迅速过时的脚本实现。

应用方式：

1. 克隆上游仓库：`git clone https://github.com/917Dhj/DeepPaperNote.git`
2. 将本压缩包解压。
3. 在本目录运行：
   `python scripts/apply_overlay.py --repo /path/to/DeepPaperNote`
4. 脚本会将教学增强参考文件复制到上游 skill 的 `references/`、`templates/`、`examples/`、`evals/` 目录，并在原 `SKILL.md` 末尾追加一段简短的增强规则入口。
5. 运行 `python scripts/apply_overlay.py --repo /path/to/DeepPaperNote --check` 检查应用状态。

脚本默认不覆盖同名文件；如果文件已存在，会停止并报告冲突。应用前建议先提交 Git commit 或备份。

## 本次设计原则

- **保留上游工作流**：配置检查、论文身份解析、PDF 获取、原始文本与证据抽取、图表决策、Synthesis Bundle、Note Plan、Grounding Lint、Final Note Lint、质量/可读性审查、Formal Save 等阶段不被删减或重排。
- **只升级教学表达层**：新增“直觉 → 公式 → 数值例子 → 算法执行 → 模块关系 → 证据与局限”的讲解协议。
- **证据优先**：论文事实必须有来源；自行构造的数值例子必须标为“示意例子”，不能伪装成论文实验。
- **按需深入**：核心方法重点展开，常识性背景不机械扩写，避免笔记变长但理解没有增加。
- **单篇论文**：继续遵循上游一次精读一篇论文的定位。

## Skill 入口

根目录 `SKILL.md` 是本增强层的 Skill 入口定义。它明确要求先执行上游完整流程，再应用教学化解释规范；不能脱离上游证据与保存流程单独宣称完成论文精读。

## 文件说明

- `references/mechanism-teaching.md`：核心方法讲解规范。
- `references/formula-explanation.md`：数学公式解释协议。
- `references/algorithm-walkthrough.md`：算法执行链还原。
- `references/module-interaction.md`：模块依赖和信息流分析。
- `references/experiment-interpretation.md`：实验与消融解释。
- `references/critical-analysis.md`：假设、局限和研究启发。
- `references/source-grounding.md`：事实、推断和示意例子的边界。
- `templates/paper-note-teaching-template.md`：笔记模板。
- `templates/formula-walkthrough-template.md`：公式讲解模板。
- `examples/TEGDA-teaching-example.md`：教学化讲解示例（只包含已明确标注的示意内容）。
- `evals/quality-rubric.md`：100 分质量评价表。
- `evals/regression-test.md`：回归测试清单。

## 适用场景

当用户说“精读这篇论文”“把核心方法讲清楚”“逐个解释公式”“我没理解这几个模块”等，使用增强规则。若用户只要求快速摘要，不应强制生成完整教学长文；应尊重本次任务范围。

## 许可证与上游关系

本增强层是独立的用户定制内容，不代表上游作者背书。上游项目当前 README 声明采用 MIT License；应用时应保留上游原有 LICENSE、版权声明和来源信息。请在实际应用前再次检查上游许可证及版本。
