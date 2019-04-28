def obtenerV(S, H):
	Voc = {}
	j = 1
	[ Voc.setdefault(x,0) for x in S]
	[ Voc.setdefault(x,0) for x in H]

	ln = []
	C0 = []
	C1 = []
	V = {}

	for i in S:
		if i not in ln:
			ln.append(i)
			Voc[i] = j
			j = j+1
		C0.append(Voc[i])

	for i in H:
		if i not in ln:
			ln.append(i)
			Voc[i] = j
			j = j+1
		C1.append(Voc[i])

	for i in Voc:
		V.setdefault(Voc[i], S.count(i) + H.count(i))
		
	return (C0, C1, V)


def naiveBayes(S, H, M):
	(C0, C1, V) = obtenerV(S, H)

	print("C0 =", C0)
	print("C1 =", C1)
	print("V =", V)

	pMC0 = len(C0)/ (len(C0) + len(C1))
	pMC1 = len(C1)/ (len(C0) + len(C1))
	
	print("P(C = C0) =", pMC0)
	print("P(C = C1) =", pMC1)

	for i in M:
		pMC0 = pMC0 * C0.count(i)/len(C0)
		pMC1 = pMC1 * C1.count(i)/len(C1)

	print("P(M, C = C0) =", pMC0)
	print("P(M, C = C1) =", pMC1)

	pM = pMC0 +	pMC1
	print("P(M) =", pM)

	pC0M = pMC0/pM
	print("P(C = C0 | M) =",pC0M)
	pC1M = pMC1/pM
	print("P(C = C0 | M) =",pC1M)


def clasificadorBayes(S, H, M):
	(C0, C1, V) = obtenerV(S, H)
	k = 1
	print("C0 =", C0)
	print("C1 =", C1)
	print("V =", V)

	pMC0 = (len(C0) + k) / ((len(C0) + len(C1)) + k * 2)
	pMC1 = (len(C1) + k) / ((len(C0) + len(C1)) + k * 2 )
	
	print("P(C = C0) =", pMC0)
	print("P(C = C1) =", pMC1)

	for i in M:
		pMC0 = pMC0 * (C0.count(i) + 1)/(len(C0) + k * len(V))
		pMC1 = pMC1 * (C0.count(i) + 1)/(len(C0) + k * len(V))

	print("P(M, C = C0) =", pMC0)
	print("P(M, C = C1) =", pMC1)

	pM = pMC0 +	pMC1
	print("P(M) =", pM)

	pC0M = pMC0/pM
	print("P(C = C0 | M) =",pC0M)
	pC1M = pMC1/pM
	print("P(C = C0 | M) =",pC1M)



def main():
	SPAM = ["oferta", "es", "secreto", 
			"click", "link", "secreto", 
			"secreto", "deportes", "link"]


	HAM =  ["practica", "deportes", "hay",
			"fue", "practica", "deportes",
			"secreto", "deportes", "evento",
			"deportes", "es", "hay",
			"deportes", "cuesta", "dinero"]

	naiveBayes(SPAM, HAM, [8,2,3])
	print("\n\nAlisando...")
	clasificadorBayes(SPAM, HAM, [8,2,3])




main()