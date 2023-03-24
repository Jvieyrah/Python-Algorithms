from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message('martes', 1) == 'm_setra'

    assert encrypt_message('martes', 2) == 'setr_am'

    assert encrypt_message('martes', 10) == 'setram'

    with raises(TypeError):
        encrypt_message(0, 0)

    with raises(TypeError):
        encrypt_message('string', 'int')
