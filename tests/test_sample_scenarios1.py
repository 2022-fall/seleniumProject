import pytest

print('Starting the sample test scenario.')


@pytest.fixture(scope='module')
def greet():
    print("\n----------------- SetUp ----------------")
    print('Helloooo Test Master!')
    yield [2,3,4]
    print("\n------------------ TearDown ------------")
    print("fixture steps are completed here.")



@pytest.mark.scen1case1
@pytest.mark.scen1
def test_scen1_case1(greet):
    print('\nscen1_case1 starting !')
    print(greet)
    greet.append(5)
    print(greet)
    assert 'hello' == 'hello'


# @pytest.mark.skip
@pytest.mark.scen1
@pytest.mark.smoketest
@pytest.mark.scen1case2
def test_scen1_case2(greet):
    print("\nscenario 1 case 2 starting ...")
    print(greet)
    greet.append(6)
    print(greet)
    assert 2 == 2, "case 2 failed"
