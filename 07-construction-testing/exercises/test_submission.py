import pytest
import System
import Staff


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
def test_change_grade(grading_staff):
    grading_staff.change_grade('akend3','comp_sci','assignment1',80)



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
@pytest.fixture
def grading_staff():
    gradingStaff = Staff.Staff()
    return gradingStaff