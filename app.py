from flask import Flask, request, render_template
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

app = Flask(__name__)

SECRET_KEY = b'1234567890123456'  # 16 bytes AES key

def decrypt_message(encrypted_message):
    
    encrypted_message_bytes = base64.b64decode(encrypted_message)
    
    iv = encrypted_message_bytes[:16]  # First 16 bytes are the Initialization Vector
    actual_encrypted_message = encrypted_message_bytes[16:]  # Rest is the encrypted message
    
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    print(encrypted_message)
    decrypted_message = decryptor.update(actual_encrypted_message) + decryptor.finalize()
    print(decrypted_message)
    
    return decrypted_message.decode('utf-8')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    
    decrypted_message = decrypt_message(encrypted_message)
    
    print(f"Decrypted message: {decrypted_message}")
    
    # Add functionality to save encrypted values to the database

    return "Message decrypted and printed to console."

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
