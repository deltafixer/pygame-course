# Faza 1
## Čas 1

Dobrodošli na prvi čas!

Na ovom času ćete naučiti:

* Šta je pygame
* Kako se instalira python i pygame
* Kako se crta u pythonu!

---

Pre nego što nastavite, nadam se da imate *osnovno znanje iz programiranja* i da Vam je poznata `python sintaksa`. To su minimalni zahtevi za ulazak u ovaj kurs.

Dakle, da pređemo na temu ovog kursa - `pygame`.

Pygame je python biblioteka koja Vam omogućava da kreirate igrice.

Gledano na ostale biblioteke koje postoje (i za druge programske jezike), pygame se svrstava u jedne od manjih. 

**Preporučljiva je za početnike** i jedna od prednosti je činjenica da je kod koji kucate izuzetno portabilan - pygame je podržan na:

* Linux
* Windows (95, 98, ME, 2000, XP, Vista, 7, 10 
* Windows CE, BeOS, MacOS, Mac OS X, FreeBSD, NetBSD, OpenBSD, BSD/OS, Solaris, IRIX, i QNX.
* Delimično podržan za
  * AmigaOS, Dreamcast, Atari, AIX, OSF/Tru64, RISC OS, SymbianOS i OS/2

Lista je ogromna i ovo je jedan od glavnih razloga zašto hobisti koriste pygame biblioteku za razvoj igrica.

---

### Instalacija python-a i dodavanje pygame-a

Za rad sa pygame bibliotekom neophodno je python okruženje.

Kako biste proverili da li imate python na Vašem računaru, otvorite terminal na Vašem sistemu i ukucajte komandu:

```
python --version
```

ukoliko dobijete ovakav odgovor:

```
'python' is not recognized as an internal or external command, operable program or batch file.
```

nemate python i potrebno ga je instalirati.

Možete ga skinuti sa ovog [linka](https://www.python.org/downloads/).

Proces instalacije je jednostavan i, za potrebe ovog kursa, predlaže se pridržavanje podrazumevanim opcijama instalacionog procesa (ili, jednostavno rečeno, pritiskajte `next` dok ne dođete do kraja).

Nakon instalacije, ponovnim pozivom komande `python --version` bi trebalo da dobijete ovakav odgovor:

```
Python 3.8.2
``` 

Broj može da varira u zavisnosti od aktuelne verzije u trenutku instaliranja.

Instaliranjem, na ovaj način, dobijate i `IDLE` okruženje za kucanje Vašeg python koda. Ovo okruženje je zapravo program koji sada možete naći u listi programa na Vašem računaru (njegovo puno ime u trenutku izrade kursa je `IDLE (Python 3.8 32-bit)`).

Ovo okruženje izgleda ovako:

!['IDLE screenshot'](./images/idle.png)

Nakon ovoga, možemo da dodamo i pygame biblioteku.

Pygame dodajete u Vaš sistem kucanjem sledeće komande, u terminal:

```
pip3 install pygame
```

ili, **ukoliko Vam sistem javi da nemate pip3**:

```
py -3 -m pip install pygame
```

Nakon što se proces instalacije završi, vreme je da proverimo ispravnost ove biblioteke!

Iskopirajte sledeći kod:

```python
import pygame
pygame.init()
prozor = pygame.display.set_mode((200, 200))
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("black"), (20, 20, 160, 160), 5)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
```

* otvorite `IDLE` 
* odaberite karticu `File` iz trake na vrhu
* kliknite na `New File`
* nalepite kod u prozor koji se otvorio
* odaberite karticu `Run` iz trake tog prozora
* kliknite na `Run Module`
* sačuvajte fajl na proizvoljno mesto, nije bitno kako ga imenujete

Trebalo bi da dobijete:

!['IDLE screenshot'](./images/pygame_test_example.png)

I ovaj prozor se zatvara 3 sekunde nakon otvaranja.

Ovime smo potvrdili ispravnost pygame-a.

---

### PygameBg

Tim Petlje je kreirao biblioteku `Pygame Toolbox for Beginners` - `PygameBg` koja automatizuje proces podešavanja otvaranja i zatvaranja prozora.

Instalira se komandom:

```
pip3 install pygamebg
```

ili

```
py -3 -m pip install pygamebg
```

Funkcije kojima se odlikuje su:

```python
pygamebg.open_window(200, 300, "PyGameBg")
```

i

```python
pygamebg.wait_loop()
```

Cela svrha ove biblioteke je da jednom linijom otvorite i jednom linijom zatvorite prozor igrice.

Kroz kurs nećemo koristiti ovu biblioteku.

---

## Koordinatni sistem

Koordinatni sistem u pygame-u funkcioniše na sledeći način:

* Tačka (0, 0) se nalazi u gornjem levom uglu.
* X raste udesno
* Y raste nadole
* Negativne koordinate ne postoje

!['Coord system'](./images/coord_system.png)
