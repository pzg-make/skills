# AI Agent Skills

个人 AI Agent Skills 集合，用于 Codex、Cursor 等编程助手。

这个仓库用于沉淀可复用的工作流、检查清单、脚本和参考资料，让编程助手在不同任务里按更稳定的方式理解需求、执行操作、验证结果并交付说明。

## 通用 Skills

| Skill | 适用场景 |
| --- | --- |
| `requirement-breakdown` | 将模糊需求、产品想法、截图、会议记录或技术改造拆成可开发、可测试、可验收的任务。 |
| `requirement-development` | 根据需求完成从理解、方案、实现、验证到交付总结的端到端开发流程。 |
| `fix-bugs` | 处理 Bug、回归、报错、异常行为、构建失败或线上问题，强调复现、根因、最小必要修复和回归验证。 |
| `third-party-integration` | 接入第三方 API、SDK、云服务或开源库时，优先基于官方文档和当前依赖版本确认契约。 |
| `harness-engineering` | 为仓库补齐面向 AI Coding Agent 的项目说明、架构索引、验证入口和协作约定。 |
| `resume-builder` | 创建、导入、编辑、优化和导出简历，重点保护原始内容和版式。 |
| `drawio-skill` | 生成架构图、流程图、UML、ERD、网络拓扑等 draw.io 图表，并支持导出图片或可编辑图。 |

## 目录约定

每个 skill 通常是一个独立目录：

```text
skill-name/
  SKILL.md
  agents/
  references/
  scripts/
```

- `SKILL.md`：核心说明，包含触发场景、工作原则、执行流程和交付要求。
- `agents/`：可选的 Agent 配置或提示词片段。
- `references/`：可选的补充说明、清单、模板或领域资料。
- `scripts/`：可选的辅助脚本，优先放置可复用、可验证的工具。

不是每个 skill 都需要完整目录结构；保持最小必要即可。

## 使用方式

1. 将本目录放在 Codex 可读取的 skills 路径下。
2. 在对话中直接描述任务，或明确点名某个 skill。
3. 编程助手会先读取对应的 `SKILL.md`，再按其中的流程执行。

示例：

```text
用 requirement-breakdown 帮我拆一下这个需求
用 fix-bugs 帮我定位这个接口报错
用 third-party-integration 帮我接入这个 SDK
```

## 维护原则

- 优先沉淀通用工作流，避免把单个项目的临时上下文写进通用 skill。
- 新增 skill 时先写清楚适用场景、非适用场景、执行步骤和交付标准。
- 需要脚本时，把脚本放进对应 skill 的 `scripts/` 目录，并在 `SKILL.md` 中说明何时使用。
- 需要参考资料时，把资料放进 `references/`，并在 `SKILL.md` 中按需引用，避免一次性塞入过多上下文。
- 修改已有 skill 时保持向后兼容，避免破坏已经稳定的触发语义和工作流。

## 快速检查

更新 skill 后建议检查：

- `SKILL.md` 是否包含清晰的 `name` 和 `description`。
- 触发场景是否足够具体，避免和其他 skill 大面积重叠。
- 工作流程是否可执行，而不是只写原则。
- 交付要求是否说明需要验证什么、如何说明风险。
- README 的通用技能索引是否同步更新。
