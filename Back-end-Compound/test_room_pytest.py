import room_pytest
from room_pytest import UserDB
import pytest

db = None


def setup_module(module):
    """
    Setup Module of Testing
    """
    print("------------Setup------------")
    global db
    db = UserDB()
    db.connect("test.json")


def teardown_module(module):
    """
    Teardown Module of Testing
    """
    print("------------Teardown------------")
    db.close()


@pytest.mark.parametrize("test_input1, test_input2, test_input3, expected_output",
                         [
                             (2, 1, 3, True),
                             (3, 2, 3, False),
                             (23, 22, 24, True),
                             (7, 8, 12, False)
                         ]
                         )
def test_room_check(test_input1, test_input2, test_input3, expected_output):
    result = room_pytest.room_check(test_input1, test_input2, test_input3)
    assert result == expected_output


@pytest.mark.parametrize("test_input1, test_input2, expected_output",
                         [
                             (1, 3, True),
                             (20, 22, True),
                             (23, 25, False),
                             (24, 27, False)
                         ]
                         )
def test_validate_input(test_input1, test_input2, expected_output):
    result = room_pytest.validate_input(test_input1, test_input2)
    assert result == expected_output
