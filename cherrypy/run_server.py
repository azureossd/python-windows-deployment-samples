import os

from waitress import serve

import app

serve(app,host="0.0.0.0",port=os.environ["PORT"])  
