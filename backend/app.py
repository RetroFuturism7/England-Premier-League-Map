from flask import Flask, jsonify, make_response, send_file, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

DEBUG = True

app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

def create_team_data_route(team):
    def get_team_data():
        try:
            df = pd.read_csv('./data/matches.csv')
            df = df[df['Team'] == team]  # select team data
            df = df[['Date', 'Venue', 'Result', 'GF', 'GA', 'Opponent', 'Team']]  # select columns
            return jsonify(df.to_dict(orient='records'))
        except pd.errors.EmptyDataError:
            return make_response(jsonify({'error': 'Empty CSV file'}), 400)
        except pd.errors.ParserError:
            return make_response(jsonify({'error': 'Error parsing CSV file'}), 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    get_team_data.__name__ = f'get_{team}_data'  # set unique function name
    return get_team_data

teams = [
    "ManchesterCity", "Arsenal", "Liverpool", "AstonVilla", "TottenhamHotspur", 
    "Chelsea", "NewcastleUnited", "ManchesterUnited", "WestHamUnited", "CrystalPalace",
    "BrightonandHoveAlbion", "Bournemouth", "Fulham", "WolverhamptonWanderers",
    "Everton", "Brentford", "NottinghamForest", "LutonTown", "Burnley", "SheffieldUnited"
]

for team in teams:
    app.add_url_rule(f'/api/matchesdata/{team}', view_func=create_team_data_route(team))

@app.route('/')
def serve():
    return send_file(os.path.join(app.static_folder, 'index.html'))

@app.route('/<path:path>')
def static_proxy(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        if file_path.endswith('.js'):
            return send_file(file_path, mimetype='application/javascript')
        elif file_path.endswith('.css'):
            return send_file(file_path, mimetype='text/css')
        elif file_path.endswith('.html'):
            return send_file(file_path, mimetype='text/html')
        elif file_path.endswith('.png'):
            return send_file(file_path, mimetype='image/png')
        elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
            return send_file(file_path, mimetype='image/jpeg')
        elif file_path.endswith('.svg'):
            return send_file(file_path, mimetype='image/svg+xml')
        elif file_path.endswith('.ico'):
            return send_file(file_path, mimetype='image/x-icon')
        else:
            return send_file(file_path)
    else:
        return send_file(os.path.join(app.static_folder, 'index.html'), mimetype='text/html')

if __name__ == '__main__':
    app.run()
