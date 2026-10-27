# 第三方组件与模型边界

本发布范围依据课题一确认单1-A4：ValueQA_Classification、uni_eval及配套工具和配置属于项目组授权的Apache-2.0范围。根LICENSE适用于已授权的项目源码，不替第三方依赖或模型授予许可。

| 组件/资产 | 版本或来源 | 许可与处理 |
|---|---|---|
| Python | 用户安装的Python 3.10+ | PSF许可证；解释器不随包分发 |
| PyYAML | 6.0.3，https://pypi.org/project/PyYAML/6.0.3/ | MIT；由pip获取发行包及许可 |
| requests | 2.32.5，https://pypi.org/project/requests/2.32.5/ | Apache-2.0；由pip获取发行包及许可 |
| tqdm | 4.67.1，https://pypi.org/project/tqdm/4.67.1/ | 保持发行包原始MIT/MPL许可与归属，不在仓中复制依赖源码 |
| PyTorch、Transformers、PEFT、Accelerate、bitsandbytes、OpenAI SDK等完整推理依赖 | ValueQA_Classification/requirements.txt及模块README | 非本次CPU冒烟安装范围；实际推理需用户安装适配版本并遵守原始许可 |
| Qwen基座与LoRA | 模块README列出的公开模型ID和固定revision | 不随发布包分发；需用户按模型发布方的获取条件和许可单独下载 |
| data/valueqa/examples/ | 三条自编虚构样例、参考标签、人工预期输出 | 依课题一1-A4授权公开；不是完整评测集，人工预期不等于模型实测 |

未纳入完整数据、实验或预测结果、模型权重、API密钥、数据库、缓存及开发虚拟环境。传递依赖由pip安装，继续适用各自发行包的许可证；本说明不宣称模型能力或分类准确率经过本次验证。
