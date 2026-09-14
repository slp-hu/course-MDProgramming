from otter.test_files import test_case

OK_FORMAT = False

name = "q03"
points = None

@test_case(points=1, hidden=False)
def test_q03_1(env):
    import numpy as np, pickle
    assert 'A' in env, '変数 A が定義されていません。'
    _ref = pickle.load(open('ref.pkl', 'rb'))
    _f = lambda x: np.arange(100, 0, -1)
    _want = np.asarray(_f(_ref['A']), dtype=float)
    _got = np.asarray(_f(env['A']), dtype=float)
    assert _got.shape == _want.shape, '変数 A の大きさが正しくありません。'
    _d = np.abs(_got - _want)
    _ok = _d <= 1e-06 + 0.001 * np.abs(_want)
    assert bool(np.all(_ok)), '変数 A の値が正しくありません。'

