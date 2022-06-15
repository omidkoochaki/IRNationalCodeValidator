class Code:
    def __init__(self, national_code):
        self.national_code = str(national_code)

    def length(self):
        if self.national_code.isnumeric():
            l = len(self.national_code)
            if l == 10:
                return self.national_code
            elif l < 10:
                self.national_code = self.national_code.zfill(10)
                return self.national_code.zfill(10)
            else:
                return "Invalid Length"
        else:
            return "Invalid Character"

    def is_valid(self):
        l = self.length()
        if l == "Invalid Length":
            return False, "Invalid Length"
        elif l == "Invalid Character":
            return False, "Invalid Character"
        else:
            sum = 0
            for i in range(0, 9):
                sum = sum + (int(self.national_code[i]) * (10 - i))
            if (sum % 11) < 2:
                if int(self.national_code[9]) == (sum % 11):
                    return True, "Valid"
                else:
                    return False, "Invalid"
            else:
                if int(self.national_code[9]) == (11 - (sum % 11)):
                    return True, "Valid"
                else:
                    return False, "Invalid"

