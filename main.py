from console import *
from Tables.orderMap import *
import Polinom.Polinom as a
import Polinom.Monom as m



if __name__ == '__main__':
    while True:
        choice_int = choice()
        match choice_int:
            case 1:
                input_polinom()
            case 2:
                input_monom()
            case 3:
                output_polinoms()
            case _:
                break
