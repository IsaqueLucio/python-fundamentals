# Python Core & OOP Fundamentals

Welcome to my Python development portfolio. This repository contains a comprehensive learning journey through Python, from fundamental syntax to advanced concepts and real-world applications. It's designed to build a solid foundation in Python programming, data structures, and Object-Oriented Programming (OOP) principles.

## Project Structure

```
PythonCore/
├── 01_basics/                 # Python fundamentals and control flow
│   ├── exercises/             # Practical exercises
│   └── teory_concepts/        # Theoretical concepts and examples
├── 02_functions/              # Function definition and advanced concepts
│   ├── exercises/             # Practical exercises
│   └── teory_concepts/        # Theoretical concepts and examples
├── 03_data_structures/        # Lists, tuples, dictionaries, sets
│   ├── exercises/             # Practical exercises
│   └── teory_concepts/        # Theoretical concepts and examples
├── 04_oop/                    # Object-oriented programming concepts
│   ├── exercises/             # Practical exercises
│   └── teory_concepts/        # Theoretical concepts and examples
├── 05_advanced/               # Advanced Python topics
│   ├── exercises/             # Practical exercises
│   └── teory_concepts/        # Theoretical concepts and examples
├── 06_libraries/              # Popular Python libraries and tools
│   ├── integrated library exercises/  # Real-world library applications
│   └── libraries/             # Library-specific examples
├── 07_frameworks/             # Web frameworks and APIs
│   ├── django/                # Django web framework
│   └── fastAPI/               # FastAPI framework
├── 08_projects/               # Practical projects and applications
│   ├── 01_calculator/
│   ├── 02_guessing_game/
│   ├── 03_api_project/
│   ├── 04_automation_scripts/
│   └── 05_final_project/
└── 09_challenges/             # Coding challenges and logic problems
    ├── delivery_fee_calculator/
    ├── hours_to_seconds/
    ├── loan_validator/
    ├── number_to_alphabet/
    ├── text_to_number_cipher/
    └── two_sum/
```

## Learning Path

### 01_basics/
Foundation of Python programming including:
* **Variables & Types** - Dynamic typing and type inference
* **Input/Output** - Interacting with users
* **Operators** - Arithmetic, comparison, logical, and assignment operators
* **Conditionals** - Decision making with `if`, `elif`, `else`
* **Loops** - Iteration with `for` and `while` loops

### 02_functions/
Modularization and code reusability:
* **Function Basics** - Definition, calling, and parameters
* **Parameters & Return** - Advanced parameters, `*args`, `**kwargs`, return values
* **Lambda Functions** - Anonymous functions and functional programming

### 03_data_structures/
Core data collection types:
* **Lists** - Ordered, mutable sequences
* **Tuples** - Ordered, immutable sequences
* **Dictionaries** - Key-value pair storage
* **Sets** - Unordered, unique collections

### 04_oop/
Object-Oriented Programming principles:
* **Classes & Objects** - Blueprints and instantiation
* **Inheritance** - Creating class hierarchies
* **Encapsulation** - Data hiding and access control
* **Polymorphism** - Method overriding and dynamic resolution

### 05_advanced/
Advanced Python concepts:
* **Modules & Packages** - Organizing code into reusable components
* **Error Handling** - Exception handling and custom exceptions
* **Decorators** - Function and class decorators
* **Generators** - Lazy evaluation and memory efficiency
* **Context Managers** - Resource management with `with` statements

### 06_libraries/
Popular Python libraries with integrated exercises:
* **requests** - HTTP requests and API interactions
* **pandas** - Data manipulation and analysis
* **numpy** - Numerical computing
* Integrated exercises: API fetching, data healing, e-commerce analytics

### 07_frameworks/
Web frameworks and API development:
* **Django** - Full-featured web framework with ORM and admin panel
  - Database models and migrations
  - URL routing and views
  - Admin interface
* **FastAPI** - Modern, fast Python web framework for building APIs

### 08_projects/
Practical applications and full projects:
* **Calculator** - Basic arithmetic operations
* **Guessing Game** - Interactive game with logic
* **API Project** - Working with external APIs
* **Automation Scripts** - Scripting and automation tasks
* **Final Project** - Capstone project integrating all concepts

### 09_challenges/
Coding challenges and logic problems:
* **Delivery Fee Calculator** - Conditional logic and calculations
* **Hours to Seconds** - Unit conversion
* **Loan Validator** - Complex validation logic
* **Number to Alphabet** - Character mapping and transformation
* **Text to Number Cipher** - Encoding/decoding algorithms
* **Two Sum** - Algorithm problem solving

## Technologies & Tools

* **Language:** Python 3.8+
* **Paradigm:** Multi-paradigm (Procedural & Object-Oriented Programming)
* **Architecture:** Console Scripts, Web Applications, & APIs
* **Frameworks:** Django, FastAPI
* **Libraries:** pandas, numpy, requests
* **IDE:** Visual Studio Code
* **Version Control:** Git
* **Database:** SQLite (Django)

## Getting Started

### Prerequisites
* Python 3.8 or higher
* pip (Python package manager)
* Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd PythonCore

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Learning Path
1. Start with the `01_basics/` directory - learn Python fundamentals
2. Progress through `02_functions/` through `05_advanced/`
3. Study `04_oop/` for object-oriented principles
4. Explore `06_libraries/` for practical library usage
5. Build applications with `07_frameworks/` (Django & FastAPI)
6. Complete projects in `08_projects/`
7. Challenge yourself with `09_challenges/`

## How to Use

### For Learning Theory
1. Navigate to the `teory_concepts/` folder in each module
2. Each file demonstrates a specific concept with explanations
3. Read through comments and run the code to understand behavior

### For Practice
1. Navigate to the `exercises/` folder in each module
2. Solve exercises in numbered folders (exe_01, exe_02, etc.)
3. Progress to `integrated_concepts_exercises/` for comprehensive challenges

### Running Scripts
```bash
# Run any Python script
python path/to/filename.py

# Run with arguments (if the script accepts them)
python path/to/filename.py arg1 arg2
```

### Working with Frameworks
```bash
# For Django projects
cd 07_frameworks/django
python manage.py runserver

# For FastAPI projects
cd 07_frameworks/fastAPI
uvicorn main:app --reload
```

### File Organization
* **Theory Concepts** - Foundational explanations and examples
* **Exercises** - Hands-on coding problems (exe_01, exe_02, etc.)
* **Integrated Exercises** - Combine multiple concepts into real-world scenarios
* **Projects** - Full applications demonstrating complete workflows
* **Challenges** - Algorithm and logic problems

## Author

**Isaque Lucio**
4th Semester Analysis and Systems Development Student | Aspiring Back-end & DevOps Developer

## License

This project is open source and available under the MIT License.
