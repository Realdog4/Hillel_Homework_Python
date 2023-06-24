from flask import Flask, request, jsonify
from http import HTTPStatus


app = Flask(__name__)


@app.route('/')
def openPage():
    return "Hello! Use the link to view information: /stats_by_city?genre=HipHop"


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ["Invalid request."])

    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    return jsonify(
            {
                'errors': messages
            },
            error.code,
        )


class MusicStats:
    def __init__(self):
        self.music_stats = {
            'HipHop': 'New York',
            'Rock': 'London',
            'Pop': 'Los Angeles',
            'R&B': 'Atlanta',
            'Country': 'Nashville',
            'Jazz': 'New Orleans',
            'Reggae': 'Kingston',
            'Electronic': 'Berlin',
            'Classical': 'Vienna',
            'Blues': 'Chicago'
        }

    def get_city_by_genre(self, genre):
        if genre in self.music_stats:
            return self.music_stats[genre]
        else:
            return None


music_stats = MusicStats()


@app.route('/stats_by_city')
def stats_by_city():
    genre = request.args.get('genre')
    city = music_stats.get_city_by_genre(genre)

    if city:
        return f"Most people listen to music in the '{genre} style' in {city}."

    return f"Music genre '{genre}' not found."


if __name__ == '__main__':
    app.run(port=5001, debug=True)

