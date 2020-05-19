# Faza 2

**_Autor: Stefan Radovanović_**

---

## Čas 2

Dobrodošli na drugi čas druge faze!

Na ovom času ćete naučiti:

- Kako da pomerate junaka igrice pomoću tastera na tastaturi
- Kako da se u igrici krećete pomoću miša

---

Na prethodnom času smo videli kako treba da izgleda igrica koju pravimo i upoznali smo se sa nekim osnovnim pravilima koje trebamo napraviti.

!['game screenshot'](./images/screen_game_1.png)

---

### Pomeranje junaka pomoću tastature

Kako smo već na prethodnom času objasnili funkcionalnost igrice i postavili junaka, sada je potrebno omogućiti mu i pomeranje po ekranu.

Za početak ćemo dodati kretanje pomoću W, A, S i D tastera, a nakon toga i kretanje pomoću strelica.

Pre svega potrebno je odrediti koliko će se pomeriti naš junak kada mu zadamo komandu tasterom. Tako ćemo na samom početku igrice, pre inicijalizacije definisati konstantu koja će se koristiti tokom cele igrice.

```python
# konstante
playerMoveRate = 5
```

Na samom početku kreiranja događaja potrebno je definisati 4 logičke promenljive koje će nam pomoći da odredimo u kom pravcu i smeru će se kretati naš junak nakon određene komande.

```python
while True:
    moveLeft = moveRight = moveUp = moveDown = False
```

Sada je potrebno kreirati događaje za svako dugme koji hoćemo da ima neku ulogu u igrici. Kao što smo rekli, to će biti W, A, S i D tasteri kao i strelice sa tastature.

U `while` petlji gde smo definisali logiku za zatvaranje cele igrice, dodaćemo upite gde ćemo proveravati koji dugme je pritisnut i u zavisnosti od tastera promeniti vrednost tačno one logičke promeljive koja će odrediti pravac i smer kretanja.

```python
if event.type == KEYDOWN:
    # pritisnuto dugme A na tastaturi
    if event.key == K_LEFT or event.key == ord('a'):
        moveLeft = True

    # pritisnuto dugme 'D' na tastaturi
    if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = True

    # pritisnuto dugme 'W' na tastaturi
    if event.key == K_UP or event.key == ord('w'):
        moveUp = True

    # pritisnuto dugme 'S' na tastaturi
    if event.key == K_DOWN or event.key == ord('s'):
        moveDown = True
```

Sada imamo događaje za sve dugmiće koje smo planirali da imaju ulogu u igrici.

Nakon testiranja dosadašnjeg koda, vidimo da se, nakon pritiskanja dugmića, naš junak i dalje ne kreće. Razlog tome je činjenica da mu nismo pružili informaciju gde da se pomeri i za koliko. Takođe, potrebno je napisati kod koji će promenjenu logičku promenljivu koja definiše smer i pravac kretanja vratiti na početnu vrednost, `False` i time ga kasnije zaustaviti jer u suprotnom naš junak će se neprekidno kretati u zadatom smeru i pravcu.

```python
if event.type == KEYUP:
    # pritisnuto dugme A na tastaturi
    if event.key == K_LEFT or event.key == ord('a'):
        moveLeft = False

    # pritisnuto dugme D na tastaturi
    if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = False

    # pritisnuto dugme W na tastaturi
    if event.key == K_UP or event.key == ord('w'):
        moveUp = False

    # pritisnuto dugme S na tastaturi
    if event.key == K_DOWN or event.key == ord('s'):
        moveDown = False
```

Time smo završili dodavanje događaja za određene tastere koji upravljaju kretanje našeg junaka. Na redu je i **zadavanje veličine koraka, smera i pravca.**

Za kretanje junaka ćemo koristiti prethodno definisane logičke promenljive gde ćemo proveriti koja promenljiva ima vrednost `True`. Pored toga potrebo je i ograničiti prostor kretanja kako bi sprečili **nestanak junaka iz prozora**, pa ćemo paralelno u zavisnosti od smera i pravca proveravati koordinate `playerRect`.

Kako smo ranije već definisali pomeraj junaka, ovde ćemo ga koristiti kao parametar za pomeranje u funkciji po određenoj koordinati:

```python
move_ip(xkoor, ykoor)
```

Funkcija `move_ip(xkoor, ykoor)` pomera playerRect objekat tako što x koordinatu poveća za `xkoor` vrednost, a y koordinatu poveća za `ykoor` vrednost. U slučaju da po nekoj koordinati nije potrebno pomeranje, tu ćemo kao parametar staviti 0.

Tako u slučaju pritiska A dugmeta ili leve strelice imamo proveru da li je aktiviran levi pomeraj i da li nismo došli do leve ivice prozora, pa ćemo u tom slučaju imati pomeraj po x osi:

```python
# pomeraj igrača
if moveLeft and playerRect.left > 0:
    playerRect.move_ip(-1 * playerMoveRate, 0)
```

Analogno ovom delu, imamo slučajeve i za ostala 3 događaja:

```python
# pomeraj igrača
if moveRight and playerRect.right < windowWidth:
    playerRect.move_ip(playerMoveRate, 0)
if moveUp and playerRect.top > 0:
    playerRect.move_ip(0, -1 * playerMoveRate)
if moveDown and playerRect.bottom < windowHeight:
    playerRect.move_ip(0, playerMoveRate)
```

Ovaj deo koda dodajemo unutar `for` petlje gde smo proveravali događaje sa tastature.

Testiranjem dosadašnjeg koda se možemo uveriti da se naš junak uspešno kreće pomoću zadatih dugmića. Time smo završili ovo poglavlje, pa nam sledi pomeranje pomoću miša.

---

### Pomeranje junaka pomoću miša

Pored pomeranja našeg junaka pomoću dugmića tastature, na ovom času ćemo naučiti kako to isto uraditi pomoću miša.

Na samom početku je potrebno sakriti pokazivač miša, da ne bi smetao pri igranju.

To ćemo odraditi sledećom linijom koda:

```python
pygame.mouse.set_visible(False)
```

koju ćemo dodati nakon inicijalizacije same igrice. Veoma je važno voditi računa o velikom slovu kod parametra funkcije, jer bi pisanjem malog `false` kompajler vratio sledeću grešku:

```python
Traceback (most recent call last):
  File "C:\Users\Korisnik\Desktop\pygame-course-master\Faza 2\Cas 1\examples\class_1.py", line 28, in <module>
    pygame.mouse.set_visible(false)
NameError: name 'false' is not defined
```

Ova funkcija će sakriti pokazivač miša samo unutar prozora aplikacije, strelica je vidljiva kada mišem napustimo prozor igrice.

Za sada nismo napravili značajan pomak u kontrolisanju junaka mišem već samo odradili estetski deo.

U delu:

```python
while True:
    for event in pygame.event.get():
    ...
```

gde smo definisali događaje za određene tastere tastature dodaćemo i događaj miša koji se realizuje sledećim kodom:

```python
if event.type == MOUSEMOTION:
    playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
```

Ovde ćemo na osnovu koordinata pokazivača miša postaviti koordinate `playerRect` objekta po x i y koordinatama, tako što x koordinata prihvata event.pos[0], a y event.pos[1].

Kako bi (nevidljivi) pokazivač miša pratio junaka i u slučaju da ga pomeramo dugmićima neophodno je da _ručno_ postavimo poziciju mišu:

```python
pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
```

Nakon svega neophodno je ažurirati displej kako bi sve izmene u ovom delu koda bile vidljive, a za to kao i do sada koristimo funkciju:

```python
pygame.display.update()
```

Sada možete pokrenuti našu igricu i isprobati funkcionalnosti koje smo odradili na ovom času.

Dosadašnji kod možete pokrenuti direktno iz foldera `examples` ovog časa, a evo kako on izgleda:

```python
import pygame, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

# izolovanje dimenzija
(windowWidth, windowHeight) = (1024, 768)

background = pygame.image.load('bg.png')
# skaliranje na željenu dimenziju
background = pygame.transform.scale(background, (windowWidth, windowHeight))

# inicijalizacija pygame-a
pygame.init()

# set window specs
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# postavljanje naslova prozora
pygame.display.set_caption('Neo i virusi')

### NOVI KOD POČETAK ###
# sakrivanje pokazivača miša
pygame.mouse.set_visible(False)
### NOVI KOD KRAJ ###

# slika junaka
playerDimensions = (30, 70)
playerImage = pygame.image.load('neo.png')
playerImage = pygame.transform.scale(playerImage, playerDimensions)
playerRect = playerImage.get_rect()

# podešavanje pozicije pravougaonika koji okružuje junaka
playerRect.topleft = (int(windowWidth / 2) - int(playerDimensions[0] / 2), windowHeight - playerDimensions[1])

# padajući objekti (virusi)
fallingObjectDimensions = (96, 80)
fallingObjectImage = pygame.image.load('object.png')
fallingObjectImage = pygame.transform.scale(fallingObjectImage, fallingObjectDimensions)
fallingObjectRect = fallingObjectImage.get_rect()


### NOVI KOD POČETAK ###
# konstante
playerMoveRate = 5

while True:
    moveLeft = moveRight = moveUp = moveDown = False

    while True:
        for event in pygame.event.get():
            # pritisnuto dugme na tastaturi
            if event.type == KEYDOWN:
                # leva strelica ili dugme A
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = True

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True

                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True

                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = True

            # otpušteno dugme sa tastature
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            # pomeraj miša
            if event.type == MOUSEMOTION:
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
            ### NOVI KOD KRAJ ###

            # klik na X dugme prozora
            if event.type == QUIT:
                terminate()

        ### NOVI KOD POČETAK ###
        # pomeranje junaka
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * playerMoveRate, 0)
        if moveRight and playerRect.right < windowWidth:
            playerRect.move_ip(playerMoveRate, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * playerMoveRate)
        if moveDown and playerRect.bottom < windowHeight:
            playerRect.move_ip(0, playerMoveRate)

        # miš prati koordinate junaka (slučaj pomeranja junaka nekim od dugmića)
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
        ### NOVI KOD KRAJ ###

        # dodavanje pozadine
        windowSurface.blit(background, (0, 0))

        # dodavanje virusa
        for i in range(3):
            fallingObjectRect.topleft = (int(windowWidth / 2) + (i - 1) * fallingObjectDimensions[0]  - int(fallingObjectDimensions[0] / 2), int(windowHeight / 2) - fallingObjectDimensions[1])
            windowSurface.blit(fallingObjectImage, fallingObjectRect)

        # dodavanje junaka
        windowSurface.blit(playerImage, playerRect)

        pygame.display.update()

    pygame.display.update()
```

!['game screenshot'](./images/after0202.jpg)
