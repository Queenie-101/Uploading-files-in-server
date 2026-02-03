from flask import Flask, render_template,redirect,url_for,flash,request
import os #upload files to the system
#create a flask app
app=Flask(__name__)
#secret key - access the flask messages
app.secret_key="abc123"
#configure the upload folder
app.config['UPLOAD_FOLDER']="uploads/"
#allowed extensions
ALLOWED_EXTENSIONS={'png','png','jpeg','pdf','docx','txt','xlsx'}
#functioon to check the file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
#route for homepage
@app.route('/',methods=['GET','POST'])
def upload_file():
    #check if the form was submitted
    if request.method=='POST':
        #check if the file exists
        if 'file' not in request.files:
            #error message
            flash("No file selcted")
            #redicrect to homepage
            return redirect(request.url)
        #get the upload file
        file=request.files['file']
        #check if filename is empty
        if file.filename=='':
            #error message
            flash("No file seleted")
            #redirect to homepage
            return redirect(request.url)
        #check if the file is allowed
        if file and allowed_file(file.filename):
            #save the file to the upload folder
            filepath=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.xave(filepath)
            #success message
            flash("File uploaded successully")
            #redicrect to homepage
            return redirect(request.url)
        else:
            #error message
            flash("File type not allowed")
            #redirect to homepage
            return redirect(request.url)
    return render_template('index.html')#display the homepage
if __name__=="__main__":
    app.run(debug=True)