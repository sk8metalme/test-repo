from flask import Flask
from app.presentation.views import bp
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "app/presentation/templates")
)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
