"""粒子系统：排序、软边与批量发射。"""

import math


def sort_key(depth, order):
    """按相机方向给深度排序键。"""
    return depth * order


def stable_sort_indices(depths):
    """同深度保持原顺序的稳定排序。"""
    return sorted(range(len(depths)), key=lambda i: depths[i])


def soft_fade(scene_depth, particle_depth, softness):
    """软粒子按场景深度与粒子深度差淡出。"""
    if softness <= 0:
        return 1.0 if scene_depth >= particle_depth else 0.0
    fade = (scene_depth - particle_depth) / softness
    return min(1.0, max(0.0, fade))


def emission_count(rate, dt, accumulator):
    """发射数量按 dt 累积余数。"""
    return int(rate * dt + accumulator)


def wrap_lifetime(age, life):
    """生命周期越界后循环。"""
    return age % life


def reflect_velocity(velocity, normal):
    """碰撞速度按法线反射。"""
    dot = sum(v * n for v, n in zip(velocity, normal))
    return [float(v - 2.0 * dot * n) for v, n in zip(velocity, normal)]


def atlas_uv(index, columns, rows):
    """图集 UV 按行列计算。"""
    col = index % columns
    row = index // columns
    du = 1.0 / columns
    dv = 1.0 / rows
    return (col * du, row * dv, du, dv)


def batch_count(total, max_batch):
    """实例按最大批次拆分。"""
    return math.ceil(total / max_batch)


def in_frustum(x, y, min_x, max_x, min_y, max_y):
    """视锥裁剪包含边界。"""
    return min_x <= x <= max_x and min_y <= y <= max_y


def commit_emitters(statuses):
    """批量发射器全部成功才提交。"""
    return all(statuses)
