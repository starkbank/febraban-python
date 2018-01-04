from febraban.cnab240.v83.result.parser import PaymentParser

file = open("output.REM", "r")

responses = PaymentParser.parseFile(file)

for response in responses:
    print response.identifier
    print response.status()
    print response.content
    print response.contentText()