# 🚀 Antigravity 最终稳定版使用说明（全中文）

> 本文档适用于 **antigravity_auto_code.yaml 最终稳定版**  
> 目标：**自动模型选择｜不断流｜所有输出强制中文｜可直接复制使用**

---

## 一、Antigravity 是什么？

**Antigravity** 是一个「智能 Agent 调度与自动执行系统」，它可以：

- 🧠 根据任务复杂度 **自动选择最合适的大模型**（Gemini / Claude / GPT）
- 🔁 自动重试、自动兜底，**永不因限额或模型不可用而中断**
- ⚙️ 支持 Planning → Agent → Tool 的全自动执行
- 🇨🇳 **强制全中文输出**（即使系统 / PowerShell / 日志是英文）

---

## 二、你现在用的这个版本能解决什么问题？

| 问题 | 是否解决 |
|----|----|
| 输出一半中文一半英文 | ✅ 已解决 |
| Gemini / Claude 输出不统一 | ✅ 已解决 |
| 执行中断 / 限额失败 | ✅ 已解决 |
| Debug 必须高准确模型 | ✅ 已解决 |
| 不想人工确认每一步 | ✅ 已解决 |

> **一句话总结：这是一个“放进去就能长期用”的生产级配置**

---

## 三、文件说明

你只需要 **一个文件**：

```text
antigravity_auto_code.yaml   ← 核心配置文件（必须）
```

无需额外脚本、无需启动参数、无需环境变量。

---

## 四、正确的目录结构（非常重要）

请确保文件 **放在工作区根目录**：

```text
your-project/
├─ antigravity_auto_code.yaml   ✅（必须在这里）
├─ README.md
├─ src/
├─ package.json / requirements.txt（可选）
└─ ...
```

❌ 错误示例：

```text
.vscode/antigravity_auto_code.yaml   ❌ 不生效
config/antigravity_auto_code.yaml    ❌ 不生效
```

---

## 五、如何确认配置已生效？

### ✅ 成功生效的表现

1. 启动 Task / Agent 后
2. 你会看到：

```text
我已完成系统健康检查，结果如下：
- 当前环境状态：正常
- 未发现严重错误
- 建议如下：...
```

➡️ **解释 + 总结一定是中文**

### ❌ 未生效的表现

- 直接输出：
  - "Analyzing workspace..."
  - "Running system diagnostics..."
- 没有中文总结

➡️ 99% 原因：**YAML 没放在根目录**

---

## 六、使用流程示意（文字图解）

### 1️⃣ 自动执行流程

```text
用户任务
   ↓
Antigravity Planning（中文）
   ↓
Agent 自动执行（强制中文）
   ↓
系统 / 工具 / PowerShell（允许英文）
   ↓
中文翻译 + 中文总结输出给你
```

---

### 2️⃣ 模型自动选择逻辑

```text
简单问题 → Gemini（快）
中等复杂 → Claude（稳）
调试 / 修复 → GPT（严）
失败 → 自动切下一个
```

你 **不需要手动切模型**。

---

## 七、关键配置说明（人话版）

### 🔒 强制全中文（最关键）

```yaml
agent_policy:
  default_language: zh-CN
  force_response_language: true
```

> 这行决定了：
> **即使系统返回英文，Agent 也必须翻译成中文再告诉你**

---

### 🔁 永不断流兜底

```yaml
execution_resilience:
  never_abort_on_quota: true
  never_abort_on_model_unavailable: true
```

> 不会因为：
> - Gemini 限额
> - Claude 不可用
> - GPT 调用失败
> 而直接中断

---

## 八、常见问题（FAQ）

### Q1：为什么 PowerShell 命令还是英文？

✔ 正常现象。

- 命令本身 = 系统英文
- **解释给你看的 = 中文**

这是最安全、也是最稳定的方式。

---

### Q2：我可以只用 Gemini 吗？

可以，但 **不推荐**。

当前方案是：
- 快 → Gemini
- 稳 → Claude
- 准 → GPT

是最不容易翻车的组合。

---

### Q3：我可以关掉自动执行吗？

可以，把这一行改为：

```yaml
ask_before_action: true
```

就会每一步询问你。

---

## 九、推荐使用场景

- Workspace Health Check
- 自动 Debug / 修复错误
- 扫描项目结构
- 自动生成 / 重构代码
- 运维 / 系统诊断

---

## 十、一句话结尾

> **你现在用的是 Antigravity 的「长期稳定模板」**  
> 不追新、不折腾、不翻车。

如果你后续需要：
- 🔥 极简版 YAML
- 🌍 中英文切换版
- 🧩 多 Agent 拆分执行版

随时可以在这个基础上继续升级。

