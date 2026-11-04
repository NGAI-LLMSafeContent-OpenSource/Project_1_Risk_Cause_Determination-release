# 课题一：价值溯因（ValueQA Classification）

发布单位：NGAI-LLMSafeContent。版本：1.0。代码许可：Apache-2.0。发布日期：2026-11-04。

本包提供Qwen初判、证据复核、确定性接受规则及统一评测runner的实际源码，另含三条经授权公开的自编虚构样例。发布范围不包括完整实验数据、预测结果、模型权重、密钥或缓存。

## CPU最小运行验证

Python 3.10+即可执行发布合同测试；模型推理所需GPU和模型文件另行准备。

```bash
python -m pip install -r requirements.txt
python ValueQA_Classification/verify_version.py
python -m unittest discover -s tests -p test_valueqa_classification_integration.py
python -m unittest ValueQA_Classification.test_framework
python tools/run.py --help
```

也可执行`python tools/release_smoke.py`，脚本自动创建临时虚拟环境、安装CPU依赖并运行以上检查。需要基础环境具备venv及pip >=22.3。HTTP测试使用本机受控模拟服务，不调用生产模型API或下载模型。

这些测试验证配置、注册、真实runner/CLI、规则、异常恢复和本机HTTP传输，不是实际Qwen推理或准确率验收；模型调用在合同测试中使用模拟后端。不得将测试通过或人工预期样例文件当成模型实测结果。

## 实际模型运行

见ValueQA_Classification/README.md，按说明准备适配GPU/CUDA、依赖、公开基础模型及LoRA，再自行设置真实复核API配置。模型和API均未随仓库提供，发布脚本不会自动申请密钥或下载权重。先检查模型许可与获取条件，再按data/valueqa/examples/README.md执行三条样例。

默认任务配置均指向data/valueqa/examples/。可使用：

```bash
python tools/run.py configs/eval_tasks/valueqa_classification_api_linux.yaml --runner.output_dir results/valueqa_examples --evaluator.state_dir results/valueqa_examples/state
```

上面的实际推理命令需要完成模型和API准备；未具备时不能声称运行成功。输出保留在results/，不应提交发布。expected_predictions.jsonl是人工预期，不能作为模型初判缓存导入。

## 来源和版本

源提交：6a08c8784f828bf98b6271e8a55841782444ea88。配置、集成测试的样例范围及版本指纹在发布输入中作了明确修改；原开发历史不随发布分支导出。框架源码/配置指纹已重新生成，不沿用开发指纹。

完整文件列表、源提交和SHA-256见RELEASE_MANIFEST.json与SHA256SUMS。第三方组件和模型边界见THIRD_PARTY_NOTICES.md；发布范围说明见RELEASE_SCOPE.md。
