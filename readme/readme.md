

# Jak-to
Plik pomocy do wyjaśniania przepływu pracy bota

### Nowy gracz
Bot powinien działać od momentu, gdy po raz pierwszy dołączysz do świata.
Automatycznie będzie budować pierwsze budynki i ukończać pierwsze zadania (jeśli włączone).
Po zbudowaniu koszar proces rekrutacji powinien się rozpocząć. 
Gdy pierwsze jednostki włóczni zaczną się tworzyć, proces farmy powinien również zacząć działać.

Po pewnym czasie bot powinien również zacząć rozpoznawać, które jednostki badać / ulepszać.


### Po pewnym czasie
Gdy twoje budynki osiągną wyższe poziomy, bot zaczyna tworzyć transakcje na targu.
Pozwala to procesowi budowania pracować z wysoką wydajnością.

Ilekroć świat ma włączony system "flag", bot będzie również próbować ulepszać i ustawiać najwyższą flagę "bonusu zasobów".
W tym momencie system dostrajania farmy (manager.py) powinien być w stanie wykryć, które farmy mają najwyższy / najniższy zysk zasobów i automatycznie dostroić parametry wioski.

### Po jeszcze większym czasie
Osiągniesz punkt, w którym inni gracze mogą cię atakować. 
Mogą myśleć, że twoja wieś to łatwy cel, ale dzięki prawidłowo ustawionym parametrom będziesz mieć bardzo dobrą armię.

Ilekroć zostanie wykryta wpadająca atak, bot zatrzyma proces farmy i automatycznie ustawi najwyższą flagę "bonusu obrony".
Wartościowe (lub do kitu obronę) jednostki zostaną ewakuowane, ilekroć masz więcej niż jedną wioskę.

Jeśli bot ma również włączoną opcję "manage_defence", wyśle jednostki obronne jako wsparcie.
Ta część można skonfigurować dla każdej wioski

### Gra średnio/późna
Po osiągnięciu etapu, w którym szlachta jest zbudowana, możesz ustawić parametr szlachty na wiosce na 1.
To będzie tworzyć niezbędne monety i będzie trenować szlachtę.

Jeśli chcesz czegoś eksperymentalnego, możesz ustawić bieżącą konfigurację farmy na zawierającą szlachtę. To powoli zacznie przejęć wszystkie otaczające wsie farmy :)

Po uzyskaniu więcej wsi możesz ustawić bota do automatycznego kopiowania istniejącej konfiguracji na nowe. Najlepiej ustaw je ręcznie, ponieważ prawdopodobnie będziesz chciał coś dostosować. 

Sugeruję również, abyś od czasu do czasu kontynuował grę, używając sesji przeglądarki, możesz natknąć się na captche, które bot złamie :)

Baw się dobrze!