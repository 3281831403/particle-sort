import pytest

from render import particles as mod

CASES = [
    ('sort_key', [2.0, -1], -2.0, True),
    ('stable_sort_indices', [[0.5, 0.2, 0.5, 0.1]], [3, 1, 0, 2], False),
    ('soft_fade', [10.0, 8.0, 4.0], 0.5, True),
    ('soft_fade', [10.0, 12.0, 4.0], 0.0, True),
    ('emission_count', [10, 0.25, 0.0], 2, False),
    ('wrap_lifetime', [5, 3], 2, False),
    ('reflect_velocity', [[1, -1, 0], [0, 1, 0]], [1.0, 1.0, 0.0], True),
    ('atlas_uv', [5, 4, 2], (0.25, 0.5, 0.25, 0.5), False),
    ('batch_count', [1000, 256], 4, False),
    ('in_frustum', [0, 0, -1, 1, -1, 1], True, False),
    ('in_frustum', [2, 0, -1, 1, -1, 1], False, False),
    ('commit_emitters', [[True, True]], True, False),
    ('sort_key', [2.0, 1], 2.0, True),
    ('emission_count', [3, 0.5, 0.9], 2, False),
    ('wrap_lifetime', [0, 3], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_particles_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
