from django.test import TestCase

from benfords.core import get_number_from_line, get_keys, prepare_leading_digits, prepare_graph_data


class BenfordsLawTestCase(TestCase):
    def test_getting_number_from_line_with_single_number(self):
        relevant_number = 12
        line = "{}".format(relevant_number)
        output_number = get_number_from_line(line)
        self.assertEqual(output_number, relevant_number)

    def test_getting_number_from_line_with_text(self):
        relevant_number = 4250
        line = "some text  {} lorem ipsum 15".format(relevant_number)
        output_number = get_number_from_line(line)
        self.assertEqual(output_number, relevant_number)

    def test_skipping_line(self):
        line = "some text"
        output = get_number_from_line(line)
        self.assertIsNone(output)

    def test_get_keys(self):
        self.assertEqual(get_keys(), (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_preparing_leading_digits(self):
        sample_input = """
        date
        19072016
        17072018
        13102020
        """
        leading_digits = prepare_leading_digits(sample_input)
        self.assertEqual(leading_digits, [1, 1, 1])

    def test_preparing_graph_data(self):
        input_data = [2, 2, 4, 7, 2, 8, 9, 2]
        expected_data = [0, 50, 0, 12.5, 0, 0, 12.5, 12.5, 12.5]
        output_data = prepare_graph_data(input_data)
        self.assertEqual(output_data, expected_data)
