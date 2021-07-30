from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Rest1(Resource):
    def get(self):
        return {'name': "Mark", 'age': 46, 'job': 'instructor'}


class Rest2(Resource):
    items = ['sample1', 'sample2']

    def get(self, index):
        return self.items


api.add_resource(Rest1, '/rest1')
api.add_resource(Rest2, '/rest2/<int:index>')
if __name__ == '__main__':
    app.run(port=5678, host='0.0.0.0', debug=True)