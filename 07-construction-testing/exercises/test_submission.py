import pytest
import System


#Test 01 - F
#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Test 02 - F
#Tests if the password login can handle the wrong password
def test_check_password(grading_system):
    grading_system.check_password('cmhbf5', 'bestTa')

#Test 03 - P
def test_change_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('akend3','comp_sci','assignment1','80')

#Test 04 - P
def test_create_assignment(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignmentTest','10/15/2020','comp_sci')

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
