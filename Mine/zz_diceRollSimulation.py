# RollDieDynamic.py

"""Dynamicznie uaktualniany wykres statystyki rzutów kostką."""

from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import sys

def polski_integer(liczba):
    """Spacja, nie przecinek w roli separatora tysięcy"""
    return f'{liczba:,}'.replace(',', ' ')
    
def polski_float(liczba):
    """Przecinek dziesiętny zamiast kropki"""
    return f'{liczba:.3f}'.replace('.', ' ')
    
def nowa_ramka(nr_ramki, rzuty_w_ramce, liczby_oczek, statystyka_oczek):
    """Konfiguracja zawartości wykresu dla każdej ramki animacji"""
    
    # symulacja następnej porcji rzutów
    for i in range(rzuty_w_ramce):
        statystyka_oczek[random.randrange(1, 7) - 1] += 1 

    # rekonfiguracja wykresu dla uaktualnionej statystyki rzutów
    plt.cla()  # wyczyszczenie dotychczasowej zawartości wykresu
    seria_str = polski_integer(sum(statystyka_oczek))
    
    nazwa_wykresu = (
        'Częstotliwości wystąpień liczb oczek po wykonaniu'
        f' {seria_str} rzutów'
    )
     
    # nowe słupki
    osie = sns.barplot(liczby_oczek, statystyka_oczek, palette='bright')  
 
    # tytuł wykresu
    osie.set_title(nazwa_wykresu)
 
    # etykiety osi
    osie.set(xlabel='Liczba oczek', ylabel='Częstotliwość')
    
    # przeskalowanie osi o 10% w stosunku do wymaganej długości
    osie.set_ylim(top=max(statystyka_oczek) * 1.10)  

    # wypisanie liczby wystąpień (bezwzględnej i procentowej)
    # nad każdym słupkiem
    for pasek, ile_razy_liczba_oczek in zip(osie.patches, statystyka_oczek):
        tekst_x = pasek.get_x() + pasek.get_width() / 2.0  
        tekst_y = pasek.get_height() 
        ile_razy_liczba_oczek_str = polski_integer(ile_razy_liczba_oczek)
        
        ile_procent_liczba_oczek = \
           100.0 * (ile_razy_liczba_oczek / sum(statystyka_oczek)) 
        
        ile_procent_liczba_oczek_str = polski_float(ile_procent_liczba_oczek) + '%'
        tekst = ile_razy_liczba_oczek_str + '\n' + ile_procent_liczba_oczek_str 
        osie.text(tekst_x, tekst_y, tekst, ha='center', va='bottom')



# sprawdzenie i odczyt parametrów wiersza poleceń
if len(sys.argv) < 3:
   print('Uruchamianie:')
   print('  ' + sys.argv[0] + ' <ramki>  <rzuty>')
   print()
   print('gdzie:')
   print('  <ramki> - liczba ramek w animacji')
   print('  <rzuty> - liczba rzutów w każdej ramce')
   print()
   sys.exit()

liczba_ramek = int(sys.argv[1])  
rzuty_w_jednej_ramce = int(sys.argv[2])  

sns.set_style('whitegrid')  # białe tło z jasnoszarą siatką
obiekt_okna = plt.figure('Symulacja serii rzutów sześcienną kostką') 
etykiety_1_do_6 = list(range(1, 7))  # liczby oczek na osi x
liczniki_oczek = [0] * 6  # liczniki wystąpień liczb oczek

# skonfigurowanie i uruchomienie animacji

animacja = animation.FuncAnimation(
    obiekt_okna, nowa_ramka, repeat=False, frames=liczba_ramek, interval=33,
    fargs=(rzuty_w_jednej_ramce, etykiety_1_do_6, liczniki_oczek))

plt.show()  # wyświetlenie okna


#**************************************************************************
#* (C) Copyright 1992-2018 by Deitel & Associates, Inc. and               *
#* Pearson Education, Inc. All Rights Reserved.                           *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book have used their     *
#* best efforts in preparing the book. These efforts include the          *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books. The authors *
#* and publisher shall not be liable in any event for incidental or       *
#* consequential damages in connection with, or arising out of, the       *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************
