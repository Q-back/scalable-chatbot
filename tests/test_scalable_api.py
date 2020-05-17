from main import DefaultAnswer
from scalable_api import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_hi_answer(cli):
    resp = cli.post(
        '/question/',
        json={'question': 'hi'}
    )
    assert resp.json()['answer'] == 'hi'
    assert resp.json()['question'] == 'hi'


def test_default_answer(cli):
    resp = cli.post(
        '/question/',
        json={'question': 'asdf'},
    )
    default_answer = DefaultAnswer(question='asdf')
    assert resp.json()['answer'] == default_answer.answer
