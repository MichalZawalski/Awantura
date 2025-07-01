# Awantura o Kasę: Home Edition

Dzień dobry Państwu! Krzysztof Ibisz, witam w Domowej edycji kultowego teleturnieju Awantura o Kasę -- grze, w której liczy się zgrany zespół, ostre licytacje i żyłka do hazardu.
Żeby zagrać, nie musisz iść do telewizji ani męczyć się w kolejce chętnych -- od dziś każdy może się Awanturować z rodziną, przyjaciółmi i każdym, kto ma w sobie pasję do teleturniejów.

## Jak mam zagrać?

Aby bawić się razem z nami, wystarczą trzy proste kroki:

### 1. Zbierz drużyny

Awantura o Kasę jest grą zespołową.
Tradycyjnie, w grze biorą udział trzy drużyny czteroosobowe oraz Krzysztof Ibisz.
Możesz jednak grać w mniejszym gronie (wtedy zespoły będą mniejsze lub z mniejszą liczbą osób), albo większym -- baw się tak jak lubisz!
Minimalny skład do gry to 3 osoby (dwie drużyny po 1 osobie i Ibisz).

Przed rozpoczęciem gry, należy podzielić się na role:
- **Krzysztof Ibisz** -- prowadzący, który będzie zadawał pytania, prowadził licytację i śmieszkował z graczami.
- **Kapitan drużyny** -- każda drużyna ma jednego kapitana, który licytuje w jej imieniu, udziela odpowiedzi, a także negocjuje z Ibiszem.
- **Członek drużyny** -- wspólnie z drużyną odpowiada na pytania i wspomaga kapitana.

### 2. Uruchom interfejs gry

Kluczowym elementem gry jest licytacja. Interfejs do licytacji znajduje się [pod następującym adresem](https://docs.google.com/spreadsheets/d/1kq946CDMJDhhmP5jHJtFsTRtXwcpKvi_y2PU4zDj-io/edit?usp=sharing).
Aby grać, skopiuj go na swój dysk Google (będziesz go edytować), a następnie udostępnij wszystkim uczestnikom gry.

W interfejsie znajdziesz:
- **Aktualny stan gry i licytacji** dla graczy.
- **Konsolę Ibisza** pozwalającą na moderowanie licytacji, a także zarządzanie stanem kont drużyn podczas rozgrywki.
- **Dedykowane ekrany dla poszczególnych drużyn**, które zawierają te same informacje co ekran główny, ale dla wygody dodatkowo oznaczają własną drużynę.

Dla drużyn, interfejs jest wyłącznie informacją, która pozwala śledzić przebieg gry.
W szczególności, drużyny nie mogą edytować interfejsu, a jedynie obserwować jego zawartość.
Stan gry jest aktualizowany przez Krzysztofa Ibisza (lub inną wyznaczoną osobę).

**Moderacja gry**

W każdej rundzie, Ibisz losuje kategorię pytania, a następnie otwiera licytację (przycisk _Rozpoczynam licytację_).
Po rozpoczęciu, kapitanowie licytują, a Ibisz aktualizuje stan gry w wierszu _Licytacja_.
Po zakończeniu licytacji, Ibisz losuje pytanie z danej kategorii i zadaje je drużynie, która wygrała licytację.
Po udzieleniu odpowiedzi, Ibisz zaznacza czy jest poprawne (przyciski _Oczywiście_ i _Niestety nie_), a stan gry automatycznie się aktualizuje.

Jeśli wylosowana kategoria to _podpowiedź_ lub _złota skrzynka_, po licytacji Ibisz zabiera pulę przyciskiem _Przenoszę do własnej puli_.

Przy odpowiadaniu, drużyna może poprosić o podpowiedź.
Wówczas negocjuje z Ibiszem jej cenę, a następnie Ibisz wprowadza uzgodnioną cenę w wierszu _Cena podpowiedzi_ dla odpowiedniej drużyny i wybiera _Sprzedaję podpowiedź_.

Podczas caej gry, jedyne pola które powinny być edytowane, to _Licytacja_ oraz _Cena podpowiedzi_.
Wszystkie pozostałe pola są aktualizowane automatycznie i nie powinny być zmieniane.
Wyjątkowo, na początku gry należy ustalić początkowe stany kont drużyn w wierszu _Całkowity stan_ na 10000.

### 3. Pytania

Nie ma teleturnieju bez pytań.
Dlatego do Twojej dyspozycji jest mechanizm losujący kategorie oraz pytania.
Kod jest napisany w Pythonie.
Jeśli nie masz doświadczenia z uruchamianiem takich programów, nie przejmuj się -- wystarczy że wykorzystasz dowolny serwis online do uruchamiania Pythona (np. [https://www.pythonanywhere.com/]()).
W konsoli bash, wykonaj następujące polecenia:
```
git clone <repo>
cd Awantura
chmod +x setup.sh
./setup.sh
```
A następnie, aby uruchomić:
```
python3 main.py
```
Pojawi się zestaw wszystkich dostępnych kategorii, a także dwie wylosowane kategorie -- dla pierwszego etapu, a także finału.
W zależności od tego który etap aktualnie gracie, zwróć uwagę tylko na ten punkt.
Wybierz kategorię (numer), z której chcesz poznać pytanie (zwykle będzie to ta, która się wylosowała) lub -1 żeby powtórzyć losowanie.
Następnie dostaniesz treść pytania.
Po wciśnięciu Enter, wyświetlą się odpowiedzi: poprawna, a także 3 niepoprawne warianty.
Jeśli drużyna orzyma podpowiedź, wówczas należy podać te 4 odpowiedzi, w losowej kolejności.
Dla wygody, przykładowa losowa kolejność również jest podawana.
Kolejny Enter rozpoczyna wszystko od nowa.

**UWAGA** Dla każdej kategorii przygotowałem ok. 20 różnych pytań, co daje w sumie ok. 520 pytań.
Pytania zostały wygeneraowane za pomocą różnych modeli językowych, używając promptu podanego w pliku `database/prompt.txt`.
Niestety, z tego powodu niektóre z nich mogą być trywialne (np. "Ile wynosi suma cyfr liczby 1234?", "Kto był przywódcą Insurekcji Kościuszkowskiej?"), źle zadane (np. "Która z wymienionych osób nie jest postacią historyczną?") lub błędne.
Dlatego przed zadaniem pytania, Ibisz powinien sprawdzić czy jest ono dobrze zadane.
Jeśli jest niewłaściwie postawione, powinien naprawić jego treść, a jeśli jest to zbyt trudne -- wylosować następne.
Uwaga: Ibisz generalnie nie powinien rozstrzygać czy pytanie jest _zbyt proste_ czy _zbyt trudne_, a jedynie czy jest poprawnie sformułowane i czy podana odpowiedź jest właściwa.

## Skrócone zasady gry

Pełne zasady gry znajdują się np. w [artykule na Wikipedii](https://pl.wikipedia.org/wiki/Awantura_o_kas%C4%99), poniżej dla wygody przypominam najważniejsze z nich.

_TODO_