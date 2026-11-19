# 粒子系统：排序、软边与批量发射

粒子在相机前忽前忽后：排序键没有随相机方向，深度相同的粒子顺序不稳定，软粒子没按场景深度淡出，发射率不随 dt 累积，生命周期越界不循环，碰撞反射没按法线，图集 UV 越界，实例批次过大，视锥裁剪漏掉边缘，批量发射器只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
render/__init__.py
render/particles.py
tests/test_particles.py
```

## 当前状态

`render/particles.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_particles.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 按相机方向计算排序键
2. 同深度粒子稳定排序
3. 软粒子按场景深度淡出
4. 发射率按 dt 累积余数
5. 生命周期循环取模
6. 碰撞速度按法线反射
7. 图集 UV 按行列计算
8. 实例按最大批次拆分
9. 视锥裁剪包含边缘
10. 批量发射器统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `render/particles.py`
后 15 条用例应全部通过。
