from flask import Flask, render_template
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Replace this with your actual mechanism to generate/retrieve the pairing code
    pairing_code = 'example-pairing-code'  # This should be dynamic based on your bot's implementation

    # Generate the QR code from the pairing code
    qr_img = qrcode.make(pairing_code)
    img_bytes = io.BytesIO()
    qr_img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Encode the image to base64 for display in HTML
    qr_code_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    return render_template('index.html', pairing_code=pairing_code, qr_code=qr_code_base64)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
