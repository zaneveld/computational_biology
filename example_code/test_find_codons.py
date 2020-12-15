import unittest
from find_codons import get_codons

class TestFindCodons(unittest.TestCase):
    

    def test_get_codons_returns_empty_list_on_empty_input(self):
        """get_codons returns [] on empty input"""
        input_seq = ""
        observed = get_codons(input_seq)
        expected = []
        self.assertEqual(observed,expected)

    def test_get_codons_functions_on_normal_input(self):
        """get_codons returns codons on a normal input sequence"""
        input_seq = "AAATTTGGGCCC"
        observed = get_codons(input_seq)

        expected = ["AAA","TTT","GGG","CCC"]

        self.assertEqual(observed,expected)

unittest.main()
