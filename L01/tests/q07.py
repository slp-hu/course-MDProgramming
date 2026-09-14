from otter.test_files import test_case

OK_FORMAT = False

name = "q07"
points = None

@test_case(points=1, hidden=False)
def test_q07_1(env):
    import re, glob, json, io
    _src = env.get('In') or env.get('_ih') or []
    _src = '\n'.join((str(_x) for _x in _src))
    if not _src.strip():
        for _f in sorted(glob.glob('*.ipynb')):
            try:
                _nb = json.load(io.open(_f, encoding='utf-8'))
            except Exception:
                continue
            for _c in _nb.get('cells', []):
                if _c.get('cell_type') == 'code':
                    _src += ''.join(_c.get('source', [])) + '\n'
    if not _src.strip():
        return
    _src = re.sub('#[^\\n]*', '', _src)
    _src = '\n'.join((_l for _l in _src.split('\n') if '.check(' not in _l))
    _f = re.search('\\bnp\\.mod(?![A-Za-z0-9_])', _src) is not None
    assert _f, 'np.mod を使ってください。'

@test_case(points=1, hidden=False)
def test_q07_2(env):
    import re, glob, json, io
    _src = env.get('In') or env.get('_ih') or []
    _src = '\n'.join((str(_x) for _x in _src))
    if not _src.strip():
        for _f in sorted(glob.glob('*.ipynb')):
            try:
                _nb = json.load(io.open(_f, encoding='utf-8'))
            except Exception:
                continue
            for _c in _nb.get('cells', []):
                if _c.get('cell_type') == 'code':
                    _src += ''.join(_c.get('source', [])) + '\n'
    if not _src.strip():
        return
    _src = re.sub('#[^\\n]*', '', _src)
    _src = '\n'.join((_l for _l in _src.split('\n') if '.check(' not in _l))
    _f = re.search('\\bif(?![A-Za-z0-9_])', _src) is not None
    assert not _f, 'if は使わないでください。'
    _f = re.search('\\bfor(?![A-Za-z0-9_])', _src) is not None
    assert not _f, 'for は使わないでください。'

@test_case(points=1, hidden=False)
def test_q07_3(env):
    import numpy as np, hashlib
    assert 'B' in env, '変数 B が定義されていません。'
    _a = np.asarray(env['B'], dtype=float)
    assert _a.shape == (10,), '変数 B の大きさが正しくありません。'
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
    assert _h == '67a397a7ad10b9de', '変数 B の値が正しくありません。'

