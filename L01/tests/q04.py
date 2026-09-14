from otter.test_files import test_case

OK_FORMAT = False

name = "q04"
points = None

@test_case(points=1, hidden=False)
def test_q04_1(env):
    import numpy as np, hashlib
    assert 'A' in env, '変数 A が定義されていません。'
    _a = np.asarray(env['A'], dtype=float)
    assert _a.shape == (5, 5), '変数 A の大きさが正しくありません。'
    _p = []
    for _v in _a.reshape(-1):
        if _v == 0:
            _p.append('0,0')
        else:
            _e = int(np.floor(np.log10(abs(_v))))
            _x = _v / 10.0 ** (_e - 5)
            _m = int(_x + 0.5) if _x >= 0 else int(_x - 0.5)
            _p.append('%d,%d' % (_m, _e))
    _h = hashlib.sha256('|'.join(_p).encode()).hexdigest()[:16]
    assert _h == '50afe6362f2297c6', '変数 A の値が正しくありません。'

