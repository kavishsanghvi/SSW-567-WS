"""
author: @kavishsanghvi
@purpose: to classify triangles and use an automated test platform
"""

import unittest   

def classifyTriangle(a, b, c):
    """ classify different types of triangle

        :param a: The side of a triangle
        :type a: float
        :param b: The side of a triangle
        :type b: float
        :param c: The side of a triangle
        :type c: float
        :rtype: str
        :return: str
    """

    if (a * a) + (b * b) == (c * c) or (b * b) + (c * c) == (a * a) or (c * c) + (b * b) == (a * a):
        return 'Right'

    if a == b and b == c and a == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        """ test classify triangle function

            :rtype: None
            :return: None
        """
        
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testSet2(self): 
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(233, 233, 233), 'Isosceles')
        self.assertEqual(classifyTriangle(2, 3, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(10, 15, 30), 'Scalene')

    def testSet3(self):
        """ test classify triangle function

            :rtype: None
            :return: None
        """

        self.assertEqual(classifyTriangle(10, 10, 1), 'Isosceles')
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene')
        self.assertEqual(classifyTriangle(10, 15, 30), 'Scalene')
        self.assertNotEqual(classifyTriangle(19, 9, 9), 'Equilateral')
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isosceles')
        
    def testSet4(self): 
        """ test classify triangle function

            :rtype: None
            :return: None
        """
        
        self.assertEqual(classifyTriangle(3, 4, 5), 'Equilateral')

if __name__ == '__main__':
    classifyTriangle
    unittest.main(exit=False)
