# Tryby-szyfrow-blokowych

## Opis zadania

Zadanie polega na zaprojektowaniu procesu "szyfrowania" obrazu graficznego. Obraz powinien być czarno-biały i mieć rozmiar rzędu kilkuset pikseli w pionie i w poziomie. Obraz zostanie podzielony na małe bloki, np. 8x8 pikseli, które będą traktowane jako bloki szyfru blokowego. Program ma wczytywać plik graficzny oraz opcjonalnie plik tekstowy z kluczem, a następnie produkować dwa pliki graficzne:

- `ecb_crypto.bmp` - obraz zaszyfrowany w trybie ECB,
- `cbc_crypto.bmp` - obraz zaszyfrowany w trybie CBC.

## Wymagania
- Program nie może korzystać z gotowych funkcji szyfrowania blokowego z bibliotek kryptograficznych.
- Implementacja trybów ECB i CBC musi być napisana ręcznie.
- Plik z kluczem (`key.txt`) jest opcjonalny, a w przypadku jego braku, program powinien wygenerować losowy klucz.
- Obraz wejściowy (`plain.bmp`) powinien być prosty, aby różnice między ECB i CBC były widoczne.

## Struktura projektu
```
/.
├── block.py          # Kod źródłowy programu
├── plain.bmp         # Obraz wejściowy
├── ecb_crypto.bmp    # Wynikowy obraz zaszyfrowany w trybie ECB
├── cbc_crypto.bmp    # Wynikowy obraz zaszyfrowany w trybie CBC
└── README.md         # Dokumentacja projektu
```
