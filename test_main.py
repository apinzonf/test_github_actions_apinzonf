import unittest
import subprocess

class TestHelloName(unittest.TestCase):
    def test_main_process(self):
        result = subprocess.run(["python", "main.py", "Alex"], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello Alex")
        
        result = subprocess.run(["python", "main.py", "John"], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello John")
        
        result = subprocess.run(["python", "main.py", "Maria"], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello Maria")

if __name__ == "__main__":
    unittest.main()
