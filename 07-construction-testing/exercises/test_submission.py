import pytest
import System

#Test 01 - F
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

#Test 02 - F
def test_check_password(grading_system):
    test = grading_system.check_password('cmhbf5', 'BESTta')
    if (test==False):
        assert False

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

#Test 06 - P - Done
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('akend3','databases')
    classes = grading_system.users['akend3']
    print(classes)
    if classes!={'courses': {'comp_sci': {'assignment1': {'grade': 0, 'submission_date': '2/1/20', 'submission': 'Blah Blah Blah', 'ontime': True}, 'assignment2': {'grade': 66, 'submission_date': '2/8/20', 'submission': 'Blah2 Blah2 Blah2', 'ontime': True}}}, 'password': '123454321', 'role': 'student'}:
        assert False

#Test 07 - P - Done
def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')
    assignments = grading_system.users['hdjsr7']['courses']['cloud_computing']
    print(assignments)
    if assignments!={'assignment1': {'grade': 'N/A', 'submission_date': '03/01/20', 'submission': 'Blahhhhh', 'ontime': True}, 'assignment2': {'Grade': 100, 'Submission Data': '2/3/20', 'Submission': 'Blah2 Blah2 Blah2', 'ontime': True}}:
        assert False

#Test 08 - F - Done
def test_check_ontime(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    test = grading_system.usr.check_ontime('03/05/20','03/02/20')
    if (test==True):
        assert False

#Test 09 - P - Done
def test_check_grades(grading_system):
    grading_system.login('akend3', '123454321')
    grades = grading_system.usr.check_grades('comp_sci')
    print(grades)
    if grades !=[['assignment1', 0], ['assignment2', 66]]:
        assert False

#Test 10 - F - Done
def test_view_assignments(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.view_assignments('databases')

#Test 11 - F - Done
#Cannot submit to assignment for class you aren't in
def test_submit_random_assignment(grading_system):
    grading_system.login('akend3', '123454321')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','this should fail', '03/01/20')

#Test 12 - F - Done
#Professors should not be able to add students to classes they don't teach
def test_add_student_to_random_class(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('akend3','cloud_computing')
    grading_system.login('akend3', '123454321')
    classes = grading_system.users['akend3']
    print(classes)
    if classes=={'courses': {'comp_sci': {'assignment1': {'grade': 0, 'submission_date': '2/1/20', 'submission': 'Blah Blah Blah', 'ontime': True}, 'assignment2': {'grade': 66, 'submission_date': '2/8/20', 'submission': 'Blah2 Blah2 Blah2', 'ontime': True}}, 'cloud_computing': {'assignment1': {'grade': 'N/A', 'submission_date': 'N/A', 'submission': 'N/A', 'ontime': 'N/A'}, 'assignment2': {'grade': 'N/A', 'submission_date': 'N/A', 'submission': 'N/A', 'ontime': 'N/A'}}}, 'password': '123454321', 'role': 'student'}:
        assert False

#Test 13 - F - Done
#TAs should not be able to change grades in classes they are not TA's for
def test_change_random_grade(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade('hdjsr7','databases','assignment1','80')
    grades = grading_system.usr.check_grades('akend3','comp_sci')
    print(grades)
    if grades==[['assignment1', 0], ['assignment2', 66]]:
        assert False

#Test 14 - F - Done
#Professors should not be able to add assignments to classes they don't teach
def test_create_random_assignment(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.create_assignment('assignmentTest','10/15/2020','cloud_computing')
    grading_system.login('hdjsr7', 'pass1234')
    assignments = grading_system.usr.view_assignments('cloud_computing')
    print(assignments)
    if assignments==[['assignment1', '2/2/20'], ['assignment2', '2/10/20'], ['assignmentTest', '10/15/2020']]:
        assert False

#Test 15 - F - Done
#TA's should not be able to submit assignments
def test_submit_assignment_as_TA(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','this should fail', '03/01/20')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
