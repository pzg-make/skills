---
name: requirement-breakdown
description: General-purpose development requirement breakdown workflow. Use as the primary planning skill when an AI coding tool is asked to analyze, clarify, split, estimate, or turn a development need into actionable engineering work, including features, requirement documents, screenshots, meeting notes, API changes, frontend/backend work, data model changes, integrations, refactors, performance work, migrations, reliability work, testing, DevOps, or vague technical ideas. Produces scope, flows, tasks, priorities, dependencies, risks, acceptance criteria, and verification plans without implementing code.
---

# General Development Requirement Breakdown Skill

## 目标

把业务想法、开发需求、技术改造、代码上下文、截图、需求文档、会议纪要、反馈记录或接口说明拆成可开发、可测试、可验收、可排期的研发任务清单。

## 核心原则

1. 先理解目标和问题，再拆方案和任务。
2. 先明确使用方、调用方和系统角色，再拆场景和链路。
3. 先确认本期范围、非本期范围、假设和约束，再进入细节拆分。
4. 先拆业务流程或技术边界，再拆页面、接口、数据、权限、状态和任务。
5. 先定义验收标准和验证方式，再输出开发任务。
6. 结果必须可开发、可测试、可验收、可排期。
7. 不确定内容标记为“待确认”，不要写成确定需求。
8. 不过度设计；优先保证当前版本可落地，必要时给出演进方案。

## 与其他 Skill 的关系

- 本 skill 主导“拆清楚要做什么、怎么验收、怎么排期”，不负责直接改代码。
- 用户要求直接落地开发时，交给 `requirement-development` 主导；本 skill 只在范围仍模糊或需要计划时补充。
- 需求本质是线上问题、失败测试或回归时，先用 `fix-bugs` 确认根因，再拆修复任务。
- 涉及服务端、数据库、AI、第三方或观测能力时，本 skill 只标出专项任务和风险；具体实现约束由对应专项 skill 负责。

## Bundled Resources

| File | Read it when |
|---|---|
| `references/breakdown-template.md` | 需要正式需求拆分文档、完整输出模板、优先级规则、验收写法或发布回滚段落时。 |

## 输入信息

输入可能包含：

- 功能描述、业务目标、需求想法、反馈记录、参考能力。
- 截图、原型、PRD、会议纪要、验收要求。
- 项目目录、代码片段、系统说明、接口文档、数据表设计。
- 技术方案、架构约束、日志、测试用例、构建或部署要求。
- 多端范围、第三方服务、上线时间、兼容性要求。

输入不完整时，优先基于已有信息和项目上下文结构化拆分，并把不确定内容放入待确认问题。只有关键阻塞信息缺失时才询问用户。

## 工作流程

1. 理解背景和目标：识别需求来源、目标使用方、要解决的问题、成功标准、当前缺口和关键约束。
2. 识别角色和调用方：列出人、端、系统、服务、任务、第三方和维护方，以及各自输入、输出和关注数据。
3. 明确范围边界：拆出本期范围、非本期范围、兼容范围、影响范围和假设条件。
4. 拆分业务或技术流程：覆盖触发条件、前置条件、主流程、分支流程、异常流程、结束状态和副作用。
5. 拆分功能和能力点：每个点说明模块、角色、输入、输出、状态变化、异常、权限、兼容和验收方式。
6. 拆分页面和交互：涉及前端时覆盖入口、字段、操作、校验、空态、加载、错误、权限和跳转。
7. 拆分接口和服务：涉及后端或系统交互时覆盖路径、参数、响应、鉴权、幂等、分页、事务、限流、重试和审计。
8. 拆分数据和状态：覆盖实体、字段、默认值、状态流转、索引、唯一约束、迁移、历史兼容和回滚。
9. 拆分权限、安全和非功能需求：覆盖权限矩阵、数据范围、敏感字段、性能、并发、缓存、告警、兼容性和可维护性。
10. 拆分开发任务：按前端、后端、数据、测试、运维、发布等维度给出任务、依赖、优先级、复杂度和验收标准。
11. 识别依赖、风险和待确认问题：明确任务前后依赖、外部依赖、交付风险、质量风险和需要谁确认。

完整优先级规则、验收标准写法和标准输出格式见 `references/breakdown-template.md`。

## 行为约束

- 不要直接跳到开发任务，必须先理解目标、角色、范围和流程。
- 不要只拆页面，不拆业务流程或技术链路。
- 不要只拆功能，不拆接口、数据、权限、状态、异常和验证。
- 不要把不确定内容写成确定结论。
- 不要忽略非功能需求、测试验收、发布回滚和监控。
- 不要让任务粒度过大导致无法估时，也不要过细导致管理成本过高。
