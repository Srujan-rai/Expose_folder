from flask import Flask,send_from_directory,jsonify
import os
app=Flask(__name__)

folder_path='NLP'

@app.route('/<path:filename>',methods=['GET'])
def download_file(filename):
    return send_from_directory(folder_path,filename)

@app.route('/list_file',methods=['GET'])
def list_file():
    try:
        files=os.listdir(folder_path)
        return jsonify(files)
    except Exception as e:
        return str(e),500


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)