import pytest
import System


#Test 01
#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Test 02
#Tests if the password login can handle the wrong password
def test_check_password(grading_system):
    grading_system.check_password('cmhbf5', 'bestTA')

#Test 03
def test_change_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('akend3','comp_sci','assignment1','80')

#Test 04
def test_create_assignment(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignmentTest','10/15/2020','comp_sci')

#Test 05
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('yted91','software_engineering')

#Test 06
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('yted91','software_engineering')

#Test 07
def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')

#Test 08
def test_check_ontime(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.check_ontime('03/01/20','03/02/20')

#Test 09
def test_check_grades(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grades = grading_system.usr.check_grades('software_engineering')
    print('\nGrades: ')
    print(grades)

#Test 10
def test_view_assignments(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    assignments = grading_system.usr.view_assignments('databases')
    print('\nAssignments: ')
    print(assignments)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
