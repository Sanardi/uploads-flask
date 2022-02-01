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

