# Solucionari del paraulògic

Aquest codi permet trobar la majoria de solucions del Paraulògic. Hi ha algunes paraules que de moment no troba, com els femenins dels adjectius.


### Llistat de mots
El llistat de mots vàlids ha sigut obtingut a través de l'[Optimot](https://aplicacions.llengua.gencat.cat/llc/AppJava/index.html), i filtrant les entrades a només aquelles procedents del [Diccionari de la llengua catalana de l'Institut d'Estudis Catalans.](https://dlc.iec.cat/)


### Com emprar
Utilitza el programa així:
```
$ python3 paraulogic.py [lletra central] [lletres extra]
```

Per exemple, per al 9 de gener de 2022:
```
$ python paraulogic.py u aelmnt
Lletra central: u
Lletres extra:  aelmnt
S'ha trobat 158 paraules:
  1. aleuta
  2. allau
  3. allunament
  4. allunat
      ...
```

### Raison d'être
La creació d'aquest repositori és per motius autodidàctics.
