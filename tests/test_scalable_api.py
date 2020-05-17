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
