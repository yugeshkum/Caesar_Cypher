import string

#to read input from plainfile
f=open("plainfile", "r")
if f.mode == 'r':
    contents = f.read()
plaintext = contents.upper()

def newfreqdist(plaintext):
    lfreq1 = {}
    aold=bold=cold=dold=eold=fold=gold=hold=iold=jold=kold=lold=mold=nold=oold=pold=qold=rold=sold=told=uold=vold=wold=xold=yold=zold=other=0
    for j in plaintext:
        if j in uppalpha:
            if j == uppalpha[0]: aold+=1
            if j == uppalpha[1]: bold+=1
            if j == uppalpha[2]: cold+=1
            if j == uppalpha[3]: dold+=1
            if j == uppalpha[4]: eold+=1
            if j == uppalpha[5]: fold+=1
            if j == uppalpha[6]: gold+=1
            if j == uppalpha[7]: hold+=1
            if j == uppalpha[8]: iold+=1
            if j == uppalpha[9]: jold+=1
            if j == uppalpha[10]: kold+=1
            if j == uppalpha[11]: lold+=1
            if j == uppalpha[12]: mold+=1
            if j == uppalpha[13]: nold+=1
            if j == uppalpha[14]: oold+=1
            if j == uppalpha[15]: pold+=1
            if j == uppalpha[16]: qold+=1
            if j == uppalpha[17]: rold+=1
            if j == uppalpha[18]: sold+=1
            if j == uppalpha[19]: told+=1
            if j == uppalpha[20]: uold+=1
            if j == uppalpha[21]: vold+=1
            if j == uppalpha[22]: wold+=1
            if j == uppalpha[23]: xold+=1
            if j == uppalpha[24]: yold+=1
            if j == uppalpha[25]: zold+=1
        else:
            other+=1
    l1 = plainlength - other
    lfreq1["A"] = aold/l1
    lfreq1["B"] = bold/l1
    lfreq1["C"] = cold/l1
    lfreq1["D"] = dold/l1
    lfreq1["E"] = eold/l1
    lfreq1["F"] = fold/l1
    lfreq1["G"] = gold/l1
    lfreq1["H"] = hold/l1
    lfreq1["I"] = iold/l1
    lfreq1["J"] = jold/l1
    lfreq1["K"] = kold/l1
    lfreq1["L"] = lold/l1
    lfreq1["M"] = mold/l1
    lfreq1["N"] = nold/l1
    lfreq1["O"] = oold/l1
    lfreq1["P"] = pold/l1
    lfreq1["Q"] = qold/l1
    lfreq1["R"] = rold/l1
    lfreq1["S"] = sold/l1
    lfreq1["T"] = told/l1
    lfreq1["U"] = uold/l1
    lfreq1["V"] = vold/l1
    lfreq1["W"] = wold/l1
    lfreq1["X"] = xold/l1
    lfreq1["Y"] = yold/l1
    lfreq1["Z"] = zold/l1

    return lfreq1

plainlength = len(plaintext)

#dictionary with letter frequencies
lfreq3= {
"A" : 8.2/100,
"B" : 1.5/100,
"C" : 2.8/100,
"D" : 4.3/100,
"E" : 12.7/100,
"F" : 2.2/100,
"G" : 2.0/100,
"H" : 6.1/100,
"I" : 7.0/100,
"J" : 0.2/100,
"K" : 0.8/100,
"L" : 4.0/100,
"M" : 2.4/100,
"N" : 6.7/100,
"O" : 7.5/100,
"P" : 1.9/100,
"Q" : 0.1/100,
"R" : 6.0/100,
"S" : 6.3/100,
"T" : 9.1/100,
"U" : 2.8/100,
"V" : 1.0/100,
"W" : 2.4/100,
"X" : 0.2/100,
"Y" : 2.0/100,
"Z" : 0.1/100
}


#all letters of alphabet
uppalpha = list(string.ascii_uppercase)

#function to encrypt to ciphertext
def encrypt(text,s):
    result=""
    #s represents shift order
    for i in plaintext:
        if i in uppalpha:
            result += chr((ord(i) + s-65) % 26 + 65)
        else:
            result += i
    return result

ciphertext = encrypt(plaintext, 3)

#print(ciphertext)

#to print output to encrypted file
f1=open('./encryptedfile', 'w+')
f1.write(ciphertext)
f1.close()

def newfreqdist(ciphertext):
    lfreq2 = {}
    anew=bnew=cnew=dnew=enew=fnew=gnew=hnew=inew=jnew=knew=lnew=mnew=nnew=onew=pnew=qnew=rnew=snew=tnew=unew=vnew=wnew=xnew=ynew=znew=other=0
    for j in ciphertext:
        if j in uppalpha:
            if j == uppalpha[0]: anew+=1
            if j == uppalpha[1]: bnew+=1
            if j == uppalpha[2]: cnew+=1
            if j == uppalpha[3]: dnew+=1
            if j == uppalpha[4]: enew+=1
            if j == uppalpha[5]: fnew+=1
            if j == uppalpha[6]: gnew+=1
            if j == uppalpha[7]: hnew+=1
            if j == uppalpha[8]: inew+=1
            if j == uppalpha[9]: jnew+=1
            if j == uppalpha[10]: knew+=1
            if j == uppalpha[11]: lnew+=1
            if j == uppalpha[12]: mnew+=1
            if j == uppalpha[13]: nnew+=1
            if j == uppalpha[14]: onew+=1
            if j == uppalpha[15]: pnew+=1
            if j == uppalpha[16]: qnew+=1
            if j == uppalpha[17]: rnew+=1
            if j == uppalpha[18]: snew+=1
            if j == uppalpha[19]: tnew+=1
            if j == uppalpha[20]: unew+=1
            if j == uppalpha[21]: vnew+=1
            if j == uppalpha[22]: wnew+=1
            if j == uppalpha[23]: xnew+=1
            if j == uppalpha[24]: ynew+=1
            if j == uppalpha[25]: znew+=1
        else:
            other+=1
    l2 = plainlength - other
    lfreq2["A"] = anew/l2
    lfreq2["B"] = bnew/l2
    lfreq2["C"] = cnew/l2
    lfreq2["D"] = dnew/l2
    lfreq2["E"] = enew/l2
    lfreq2["F"] = fnew/l2
    lfreq2["G"] = gnew/l2
    lfreq2["H"] = hnew/l2
    lfreq2["I"] = inew/l2
    lfreq2["J"] = jnew/l2
    lfreq2["K"] = knew/l2
    lfreq2["L"] = lnew/l2
    lfreq2["M"] = mnew/l2
    lfreq2["N"] = nnew/l2
    lfreq2["O"] = onew/l2
    lfreq2["P"] = pnew/l2
    lfreq2["Q"] = qnew/l2
    lfreq2["R"] = rnew/l2
    lfreq2["S"] = snew/l2
    lfreq2["T"] = tnew/l2
    lfreq2["U"] = unew/l2
    lfreq2["V"] = vnew/l2
    lfreq2["W"] = wnew/l2
    lfreq2["X"] = xnew/l2
    lfreq2["Y"] = ynew/l2
    lfreq2["Z"] = znew/l2

    return lfreq2

lfreq1 = newfreqdist(plaintext)
lfreq2 = newfreqdist(ciphertext)
print(" \n General Letter frequency \n")
print(lfreq3 )
print(" \n \n Plain text frequency \n")
print(lfreq1)
print(" \n \n Cipher text frequency \n")
print(lfreq2)
print("\n")

