import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509 import *
from cryptography.x509.oid import NameOID
import random
import datetime
import os


def generate_mathematical_equation():
    # Replace this with your logic to generate a suitable mathematical equation
    # for the professor to solve, ensuring appropriate difficulty levels.
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    equation = f"{num1} {operator} {num2} = ?"
    return equation, num1 + num2 if operator == '+' else num1 - num2 if operator == '-' else num1 * num2


def verify_professor_identity(equation, correct_answer):
    # Prompt the professor to solve the equation
    answer = int(input(f"Please solve the following equation to verify your identity:\n{equation}\nAnswer: "))
    # Check the answer
    return answer == correct_answer


def generate_teacher_certificate(ca_cert, ca_key, teacher_csr, username):
    # Load the CA certificate and private key
    with open(ca_cert, 'rb') as f:
        ca_cert = x509.load_pem_x509_certificate(f.read(), default_backend())
    with open(ca_key, 'rb') as f:
        ca_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

    # Load the teacher's CSR
    with open(teacher_csr, 'rb') as f:
        teacher_csr = x509.load_pem_x509_csr(f.read(), default_backend())

    # Identity verification step
    equation, correct_answer = generate_mathematical_equation()

    if verify_professor_identity(equation, correct_answer):
        # Identity verified, proceed with certificate creation
        # Create the teacher's certificate
        teacher_cert = x509.CertificateBuilder() \
            .subject_name(teacher_csr.subject) \
            .issuer_name(ca_cert.subject) \
            .public_key(teacher_csr.public_key()) \
            .serial_number(x509.random_serial_number()) \
            .not_valid_before(datetime.datetime.utcnow()) \
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365)) \
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True) \
            .sign(ca_key, cryptography.hazmat.primitives.hashes.SHA256(), default_backend())
        # Save the teacher's certificate
        with open('teachers_certificates/'+username+'_certificate.pem', 'wb') as f:
            f.write(teacher_cert.public_bytes(serialization.Encoding.PEM))
        print("Teacher Identity verified. Teacher Certificate is created.")
    else:
        print("Identity verification failed. Certificate cannot be issued.")
