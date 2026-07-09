---
name: fix-bugs
description: Expert bug investigation and repair workflow. Use as the primary skill when an AI coding tool is asked to fix, debug, diagnose, reproduce, verify, or explain a software bug, regression, failing test, production issue, unexpected behavior, interface error, UI display issue, data inconsistency, performance degradation, build failure, flaky issue, or historical logic regression. Focus on root cause, proportional repair scope, retesting, similar-case checks, and concise repair conclusions.
---

# Bug Fix Skill

## 目标

根据用户提供的问题描述、报错、截图、日志、失败测试、代码片段或项目上下文，完成 Bug 定位、根因确认、最小必要修复、回归验证和交付说明。

## 核心原则

1. 优先复现，再修复；无法复现时说明证据链和不确定点。
2. 先理解业务预期，再判断代码对错。
3. 修复必须消除根因，不只压住表面报错。
4. 选择长期行为正确的最小必要改动，不硬编码当前 case。
5. 修改后运行相关原有测试，并按风险补充新测试。
6. 主动检查相似入口、字段、状态、工具类或异常处理模式，避免过度拟合。
7. 小问题保持轻量；复杂问题记录假设、取舍、影响面和验证边界。
8. 最终说明必须覆盖复现或证据、根因、修改点、验证方式和残余风险。

## 与其他 Skill 的关系

- 本 skill 是 Bug、回归、失败测试和异常行为的主流程；不要用 `requirement-development` 绕过根因分析。
- 根因落在服务端接口、幂等、事务、缓存、消息、任务或生产稳定性上时，结合 `backend-production-engineering` 补充生产边界。
- 根因落在表结构、SQL、索引、迁移、历史数据或数据修复上时，结合 `database-performance-migration` 保护数据安全和回滚路径。
- 根因落在第三方 API、SDK、CLI 或版本兼容上时，结合 `third-party-integration` 核对官方契约。
- 根因落在模型输出、RAG、Agent、Prompt 或 AI 评测缺口上时，结合 `ai-application-development`。
- 问题暴露日志不足、Trace 断链、临时日志残留、敏感信息泄漏或告警缺失时，结合 `observability-logging-engineering` 补齐必要观测。
- 另有项目专用 skill 时，同时遵守该项目的路径、模块、构建、测试和交付约定。

## Bundled Resources

| File | Read it when |
|---|---|
| `references/bug-fix-workflow.md` | Bug 复杂、根因不清、需要验证矩阵、需要输出模板，或修复前需要明确闸门和层级决策。 |

## 输入信息

用户可能提供：

- Bug 描述、预期行为、实际行为、操作步骤。
- 报错日志、截图、相关代码、项目目录。
- 测试用例、接口请求与响应。
- 线上环境、版本号、分支名、提交记录。

信息不足时，先基于代码、日志和可运行检查补证据；只有关键阻塞信息缺失，才询问用户。

## 工作流程

1. 理解问题和业务预期：区分用户可见现象、日志报错、直接触发点和期望行为。
2. 建立可证伪假设：列出最可能的 1-3 个根因和需要确认或排除的证据。
3. 定位调用链：从入口、转换、决策、副作用到返回完整走一遍，不只改报错行。
4. 复现问题：优先用失败测试、用户步骤、最小输入、请求样例或代码级测试锁定问题。
5. 确认根因：说明哪个条件触发、哪段逻辑错误、为什么当前输入会失败、为什么修复点能消除根因。
6. 制定修复方案：选择能真正解决根因、兼容现有行为、验证路径清楚的最小必要改动。
7. 修改代码：保持范围聚焦，避免无关重构、吞异常、删除测试或写死当前输入。
8. 验证修复：运行原始复现、相关测试和必要边界测试；无法运行时说明原因和建议命令。
9. 检查类似问题：搜索同类字段、入口、状态流、工具类、异常处理和配置读取模式。
10. 交付结论：说明问题、根因、改动、验证、相似排查和残余风险。

复杂或高风险 Bug 的修复前闸门、验证矩阵、层级决策和输出模板见 `references/bug-fix-workflow.md`。

## 行为约束

- 不要在没有证据的情况下直接修改代码。
- 不要只根据报错信息下结论。
- 不要为了通过测试删除断言或弱化测试。
- 不要留下临时日志、调试代码、测试数据或无关格式化。
- 不要擅自扩大修改范围；同类问题只有确认真实存在才同步修复。
- 无法确认根因时，必须说明当前证据、不确定点和下一步验证方式。
