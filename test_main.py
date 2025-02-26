import unittest
import subprocess

class TestHelloName(unittest.TestCase):
    def test_main_process(self):
        for name in ["Alex", "John", "Maria"]:
            print(f"Running test with name: {name}")
            result = subprocess.run(["python", "main.py", name], capture_output=True, text=True)
            print(f"Output: {result.stdout}")
            self.assertEqual(result.stdout.strip(), f"Hello {name}", f"Unexpected output: {result.stdout}")

if __name__ == "__main__":
    unittest.main()
