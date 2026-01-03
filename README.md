Mode dev : 
app.run(debug=True)

Mode prod : 
from waitress import serve
serve(app, host="0.0.0.0", port=8080)