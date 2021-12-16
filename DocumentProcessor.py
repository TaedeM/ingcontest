try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class DocumentProcessor:

    def retrieveContractNumber(self, filename):
        ocrText = pytesseract \
            .image_to_string(Image.open(filename)) \
            .split('\n')
        _lineWithContractNumber = self.__findLineContractNumber(ocrText)
        _contractNumber =  self.__filterContractNumberFromLine(_lineWithContractNumber)
        return _contractNumber

    def __findLineContractNumber(self, stringList):
        for line in stringList[:9]:
            if "Contractnummer" in line:
                return line
            elif "Leningnummer" in line:
                return line
            elif "Contractnr" in line:
                return line
            elif "contractnr" in line:
                return line
            elif "contractnummer" in line:
                return line
            elif "INGnummer" in line:
                return line
            elif "Ons kenmerk" in line:
                return line
        return "not found"

    def __filterContractNumberFromLine(self,line):
        #print(line, line.find("Datum:"))
        if "Datum:" in line:
            line = line[:line.find("Datum:")]    
        line = line.replace(":", "")
        line = line.replace(".", "")
        line = line.replace(" ", "")
        line = line.replace("Contractnummer", "")
        line = line.replace("contractnummer", "")
        line = line.replace("Contractnummer:", "")
        line = line.replace("Leningnummer", "")
        line = line.replace("Contractnr", "")
        line = line.replace("contractnr", "")
        line = line.replace("INGnummer", "")
        line = line.replace("Ons kenmerk", "")
        line = line.strip()
        return line
