# For prod running

from flask import Flask
from routes import api_bp
import os

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))