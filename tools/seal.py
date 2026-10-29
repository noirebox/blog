#!/usr/bin/env python3
"""seal.py · scelle le blog : SHA-256 par fichier, chaîne, signature Ed25519.
Usage : python3 tools/seal.py [--verify]"""
import base64, hashlib, json, pathlib, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
GENESIS = 'blog-noirebox-genesis'
KEY = ROOT / 'keys' / 'blog-noirebox-seal.key'
FILES = sorted(['index.html', 'article.html', 'legal.html', 'INDEX.md', 'rss.xml']
           + [p.replace(ROOT.as_posix()+'/', '') for p in __import__('glob').glob(str(ROOT/'posts/*.md'))])

p = 2**255 - 19
l = 2**252 + 27742317777372353535851937790883648493
I = pow(2, (p - 1) // 4, p)
d = (-121665 * pow(121666, p - 2, p)) % p
By = 4 * pow(5, p - 2, p) % p

def inv(x): return pow(x, p - 2, p)

def xrecover(y):
    xx = (y * y - 1) * inv(d * y * y + 1) % p
    x = pow(xx, (p + 3) // 8, p)
    if (x * x - xx) % p != 0: x = (x * I) % p
    if (x * x - xx) % p != 0: raise ValueError
    if x % 2 != 0: x = p - x
    return x

B = (xrecover(By), By)

def edwards(P, Q):
    x1, y1 = P; x2, y2 = Q
    return ((x1*y2+x2*y1) * inv(1+d*x1*x2*y1*y2) % p, (y1*y2+x1*x2) * inv(1-d*x1*x2*y1*y2) % p)

def scalarmult(P, e):
    if e == 0: return (0, 1)
    Q = scalarmult(P, e // 2); Q = edwards(Q, Q)
    if e & 1: Q = edwards(Q, P)
    return Q

def encodepoint(P):
    x, y = P
    bits = [(y >> i) & 1 for i in range(255)] + [x & 1]
    return bytes(sum(bits[i*8+j] << j for j in range(8)) for i in range(32))

def decodepoint(b):
    y = int.from_bytes(b, 'little'); sign = y >> 255; y &= (1 << 255) - 1
    if y >= p: raise ValueError
    xx = (y*y-1) * inv(d*y*y+1) % p
    x = pow(xx, (p+3)//8, p)
    if (x*x-xx) % p != 0: x = (x*I) % p
    if (x*x-xx) % p != 0: raise ValueError
    if x % 2 != sign: x = p - x
    return (x, y)

def clamp(h):
    a = bytearray(h[:32]); a[0] &= 248; a[31] &= 127; a[31] |= 64
    return int.from_bytes(a, 'little')

def publickey(sk):
    return encodepoint(scalarmult(B, clamp(hashlib.sha512(sk).digest())))

def signature(sk, msg):
    h = hashlib.sha512(sk).digest(); a = clamp(h); prefix = h[32:]
    A = encodepoint(scalarmult(B, a))
    r = int.from_bytes(hashlib.sha512(prefix+msg).digest(), 'little') % l
    R = encodepoint(scalarmult(B, r))
    k = int.from_bytes(hashlib.sha512(R+A+msg).digest(), 'little') % l
    return R + ((r + k*a) % l).to_bytes(32, 'little')

def verify(pk, msg, sig):
    R, S = sig[:32], int.from_bytes(sig[32:], 'little')
    if S >= l: return False
    try:
        A = decodepoint(pk); Rr = decodepoint(R)
    except ValueError: return False
    k = int.from_bytes(hashlib.sha512(R+pk+msg).digest(), 'little') % l
    return scalarmult(B, S) == edwards(Rr, scalarmult(A, k))

# self-test RFC 8032
_SK = bytes.fromhex('9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60')
_PK = bytes.fromhex('d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a')
_SG = bytes.fromhex('e5564300c360ac729086e2cc806e828a84877f1eb8e5d974d873e065224901555fb8821590a33bacc61e39701cf9b46bd25bf5f0595bbe24655141438e7a100b')
assert publickey(_SK) == _PK and signature(_SK, b'') == _SG and verify(_PK, b'', _SG)

sha = lambda b: hashlib.sha256(b).hexdigest()

def main():
    entries = []
    for name in FILES:
        f = ROOT / name
        if not f.exists(): sys.exit(f'manquant : {name}')
        data = f.read_bytes()
        entries.append({'name': name, 'sha256': sha(data), 'bytes': len(data)})
    head = sha(GENESIS.encode())
    for e in entries: head = sha((head + e['name'] + e['sha256']).encode())
    KEY.parent.mkdir(exist_ok=True)
    if not KEY.exists():
        import os
        KEY.write_bytes(os.urandom(32)); os.chmod(KEY, 0o600)
        print('clé Ed25519 générée → keys/blog-seal.key (0600 · jamais committée)')
    sk = KEY.read_bytes(); pk = publickey(sk)

    if '--verify' in sys.argv:
        man = json.loads((ROOT / 'manifest.json').read_text())
        ok = True
        print(f"site {man['site']} · construit {man['built_at']}")
        for e in man['files']:
            f = ROOT / e['name']
            good = f.exists() and sha(f.read_bytes()) == e['sha256']
            ok = ok and good
            print(f"  {'PASS' if good else 'FAIL'}  {e['name']}")
        chain = sha(GENESIS.encode())
        for e in man['files']:
            chain = sha((chain + e['name'] + e['sha256']).encode())
        chain_ok = (chain == man['head']); ok = ok and chain_ok
        sig_ok = verify(base64.b64decode(man['pubkey']), man['head'].encode(), base64.b64decode(man['sig']))
        ok = ok and sig_ok
        print(f"chaîne {'PASS' if chain_ok else 'FAIL'} · signature {'PASS' if sig_ok else 'FAIL'}")
        print('VERDICT :', 'INTACT · rien n\'a bougé depuis le dernier scellement.' if ok else 'COMPROMIS ou modifié depuis le dernier scellement.')
        sys.exit(0 if ok else 1)

    sig = signature(sk, head.encode())
    assert verify(pk, head.encode(), sig)
    man = {'site': 'blog.noirebox.eu', 'format': 'seal v1 · SHA-256 chain + Ed25519',
           'built_at': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
           'genesis': GENESIS, 'files': entries, 'head': head,
           'sig': base64.b64encode(sig).decode(), 'pubkey': base64.b64encode(pk).decode(),
           'fingerprint': 'sha256:' + sha(pk)[:16]}
    (ROOT / 'manifest.json').write_text(json.dumps(man, indent=1, ensure_ascii=False) + '\n')
    print(f"scellé · head {head[:16]}…  fingerprint {man['fingerprint']}  ({len(entries)} fichiers)")

main()
