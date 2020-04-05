import hashlib
import requests

import sys
import json

from uuid import uuid4

from timeit import default_timer as timer

import random

#isInEndOfChain = False

def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()
    print(last_proof, "Searching for next proof")
    proof = 0
    last_hash = hashlib.sha256(str(last_proof).encode()).hexdigest()
    #if isInEndOfChain:
    #    proof = int(last_proof)
    #    while not valid_proof(last_hash, proof):
    #        proof += 1
    #else:
    rangeBits = [i for i in range(16,64)]
    while not valid_proof(last_hash, proof):
        proof = random.getrandbits(random.choice(rangeBits))
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof

def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
    guess_hash = hashlib.sha256(str(proof).encode()).hexdigest()
    #print(last_hash[-6:], guess_hash[:6], proof)
    return last_hash[-6:] == guess_hash[:6]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()


    #r = requests.get(url=node + "/full_chain")
    #data = r.json()
    #if data['chain'][-1]['transactions']['recipient'] == id:
    #    isInEndOfChain = True
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = { "proof": new_proof, "id": id }

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            #isInEndOfChain = True
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
