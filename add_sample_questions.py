"""
Sample Questions Setup Script
Run this script to populate the questions table with sample test questions
"""

import sqlite3
import json
import os

def add_sample_questions():
    """Add sample questions to the database"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'sga.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Clear existing questions first
        cursor.execute("DELETE FROM questions")
        print("✓ Cleared existing questions")

        # Sample questions for Python
        python_questions = [
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'What is the output of print(2 ** 3)?',
                'options': json.dumps(['6', '8', '9', '16']),
                'correct_answer': '8',
                'explanation': 'The ** operator is exponentiation in Python.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'Which of the following is NOT a valid Python data type?',
                'options': json.dumps(['int', 'str', 'float', 'integer']),
                'correct_answer': 'integer',
                'explanation': 'Python uses "int" for integers, not "integer".',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'code',
                'question_text': 'Write a Python function that takes a list of numbers and returns the sum of all even numbers in the list.',
                'options': None,
                'correct_answer': 'def sum_even_numbers(numbers):\n    return sum(num for num in numbers if num % 2 == 0)',
                'explanation': 'Use list comprehension with modulo operator to filter even numbers.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'What does the "len()" function do in Python?',
                'options': json.dumps(['Returns the length of a string', 'Returns the length of a list or string', 'Creates a new list', 'Sorts a list']),
                'correct_answer': 'Returns the length of a list or string',
                'explanation': 'len() returns the number of items in a container.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'Which keyword is used to define a function in Python?',
                'options': json.dumps(['function', 'def', 'func', 'define']),
                'correct_answer': 'def',
                'explanation': 'def keyword is used to define functions in Python.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'code',
                'question_text': 'Write a Python function that checks if a number is prime.',
                'options': None,
                'correct_answer': 'def is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True',
                'explanation': 'Check divisibility from 2 to square root of n.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'What is a list comprehension in Python?',
                'options': json.dumps(['A way to create lists', 'A way to sort lists', 'A way to filter lists', 'A way to create dictionaries']),
                'correct_answer': 'A way to create lists',
                'explanation': 'List comprehensions provide a concise way to create lists.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'Which of the following is used to handle exceptions in Python?',
                'options': json.dumps(['try-except', 'if-else', 'for-loop', 'while-loop']),
                'correct_answer': 'try-except',
                'explanation': 'try-except blocks are used for exception handling.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'code',
                'question_text': 'Write a Python function that reverses a string.',
                'options': None,
                'correct_answer': 'def reverse_string(s):\n    return s[::-1]',
                'explanation': 'Use slicing with negative step to reverse the string.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'What does the "import" statement do in Python?',
                'options': json.dumps(['Exports modules', 'Imports modules', 'Creates modules', 'Deletes modules']),
                'correct_answer': 'Imports modules',
                'explanation': 'import statement is used to include external modules.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'Which data structure uses LIFO (Last In, First Out) principle?',
                'options': json.dumps(['Queue', 'Stack', 'List', 'Dictionary']),
                'correct_answer': 'Stack',
                'explanation': 'Stack follows LIFO principle.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'code',
                'question_text': 'Write a Python function that calculates factorial of a number using recursion.',
                'options': None,
                'correct_answer': 'def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n-1)',
                'explanation': 'Recursive function that multiplies n by factorial of n-1.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'What is the purpose of the "__init__" method in Python classes?',
                'options': json.dumps(['To delete objects', 'To initialize objects', 'To compare objects', 'To print objects']),
                'correct_answer': 'To initialize objects',
                'explanation': '__init__ is the constructor method that initializes object attributes.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'python',
                'question_type': 'mcq',
                'question_text': 'Which module is used for regular expressions in Python?',
                'options': json.dumps(['regex', 're', 'regexp', 'pattern']),
                'correct_answer': 're',
                'explanation': 'The re module provides regular expression operations.',
                'difficulty': 'intermediate'
            }
        ]

        # Sample questions for JavaScript
        javascript_questions = [
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'What does "===" mean in JavaScript?',
                'options': json.dumps(['Assignment', 'Strict equality', 'Loose equality', 'Comparison']),
                'correct_answer': 'Strict equality',
                'explanation': '=== checks for both value and type equality.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'Which method adds an element to the end of an array?',
                'options': json.dumps(['push()', 'pop()', 'shift()', 'unshift()']),
                'correct_answer': 'push()',
                'explanation': 'push() adds elements to the end of an array.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'code',
                'question_text': 'Write a JavaScript function that reverses a string.',
                'options': None,
                'correct_answer': 'function reverseString(str) {\n    return str.split("").reverse().join("");\n}',
                'explanation': 'Split into array, reverse, then join back to string.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'What will console.log(typeof null) output?',
                'options': json.dumps(['null', 'undefined', 'object', 'boolean']),
                'correct_answer': 'object',
                'explanation': 'In JavaScript, typeof null returns "object" (this is a known bug).',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'Which of these is NOT a JavaScript data type?',
                'options': json.dumps(['string', 'boolean', 'integer', 'undefined']),
                'correct_answer': 'integer',
                'explanation': 'JavaScript uses "number" for all numeric types, not "integer".',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'code',
                'question_text': 'Write a JavaScript function that finds the maximum number in an array.',
                'options': None,
                'correct_answer': 'function findMax(arr) {\n    return Math.max(...arr);\n}',
                'explanation': 'Use spread operator with Math.max to find maximum value.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'What is the difference between "==" and "===" in JavaScript?',
                'options': json.dumps(['No difference', '=== checks type and value', '== checks type only', '=== is for strings only']),
                'correct_answer': '=== checks type and value',
                'explanation': '=== performs strict equality checking both value and type.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'Which method removes the last element from an array?',
                'options': json.dumps(['pop()', 'push()', 'shift()', 'unshift()']),
                'correct_answer': 'pop()',
                'explanation': 'pop() removes and returns the last element of an array.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'code',
                'question_text': 'Write a JavaScript function that checks if a string is a palindrome.',
                'options': None,
                'correct_answer': 'function isPalindrome(str) {\n    const reversed = str.split("").reverse().join("");\n    return str === reversed;\n}',
                'explanation': 'Reverse the string and compare with original.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'What does the "this" keyword refer to in JavaScript?',
                'options': json.dumps(['The global object', 'The current function', 'Depends on context', 'The parent object']),
                'correct_answer': 'Depends on context',
                'explanation': '"this" refers to different things based on how the function is called.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'Which of the following is NOT a JavaScript loop?',
                'options': json.dumps(['for', 'while', 'foreach', 'do-while']),
                'correct_answer': 'foreach',
                'explanation': 'JavaScript has forEach method, not foreach loop.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'code',
                'question_text': 'Write a JavaScript arrow function that doubles each number in an array.',
                'options': None,
                'correct_answer': 'const doubleArray = arr => arr.map(num => num * 2);',
                'explanation': 'Use arrow function with map to double each element.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'javascript',
                'question_type': 'mcq',
                'question_text': 'What is a closure in JavaScript?',
                'options': json.dumps(['A way to close functions', 'A function with access to outer scope', 'A method to end loops', 'A type of variable']),
                'correct_answer': 'A function with access to outer scope',
                'explanation': 'Closures allow functions to access variables from their outer scope.',
                'difficulty': 'advanced'
            }
        ]

        # Sample questions for SQL
        sql_questions = [
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'Which SQL clause is used to filter records?',
                'options': json.dumps(['SELECT', 'WHERE', 'FROM', 'ORDER BY']),
                'correct_answer': 'WHERE',
                'explanation': 'WHERE clause filters records based on conditions.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'What does JOIN do in SQL?',
                'options': json.dumps(['Deletes records', 'Combines tables', 'Sorts records', 'Groups records']),
                'correct_answer': 'Combines tables',
                'explanation': 'JOIN combines rows from two or more tables.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'code',
                'question_text': 'Write an SQL query to find all users whose name starts with "A".',
                'options': None,
                'correct_answer': 'SELECT * FROM users WHERE name LIKE "A%";',
                'explanation': 'Use LIKE with wildcard % to match names starting with A.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'Which SQL command is used to remove all records from a table?',
                'options': json.dumps(['DELETE', 'DROP', 'TRUNCATE', 'REMOVE']),
                'correct_answer': 'TRUNCATE',
                'explanation': 'TRUNCATE removes all rows from a table without logging individual row deletions.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'What does GROUP BY do in SQL?',
                'options': json.dumps(['Sorts results', 'Groups rows with same values', 'Filters results', 'Joins tables']),
                'correct_answer': 'Groups rows with same values',
                'explanation': 'GROUP BY groups rows that have the same values in specified columns.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'code',
                'question_text': 'Write an SQL query to find the total salary by department.',
                'options': None,
                'correct_answer': 'SELECT department, SUM(salary) FROM employees GROUP BY department;',
                'explanation': 'Use SUM() aggregate function with GROUP BY to calculate totals per group.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'What is a primary key in SQL?',
                'options': json.dumps(['A unique identifier for a record', 'A foreign key reference', 'An index for faster searches', 'A constraint for data types']),
                'correct_answer': 'A unique identifier for a record',
                'explanation': 'Primary key uniquely identifies each record in a table.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_type': 'mcq',
                'question_text': 'Which SQL command is used to modify existing records?',
                'options': json.dumps(['INSERT', 'UPDATE', 'DELETE', 'ALTER']),
                'correct_answer': 'UPDATE',
                'explanation': 'UPDATE command modifies existing records in a table.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'code',
                'question_text': 'Write an SQL query to find employees with salary greater than 50000.',
                'options': None,
                'correct_answer': 'SELECT * FROM employees WHERE salary > 50000;',
                'explanation': 'Use WHERE clause with comparison operator.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'What does INNER JOIN do?',
                'options': json.dumps(['Returns all records', 'Returns matching records only', 'Returns left table records', 'Returns right table records']),
                'correct_answer': 'Returns matching records only',
                'explanation': 'INNER JOIN returns only records that have matching values in both tables.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'Which aggregate function counts the number of rows?',
                'options': json.dumps(['SUM', 'AVG', 'COUNT', 'MAX']),
                'correct_answer': 'COUNT',
                'explanation': 'COUNT() function returns the number of rows that match the query.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'sql',
                'question_type': 'code',
                'question_text': 'Write an SQL query to find the average salary by department, ordered by average salary descending.',
                'options': None,
                'correct_answer': 'SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary) DESC;',
                'explanation': 'Use AVG() with GROUP BY and ORDER BY for descending sort.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'sql',
                'question_type': 'mcq',
                'question_text': 'What is a foreign key?',
                'options': json.dumps(['A primary key from another table', 'A unique key in the same table', 'An index for performance', 'A constraint on data types']),
                'correct_answer': 'A primary key from another table',
                'explanation': 'Foreign key references the primary key of another table.',
                'difficulty': 'intermediate'
            }
        ]

        # Sample questions for HTML/CSS
        html_questions = [
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'Which tag is used to create a hyperlink in HTML?',
                'options': json.dumps(['<link>', '<a>', '<href>', '<url>']),
                'correct_answer': '<a>',
                'explanation': 'The <a> tag defines a hyperlink in HTML.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'Which CSS property controls text color?',
                'options': json.dumps(['font-color', 'text-color', 'color', 'background-color']),
                'correct_answer': 'color',
                'explanation': 'The color property sets the color of text.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'Which HTML element is used for the largest heading?',
                'options': json.dumps(['<h1>', '<h6>', '<head>', '<header>']),
                'correct_answer': '<h1>',
                'explanation': '<h1> is the largest heading tag, <h6> is the smallest.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'What does CSS stand for?',
                'options': json.dumps(['Computer Style Sheets', 'Cascading Style Sheets', 'Creative Style Sheets', 'Colorful Style Sheets']),
                'correct_answer': 'Cascading Style Sheets',
                'explanation': 'CSS stands for Cascading Style Sheets.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'Which attribute is used to provide alternative text for images?',
                'options': json.dumps(['title', 'alt', 'src', 'href']),
                'correct_answer': 'alt',
                'explanation': 'The alt attribute provides alternative text for images.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'What is the purpose of the <div> tag?',
                'options': json.dumps(['To create divisions or sections', 'To create links', 'To create images', 'To create forms']),
                'correct_answer': 'To create divisions or sections',
                'explanation': '<div> is a block-level element used to group content.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'Which tag is used to create an unordered list?',
                'options': json.dumps(['<ol>', '<ul>', '<li>', '<list>']),
                'correct_answer': '<ul>',
                'explanation': '<ul> creates an unordered (bulleted) list.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'How do you select an element with id "header" in CSS?',
                'options': json.dumps(['#header', '.header', 'header', '*header']),
                'correct_answer': '#header',
                'explanation': '# is used to select elements by their id attribute.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'What does the "display: flex" property do?',
                'options': json.dumps(['Makes element invisible', 'Creates a flexbox layout', 'Changes text color', 'Adds borders']),
                'correct_answer': 'Creates a flexbox layout',
                'explanation': 'display: flex enables flexbox layout for the element.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'What does the <form> tag do?',
                'options': json.dumps(['Creates a table', 'Creates a form for user input', 'Creates a link', 'Creates an image']),
                'correct_answer': 'Creates a form for user input',
                'explanation': '<form> element is used to create HTML forms.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'Which property is used to change the background color?',
                'options': json.dumps(['color', 'background-color', 'bgcolor', 'background']),
                'correct_answer': 'background-color',
                'explanation': 'background-color property sets the background color of an element.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'What is the correct HTML for creating a checkbox?',
                'options': json.dumps(['<input type="checkbox">', '<checkbox>', '<input type="check">', '<check>']),
                'correct_answer': '<input type="checkbox">',
                'explanation': 'Checkbox input is created with <input type="checkbox">.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'What does "margin: 10px 20px" mean?',
                'options': json.dumps(['10px top/bottom, 20px left/right', '10px all sides', '20px top/bottom, 10px left/right', '10px left/right only']),
                'correct_answer': '10px top/bottom, 20px left/right',
                'explanation': 'Two values: first for top/bottom, second for left/right.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'Which tag is used for the main content of a document?',
                'options': json.dumps(['<body>', '<main>', '<content>', '<article>']),
                'correct_answer': '<main>',
                'explanation': '<main> represents the main content of the document.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'css',
                'question_type': 'mcq',
                'question_text': 'How do you make text bold in CSS?',
                'options': json.dumps(['font-weight: bold', 'text-decoration: bold', 'font-style: bold', 'text-weight: bold']),
                'correct_answer': 'font-weight: bold',
                'explanation': 'font-weight property controls the boldness of text.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'html',
                'question_type': 'mcq',
                'question_text': 'What does the <meta> tag do?',
                'options': json.dumps(['Creates metadata about the document', 'Creates a menu', 'Creates a table', 'Creates a form']),
                'correct_answer': 'Creates metadata about the document',
                'explanation': '<meta> provides metadata about the HTML document.',
                'difficulty': 'intermediate'
            }
        ]

        # Sample questions for React
        react_questions = [
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What is JSX in React?',
                'options': json.dumps(['A database', 'A syntax extension for JavaScript', 'A CSS framework', 'A testing library']),
                'correct_answer': 'A syntax extension for JavaScript',
                'explanation': 'JSX is a syntax extension that allows writing HTML-like code in JavaScript.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What hook is used to manage state in functional components?',
                'options': json.dumps(['useEffect', 'useState', 'useContext', 'useReducer']),
                'correct_answer': 'useState',
                'explanation': 'useState hook is used to add state to functional components.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'code',
                'question_text': 'Write a simple React functional component that displays "Hello World".',
                'options': None,
                'correct_answer': 'function HelloWorld() {\n    return <h1>Hello World</h1>;\n}',
                'explanation': 'Basic functional component returning JSX.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What is the purpose of useEffect hook?',
                'options': json.dumps(['To manage state', 'To handle side effects', 'To create components', 'To handle events']),
                'correct_answer': 'To handle side effects',
                'explanation': 'useEffect hook is used to perform side effects in functional components.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What is a React component?',
                'options': json.dumps(['A JavaScript function or class', 'An HTML element', 'A CSS class', 'A database table']),
                'correct_answer': 'A JavaScript function or class',
                'explanation': 'React components are JavaScript functions or classes that return JSX.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'react',
                'question_type': 'code',
                'question_text': 'Write a React component that uses useState to manage a counter.',
                'options': None,
                'correct_answer': 'function Counter() {\n    const [count, setCount] = useState(0);\n    return (\n        <div>\n            <p>Count: {count}</p>\n            <button onClick={() => setCount(count + 1)}>Increment</button>\n        </div>\n    );\n}',
                'explanation': 'Use useState hook to manage counter state and onClick handler.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What does props stand for in React?',
                'options': json.dumps(['Properties', 'Parameters', 'Functions', 'Components']),
                'correct_answer': 'Properties',
                'explanation': 'Props (properties) are used to pass data from parent to child components.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'Which method is used to render a React component?',
                'options': json.dumps(['render()', 'display()', 'show()', 'ReactDOM.render()']),
                'correct_answer': 'ReactDOM.render()',
                'explanation': 'ReactDOM.render() is used to render React components to the DOM.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'code',
                'question_text': 'Write a React component that maps over an array of names and displays them in a list.',
                'options': None,
                'correct_answer': 'function NameList({ names }) {\n    return (\n        <ul>\n            {names.map((name, index) => (\n                <li key={index}>{name}</li>\n            ))}\n        </ul>\n    );\n}',
                'explanation': 'Use map() to iterate over array and return list items with unique keys.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'What is the virtual DOM in React?',
                'options': json.dumps(['A copy of the real DOM', 'A database', 'A styling system', 'A routing library']),
                'correct_answer': 'A copy of the real DOM',
                'explanation': 'Virtual DOM is a lightweight copy of the real DOM that React uses for optimization.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'react',
                'question_type': 'mcq',
                'question_text': 'Which hook is used for context in React?',
                'options': json.dumps(['useContext', 'useState', 'useEffect', 'useReducer']),
                'correct_answer': 'useContext',
                'explanation': 'useContext hook is used to consume context values.',
                'difficulty': 'advanced'
            },
            {
                'skill_name': 'react',
                'question_type': 'code',
                'question_text': 'Write a React component that fetches data using useEffect.',
                'options': None,
                'correct_answer': 'function DataComponent() {\n    const [data, setData] = useState(null);\n    \n    useEffect(() => {\n        fetch("/api/data")\n            .then(response => response.json())\n            .then(setData);\n    }, []);\n    \n    return <div>{data ? JSON.stringify(data) : "Loading..."}</div>;\n}',
                'explanation': 'Use useEffect with empty dependency array to fetch data on mount.',
                'difficulty': 'advanced'
            }
        ]

        # Sample questions for Git
        git_questions = [
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What command is used to stage files for commit?',
                'options': json.dumps(['git add', 'git commit', 'git push', 'git pull']),
                'correct_answer': 'git add',
                'explanation': 'git add stages files for the next commit.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What does "git clone" do?',
                'options': json.dumps(['Creates a new repository', 'Copies an existing repository', 'Deletes a repository', 'Merges branches']),
                'correct_answer': 'Copies an existing repository',
                'explanation': 'git clone creates a copy of an existing repository.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'code',
                'question_text': 'Write the command to create a new branch called "feature-login".',
                'options': None,
                'correct_answer': 'git checkout -b feature-login',
                'explanation': 'git checkout -b creates and switches to a new branch.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What does "git status" show?',
                'options': json.dumps(['Repository history', 'Current branch status', 'Remote repository info', 'Commit messages']),
                'correct_answer': 'Current branch status',
                'explanation': 'git status shows the current state of the working directory and staging area.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What is a Git merge conflict?',
                'options': json.dumps(['When two branches have different commits', 'When Git cannot merge branches automatically', 'When files are deleted', 'When commits are lost']),
                'correct_answer': 'When Git cannot merge branches automatically',
                'explanation': 'Merge conflicts occur when Git cannot automatically resolve differences between branches.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'git',
                'question_type': 'code',
                'question_text': 'Write the command to see the commit history.',
                'options': None,
                'correct_answer': 'git log',
                'explanation': 'git log shows the commit history of the repository.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What does "git pull" do?',
                'options': json.dumps(['Pushes changes to remote', 'Fetches and merges from remote', 'Creates a new branch', 'Deletes commits']),
                'correct_answer': 'Fetches and merges from remote',
                'explanation': 'git pull fetches changes from remote and merges them into current branch.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What is the staging area in Git?',
                'options': json.dumps(['Where commits are stored', 'Where changes are prepared for commit', 'Where branches are created', 'Where remotes are configured']),
                'correct_answer': 'Where changes are prepared for commit',
                'explanation': 'Staging area holds changes that will be included in the next commit.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'git',
                'question_type': 'code',
                'question_text': 'Write the command to undo the last commit but keep changes staged.',
                'options': None,
                'correct_answer': 'git reset --soft HEAD~1',
                'explanation': 'git reset --soft HEAD~1 undoes the last commit but keeps changes staged.',
                'difficulty': 'advanced'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What does "git stash" do?',
                'options': json.dumps(['Deletes uncommitted changes', 'Saves uncommitted changes temporarily', 'Commits all changes', 'Shows hidden files']),
                'correct_answer': 'Saves uncommitted changes temporarily',
                'explanation': 'git stash temporarily saves uncommitted changes so you can work on something else.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'git',
                'question_type': 'mcq',
                'question_text': 'What is a Git remote?',
                'options': json.dumps(['A local branch', 'A remote repository', 'A commit', 'A tag']),
                'correct_answer': 'A remote repository',
                'explanation': 'A remote is a reference to a remote repository.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'git',
                'question_type': 'code',
                'question_text': 'Write the command to see differences between working directory and last commit.',
                'options': None,
                'correct_answer': 'git diff',
                'explanation': 'git diff shows changes between working directory and staging area.',
                'difficulty': 'intermediate'
            }
        ]

        # Sample questions for Node.js
        nodejs_questions = [
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'What does npm stand for?',
                'options': json.dumps(['Node Package Manager', 'New Package Manager', 'Node Project Manager', 'Network Package Manager']),
                'correct_answer': 'Node Package Manager',
                'explanation': 'npm is the package manager for Node.js.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'Which module is used to create a web server in Node.js?',
                'options': json.dumps(['fs', 'http', 'path', 'os']),
                'correct_answer': 'http',
                'explanation': 'The http module provides HTTP server and client functionality.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'What is the event loop in Node.js?',
                'options': json.dumps(['A loop that handles events', 'A database connection', 'A file system', 'A web server']),
                'correct_answer': 'A loop that handles events',
                'explanation': 'The event loop is what allows Node.js to perform non-blocking I/O operations.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'code',
                'question_text': 'Write a simple Node.js HTTP server that responds with "Hello World".',
                'options': None,
                'correct_answer': 'const http = require("http");\nconst server = http.createServer((req, res) => {\n    res.writeHead(200, {"Content-Type": "text/plain"});\n    res.end("Hello World");\n});\nserver.listen(3000);',
                'explanation': 'Create HTTP server using http module and listen on port 3000.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'Which method is used to read files asynchronously in Node.js?',
                'options': json.dumps(['readFile', 'readFileSync', 'readAsync', 'read']),
                'correct_answer': 'readFile',
                'explanation': 'readFile method from fs module reads files asynchronously.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'What does "require()" do in Node.js?',
                'options': json.dumps(['Exports modules', 'Imports modules', 'Creates modules', 'Deletes modules']),
                'correct_answer': 'Imports modules',
                'explanation': 'require() function is used to import modules in Node.js.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'code',
                'question_text': 'Write Node.js code to read a file and log its contents.',
                'options': None,
                'correct_answer': 'const fs = require("fs");\nfs.readFile("file.txt", "utf8", (err, data) => {\n    if (err) throw err;\n    console.log(data);\n});',
                'explanation': 'Use fs.readFile with callback to read file asynchronously.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'What is middleware in Express.js?',
                'options': json.dumps(['Database queries', 'Functions that process requests', 'HTML templates', 'CSS styles']),
                'correct_answer': 'Functions that process requests',
                'explanation': 'Middleware functions have access to request and response objects.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'Which package is commonly used for routing in Node.js?',
                'options': json.dumps(['mongoose', 'express', 'socket.io', 'passport']),
                'correct_answer': 'express',
                'explanation': 'Express.js is a web application framework for Node.js.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'code',
                'question_text': 'Write an Express.js route that handles GET requests to "/api/users".',
                'options': None,
                'correct_answer': 'app.get("/api/users", (req, res) => {\n    res.json({ users: [] });\n});',
                'explanation': 'Use app.get() to define a route handler for GET requests.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'What is npm init used for?',
                'options': json.dumps(['Install packages', 'Create package.json', 'Run scripts', 'Update Node.js']),
                'correct_answer': 'Create package.json',
                'explanation': 'npm init creates a package.json file for your project.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'nodejs',
                'question_type': 'mcq',
                'question_text': 'Which module is used for path operations in Node.js?',
                'options': json.dumps(['fs', 'http', 'path', 'url']),
                'correct_answer': 'path',
                'explanation': 'The path module provides utilities for working with file and directory paths.',
                'difficulty': 'intermediate'
            }
        ]

        # Sample questions for Data Science
        datascience_questions = [
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'Which Python library is commonly used for data manipulation and analysis?',
                'options': json.dumps(['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']),
                'correct_answer': 'Pandas',
                'explanation': 'Pandas is the primary library for data manipulation in Python.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'What does CSV stand for?',
                'options': json.dumps(['Computer System Values', 'Comma Separated Values', 'Common Style Variables', 'Cascading Style Values']),
                'correct_answer': 'Comma Separated Values',
                'explanation': 'CSV is a common format for storing tabular data.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'Which library is used for creating visualizations in Python?',
                'options': json.dumps(['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']),
                'correct_answer': 'Matplotlib',
                'explanation': 'Matplotlib is the primary plotting library in Python.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'What type of machine learning algorithm is used for classification?',
                'options': json.dumps(['Linear Regression', 'Decision Trees', 'K-Means Clustering', 'Principal Component Analysis']),
                'correct_answer': 'Decision Trees',
                'explanation': 'Decision Trees can be used for both classification and regression tasks.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'What does supervised learning require?',
                'options': json.dumps(['No labeled data', 'Labeled training data', 'Only input features', 'Unlabeled data only']),
                'correct_answer': 'Labeled training data',
                'explanation': 'Supervised learning algorithms learn from labeled examples.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'What is the purpose of data cleaning?',
                'options': json.dumps(['To create visualizations', 'To prepare data for analysis', 'To build models', 'To deploy applications']),
                'correct_answer': 'To prepare data for analysis',
                'explanation': 'Data cleaning involves removing errors and inconsistencies from data.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'Which statistical measure describes the spread of data?',
                'options': json.dumps(['Mean', 'Median', 'Standard deviation', 'Mode']),
                'correct_answer': 'Standard deviation',
                'explanation': 'Standard deviation measures how spread out the values are from the mean.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'What is overfitting in machine learning?',
                'options': json.dumps(['Model performs well on training data', 'Model performs poorly on training data', 'Model is too simple', 'Model memorizes training data too well']),
                'correct_answer': 'Model memorizes training data too well',
                'explanation': 'Overfitting occurs when a model learns the training data too well and fails to generalize.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'What does ETL stand for?',
                'options': json.dumps(['Extract, Transform, Load', 'Evaluate, Test, Learn', 'Explore, Train, Launch', 'Edit, Transfer, Link']),
                'correct_answer': 'Extract, Transform, Load',
                'explanation': 'ETL is a process in data warehousing for extracting, transforming, and loading data.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'Which algorithm is used for unsupervised learning?',
                'options': json.dumps(['Linear Regression', 'K-Means Clustering', 'Decision Trees', 'Logistic Regression']),
                'correct_answer': 'K-Means Clustering',
                'explanation': 'K-Means is an unsupervised learning algorithm for clustering data.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'What is a DataFrame in Pandas?',
                'options': json.dumps(['A 2D data structure', 'A 1D data structure', 'A database table', 'A visualization tool']),
                'correct_answer': 'A 2D data structure',
                'explanation': 'DataFrame is a 2-dimensional labeled data structure in Pandas.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'What is cross-validation used for?',
                'options': json.dumps(['To train models faster', 'To evaluate model performance', 'To clean data', 'To visualize data']),
                'correct_answer': 'To evaluate model performance',
                'explanation': 'Cross-validation is used to assess how well a model generalizes to unseen data.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'data science',
                'question_type': 'mcq',
                'question_text': 'Which library is used for numerical computing in Python?',
                'options': json.dumps(['Pandas', 'NumPy', 'Matplotlib', 'Seaborn']),
                'correct_answer': 'NumPy',
                'explanation': 'NumPy provides support for large, multi-dimensional arrays and matrices.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'machine learning',
                'question_type': 'mcq',
                'question_text': 'What is the bias-variance tradeoff?',
                'options': json.dumps(['Balance between model complexity and performance', 'Choice between different algorithms', 'Selection of training data', 'Optimization technique']),
                'correct_answer': 'Balance between model complexity and performance',
                'explanation': 'Bias-variance tradeoff involves finding the right balance between underfitting and overfitting.',
                'difficulty': 'advanced'
            }
        ]

        # Sample questions for DevOps/Cloud
        devops_questions = [
            {
                'skill_name': 'docker',
                'question_type': 'mcq',
                'question_text': 'What is Docker primarily used for?',
                'options': json.dumps(['Database management', 'Containerization', 'Web development', 'Testing']),
                'correct_answer': 'Containerization',
                'explanation': 'Docker is a platform for developing, shipping, and running applications in containers.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'docker',
                'question_type': 'code',
                'question_text': 'Write the command to build a Docker image from a Dockerfile.',
                'options': None,
                'correct_answer': 'docker build -t my-image .',
                'explanation': 'docker build command creates an image from a Dockerfile.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'aws',
                'question_type': 'mcq',
                'question_text': 'What AWS service is used for serverless computing?',
                'options': json.dumps(['EC2', 'S3', 'Lambda', 'RDS']),
                'correct_answer': 'Lambda',
                'explanation': 'AWS Lambda is a serverless compute service.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'linux',
                'question_type': 'mcq',
                'question_text': 'Which command is used to list files in a directory in Linux?',
                'options': json.dumps(['dir', 'ls', 'list', 'show']),
                'correct_answer': 'ls',
                'explanation': 'ls command lists directory contents in Linux.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'linux',
                'question_type': 'code',
                'question_text': 'Write the command to change file permissions to read, write, execute for owner and read for group and others.',
                'options': None,
                'correct_answer': 'chmod 755 filename',
                'explanation': '755 gives rwx for owner, rx for group and others.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'docker',
                'question_type': 'mcq',
                'question_text': 'What is a Docker container?',
                'options': json.dumps(['A virtual machine', 'A running instance of an image', 'A Dockerfile', 'A registry']),
                'correct_answer': 'A running instance of an image',
                'explanation': 'A container is a runnable instance of a Docker image.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'docker',
                'question_type': 'mcq',
                'question_text': 'What does "docker run" do?',
                'options': json.dumps(['Builds an image', 'Runs a container', 'Stops a container', 'Deletes an image']),
                'correct_answer': 'Runs a container',
                'explanation': 'docker run creates and starts a container from an image.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'aws',
                'question_type': 'mcq',
                'question_text': 'What is Amazon S3 used for?',
                'options': json.dumps(['Computing', 'Storage', 'Databases', 'Networking']),
                'correct_answer': 'Storage',
                'explanation': 'Amazon S3 is an object storage service.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'aws',
                'question_type': 'mcq',
                'question_text': 'What is Amazon EC2?',
                'options': json.dumps(['Storage service', 'Compute service', 'Database service', 'Networking service']),
                'correct_answer': 'Compute service',
                'explanation': 'Amazon EC2 provides resizable compute capacity in the cloud.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'linux',
                'question_type': 'mcq',
                'question_text': 'Which command is used to find text in files?',
                'options': json.dumps(['find', 'grep', 'locate', 'search']),
                'correct_answer': 'grep',
                'explanation': 'grep searches for patterns in files.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'linux',
                'question_type': 'mcq',
                'question_text': 'What does "sudo" stand for?',
                'options': json.dumps(['Super user do', 'System user do', 'Secure user do', 'Simple user do']),
                'correct_answer': 'Super user do',
                'explanation': 'sudo allows users to run commands as superuser.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'docker',
                'question_type': 'code',
                'question_text': 'Write the command to list all running containers.',
                'options': None,
                'correct_answer': 'docker ps',
                'explanation': 'docker ps lists all running containers.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'aws',
                'question_type': 'mcq',
                'question_text': 'What is AWS RDS?',
                'options': json.dumps(['Relational Database Service', 'Resource Description Service', 'Remote Data Service', 'Regional Data Store']),
                'correct_answer': 'Relational Database Service',
                'explanation': 'AWS RDS is a managed relational database service.',
                'difficulty': 'intermediate'
            },
            {
                'skill_name': 'linux',
                'question_type': 'code',
                'question_text': 'Write the command to see disk usage.',
                'options': None,
                'correct_answer': 'df -h',
                'explanation': 'df -h shows disk space usage in human-readable format.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'docker',
                'question_type': 'mcq',
                'question_text': 'What is a Dockerfile?',
                'options': json.dumps(['A container image', 'A text file with build instructions', 'A running container', 'A registry']),
                'correct_answer': 'A text file with build instructions',
                'explanation': 'A Dockerfile contains instructions to build a Docker image.',
                'difficulty': 'beginner'
            },
            {
                'skill_name': 'aws',
                'question_type': 'mcq',
                'question_text': 'What is AWS CloudFormation?',
                'options': json.dumps(['A computing service', 'Infrastructure as Code service', 'Storage service', 'Monitoring service']),
                'correct_answer': 'Infrastructure as Code service',
                'explanation': 'CloudFormation allows you to model and provision AWS resources using code.',
                'difficulty': 'advanced'
            }
        ]

        # Insert all questions
        all_questions = python_questions + javascript_questions + sql_questions + html_questions + react_questions + git_questions + nodejs_questions + datascience_questions + devops_questions

        for question in all_questions:
            cursor.execute("""
                INSERT INTO questions (skill_name, question_type, question_text, options, correct_answer, explanation, difficulty)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                question['skill_name'],
                question['question_type'],
                question['question_text'],
                question['options'],
                question['correct_answer'],
                question['explanation'],
                question['difficulty']
            ))

        conn.commit()
        print(f"✓ Successfully added {len(all_questions)} sample questions!")

        # Print summary
        cursor.execute("SELECT skill_name, COUNT(*) as count FROM questions GROUP BY skill_name")
        skill_counts = cursor.fetchall()
        print("\nQuestions added by skill:")
        for skill, count in skill_counts:
            print(f"- {skill}: {count} questions")

        cursor.close()
        conn.close()

        return True

    except sqlite3.Error as e:
        print(f"✗ Error adding sample questions: {e}")
        return False

if __name__ == "__main__":
    add_sample_questions()