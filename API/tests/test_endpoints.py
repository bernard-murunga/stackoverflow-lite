import pytest
from api.v1.views import get_questions

#  Test if endpoint returns all questions
def test_get_all_questions(client):
    expected_result = {
    "questions": [
         {
        'id': 1,
        'question': 'What is linting?',
        'answers': {'one': 'Showing syntax errors', 'two': 'Highlight style error'}
    },
    {
        'id': 2,
        'question': 'What is TDD?',
        'answers': {'one': 'Writing tests', 'two': 'Writing tests before application code'}
    }
    ]
}
    response = client.get('/questions')
    assert response.status_code == 200
    assert b'"id":1' in response.data
    assert b'"id":2' in response.data
    assert expected_result == response.get_json()
