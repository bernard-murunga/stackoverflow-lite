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


if __name__ == '__main__':
    app.run(debug=True)
