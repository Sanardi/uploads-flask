import os
from flask import Flask
from flask import (Response,
jsonify,
send_from_directory, 
request, 
flash,
g,
redirect,
render_template,
request,
session,
url_for,
make_response)
import config
import io

#################################################################################

# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()

# @auth.get_password
# def get_password(username):
#     if username == 'pleasemakethisdifficult':
#        return 'andthis'
#    return None

# @auth.error_handler
#def unauthorized():
#    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

#################################################################################
#################################################################################



from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
    

# Just define this once
classes = 'w3-table w3-striped w3-border'

def gen_dict(df, title):
    return {'title': title,
            'table': df.to_html(classes=classes)
            }



#######################################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = config.Config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

# @app.route('/secret')
# @auth.login_required
# def hello_secret():
#     return 'this is secret!'


@app.route('/file')
def upload_form():
    return render_template('upload.html')

@app.route('/file', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
