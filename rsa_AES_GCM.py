import os
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from generar_claves import generar_par_claves


def encrypt_document(document: bytes, recipient_public_key_pem: bytes) -> bytes:
    # Generar clave AES-256
    aes_key = get_random_bytes(32)

    # Cifrar el documento con AES-256-GCM
    cipher_aes = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher_aes.encrypt_and_digest(document)
    nonce = cipher_aes.nonce

    # Cifrar la clave AES con la clave con RSA
    public_key = RSA.import_key(recipient_public_key_pem)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)

    # Empaquetar todo en un solo objeto bytes
    package = {
        "encrypted_key": base64.b64encode(encrypted_key).decode("utf-8"),
        "nonce": base64.b64encode(nonce).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8"),
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8")
    }

    return json.dumps(package).encode("utf-8")

def decrypt_document(pkg: bytes, recipient_private_key_pem: bytes) -> bytes:
    # Desempaquetar el contenido
    package = json.loads(pkg.decode("utf-8"))

    encrypted_key = base64.b64decode(package["encrypted_key"])
    nonce = base64.b64decode(package["nonce"])
    tag = base64.b64decode(package["tag"])
    ciphertext = base64.b64decode(package["ciphertext"])

    # Descifrar la clave AES con RSA privada
    private_key = RSA.import_key(recipient_private_key_pem, passphrase="lab04uvg")
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_key)

    # Descifrar el documento con AES-GCM
    cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    document = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return document

if __name__ == '__main__':
    generar_par_claves(2048)

    with open("public_key.pem", "rb") as f: pub = f.read()
    with open("private_key.pem", "rb") as f: priv = f.read()

    # Generen un cifrado de un texto
    doc = b"Contrato de confidencialidad No. 2025-GT-001"
    pkg = encrypt_document(doc, pub)
    resultado = decrypt_document(pkg, priv)


    # Prueba con archivo de 1 MB (simula un contrato real)
    doc_grande = os.urandom(1024 * 1024)
    pkg2 = encrypt_document(doc_grande, pub)
    assert decrypt_document(pkg2, priv) == doc_grande
    print("Archivo 1 MB: OK")
