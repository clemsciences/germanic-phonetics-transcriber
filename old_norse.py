
from phonetics import *

__author__ = "Clément Besnier"


a = Vowel("open", "front", False, "short", "a")
ee = Vowel("open-mid", "front", False, "short", "ɛ")
e = Vowel("close-mid", "front", False, "short", "e")
oee = Vowel("close-mid", "front", True, "short", "ø")
oe = Vowel("open-mid", "front", True, "short", "œ")
i = Vowel("close", "front", False, "short", "i")
y = Vowel("close", "front", True, "short", "y")
ao = Vowel("open", "back", True, "short", "ɒ"),
oo = Vowel("open-mid", "back", True, "short", "ɔ")
o = Vowel("close-mid", "back", True, "short", "o")
u = Vowel("close", "back", True, "short", "u")

b = Consonant("bilabial", "stop", True, "b")
d = Consonant("alveolar", "stop", True, "d")
f = Consonant("labio-dental", "frictative", False, "f")
g = Consonant("velar", "stop", True, "g")
gh = Consonant("velar", "frictative", True, "Ɣ")
h = Consonant("glottal", "frictative", False, "h")
j = Consonant("palatal", "frictative", True, "j")
k = Consonant("velar", "stop", False, "k")
l = Consonant("alveolar", "lateral", True, "l")
m = Consonant("bilabial", "nasal", True, "m")
n = Consonant("labio-dental", "nasal", True, "n")
p = Consonant("bilabial", "stop", False, "p")
r = Consonant("alveolar", "trill", False, "r")
s = Consonant("alveolar", "frictative", False, "s")
t = Consonant("alveolar", "stop", False, "t")
v = Consonant("labio-dental", "frictative", True, "v")
# θ = Consonant("dental", "frictative", False, "θ")
th = Consonant("dental", "frictative", False, "θ")
# ð = Consonant("dental", "frictative", True, "ð")
dh = Consonant("dental", "frictative", True, "ð")

OLD_NORSE8_PHONOLOGY = [
    a, ee, e, oe, i, y, ao, oo, u, a.lengthen(),
    e.lengthen(), i.lengthen(), o.lengthen(), u.lengthen(),
    y.lengthen(), b, d, f, g, h, k, l, m, n, p, r, s, t, v, th, dh
]



# IPA Dictionary
DIPHTONGS_IPA = {
    "ey": "ɐy",  # Dipthongs
    "au": "ɒu",
    "øy": "ɐy",
    "ei": "ei",
}
DIPHTONGS_IPA_class = {
    "ey": Vowel("open", "front", True, "short", "ɐy"),
    "au": Vowel("open", "back", True, "short", "ɒu"),
    "øy": Vowel("open", "front", True, "short", "ɐy"),
    "ei": Vowel("open", "front", True, "short", "ɛi"),
}
IPA = {
    "a": "a",  # Short vowels
    "e": "ɛ",
    "i": "i",
    "o": "ɔ",
    "ǫ": "ɒ",
    "ö": "ø",
    "ø": "ø",
    "u": "u",
    "y": "y",
    "á": "aː",  # Long vowels
    "æ": "ɛː",
    "œ": "œ:",
    "é": "eː",
    "í": "iː",
    "ó": "oː",
    "ú": "uː",
    "ý": "y:",
    # Consonants
    "b": "b",
    "d": "d",
    "f": "f",
    "g": "g",
    "h": "h",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "p": "p",
    "r": "r",
    "s": "s",
    "t": "t",
    "v": "v",
    "þ": "θ",
    "ð": "ð",
}

IPA_class = {
    "a": a,  # Short vowels
    "e": ee,
    "i": i,
    "o": oo,
    "ǫ": ao,
    "ø": oee,
    "u": u,
    "y": y,
    "á": a.lengthen(),  # Long vowels
    "æ": ee.lengthen(),
    "ö": oe,
    "œ": oe.lengthen(),
    "é": e.lengthen(),
    "í": i.lengthen(),
    "ó": o.lengthen(),
    "ú": u.lengthen(),
    "ý": y.lengthen(),
    # Consonants
    "b": b,
    "d": d,
    "f": f,
    "g": g,
    "h": h,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "p": p,
    "r": r,
    "s": s,
    "t": t,
    "v": v,
    "þ": th,
    "ð": dh,
}
GEMINATE_CONSONANTS = {
    "bb": "b:",
    "dd": "d:",
    "ff": "f:",
    "gg": "g:",
    "kk": "k:",
    "ll": "l:",
    "mm": "m:",
    "nn": "n:",
    "pp": "p:",
    "rr": "r:",
    "ss": "s:",
    "tt": "t:",
    "vv": "v:",
}


if __name__ == "__main__":
    # Word()lpp
    sentence = "Gylfi konungr var maðr vitr ok fjölkunnigr"
    s1 = "almáttigr guð skapaði í upphafi himin ok jörð ok alla þá hluti, er þeim fylgja, og síðast menn tvá, " \
         "er ættir eru frá komnar, adam ok evu, ok fjölgaðist þeira kynslóð ok dreifðist um heim allan."
    s1 = s1.replace(",", "")
    s1 = s1.replace(".", "")
    print(s1)
    translitterated = []
    for w in s1.split(" "):
        # word = "vagfa"
        word = w
        print(word)
        rules = []
        rules.extend(rule_f)
        rules.extend(rule_g)
        rules.extend(rule_th)
        tr = Transcriber()
        first_res = tr.first_process(word)
        print([type(c) for c in first_res])
        print([c.ipar for c in first_res])
        second_res = tr.second_process(first_res, rules)
        print(second_res)
        translitterated.append(second_res)
    print(s1)
    print("["+" ".join(translitterated)+"]")