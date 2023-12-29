from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID

class CSRGenerator:
    def __init__(self, private_key_path='teacher_private.key', csr_path='teacher_csr.pem'):
        self.private_key_path = private_key_path
        self.csr_path = csr_path

    def generate_csr(self,teacher_name):
        # Generate a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Generate a CSR
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "SY"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Damascus"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Damascus University"),
            x509.NameAttribute(NameOID.COMMON_NAME, teacher_name),
        ])

        csr = x509.CertificateSigningRequestBuilder().subject_name(subject).sign(
            private_key, algorithm=hashes.SHA256(), backend=default_backend()
        )

        # Save private key to a file
        with open(self.private_key_path, 'wb') as private_key_file:
            private_key_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            private_key_file.write(private_key_pem)

        # Save CSR to a file
        with open(self.csr_path, 'wb') as csr_file:
            csr_pem = csr.public_bytes(serialization.Encoding.PEM)
            csr_file.write(csr_pem)
         # Return CSR content
            return csr_pem.decode('utf-8')

        # Print CSR content
   #     csr_content = csr.public_bytes(serialization.Encoding.PEM).decode('utf-8')
   #     print("Generated CSR:")
   #     print(csr_content)
