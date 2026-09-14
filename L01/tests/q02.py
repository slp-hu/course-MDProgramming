from otter.test_files import test_case

OK_FORMAT = False

name = "q02"
points = None

@test_case(points=1, hidden=False)
def test_q02_1(env):
    import numpy as np, pickle
    assert 'a' in env, '変数 a が定義されていません。'
    _ref = pickle.load(open('ref.pkl', 'rb'))
    _f = lambda x: np.sin(np.sqrt(np.pi)) + np.log(np.tan(1))
    _want = np.asarray(_f(_ref['a']), dtype=float)
    _got = np.asarray(_f(env['a']), dtype=float)
    assert _got.shape == _want.shape, '変数 a の大きさが正しくありません。'
    _d = np.abs(_got - _want)
    _ok = _d <= 1e-06 + 0.001 * np.abs(_want)
    assert bool(np.all(_ok)), '変数 a の値が正しくありません。'

