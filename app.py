from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import base64
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)
app.secret_key = b'secretkeybutnotfordeployment'

# only for certain image file types
ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'])

# route to the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

#  route to the uploading and converting page
@app.route('/upload_page', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        pic = request.files['pic']
        # if no picture was uploaded, show the error
        if not pic:
            return 'No pic uploaded!', 400
        filename = secure_filename(pic.filename)
        # checking if the correct file type was uploaded by checking the extension
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in ALLOWED_EXTENSIONS:
            flash(f"File Type Not Accepted! Try again with an image!")
            return render_template("upload.html", uploaded=False)
        mimetype = pic.mimetype
        if not filename or not mimetype:
            flash(f"File Type Not Accepted! Try again with an image!")
            return render_template("upload.html", uploaded=False)

        # implementation of sobel filter using OpenCV
        img0 = cv2.imdecode(np.fromstring(
            request.files['pic'].read(), np.uint8), cv2.IMREAD_UNCHANGED)

        gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

        # Remove noise:
        img = cv2.GaussianBlur(gray, (3, 3), 0)

        kernel_size = 3

        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=kernel_size)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=kernel_size)

        # Convert output to a CV_8U(8 bit) image
        abs_sobelx = cv2.convertScaleAbs(sobelx)
        abs_sobely = cv2.convertScaleAbs(sobely)

        grad = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)

        img = Image.fromarray(grad)
        data = BytesIO()
        img.save(data, "JPEG")
        data64 = base64.b64encode(data.getvalue())
        decoded_img = data64.decode("UTF-8")
        img_data = f"data:image/jpeg;base64,{decoded_img}"
        return render_template('upload.html', image=img_data, uploaded=True)

    else:
        return render_template("upload.html", uploaded=False)


if __name__ == "__main__":
    app.run(debug=True)
