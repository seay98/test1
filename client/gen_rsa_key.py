import rsa

(pub_key, pri_key) = rsa.newkeys(1024)
# Public key file
public = pub_key.save_pkcs1()
with open('public.pem', 'wb') as pubfile:
    pubfile.write(public)

# Private key file
private = pri_key.save_pkcs1()
with open('private.pem', 'wb') as prifile:
    prifile.write(private)