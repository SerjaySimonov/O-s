tekst = input("Ievadit Virkne Tekstu: ")

def ReplaceO(tekst):
  if tekst.count("O")>0 or tekst.count("o")>0:
    tekst = tekst.replace("O","%")
    tekst = tekst.replace("o","%")
    print(tekst)
  else:
    tekst = "Nekas Netika Aizvietots!"
    print(tekst)
ReplaceO(tekst) 