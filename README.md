Largest Rectangle Area Calculator
This is a simple web application that calculates the largest rectangle area given a list of heights. The application is built using Python and Flask for the backend, and HTML for the user interface.

How It Works
Start the application by running python app.py in the terminal.
Open a web browser and visit http://localhost:5000.
You will see a web form where you can enter a list of heights. The heights should be entered as a comma-separated list of numbers. For example, you can enter 2,1,5,6,2,3 as the heights.
Click the "Calculate" button to submit the form.
The application will calculate the largest rectangle area based on the provided heights and display the result on the page.
Example
Suppose you want to calculate the largest rectangle area for the heights [2, 1, 5, 6, 2, 3].

Enter 2,1,5,6,2,3 in the input field.
Click the "Calculate" button.
The application will process the input and calculate the largest rectangle area.
The result, 10, will be displayed on the page.
You can try different sets of heights by entering a comma-separated list of numbers in the input field. The application will handle the user input and provide the corresponding results.

Testing
The application includes a test suite that covers the calculation logic of the Solution class and the user interface using Selenium for end-to-end testing.

To run the tests, execute the following command in the terminal:

bash
Copy code
python -m unittest app.py
The test suite will run, and you will see the test results in the terminal output.
