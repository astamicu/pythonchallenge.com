def translate():
    global alphabet, newalphabet
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    newalphabet = []
    for u in alphabet:
        newalphabet.append(alphabet[2])
        alphabet += [alphabet.pop(0)]

whatIsThis = list("cjqccjqccjqccjqccjqc")


translate()
##print(alphabet)
def reiter():
    global a, b
    a = iter(alphabet)
    b = iter(newalphabet)


def test():
    global c, d, a, b
    c = next(a)
    d = next(b)
##    print('litera din alfabet: ' + str(c))
##    print('litera din noul alfabet: ' + str(d))


e = iter(whatIsThis)
def bau():
    global f
    f = next(e)
##    print('litera din cod: ' + str(f))


traducere = []
def astae():
    global c, f, d, trad
    for val in whatIsThis:
        if f == c:
            traducere.append(d)
            trad = ''.join(traducere)
            print('codul: ' + trad)
            bau()
            reiter()
            break
        elif f == ' ':
            traducere.append(' ')
            trad = ''.join(traducere)
           
            bau()
            break
        elif f == '.':
            traducere.append('.')
            trad = ''.join(traducere)
           
            bau()
            break
        elif f == "'":
            traducere.append("'")
            trad = ''.join(traducere)
         
            bau()
            break
        elif f == '(':
            traducere.append('(')
            trad = ''.join(traducere)
            
            bau()
            break
        elif f == ')':
            traducere.append(')')
            trad = ''.join(traducere)
            
            bau()
            break
        else:
            test()
            continue
        
reiter()
bau()
test()
astae()

for val in whatIsThis:
    astae()
        





    
   

##print(newalphabet)


##a = iter(alphabet)
##old = next(a)
##print(a)


##print(g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.)
