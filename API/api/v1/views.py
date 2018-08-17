from flask import Flask, jsonify, abort, make_response, request

from . import app

questions = [
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


@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})


if __name__ == '__main__':
    app.run(debug=True)
