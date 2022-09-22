# Mikroprojekt
Repozytorium zawiera programy do obsługi kamery Basler z obiektywem katadioptrycznym oraz do tworzenia zdjęć panoramicznych na podstawie zdjęć dookólnych.


## basler camera and simple panorama  
W folderze "basler camera and simple panorama" znajduje się plik main.py oraz panoramic.py napisane w języku Python.

main.py - służy do zapisywania zdjęć z kamery do folderu w wyznaczonym miejscu. Przed uruchomieniem programu należy upewnić się, że:
- numer seryjny kamery zgadza się z numerem seryjnym w kodzie,
- ścieżka do której zapisywane są zdjęcia istnieje.

Program uruchamiany jest z terminala za pomocą przykładowej komendy: `python3 main.py manual -p`  
Aby wyłączyć program należy wcisnąć klawisz `q`. Wykonanie zdjęcia w trybie manual następuje po wciśnięciu klawisza `m`.
Po każdym uruchomieniu programu tworzony jest nowy folder do którego zapisywane są zdjęcia.

panoramic.py - zawiera dwie funkcje. Funkcja `video` służy do utworzenia pliku .avi ze zdjęć znajdujących się w podanej ścieżce. Funkcja `panorama` służy do utworzenia zdjęć panoramicznych metodą bezpośrednią. W kodzie programu należy podać ścieżkę do folderu w którym znajdują się zdjęcia dookólne. Skrypt należy uruchomić bez parametrów.

## panorama with central horizontal line  
W folderze "panorama with central horizontal line" znajdują się pliki programu (napisanego w języku C++) służącego do tworzenia zdjęcia panoramicznego z wykorzystaniem wiedzy o parametrach kamery z centralną linią horyzontalną.  
Po zbudowaniu projektu w folderze `build` należy umieścić plik kalibracyjny o nazwie `calib_results.txt`, który powstał w wyniku przeprowadzonej kalibracji kamery.

## calibration
W tym folderze znajdują się foldery "images" (zawiera zdjęcia do kalibracji) oraz "Scaramuzza_OCamCalib_v3.0_win" (ToolBox do kalibracji w MatLabie).  
Przed kalibracją należy umieścić zdjęcia z folderu images w folderze Scaramuzza_OCamCalib_v3.0_win. Informacje o używaniu ToolBoxa znajdują się na stronie:  
https://sites.google.com/site/scarabotix/ocamcalib-omnidirectional-camera-calibration-toolbox-for-matlab  
Aby wczytać wszystkie zdjęcia do kalibracji, po naciśnięciu przycisku "Read names" pojawia się komunikat "Basename camera calibration images (without number nor suffix):", należy wpisać "img", a następnie wybrać rozszerzenie j.  
Liczba kwadratów wzdłuż linii x wynosi: 7, a wzdłuż linii y: 4. Kwadraty mają rozmiar 10cm x 10cm.
