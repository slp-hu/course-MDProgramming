from otter.test_files import test_case

OK_FORMAT = False

name = "q01"
points = None

@test_case(points=1, hidden=False)
def test_q01_1(env):
    import numpy as np, hashlib
    assert 'a' in env, '変数 a が定義されていません。'
    try:
        _v = float(env['a'])
    except (TypeError, ValueError):
        raise AssertionError('変数 a の値が正しくありません。')
    if _v == 0:
        _m, _e = (0, 0)
    else:
        _e = int(np.floor(np.log10(abs(_v))))
        _x = _v / 10.0 ** (_e - 5)
        _m = int(_x + 0.5) if _x >= 0 else int(_x - 0.5)
    _h = hashlib.sha256(('%d,%d' % (_m, _e)).encode()).hexdigest()[:16]
    assert _h == '46a5a0baf6159029', '変数 a の値が正しくありません。'

