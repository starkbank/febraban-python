from febraban.cnab240.itau.sispag import PaymentParser


file = open("SB06069A.RET.txt", "r")

responses = PaymentParser.parseFile(file)

for response in responses:
    print "-------------------------------------------------------------------"
    print response.identifier
    print response.authentication
    print response.status()
    print response.amountInCents
    print response.type
    print response.contentText()
