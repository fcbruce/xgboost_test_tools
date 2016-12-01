xgboost test tools
====

用于XGBoost模型的测试脚本

### 代码结构说明

* `src/map_rule.py` - feature映射规则
* `src/feature2array.py` - `JSON`转成`numpy array`
* `src/xgb_run.py` - 跑分


### 数据文件存放
* `data/` - 存放`numpy array`
* `feature/` - 存放`JSON`格式的feature
* `models/` - 存放XGBoost训练出来的model
* `rule/` - 存放`JSON` map to `numpy array`的规则
