from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from webscrapingtest import google_image_search
from segmentation import segment_image

def specialFunction(imagepath):
    jsondata = google_image_search(imagepath)
    segmented_image_path = segment_image(imagepath, output_dir="uploads")
    return jsondata, segmented_image_path

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/image_upload_db"
mongo = PyMongo(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

CORS(app, resources={r"/*": {"origins": "*"}})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/files', methods=['GET'])
def get_files():
    try:
        files = mongo.db.files.find()
        file_list = [{'filename': file['filename'], 'userid': file['userid'], 'original_filepath': file['original_filepath'], 'jsondata': file['jsondata'], 'segmented_image_path': file['segmented_image_path']} for file in files]
        return jsonify({'status': 'success', 'files': file_list}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Unable to fetch files'}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'}), 400

        file = request.files['file']
        userid = request.form.get('userid')

        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)

            # Call the specialFunction to process the image
            jsondata, segmented_image_path = specialFunction(filepath)

            # Save all data to MongoDB
            mongo.db.files.insert_one({
                'filename': filename,
                'userid': userid,
                'original_filepath': filepath,
                'jsondata': jsondata,
                'segmented_image_path': segmented_image_path
            })
            
            return jsonify({'status': 'success', 'message': 'File uploaded successfully and processed', 'data': {
                'filename': filename,
                'userid': userid,
                'original_filepath': filepath,
                'jsondata': jsondata,
                'segmented_image_path': segmented_image_path
            }}), 200
        
        return jsonify({'status': 'error', 'message': 'Invalid file'}), 400
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

@app.route('/uploads/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
