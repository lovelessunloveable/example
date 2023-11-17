def todecimal(*number):
  if len(number) > 0:
    number, base = number  
  number = input("Введите ваше число: ")
  base = int(input("Введите систему счисления числа: "))
  number = number[::-1]
  result = 0
  abc = '0123456789ABCDEF'
  def toDecimal(*number):
    try:
        for i in range(len(number)):
        result += abc.index(number[i]) * base**i
        return result  
    except ValueError:
        print('Невозможное число в {base}-ичной СС')
        return result

def fromdecimal(*number):
    if len(number) > 0:
        number, base = number
    number = int(input("Введите ваше число в десятичную систему счисления: "))
    base = int(input("Введите систему счисления, в которую нужно перевести число: "))
    result = ""
    def fromDecimal():
        try:
            while number > 0:
                remainder = number % base
                if remainder > 9:
                    abc = '0123456789ABCDEF'
                    remainder = abc[remainder]
                number = number // base
                result = str(remainder) + result
            return result    
        except ValueError:
            print("error")
            return result
        
def fromanytoany():
    

print('Введите 1, чтобы перевести число в десятичную СС')
print('Введите 2, чтобы перевести число из десятичной СС в другую')
a = 0
while a != 1:
  select = int(input('Ваш выбор - '))
  if select == 1:
    a = 1
    print("Ваше число в десятичной системе: " , todecimal())
  elif select == 2:
    a = 1
    print("Ваше десятичное число в выбранной СС: " , fromdecimal())