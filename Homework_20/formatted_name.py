import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_full_name_without_middle_name(self):
        result = formatted_name("johny", "smith")
        self.assertEqual(result, "Johny Smith")

    def test_full_name_with_middle_name(self):
        result = formatted_name("johny", "smith", "michael")
        self.assertEqual(result, "Johny Michael Smith")

    def test_full_name_with_empty_middle_name(self):
        result = formatted_name("johny", "smith", "")
        self.assertEqual(result, "Johny Smith")

    def test_names_without_last_name(self):
        result = formatted_name("johny", "", "michael")
        self.assertEqual(result, "Johny Michael ")


if __name__ == '__main__':
    unittest.main()
