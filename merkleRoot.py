import hashlib

#create a test transactions(txN) set
tx1 = "transaction 1"
tx2 = "transaction 2"
tx3 = "transaction 3"
tx4 = "transaction 4"
transactions = [tx1, tx2, tx3, tx4]
for x in transactions:
	x = x.encode()





# getMerkleRoot returns the SHA256 merkle root hash of the merkle tree
# @param hashes the list of hashes the merkle root will be based on
def getMerkleRoot(hashes):
	updatedHashes = []
	i = len(hashes)
	if i == 0:
		print("Error")
	elif i == 1:
		return hashlib.sha256((hashes[0] + hashes[0]).encode()).hexdigest()
	elif i == 2:
		return hashlib.sha256((hashes[0] + hashes[1]).encode()).hexdigest()
	else:
		for x in range(0, i, 2):
			if i%2 == 0:
				updatedHashes.append(hashlib.sha256((hashes[x] + hashes[x+1]).encode()).hexdigest())
			else:
				if x == i:
					updatedHashes.append(hashlib.sha256((hashes[x] + hashes[x]).encode()).hexdigest())
				else:
					updatedHashes.append(hashlib.sha256((hashes[x] + hashes[x+1]).encode()).hexdigest())
		return getMerkleRoot(updatedHashes)			
					


merkleRoot = getMerkleRoot(transactions)
print(merkleRoot)