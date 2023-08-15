from durable.lang import *
from metafory import *
from coto import *
with ruleset('Kawa'):

    @when_all((m.pozycja == 'bramkarz') & (m.doswiadczenie =='czlonek podstawowej 11'))
    def artur_boruc(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Artur Boruc', 'metafora': bramkarz1, 'wyjasnienie': bramkarz11})
        
    @when_all((m.pozycja == 'bramkarz') & (m.doswiadczenie =='klasa swiatowa'))
    def gianluigi_donarumma(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Gianluigi Donnaruma', 'metafora': bramkarz2 , 'wyjasnienie': bramkarz22})
        
    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_obronca == 'lewy obronca'))
    def marcelo(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Marcelo', 'metafora': obronca1, 'wyjasnienie': obronca11})

    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_obronca == 'lewy obronca'))
    def alphonso_davies(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Alphonso Davies', 'metafora': obronca2, 'wyjasnienie': obronca22})
        
    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_obronca == 'srodkowy obronca'))
    def michal_pazdan(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Michal Pazdan', 'metafora': obronca3, 'wyjasnienie': obronca33})
        
    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_obronca == 'srodkowy obronca'))
    def raphael_varane(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Raphael Varane', 'metafora': obronca4, 'wyjasnienie': obronca44})

    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_obronca == 'prawy obronca'))
    def sean_kleiber(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Sean Kleiber', 'metafora': obronca5, 'wyjasnienie': obronca55})

    @when_all((m.pozycja == 'obronca') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_obronca == 'prawy obronca'))
    def benjamin_pavard(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Benjamin Pavard', 'metafora': obronca6, 'wyjasnienie': obronca66})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_pomocnik == 'srodkowy pomocnik'))
    def martin_odeegard(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Martin Odeegard', 'metafora': pomocnik1, 'wyjasnienie': pomocnik11})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_pomocnik == 'srodkowy pomocnik'))
    def paul_pogba(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Paul Pogba', 'metafora': pomocnik2, 'wyjasnienie': pomocnik22})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_pomocnik == 'srodkowy pomocnik ofensywny'))
    def nicolo_zaniolo(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Nicolo Zaniolo', 'metafora': pomocnik3, 'wyjasnienie': pomocnik33})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_pomocnik == 'srodkowy pomocnik ofensywny'))
    def kevin_de_bruyne(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Kevin de Bruyne', 'metafora': pomocnik4, 'wyjasnienie': pomocnik44})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_pomocnik == 'pomocnik boczny'))
    def marc_cucurela(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Marc Cucurela', 'metafora': pomocnik5, 'wyjasnienie': pomocnik55})

    @when_all((m.pozycja == 'pomocnik') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_pomocnik == 'pomocnik boczny'))
    def bukayo_saka(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Bukayo Saka', 'metafora': pomocnik6, 'wyjasnienie': pomocnik66})

    @when_all((m.pozycja == 'napastnik') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_napastnik == 'skrzydlowy'))
    def christian_pulisic(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Christian Pulisic', 'metafora': napastnik1, 'wyjasnienie': napastnik11})

    @when_all((m.pozycja == 'napastnik') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_napastnik == 'skrzydlowy'))
    def neymar(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Neymar', 'metafora': napastnik2, 'wyjasnienie': napastnik22})

    @when_all((m.pozycja == 'napastnik') & (m.doswiadczenie =='czlonek podstawowej 11')& (m.pozycja_napastnik == 'srodkowy napastnik'))
    def arkadiusz_milik(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Christian Pulisic', 'metafora': napastnik3, 'wyjasnienie': napastnik33})

    @when_all((m.pozycja == 'napastnik') & (m.doswiadczenie =='klasa swiatowa')& (m.pozycja_napastnik == 'srodkowy napastnik'))
    def robert_lewandowski(c):
        c.assert_fact({ 'zamowienie': c.m.zamowienie, 'wynik':'Robert Lewandowski', 'metafora': napastnik4, 'wyjasnienie': napastnik44})

    

    
    @when_all(+m.zamowienie)
    def output(c):
        print('Dotyczy: {0} otrzymałeś:{1} metafora:{2} coto:{3} '.format(c.m.zamowienie,c.m.wynik,c.m.metafora,c.m.wyjasnienie))

post('Kawa', { 'zamowienie': '1', 'pozycja': 'bramkarz', 'doswiadczenie': 'czlonek podstawowej 11'})
post('Kawa', { 'zamowienie': '2', 'pozycja': 'bramkarz', 'doswiadczenie': 'klasa swiatowa'})

post('Kawa', { 'zamowienie': '3', 'pozycja': 'obronca', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_obronca': 'lewy obronca'})
post('Kawa', { 'zamowienie': '4', 'pozycja': 'obronca', 'doswiadczenie': 'klasa swiatowa', 'pozycja_obronca': 'lewy obronca'})
post('Kawa', { 'zamowienie': '5', 'pozycja': 'obronca', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_obronca': 'srodkowy obronca'})
post('Kawa', { 'zamowienie': '6', 'pozycja': 'obronca', 'doswiadczenie': 'klasa swiatowa', 'pozycja_obronca': 'srodkowy obronca'})
post('Kawa', { 'zamowienie': '7', 'pozycja': 'obronca', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_obronca': 'prawy obronca'})
post('Kawa', { 'zamowienie': '8', 'pozycja': 'obronca', 'doswiadczenie': 'klasa swiatowa', 'pozycja_obronca': 'prawy obronca'})

post('Kawa', { 'zamowienie': '9', 'pozycja': 'pomocnik', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_pomocnik': 'srodkowy pomocnik'})
post('Kawa', { 'zamowienie': '10', 'pozycja': 'pomocnik', 'doswiadczenie': 'klasa swiatowa', 'pozycja_pomocnik': 'srodkowy pomocnik'})
post('Kawa', { 'zamowienie': '11', 'pozycja': 'pomocnik', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_pomocnik': 'srodkowy pomocnik ofensywny'})
post('Kawa', { 'zamowienie': '12', 'pozycja': 'pomocnik', 'doswiadczenie': 'klasa swiatowa', 'pozycja_pomocnik': 'srodkowy pomocnik ofensywny'})
post('Kawa', { 'zamowienie': '13', 'pozycja': 'pomocnik', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_pomocnik': 'pomocnik boczny'})
post('Kawa', { 'zamowienie': '14', 'pozycja': 'pomocnik', 'doswiadczenie': 'klasa swiatowa', 'pozycja_pomocnik': 'pomocnik boczny'})

post('Kawa', { 'zamowienie': '15', 'pozycja': 'napastnik', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_napastnik': 'skrzydlowy'})
post('Kawa', { 'zamowienie': '16', 'pozycja': 'napastnik', 'doswiadczenie': 'klasa swiatowa', 'pozycja_napastnik': 'skrzydlowy'})
post('Kawa', { 'zamowienie': '17', 'pozycja': 'napastnik', 'doswiadczenie': 'czlonek podstawowej 11', 'pozycja_napastnik': 'srodkowy napastnik'})
post('Kawa', { 'zamowienie': '18', 'pozycja': 'napastnik', 'doswiadczenie': 'klasa swiatowa', 'pozycja_napastnik': 'srodkowy napastnik'})




