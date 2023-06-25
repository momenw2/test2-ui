import unittest
from flask import Flask, request, render_template
from selenium import webdriver

app = Flask(__name__)

class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []  # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        heights = list(map(int, request.form['heights'].split(',')))
        solution = Solution()
        max_area = solution.largestRectangleArea(heights)
        return render_template('index.html', max_area=max_area)
    return render_template('index.html')

class SolutionUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:5000')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_largestRectangleArea(self):
        # Test case 1: heights are [2, 1, 5, 6, 2, 3]
        self.driver.find_element_by_id('heights').send_keys('2,1,5,6,2,3')
        self.driver.find_element_by_id('submit').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '10')

        # Test case 2: heights are [1, 1, 1, 1, 1]
        self.driver.find_element_by_id('heights').send_keys('1,1,1,1,1')
        self.driver.find_element_by_id('submit').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '5')

        # Test case 3: heights are [2, 2, 2, 2, 2]
        self.driver.find_element_by_id('heights').send_keys('2,2,2,2,2')
        self.driver.find_element_by_id('submit').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '10')

        # Test case 4: heights are [3, 2, 1, 1, 3]
        self.driver.find_element_by_id('heights').send_keys('3,2,1,1,3')
        self.driver.find_element_by_id('submit').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '5')

        # Test case 5: heights are [1, 2, 3, 4, 5]
        self.driver.find_element_by_id('heights').send_keys('1,2,3,4,5')
        self.driver.find_element_by_id('submit').click()
        result = self.driver.find_element_by_id('result').text
        self.assertEqual(result, '9')

if __name__ == '__main__':
    unittest.main()
