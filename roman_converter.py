class RomanCalculator:
    dict = {'I': 1, 'IV': 4, 'V' : 5, 'IX': 9, 'X': 10, 'XL': 40, 'L':50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500}
    list_values = list(dict.values())
    list_keys = list(dict.keys())
    result = ''

    def convert_to_roman(self, number):
        self.result = ''
        while number > 0:
            for i in range(len(self.list_values)):
                if number > self.list_values[i] and number < self.list_values[i + 1]:
                    self.result += self.list_keys[i]
                    number -= self.list_values[i]
                elif number == self.list_values[i]:
                    self.result += self.list_keys[i]
                    number -= self.list_values[i]
                else:
                    continue
        return self.result

    def convert_to_roman_series(self, start, stop):
        for i in range(start, stop+1):
            print("{}: {}".format(i, self.convert_to_roman(i)))


    def convert_to_number(self, roman):
        self.count = 0
        roman = roman[::-1]
        roman = roman.upper()
        self.previous = 0
        for r in roman:
            for key in self.list_keys:
                if r == key:
                    if self.dict[r] >= self.previous:
                        self.count += self.dict[r]
                        self.previous = self.dict[r]
                    else:
                        self.count -= self.dict[r]
                        self.previous = self.dict[r]

        return self.count

try1 = RomanCalculator()
try1.convert_to_roman_series(5, 100)
print(try1.convert_to_roman(153))
print(try1.convert_to_number("XCIV"))
