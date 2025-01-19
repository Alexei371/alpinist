# tests/test_logic.py
import unittest
from logic import create_employee, add_route_to_journal, display_journal


class TestLogic(unittest.TestCase):
    def test_create_employee(self):
        emp = create_employee("АльпКлуб", "contact@club.ru", "Иван Иванов", "Тренер", 5)
        self.assertEqual(emp.full_name, "Иван Иванов")
        self.assertEqual(emp.position, "Тренер")
        self.assertEqual(emp.experience, 5)

    def test_add_route_to_journal(self):
        emp = create_employee("АльпКлуб", "contact@club.ru", "Иван Иванов", "Тренер", 5)
        add_route_to_journal(emp, "Эверест", "Сложно")
        self.assertIn("Route: Эверест, Difficulty: Сложно", display_journal(emp))


if __name__ == "__main__":
    unittest.main()
