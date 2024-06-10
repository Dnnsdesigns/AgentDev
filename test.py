import unittest
from main import generate_code, debug_code, explain_code

class TestAgentDev(unittest.TestCase):

    def test_generate_code(self):
        prompt = "Write a Python function that returns the factorial of a number."
        code = generate_code(prompt)
        self.assertIn("def factorial", code)

    def test_debug_code(self):
        code = "def factorial(n): return n * factorial(n-1)"
        debugged_code = debug_code(code)
        self.assertIn("base case", debugged_code)

    def test_explain_code(self):
        code = "def reverse_string(s): return s[::-1]"
        explanation = explain_code(code)
        self.assertIn("reverses", explanation)

if __name__ == "__main__":
    unittest.main()
