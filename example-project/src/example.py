import math


def disp_sqrt(val):
    try:
        if not isinstance(val, int | float):
            raise TypeError('argüman int ya da float olmak zorunda!')
        if val < 0:
            raise ValueError('argüman negatif olamaz!')

        result = math.sqrt(val)
        print(result)
    finally:
        print('finally bölümü çalıştıtılıyor...')


def main():
    try:
        val = float(input('Bir değer giriniz:'))
        disp_sqrt(val)
    except Exception as e:
        print(e)


main()
