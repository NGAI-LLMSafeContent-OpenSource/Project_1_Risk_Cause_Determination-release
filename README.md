# DeepSafe / ValueQA价值溯因

保留原仓统一评测框架、ValueQA分类与证据复核，以及当前配置和集成入口。

发布单位：NGAI-LLMSafeContent。发布分支：`release/1.0`；更新日期：2026-11-21；自研代码许可：Apache-2.0，第三方保留原许可。

## 功能

- ValueQA初判、复核、接受规则、检查点与恢复
- uni_eval模型、数据集、评估器、runner及多任务配置
- 批量评测、模型路由工具和OpenClaw集成源码

## 安装与快速开始

完整环境依原requirements.txt准备；真实推理另需适配GPU/CUDA、Qwen/LoRA及复核API。不同评测任务的模型与数据遵循各自许可。

从公开仓下载同一发布分支：

```bash
git clone --branch release/1.0 https://github.com/NGAI-LLMSafeContent-OpenSource/Project_1_Risk_Cause_Determination-release.git
cd Project_1_Risk_Cause_Determination-release
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell改用 .venv\Scripts\Activate.ps1
```

以下命令均以仓库根目录为起点，注释中的外部条件需先准备：

```bash
python -m pip install -r requirements.txt
python ValueQA_Classification/verify_version.py
python tools/run.py --help
# 准备原配置引用的模型、评测数据和API后执行
python tools/run.py configs/eval_tasks/valueqa_classification_api_linux.yaml
```

## 使用与输出

ValueQA说明见 `ValueQA_Classification/README.md`；三条原仓公开示例在 `data/valueqa/examples/`，不会替代原配置指向的完整数据。其他评测任务配置在 `configs/eval_tasks/`；OpenClaw集成在 `integrations/openclaw-deepsafe/`。输出保存在配置的results目录，不计入发布清单。

## 配置与外部依赖

所有既有配置与版本指纹保持原样。完整数据、模型和预测缓存未捆绑；指纹涉及CRLF文件时应遵循原.gitattributes检出规则。不能把CPU规则/模拟测试当作真实Qwen性能报告。

真实凭据只在自己的运行环境或平台Secrets中配置，不提交.env、用户上传、模型权重或运行结果。原仓文件中的内网服务地址经发布负责人确认按原样保留，使用者应在本地配置自己的可达服务。

## 验证与已知问题

完成对应依赖准备后运行：

```bash
python tools/release_check.py
```

检查包含发布文件完整性、原仓文件一致性与声明的最小测试。它不会自动下载模型或申请API，也不代表全部真实业务/准确率验收。保留的原仓错误、未运行项及外部依赖见 [KNOWN_ISSUES.md](KNOWN_ISSUES.md)。

## 发布版本与文件清单

本版本以原开发仓主分支提交 `6a08c8784f828bf98b6271e8a55841782444ea88` 为源。功能实现与对应原文件保持一致；README、许可说明和发布辅助材料单独登记。当前功能的必要源码、配置、界面与运行资源保留，明确弃用的原型、历史结果和开发缓存不捆绑。

- [逐文件发布清单](RELEASE_FILES.md)
- [原仓文件与Git对象对应关系](SOURCE_ALIGNMENT.json)
- [完整文件SHA-256及权限](RELEASE_MANIFEST.json)，校验表为SHA256SUMS

校验值按Git存储字节生成；若原.gitattributes规定检出换行转换，请用Git对象或发布检查脚本校验，避免将LF/CRLF误认为源码变化。各公开平台release/1.0使用同一个提交，平台生成的运行分支不属于此发布清单。

## 反馈、贡献与许可证

请通过 [公开仓Issues](https://github.com/NGAI-LLMSafeContent-OpenSource/Project_1_Risk_Cause_Determination-release/issues) 提交复现步骤、环境和日志摘要，勿附真实凭据或用户数据。代码问题由课题维护者在原开发仓处理，发布负责人同步审核后的版本；不要仅修一个平台造成分歧。

自研代码采用[Apache-2.0](LICENSE)。模型、数据集、外部服务和第三方代码遵循各自许可与使用条件，见[第三方说明](THIRD_PARTY_NOTICES.md)。


## 公开版本地址占位符

本发布版本将原部署环境的内网 IP 替换为 `example.invalid` 下的保留示例域名，保留原端口和接口路径。部署前请通过项目现有环境变量或配置项填写自己的服务地址；这些域名不是可访问的线上服务。

- `evaluation.example.invalid`：评价体系前端示例地址。
- `model-api.example.invalid`、`llm-api.example.invalid`：模型 API 地址。
- `platform.example.invalid`：治理平台或审计工作台地址。
- `proxy.example.invalid`：代理地址。
- `inference.example.invalid`：推理服务机器地址。

本次仅经授权替换地址字符串及配套测试中的同一地址，未修改接口路径、端口或业务算法。具体例外及文件校验记录见 `SOURCE_ALIGNMENT.json`、`RELEASE_FILES.md` 和 `RELEASE_MANIFEST.json`。
