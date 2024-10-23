const secretKey = CryptoJS.enc.Utf8.parse('1234567890123456');  // 16-byte key for AES-128

    document.getElementById('encryptedForm').addEventListener('submit', function (e) {
        e.preventDefault();  // Prevent the form from submitting the default way

        const message = document.getElementById('message').value;

        // Generate a Initialization Vector
        const iv = CryptoJS.lib.WordArray.random(16);

        // Encrypt the message using AES with the key and IV
        const encrypted = CryptoJS.AES.encrypt(message, secretKey, {
            iv: iv,
            mode: CryptoJS.mode.CFB,
            padding: CryptoJS.pad.NoPadding 
        });

        // Concatenate IV + Ciphertext and encode as Base64
        const ivAndCiphertext = iv.concat(encrypted.ciphertext).toString(CryptoJS.enc.Base64);

        document.getElementById('encrypted_message').value = ivAndCiphertext;

        // Submit the form after encryption
        this.submit();
    }
);