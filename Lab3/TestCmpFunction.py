'''
    Right - Easy test just to validate that the function does what it has to do. 
    Validated that the metadata is different and validate that the file content is equal
    B - I did not find any test case for Boundaries test
    I - I did not find any test case for Inverse relationships test
    C - I did not find any test case for Cross-check test
    E - I did not find any test case for Errors test
    P - I tested the function using large files to check the performance and if it returns the correct result
'''

import unittest
import filecmp

class TestMathCeilFunction(unittest.TestCase):

    # Compare file metadata
    def test_positive_metadata(self):
        self.assertTrue(filecmp.cmp("Equal1.txt", "Equal2TestFile.txt"))

    # Compare file equal content
    def test_equal_content(self):
        self.assertTrue(filecmp.cmp("Equal1.txt", "Equal2TestFile.txt", False))

    # Compare file diffrent content
    def test_different_content(self):
        self.assertFalse(filecmp.cmp("Equal1.txt", "Different.txt", False))

    def test_same_different_content_largefile(self):
        self.assertFalse(filecmp.cmp("LargeFile.txt", "Different.txt", False))

    def test_same_equal_content_largefile(self):
        self.assertTrue(filecmp.cmp("LargeFile.txt", "LargeFileEqual2.txt", False))


if __name__ == '__main__':
    unittest.main()