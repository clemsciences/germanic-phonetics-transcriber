"""

"""

__author__ = ['Clément Besnier <clemsciences@aol.com>']

import old_norse
import old_swedish
import gothic
import phonetics as ut
import unittest


class TestSequenceFunctions(unittest.TestCase):
    """Class for unittest"""

    def test_old_norse_transcriber(self):
        example_sentence = "Almáttigr guð skapaði í upphafi himin ok jörð ok alla þá hluti, er þeim fylgja, og " \
                           "síðast menn tvá, er ættir eru frá komnar, Adam ok Evu, ok fjölgaðist þeira kynslóð ok " \
                           "dreifðist um heim allan."

        tr = Transcriber()
        transcribed_sentence = tr.main(example_sentence, old_norse.old_norse_rules)
        target = "[almaːtːiɣr guð skapaði iː upːhavi himin ɔk jœrð ɔk alːa θaː hluti ɛr θɛim fylɣja ɔɣ siːðast mɛnː " \
                 "tvaː ɛr ɛːtːir ɛru fraː kɔmnar adam ɔk ɛvu ɔk fjœlɣaðist θɛira kynsloːð ɔk drɛivðist um hɛim alːan]"
        self.assertEqual(target, transcribed_sentence)

    def test_gothic_transcriber(self):
        example_sentence = "Anastodeins aiwaggeljons Iesuis Xristaus sunaus gudis."

        tr = ut.Transcriber(gothic.DIPHTHONGS_IPA,
                            gothic.DIPHTHONGS_IPA_class, gothic.IPA_class, gothic.gothic_rules)
        transcribed_sentence = tr.main(example_sentence)
        target = "[anastoːðiːns ɛwaŋgeːljoːns jeːsuis kristɔs sunɔs guðis]"
        self.assertEqual(target, transcribed_sentence)

    def test_old_swedish(self):
        sentence = "a"
        tr = ut.Transcriber(old_swedish.DIPHTHONGS_IPA, old_swedish.DIPHTHONGS_IPA_class, old_swedish.IPA_class,
                         old_swedish.old_swedish_rules)
        transcribed_sentence = tr.main(sentence)
        self.assertEqual("[a]", transcribed_sentence)

    def test_utils(self):
        # definition of a Vowel
        a = ut.Vowel("open", "front", False, "short", "a")
        self.assertEqual(a.ipar, "a")
        self.assertEqual(a.backness, "front")
        self.assertEqual(a.height, "open")
        self.assertEqual(a.length, "short")
        self.assertEqual(a.rounded, False)

        # how lengthen works
        aa = a.lengthen()
        self.assertEqual(aa.ipar, "aː")

        # example of a Consonant
        b = ut.Consonant("bilabial", "stop", True, "b", False)
        self.assertEqual(b.ipar, "b")
        self.assertEqual(b.manner, "stop")
        self.assertEqual(b.place, "bilabial")
        self.assertEqual(b.voiced, True)
        self.assertEqual(b.geminate, False)

        # This is how Consonant instances can be added to each other
        k = ut.Consonant("velar", "stop", False, "k", False)
        s = ut.Consonant("alveolar", "frictative", False, "s", False)
        x = k+s
        self.assertEqual(x.ipar, "ks")

        # examples of Rule instances
        th = ut.Consonant("dental", "frictative", False, "θ", False)
        dh = ut.Consonant("dental", "frictative", True, "ð", False)
        rule1 = ut.Rule(ut.AbstractPosition("inner", [ut.AbstractVowel()], [ut.AbstractVowel()]), th, dh)

        pos1 = ut.Position("inner", a, a)
        self.assertEqual(rule1.can_apply(pos1), True)

        pos2 = ut.Position("inner", k, a)
        self.assertEqual(rule1.can_apply(pos2), False)

        pos3 = ut.Position("inner", a, s)
        self.assertEqual(rule1.can_apply(pos3), False)

        rule2 = ut.Rule(ut.AbstractPosition("inner", [ut.AbstractConsonant(voiced=True)],
                                            [ut.AbstractConsonant(voiced=True)]), th, dh)
        pos1 = ut.Position("inner", a, a)
        self.assertEqual(rule2.can_apply(pos1), False)

        pos2 = ut.Position("inner", k, a)
        self.assertEqual(rule2.can_apply(pos2), False)

        pos3 = ut.Position("inner", a, s)
        self.assertEqual(rule2.can_apply(pos3), False)

        pos4 = ut.Position("inner", b, b)
        self.assertEqual(rule2.can_apply(pos4), True)

        # Definition of real Vowel and Consonant instances
        a = ut.Vowel("open", "front", False, "short", "a")
        e = ut.Vowel("close-mid", "front", False, "short", "e")
        i = ut.Vowel("close", "front", False, "short", "i")
        o = ut.Vowel("close-mid", "back", True, "short", "o")
        u = ut.Vowel("close", "back", True, "short", "u")

        b = ut.Consonant("bilabial", "stop", True, "b", False)
        d = ut.Consonant("alveolar", "stop", True, "d", False)
        f = ut.Consonant("labio-dental", "frictative", False, "f", False)
        g = ut.Consonant("velar", "stop", True, "g", False)
        k = ut.Consonant("velar", "stop", False, "k", False)
        p = ut.Consonant("bilabial", "stop", False, "p", False)
        s = ut.Consonant("alveolar", "frictative", False, "s", False)
        t = ut.Consonant("alveolar", "stop", False, "t", False)
        v = ut.Consonant("labio-dental", "frictative", True, "v", False)
        th = ut.Consonant("dental", "frictative", False, "θ", False)
        dh = ut.Consonant("dental", "frictative", True, "ð", False)

        # examples of phonology and ipa_class
        PHONOLOGY = [
            a, e, i, o, u, b, d, f, g, k, p, s, t, v, th, dh
        ]

        IPA_class = {
            "a": a,
            "e": e,
            "i": i,
            "o": o,
            "u": u,
            "b": b,
            "d": d,
            "f": f,
            "g": g,
            "k": k,
            "p": p,
            "s": s,
            "t": t,
            "v": v,
            "þ": th,
            "ð": dh,
        }

        # examples of ipa_to_regular_expression and from_regular_expression methods
        ru1 = ut.Rule(ut.AbstractPosition("inner", [ut.AbstractConsonant(voiced=False)],
                                          [ut.AbstractConsonant(voiced=True)]), th, th)
        self.assertEqual(ru1.ipa_to_regular_expression(PHONOLOGY), "(?<=[fkpstθ])θ(?=[bdgvð])")

        ru2 = ut.Rule(ut.AbstractPosition("first", None, [ut.AbstractConsonant(place="velar")]), p, k)
        self.assertEqual(ru2.ipa_to_regular_expression(PHONOLOGY), "^p(?=[gk])")

        ru3 = ut.Rule(ut.AbstractPosition("last", [ut.AbstractConsonant(manner="stop")], None), dh, th)
        self.assertEqual(ru3.ipa_to_regular_expression(PHONOLOGY), "(?<=[bdgkpt])ð$")

        # from regular expression to Rule
        example = r'(?<=[aeiou])f(?=[aeiou])'
        ru4 = ut.Rule.from_regular_expression(example, "v", IPA_class)
        self.assertEqual(ru4.ipa_to_regular_expression(PHONOLOGY), example)

        # pattern3 = ru3.ipa_to_regular_expression(PHONOLOGY)
        # print(ut.Rule.from_regular_expression(pattern3, ru3.temp_sound.ipar, IPA_class))

if __name__ == '__main__':
    unittest.main()
