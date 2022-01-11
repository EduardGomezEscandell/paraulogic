# Solucionari del paraulògic

Aquest codi permet trobar la majoria de solucions del Paraulògic. Hi ha algunes paraules que de moment no troba, com els femenins dels adjectius. Això es deu a que encara no he implementat una forma de generar-los a partir de les entrades del DIEC.


### Llistat de mots
El llistat de mots vàlids ha sigut obtingut a través de l'[Optimot](https://aplicacions.llengua.gencat.cat/llc/AppJava/index.html), i filtrant les entrades a només aquelles procedents del [Diccionari de la llengua catalana de l'Institut d'Estudis Catalans.](https://dlc.iec.cat/)


### Com emprar
Utilitza el programa així:
```
$ python3 paraulogic.py [lletra central] [lletres extra]
```

Per exemple, per al 10 de gener de 2022:
```
$ python paraulogic.py u aelmnt
Lletra central: e
Lletres extra:  urflps
S'ha trobat 84 paraules:
  1. elf
  2. ell
  3. els
  4. elul
      ...
```

Per fer un test respecte una llista de paraules coneguda, pots fer servir `test.py [data]`:
```
$ python /home/eduard/Code/paraulogic/test.py 2021 01 09
Lletra central: u
Lletres extra:  aelmnt

Manquen les següents paraules:
- muntana
- nueta
- unena
```

### Raison d'être
La creació d'aquest repositori és per motius autodidàctics.
