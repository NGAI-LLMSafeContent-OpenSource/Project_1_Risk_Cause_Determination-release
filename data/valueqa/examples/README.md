# 自编最小公开样例

本目录包含为本项目新编的 3 条虚构样例。材料、评论、问题和答案均为本次编写，不摘录网络文章，不使用原实验语料，不包含真实个人信息。它们用于展示数据格式和检查运行流程，不是正式评测集，不能用于证明模型分类性能。发布许可遵循项目方最终批准的许可，不代表为其他数据或模型授予许可。

## 文件与预期等级

| 文件 | 用途 |
| --- | --- |
| `evaluation_samples.jsonl` | 3 条输入，字段名称与现有数据一致；`label` 为参考标签，不进入模型提示词 |
| `reference_annotations.jsonl` | 配套参考标签；`annotations: []` 表示本样例不提供片段定位标注 |
| `expected_predictions.jsonl` | 人工设定的预期 `final_label`，仅用于核对，不是实际模型输出或可导入的初判缓存 |

| sample_id | 预期等级 | 判定依据 |
| --- | --- | --- |
| `example_reading_room_high` | `high` | 准确说明延后一小时、先试行四周，以及根据人数和成本决定长期实施的条件关系 |
| `example_reading_room_medium` | `medium` | 延时方向正确，但没有回答题目明确要求的试行与长期实施之间的关系；补充即可完善 |
| `example_reading_room_low` | `low` | 将评论对试行的支持误读为反对，反转中心立场 |

同一材料下的三种答案是演示用对照，不得拆分到训练集和测试集后当成独立泛化证据。

## 运行

先按照 [框架 README](../../../ValueQA_Classification/README.md) 准备依赖、基础模型、LoRA 和 `LLM_REVIEW_API_KEY`。以下命令在项目根目录执行，Windows PowerShell 和 Linux 均可使用。Linux 将任务配置名替换为 `valueqa_classification_api_linux.yaml`。

```bash
python tools/run.py configs/eval_tasks/valueqa_classification_api.yaml --dataset.path data/valueqa/examples/evaluation_samples.jsonl --dataset.references_path data/valueqa/examples/reference_annotations.jsonl --runner.output_dir results/valueqa_classification_examples --evaluator.state_dir results/valueqa_classification_examples/state
```

实际结果输出到 `results/valueqa_classification_examples/`，其中 `state/predictions.jsonl` 记录每条样例的 `sample_id` 和 `final_label`，`report.md` 与 `result.json` 提供评分。按 `sample_id` 与本目录的 `expected_predictions.jsonl` 核对等级即可；其他运行记录字段无需完全相同。

预期等级是验收目标，实际 Qwen 初判或独立复核可能与之不同。应保留并分析差异，不能把预期文件作为模型预测导入、覆盖结果或据此声称实测 ACC 为 100%。
