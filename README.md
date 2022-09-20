# Mikroprojekt
Repozytorium zawiera programy do obsługi kamery Basler z obiektywem katadioptrycznym oraz do tworzenia zdjęć panoramicznych na podstawie zdjęć dookólnych.

W folderze "basler camera and simple panorama" znajduje się plik main.py oraz panoramic.py

main.py - służy do zapisywania zdjęć z kamery do folderu w wyznaczonym miejscu. Przed uruchomieniem programu należy upewnić się, że:
- numer seryjny kamery zgadza się z numerem seryjnym w kodzie,
- ścieżka do której zapisywane są zdjęcia istnieje.

Program uruchamiany jest z terminala za pomocą przykładowej komendy: python3 main.py manual -p
Aby wyłączyć program należy wcisnąć klawisz 'q'. Wykonanie zdjęcia w trybie 'manual' następuje po wciśnięciu klawisza 'm'.
Po każdym uruchomieniu programu tworzony jest nowy folder do którego zapisywane są zdjęcia.

panoramic.py - zawiera dwie funkcje. Funkcja 'video' służy do utworzenia pliku .avi ze zdjęć znajdujących się w podanej ścieżce. Funkcja 'panorama' służy do utworzenia zdjęć panoramicznych metodą bezpośrednią
