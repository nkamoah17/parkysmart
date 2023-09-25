try:
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    import api
    import data_storage
    import caching
    import inference
except ImportError as e:
    print(f"Error importing modules: {e}")
    exit(1)

app = Flask(__name__)
CORS(app)

# Initialize the database connection pool and the S3 client
data_storage.init_app(app)
blob_storage.init_app(app)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            file_id = data_storage.save_file(file)
            occupancy = inference.predict(file)
            caching.save(file_id, occupancy)
            return jsonify({'file_id': file_id, 'occupancy': occupancy}), 200
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@app.route('/occupancy/<id>', methods=['GET'])
def get_occupancy(id):
    try:
        occupancy = caching.get(id)
        if occupancy is None:
            metadata = data_storage.get_metadata(id)
            if metadata is None:
                return jsonify({'error': 'No such file'}), 404
            occupancy = inference.predict(metadata['file'])
            caching.save(id, occupancy)
        return jsonify({'occupancy': occupancy}), 200
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@app.route('/api-key', methods=['GET'])
def get_api_key():
    try:
        return jsonify({'api_key': api.generate_key()}), 200
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit(1)

