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




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem