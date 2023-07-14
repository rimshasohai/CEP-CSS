from cryptography.fernet import Fernet
import base64

# Fernet key as string
fernet_key_str = "147bcd78fe84b14908200715a78e09de"

# Convert key to bytes and decode from base64
fernet_key = base64.urlsafe_b64decode(fernet_key_str)

# Create a Fernet object
fernet = Fernet(fernet_key)


