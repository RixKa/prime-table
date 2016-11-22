import pytest
import random
import __builtin__

from helper.input_handler import prompt_user, validate_input


class TestInputHandler(object):
    @classmethod
    def setup_class(cls):
        cls.mocked_input = '3'

    def mock_raw_input(self, *args, **kwargs):
        # fake user input
        return self.mocked_input

    def test_prompt_user(self, monkeypatch):
        monkeypatch.setattr(__builtin__, 'raw_input', self.mock_raw_input)
        assert prompt_user() == self.mocked_input

    def test_retry_prompt_user(self, monkeypatch):
        monkeypatch.setattr(__builtin__, 'raw_input', self.mock_raw_input)
        assert prompt_user(True) == self.mocked_input


class TestInputValidation(object):
    def test_n_equals_0(self):
        n = 0
        assert not validate_input(n)

    def test_n_is_int(self):
        n = random.randint(1, 100)
        assert validate_input(n)

    def test_n_is_digit(self):
        n = random.choice(['2', '3', '5', '7'])
        assert validate_input(n)

    def test_n_is_bad(self):
        n = random.choice(['x', 'word', [1,2,3], {'foo': 'bar'}])
        assert not validate_input(n)
