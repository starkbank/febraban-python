from febraban.cnab240.itau.charge import SlipParser

file = open("output.RET", "r")

responses = SlipParser.parseFile(file)

for response in responses:
    print response.identifier
    print response.status()
    print response.amountInCents
    print response.fine
    print response.content
    print response.contentText()