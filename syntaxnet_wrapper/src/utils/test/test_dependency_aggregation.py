# coding=utf-8

from syntaxnet_wrapper.src.utils.dependency_aggregation import dependency_aggregate
from unittest2 import TestCase

from syntaxnet_wrapper.src.abstract_wrapper import AbstractSyntaxNetWrapper


class TestDependencyAggregation(TestCase):
    def test_dependency_aggregate(self):
        test_values = [
            (
                [
                    AbstractSyntaxNetWrapper(language='French').transform_dependency(
                        sent
                    )
                    for sent in u"1\tIl\t_\tPRON\t_\tGender=Masc|Number=Sing|Person=3|PronType=Prs|fPOS=PRON++\t7\tnsubj\t_\t_\n2\t\xe9tait\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin|fPOS=VERB++\t7\tcop\t_\t_\n3\tune\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t4\tdet\t_\t_\n4\tfois\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t7\tnmod\t_\t_\n5\tune\t_\tDET\t_\tDefinite=Ind|Gender=Fem|Number=Sing|PronType=Dem|fPOS=DET++\t7\tdet\t_\t_\n6\tpetite\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t7\tamod\t_\t_\n7\tfille\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t0\tROOT\t_\t_\n8\tqui\t_\tPRON\t_\tPronType=Rel|fPOS=PRON++\t9\tnsubj\t_\t_\n9\ts\u2019appelait\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin|fPOS=VERB++\t7\tacl:relcl\t_\t_\n10\tAlice\t_\tPROPN\t_\tfPOS=PROPN++\t9\tdobj\t_\t_\n11\t\u2014\t_\tPUNCT\t_\tfPOS=PUNCT++\t9\tpunct\t_\t_\n12\tet\t_\tCONJ\t_\tfPOS=CONJ++\t9\tcc\t_\t_\n13\telle\t_\tPRON\t_\tGender=Fem|Number=Sing|Person=3|PronType=Prs|fPOS=PRON++\t14\tnsubj\t_\t_\n14\tfit\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t9\tconj\t_\t_\n15\tun\t_\tDET\t_\tDefinite=Ind|Gender=Masc|Number=Sing|PronType=Dem|fPOS=DET++\t16\tdet\t_\t_\n16\tr\xeave\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t14\tdobj\t_\t_\n17\tcurieux.\t_\tADJ\t_\tGender=Masc|Number=Sing|fPOS=ADJ++\t16\tamod\t_\t_\n\n1\tAimeriez-vous\t_\tPRON\t_\tNumber=Plur|Person=1|PronType=Prs|fPOS=PRON++\t2\tdobj\t_\t_\n2\tentendre\t_\tVERB\t_\tVerbForm=Inf|fPOS=VERB++\t6\tadvcl\t_\t_\n3\tde\t_\tADP\t_\tfPOS=ADP++\t4\tcase\t_\t_\n4\tquoi\t_\tPRON\t_\tfPOS=PRON++\t2\tnmod\t_\t_\n5\telle\t_\tPRON\t_\tGender=Fem|Number=Sing|Person=3|PronType=Prs|fPOS=PRON++\t6\tnsubj\t_\t_\n6\tr\xeava\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t0\tROOT\t_\t_\n7\t?\t_\tPUNCT\t_\tfPOS=PUNCT++\t6\tpunct\t_\t_\n\n1\tEh\t_\tINTJ\t_\tfPOS=PART++\t2\texpl\t_\t_\n2\tbien,\t_\tNOUN\t_\tfPOS=PROPN++\t3\tnsubj\t_\t_\n3\tvoici\t_\tVERB\t_\tMood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t0\tROOT\t_\t_\n4\tla\t_\tDET\t_\tDefinite=Def|Gender=Fem|Number=Sing|fPOS=DET++\t6\tdet\t_\t_\n5\tpremi\xe8re\t_\tADJ\t_\tGender=Fem|Number=Sing|fPOS=ADJ++\t6\tamod\t_\t_\n6\tchose\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t3\tdobj\t_\t_\n7\tqui\t_\tPRON\t_\tPronType=Rel|fPOS=PRON++\t8\tnsubj\t_\t_\n8\tarriva.\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin|fPOS=VERB++\t6\tacl:relcl\t_\t_\n\n1\tUn\t_\tDET\t_\tDefinite=Ind|Gender=Masc|Number=Sing|PronType=Dem|fPOS=DET++\t2\tdet\t_\t_\n2\tlapin\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t4\tnsubj\t_\t_\n3\tblanc\t_\tADJ\t_\tGender=Masc|Number=Sing|fPOS=ADJ++\t2\tamod\t_\t_\n4\tarriva\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t0\tROOT\t_\t_\n5\ten\t_\tADP\t_\tfPOS=ADP++\t6\tcase\t_\t_\n6\tcourant\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t4\tnmod\t_\t_\n7\t\xe0\t_\tADP\t_\tfPOS=ADP++\t9\tcase\t_\t_\n8\ttoute\t_\tDET\t_\tGender=Fem|Number=Sing|fPOS=DET++\t9\tdet\t_\t_\n9\tallure\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t4\tnmod\t_\t_\n10\t;\t_\tPUNCT\t_\tfPOS=PUNCT++\t4\tpunct\t_\t_\n11\tet,\t_\tSYM\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t4\tappos\t_\t_\n12\tau\t_\tADJ\t_\tfPOS=ADP++\t13\tcase\t_\t_\n13\tmoment\t_\tNOUN\t_\tGender=Masc|Number=Sing|fPOS=NOUN++\t11\tnmod\t_\t_\n14\to\xf9\t_\tPRON\t_\tPronType=Rel|fPOS=PRON++\t16\tnmod\t_\t_\n15\til\t_\tPRON\t_\tGender=Masc|Number=Sing|Person=3|PronType=Prs|fPOS=PRON++\t16\tnsubj\t_\t_\n16\tpassa\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t11\tacl:relcl\t_\t_\n17\tpr\xe8s\t_\tADV\t_\tfPOS=ADV++\t16\tadvmod\t_\t_\n18\td\u2019Alice,\t_\tPROPN\t_\tfPOS=PROPN++\t16\tdobj\t_\t_\n\n1\til\t_\tPRON\t_\tGender=Masc|Number=Sing|Person=3|PronType=Prs|fPOS=PRON++\t2\tnsubj\t_\t_\n2\ts\u2019arr\xeata\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t0\tROOT\t_\t_\n3\tet\t_\tCONJ\t_\tfPOS=CONJ++\t2\tcc\t_\t_\n4\tsortit\t_\tVERB\t_\tMood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|fPOS=VERB++\t2\tconj\t_\t_\n5\tsa\t_\tPRON\t_\tGender=Fem|Number=Sing|fPOS=DET++\t6\tnmod:poss\t_\t_\n6\tmontre\t_\tVERB\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t4\tdobj\t_\t_\n7\tde\t_\tADP\t_\tfPOS=ADP++\t9\tcase\t_\t_\n8\tsa\t_\tDET\t_\tGender=Fem|Number=Sing|fPOS=DET++\t9\tnmod:poss\t_\t_\n9\tpoche.\t_\tNOUN\t_\tGender=Fem|Number=Sing|fPOS=NOUN++\t6\tnmod\t_\t_\n\n".split(
                        '\n\n'
                    )
                ],
                {
                    'cc': 2,
                    'list': 0,
                    'orphan': 0,
                    'ccomp': 0,
                    'csubj': 0,
                    'conj': 2,
                    'acl': 0,
                    'vocative': 0,
                    'clf': 0,
                    'mark': 0,
                    'discourse': 0,
                    'advcl': 1,
                    'dislocated': 0,
                    'aux': 0,
                    'parataxis': 0,
                    'flat': 0,
                    'nsubj': 9,
                    'reparadum': 0,
                    'nummod': 0,
                    'advmod': 1,
                    'punct': 3,
                    'compound': 0,
                    'goeswith': 0,
                    'case': 5,
                    'cop': 1,
                    'obl': 0,
                    'obj': 0,
                    'dep': 0,
                    'appos': 1,
                    'det': 6,
                    'xcomp': 0,
                    'nmod': 7,
                    'amod': 4,
                    'iobj': 0,
                    'expl': 1,
                    'fixed': 0,
                    'root': 0,
                },
            )
        ]
        for input_test, result in test_values:
            self.assertDictEqual(result, dependency_aggregate(input_test))
