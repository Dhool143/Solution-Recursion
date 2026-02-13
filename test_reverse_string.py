
    


import unittest
from main import reverse_string
class TestReverString(unittest.TestCase):
  
  # Normal case test
  
  def test_hello(self):
    self.assertEqual(reverse_string("hello"), "olleh")
    
    
  def test_world(self):
    self.assertEqual(reverse_string("world"), "dlrow")
    
  def test_pen(self):
    self.assertEqual(reverse_string("pen"), "nep")
    
    
    
    # Edge case test
    
    
    
  def test_empty_string(self):
    self.assertEqual(reverse_string(""), "")
    
  def test_single_chacarter(self):
    self.assertEqual(reverse_string("f"), "f")
    
    
  def test_space(self):
    self.assertEqual(reverse_string(" "), " ")
    
    
if __name__ == "__main__":
  unittest.main()
  