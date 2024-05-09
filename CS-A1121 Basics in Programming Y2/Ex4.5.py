import unittest
#from jump import jump

# Implement a test inside the given function that shows a flaw in the function "jump"
# the test should pass when the "jump" function works accordingly.

def jump(result):

    if result > 228:
        return("The jumper qualifies for the final.")
    else:
        return("The jumper does not qualify.")

class TestJumpFunction(unittest.TestCase):

    # Implement your function here:

    
    def test_1(self):
        word = "The jumper qualifies for the final."
        word2 = "The jumper does not qualify."
        self.assertEqual(jump(228.00000000000001), word)

   

if __name__ == '__main__':
    unittest.main()
