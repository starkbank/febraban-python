from febraban.cnab240.itau.transferV83 import PaymentParser


file = open("SB25058A.RET", "r")

responses = PaymentParser.parseFile(file)

for response in responses:
    print response.identifier
    print response.authentication
    print response.status()
    print response.content
    print response.contentText()