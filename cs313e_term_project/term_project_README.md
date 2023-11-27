# CS 313E Term Project: Payroll Calculator Documentation

1) What is your project idea?

    My project idea is a payroll calculator that addresses and corrects some isses with the current payroll
    calculator Great Clips uses which does not account for employees working at multiple locations, incorrect
    overtime calculations due to employees working at multiple locations, and lack of concise breakdown of
    vital payroll information for employees and employers.

2) If you use any datasets, describe the dataset and provide how one can access and download it.

    The dataset I use contains vital information on employees names, database IDs, wages, and a breakdown of
    the different types of hours. I obtained this information personally from local Great Clips franchise owners
    in Austin and there is not a public way of accessing this information since it is private. However I have included
    some samples files for testing.

3) Describe your design for main packages, classes, methods, functions, and iterations between them.

    To begin, class functions/behaviors and design was the first priority since they would be the building blocks my core program.
    Most of the classes I created are data classes meaning their sole purpose is to hold the data, specifically the paycheck
    classes. However, my paycheck classes had a few functions such as calculating pay based on the information contained in the
    paycheck class. My employee class is generic as it contains the vital information on the employee like IDs and names, but each
    employee class performs functions on the paycheck class, manipulating and saving information on paycheck information. I did not
    add more methods/functions than neccessary to classes or create more functions than neccessary since the primary goal is to
    solve the defined problem I had. As more issues and/or corrections are needed to solve future problems, more functions and classes
    will be added but for this project I wanted to keep it minimal and solve the immediate issue with the payroll system/calculation.
    There are helper functions which mainly focus on preparing the data in the file, setting up the file, and correctly creating output
    files.

4) Describe any libraries that you used.

    The libraries I used in this project include `csv`, `datetime`, and `pandas`. The `csv` module was mainly used to help me work with
    the .csv files I was using as input and that contained the original payroll information. The `datetime` module was primarily used to
    correct some date-time formatting issues with some input files. Lastly the `pandas` module was used for working with the .csv file's 
    information, helping create tables/dataframes from which I could filter information to make correct payroll calculations.

5) Design some test cases that can test the correctness of your software

    ...

6) What is your current expectation of your software? For example, do you expect that it works well? What are the expected weaknesses?

    I expect this software to run correctly and solve the issues I set out fix in this project with the payroll calculations. However, some
    weaknesses I expect are that as the database (which contains the information and formatting of payroll CSVs) updates and potentially
    reformats the CSV and data in the CSVs, my program will break and I will have to update it or that my program will become redundant as
    they fix the payroll system and calculations. Otherwise, I believe my program will run great any valid Great Clips payroll CSV given to
    it and that it will produce the correct output a majority of the time.