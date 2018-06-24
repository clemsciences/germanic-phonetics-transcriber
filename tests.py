"""

"""

__author__ = ['Clément Besnier <clemsciences@aol.com>']

import old_norse
import old_swedish
import gothic
from phonetics import *
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
        tr = Transcriber(old_swedish.DIPHTHONGS_IPA, old_swedish.DIPHTHONGS_IPA_class, old_swedish.IPA_class,
                         old_swedish.old_swedish_rules)
        transcribed_sentence = tr.main(sentence)
        self.assertEqual("[a]", transcribed_sentence)

    def test_utils(self):
        a = Vowel("open", "front", False, "short", "a")
        self.assertEqual(a.ipar, "a")
        self.assertEqual(a.backness, "front")
        self.assertEqual(a.height, "open")
        self.assertEqual(a.length, "short")
        self.assertEqual(a.rounded, False)

        aa = a.lengthen()
        self.assertEqual(aa.ipar, "aː")

        b = Consonant("bilabial", "stop", True, "b", False)
        self.assertEqual(b.ipar, "b")
        self.assertEqual(b.manner, "stop")
        self.assertEqual(b.place, "bilabial")
        self.assertEqual(b.voiced, True)
        self.assertEqual(b.geminate, False)

        k = Consonant("velar", "stop", False, "k", False)
        s = Consonant("alveolar", "frictative", False, "s", False)
        x = k+s
        self.assertEqual(x.ipar, "ks")

        th = Consonant("dental", "frictative", False, "θ", False)
        dh = Consonant("dental", "frictative", True, "ð", False)
        rule1 = Rule(AbstractPosition("inner", AbstractVowel(), AbstractVowel()), th, dh)

        pos1 = Position("inner", a, a)
        self.assertEqual(rule1.apply(pos1), True)

        pos2 = Position("inner", k, a)
        self.assertEqual(rule1.apply(pos2), False)

        pos3 = Position("inner", a, s)
        self.assertEqual(rule1.apply(pos3), False)

        rule2 = Rule(AbstractPosition("inner", AbstractConsonant(voiced=True), AbstractConsonant(voiced=True)), th, dh)
        pos1 = Position("inner", a, a)
        self.assertEqual(rule2.apply(pos1), False)

        pos2 = Position("inner", k, a)
        self.assertEqual(rule2.apply(pos2), False)

        pos3 = Position("inner", a, s)
        self.assertEqual(rule2.apply(pos3), False)

        pos4 = Position("inner", b, b)
        self.assertEqual(rule2.apply(pos4), True)


if __name__ == '__main__':
    unittest.main()
