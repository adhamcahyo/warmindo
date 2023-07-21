from warmindo import Warmindo
from .api_config import BASE_URL

app = Warmindo()

@app.route('/api/data')
def get_data_from_api():
    return "<h2>Data dari API:</h2><p>Ini adalah data dari API yang diambil menggunakan Warmindo.</p>"

if __name__ == '__main__':
    app.run()