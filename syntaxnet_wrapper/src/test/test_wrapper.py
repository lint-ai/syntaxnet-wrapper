# coding: utf-8

from unittest2 import TestCase

from syntaxnet_wrapper.src.wrapper import *


class TestWrapper(TestCase):
    def test_morpho_sentence(self):
        with self.assertRaises(ValueError):
            SyntaxNetWrapper(language='French').morpho_sentence(u"")

        input_sentence = u"Cette phrase est un test"
        result = u'1\tCette\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=DET++\t0\t_\t_\t_\n2\tphrase\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n3\test\t_\t_\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\t_\t_\t_\n4\tun\t_\t_\t_\tDefinite=Ind|Gender=Masc|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n5\ttest\t_\t_\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n\n'
        self.assertEqual(
            result, SyntaxNetWrapper(language='French').morpho_sentence(input_sentence)
        )

    def test_morpho_sentences(self):
        input_sentences = [
            u"Une première phrase de test",
            u"Une expression est secondaire",
        ]
        results = u'1\tUne\t_\t_\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\tpremi\xe8re\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n3\tphrase\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n4\tde\t_\t_\t_\tfPOS=ADP++\t0\t_\t_\t_\n5\ttest\t_\t_\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n\n1\tUne\t_\t_\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\texpression\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n3\test\t_\t_\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\t_\t_\t_\n4\tsecondaire\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n\n'
        self.assertEqual(
            results,
            SyntaxNetWrapper(language='French').morpho_sentences(input_sentences),
        )

    def test_several_call(self):
        input_sentences = [
            u"Une première phrase de test",
            u"Une expression est secondaire",
        ]
        results = [
            u'1\tUne\t_\t_\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\tpremi\xe8re\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n3\tphrase\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n4\tde\t_\t_\t_\tfPOS=ADP++\t0\t_\t_\t_\n5\ttest\t_\t_\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n\n',
            u'1\tUne\t_\t_\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\texpression\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n3\test\t_\t_\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\t_\t_\t_\n4\tsecondaire\t_\t_\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n\n',
        ]

        sn_wrapper = SyntaxNetWrapper(language='French')
        for idx, sentence in enumerate(input_sentences):
            self.assertEqual(results[idx], sn_wrapper.morpho_sentence(sentence))

    def test_tag_sentence(self):
        input_sentence = u"Cette phrase est un test"
        result = u'1\tCette\t_\tDET\t_\tGender=Fem|Number=Sing|fPOS=DET++\t0\t_\t_\t_\n2\tphrase\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n3\test\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\t_\t_\t_\n4\tun\t_\tDET\t_\tDefinite=Ind|Gender=Masc|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n5\ttest\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n\n'
        self.assertEqual(
            result, SyntaxNetWrapper(language='French').tag_sentence(input_sentence)
        )

    def test_tag_sentences(self):
        input_sentences = [
            u"Une première phrase de test",
            u"Une expression est secondaire",
        ]
        result = u'1\tUne\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\tpremi\xe8re\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n3\tphrase\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n4\tde\t_\tADP\t_\tfPOS=ADP++\t0\t_\t_\t_\n5\ttest\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n\n1\tUne\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t0\t_\t_\t_\n2\texpression\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\t_\t_\t_\n3\test\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\t_\t_\t_\n4\tsecondaire\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\t_\t_\t_\n\n'
        self.assertEqual(
            result, SyntaxNetWrapper(language='French').tag_sentences(input_sentences)
        )

    def test_parse_sentence(self):
        input_sentence = u"Cette phrase est un test"
        result = u'1\tCette\t_\tDET\t_\tGender=Fem|Number=Sing|fPOS=DET++\t2\tdet\t_\t_\n2\tphrase\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t5\tnsubj\t_\t_\n3\test\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t5\tcop\t_\t_\n4\tun\t_\tDET\t_\tDefinite=Ind|Gender=Masc|Number=Sing|PronType=Dem|fPOS=DET++\t5\tdet\t_\t_\n5\ttest\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t0\tROOT\t_\t_\n\n'
        self.assertEqual(
            result, SyntaxNetWrapper(language='French').parse_sentence(input_sentence)
        )

    def test_parse_sentences(self):
        input_sentences = [
            u"Une première phrase de test",
            u"Une expression est secondaire",
        ]
        result = u'1\tUne\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t3\tdet\t_\t_\n2\tpremi\xe8re\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t3\tamod\t_\t_\n3\tphrase\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\tROOT\t_\t_\n4\tde\t_\tADP\t_\tfPOS=ADP++\t5\tcase\t_\t_\n5\ttest\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t3\tnmod\t_\t_\n\n1\tUne\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t2\tdet\t_\t_\n2\texpression\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t4\tnsubj\t_\t_\n3\test\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t4\tcop\t_\t_\n4\tsecondaire\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t0\tROOT\t_\t_\n\n'
        self.assertEqual(
            result, SyntaxNetWrapper(language='French').parse_sentences(input_sentences)
        )

    def test_parse_sentence_en(self):
        input_sentence = u"This is a test sentence"
        result = u'1\tThis\t_\tPRON\tDT\tNumber=Sing|PronType=Dem|fPOS=PRON++DT\t5\tnsubj\t_\t_\n2\tis\t_\tVERB\tVBZ\tMood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++VBZ\t5\tcop\t_\t_\n3\ta\t_\tDET\tDT\tDefinite=Ind|PronType=Art|fPOS=DET++DT\t5\tdet\t_\t_\n4\ttest\t_\tADJ\tJJS\tDegree=Pos|fPOS=ADJ++JJ\t5\tcompound\t_\t_\n5\tsentence\t_\tNOUN\tNN\tNumber=Sing|fPOS=NOUN++NN\t0\tROOT\t_\t_\n\n'
        self.assertEqual(result, SyntaxNetWrapper().parse_sentence(input_sentence))
