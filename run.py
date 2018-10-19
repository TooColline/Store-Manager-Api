import os
from app import create_app


app = create_app(os.getenv('production'))
    

if __name__ == '__main__':
    app.run(debug=True)