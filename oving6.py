import rsa

def crack():
    message = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    public_key = (29815, 100127)
    pk, public_key = rsa.generate_keypair()
    message = rsa.encrypt(public_key, "vi skulle egentlig ha en pong greie")

    e,n = public_key

    primes = rsa.PrimeGen(1000)
    for p in primes:
        if n%p == 0:
            q = n//p
            break
    phi = (p-1) * (q-1)
    d = rsa.multiplicative_inverse(e,phi)

    attempt = rsa.decrypt( (d,n), message)
    #print(attempt)


