from febraban.cnab240.bradesco.multipag.result.parser import PaymentParser


file = open("retornoBradesco.RET", "r")

responses = PaymentParser.parseFile(file)


# line = PaymentParser.parseLines(["2370001300001N000DEV-5092391946027008PGIT0900000000000007                              200320260000000000010006621  020003416905482216190320260000000000000000000000000000100000000000000000000000000000000020032026                  BD"])
# print(line[0].status())
# print(line[0].occurrencesText())

# print(occurrences)
for response in responses:
    print("-------------------------------------------------------------------")
    print(response.identifier)
    print(response.status())
    print(response.occurrences)
    # print(response.contentText())
    print("-------------------------------------------------------------------")