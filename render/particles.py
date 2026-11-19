"""粒子系统：排序、软边与批量发射：待实现的核心模块。"""


def sort_key(depth, order):
    """按相机方向给深度排序键。"""
    raise NotImplementedError

def stable_sort_indices(depths):
    """同深度保持原顺序的稳定排序。"""
    raise NotImplementedError

def soft_fade(scene_depth, particle_depth, softness):
    """软粒子按场景深度与粒子深度差淡出。"""
    raise NotImplementedError

def emission_count(rate, dt, accumulator):
    """发射数量按 dt 累积余数。"""
    raise NotImplementedError

def wrap_lifetime(age, life):
    """生命周期越界后循环。"""
    raise NotImplementedError

def reflect_velocity(velocity, normal):
    """碰撞速度按法线反射。"""
    raise NotImplementedError

def atlas_uv(index, columns, rows):
    """图集 UV 按行列计算。"""
    raise NotImplementedError

def batch_count(total, max_batch):
    """实例按最大批次拆分。"""
    raise NotImplementedError

def in_frustum(x, y, min_x, max_x, min_y, max_y):
    """视锥裁剪包含边界。"""
    raise NotImplementedError

def commit_emitters(statuses):
    """批量发射器全部成功才提交。"""
    raise NotImplementedError
