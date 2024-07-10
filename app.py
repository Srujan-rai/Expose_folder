from flask import Flask,send_from_directory

app=Flask(__name__)

folder_path='file'

@app.route('/file/<path:filename>',methods=['GET'])
def download_file(filename):
    return send_from_directory(folder_path,filename)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')