import pytest
import System

#Test 01 - F
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Test 02 - F
def test_check_password(grading_system):
    grading_system.check_password('cmhbf5', 'bestTa')

#Test 03 - P - Done
def test_change_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('akend3','comp_sci','assignment1','80')
    grades = grading_system.usr.check_grades('akend3','comp_sci')
    print(grades)
    if grades!=[['assignment1', 0], ['assignment2', 66]]:
        assert False

#Test 04 - P - Done
def test_create_assignment(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignmentTest','10/15/2020','comp_sci')
    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('comp_sci')
    print (assignments)
    if assignments!=[['assignment1', '2/2/20'], ['assignment2', '2/10/20'], ['assignmentTest', '10/15/2020']]:
        assert False


#Test 05 - F
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('pnrouff','software_engineering')

#Test 06 - P
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('akend','databases')

#Test 07 - P
def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')
    assignments = grading_system.users['hdjsr7']['courses']['cloud_computing']
    grades = []
    for key in assignments:
        grades.append([key, assignments[key]['submission']])
    print(grades)
    assert False

#Test 08 - P
def test_check_ontime(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.check_ontime('03/01/20','03/02/20')

#Test 09 - F
def test_check_grades(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.check_grades('software_engineering')

#Test 10 - F
def test_view_assignments(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.view_assignments('databases')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
