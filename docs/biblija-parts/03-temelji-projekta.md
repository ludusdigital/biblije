## Modul 3: Temelji projekta — git, CLAUDE.md i merni instrumenti

U Modulu 2 si pripremio okruženje i vodio prvi razgovor sa Claude-om. Pre nego što počneš da gradiš proizvod, treba ti tri stvari koje grade svaki ozbiljan projekat: vremenska mašina (git), zajednička memorija (`CLAUDE.md`) i kontrolna tabla (testovi, lint i build). Bez njih radiš naslepo — sa njima možeš da letiš.

### Šta ćeš naučiti

- Zašto sa git-om ništa ne može da se nepovratno pokvari — i kako te to oslobađa straha
- Kako da koristiš git i GitHub prirodnim jezikom, bez učenja ijedne git komande
- Šta je `/init`, šta `CLAUDE.md` treba da sadrži i kako da ga održavaš
- Zašto PRVO tražiš merne instrumente (testovi, lint, build) — pre prve funkcionalnosti
- Šta je CI i zašto želiš automatsku kontrolu svake izmene

### Git: vremenska mašina za tvoj projekat

Git je alat koji pravi snimke stanja celog projekta. Svaki snimak se zove **commit** — fotografija svih fajlova u jednom trenutku, sa kratkim opisom šta se promenilo. Projekat sa git-om je dokument sa beskonačnim "Undo" dugmetom: u svakom trenutku možeš da se vratiš na bilo koji raniji snimak.

Ovo je najvažnija psihološka činjenica celog kursa: **dok god redovno praviš commit-e, ništa ne može da se nepovratno pokvari.** Claude je obrisao pola koda? Vratiš se na jučerašnji snimak. Nova funkcionalnost je sve polomila? Vratiš se na stanje od pre sat vremena. Strah od "šta ako nešto upropastim" nestaje — a bez njega ćeš se usuditi da eksperimentišeš.

**GitHub** je nešto drugo, mada povezano: sef u oblaku. Git čuva snimke na tvom računaru; GitHub čuva njihovu kopiju na internetu. Mesto gde GitHub čuva tvoj projekat zove se **repozitorijum** (skraćeno: repo) — jedan projekat = jedan repozitorijum. Ako ti laptop padne u kadu, projekat je bezbedan. GitHub je kasnije i mesto odakle se aplikacija lansira (Modul 9) i gde rade automatske provere (CI, na kraju ovog modula).

### Ne moraš da naučiš git komande

Ovo je deo koji laici najčešće ne veruju: **nikada ne moraš da ukucaš nijednu git komandu.** Claude ih zna sve. Ti samo kažeš šta hoćeš, prirodnim jezikom:

```
Napravi commit sa svim trenutnim izmenama. Opiši u poruci šta smo uradili.
```

```
Vrati projekat na stanje od pre sat vremena. Nešto smo pokvarili
i hoću da krenemo ispočetka od poslednje verzije koja je radila.
```

```
Napravi mi GitHub repozitorijum za ovaj projekat i pošalji sve commit-e tamo.
```

Tvoja jedina disciplina je **navika**: commit svaki put kad bi te zabolelo da izgubiš ono što je upravo urađeno. Da te Claude na to podseća, upiši pravilo u trajnu memoriju porukom koja počinje sa `#`:

```
# Posle svake završene i proverene funkcionalnosti predloži commit sa jasnom porukom.
```

### /init i CLAUDE.md: memorija projekta

Iz Modula 1 znaš da Claude između sesija ne pamti ništa — osim fajla `CLAUDE.md`, koji se učitava na početku svake sesije. To je pisana memorija projekta: svaki novi razgovor počinje kao novi zaposleni koji je prvo pročitao priručnik firme.

Komanda `/init` generiše početni `CLAUDE.md` analizom projekta — pokreni je čim projekat dobije prve fajlove. Ali generisani fajl je samo početak; najvredniji deo dodaješ ti. Dobar `CLAUDE.md` sadrži:

- **Opis proizvoda**: šta aplikacija radi i za koga, u dve-tri rečenice
- **Ključne odluke**: "koristimo X za bazu", "interfejs je na srpskom", "ciljamo mobilne korisnike"
- **Konvencije**: kako se šta imenuje, gde šta stoji, šta je zabranjeno
- **Komande**: kako se pokreću testovi, lint, build, dev server

Održavanje je jednostavno: kad god u razgovoru donesete važnu odluku, reci:

```
Ovo je važna odluka za ceo projekat. Zabeleži u CLAUDE.md da sva plaćanja
idu preko Stripe-a i da cene uvek prikazujemo u dinarima.
```

Loš `CLAUDE.md` je onaj u koji niko ništa ne upisuje — posle mesec dana Claude radi po pravilima koja više ne važe. Tretiraj ga kao živ dokument, ne kao formalnost.

### Merni instrumenti: kontrolna tabla tvog aviona

Sada najvažniji deo modula. Pilot bez instrumenata ne zna ni visinu, ni brzinu, ni da li motor gori — leti naslepo. Ti si u istoj poziciji: ne čitaš kod, pa ne možeš pogledom da proceniš da li nešto radi. Trebaju ti instrumenti koji mere umesto tebe:

- **Testovi** — mali automatski programi koji proveravaju da aplikacija radi ono što treba ("kad korisnik unese pogrešnu lozinku, prikaže se greška"). Jedna komanda, jasan rezultat: prošlo ili palo.
- **Lint** — automatski kontrolor stila i čestih grešaka u kodu; hvata probleme pre nego što postanu bagovi.
- **Build** — proba "sklapanja" cele aplikacije u oblik spreman za objavljivanje. Ako build pukne, lansiranja nema.

Zato instrumente tražiš **PRVO, pre prve funkcionalnosti**: bez njih je svaka Claude-ova tvrdnja "gotovo je, radi" samo tvrdnja; sa njima imaš dokaz — princip iz Modula 1 na delu. A autonomni rad iz Modula 7 (`/goal`, `/loop`) bukvalno zavisi od njih: autonomiji daješ uslov tipa "radi dok svi testovi ne prolaze", što je moguće samo ako testovi postoje. Bez instrumenata nema autopilota.

Evo tačnog prompta — iskopiraj ga čim projekat postoji:

```
Pre nego što napravimo bilo koju funkcionalnost, podesi merne instrumente projekta:

1. Testove — okvir za automatske testove i bar jedan primer testa koji prolazi.
2. Lint — automatsku proveru stila i čestih grešaka.
3. Build — proveru da se cela aplikacija uspešno sklapa.

Sve tri provere moraju da se pokreću jednom jednostavnom komandom.
Upiši te komande u CLAUDE.md. Na kraju mi pokaži izlaz sve tri komande
kao dokaz da prolaze, i objasni mi jednostavnim jezikom šta koja proverava.
```

Od tog trenutka tvoj refren posle svake izmene glasi: "pokreni testove, lint i build i pokaži mi rezultat." Zelena tabla = letimo dalje. Crvena lampica = popravljamo pre nego što nastavimo.

### CI: kontrolor koji nikad ne spava

Poslednji temelj je **CI** (continuous integration — "neprekidna provera"): automatika na GitHub-u koja pokreće tvoje instrumente pri svakoj izmeni koja stigne u repozitorijum. Radi se preko **GitHub Actions** — automatizacije vezane za tvoj repo, koja može npr. da pregleda svaki PR (pull request — formalni predlog izmena koji čeka pregled pre nego što uđe u glavnu verziju koda) ili pokrene sve provere bez tvog angažovanja.

Instrumenti u avionu su tu dok ti letiš; CI je kontrola letenja na zemlji koja proverava svaki let, čak i dok spavaš. Ako neka izmena polomi testove, CI je obeleži crvenim pre nego što se približi produkciji.

```
Podesi GitHub Actions za ovaj repozitorijum tako da se pri svakoj izmeni
automatski pokreću testovi, lint i build. Ako bilo šta padne, izmena mora
biti jasno označena kao neispravna. Objasni mi gde na GitHub-u vidim rezultate.
```

Time je krug zatvoren: git čuva prošlost, `CLAUDE.md` čuva znanje, instrumenti mere sadašnjost, a CI stražari nad budućnošću.

### Vežba

Uradi ovo na projektu iz Modula 2 (ili napravi prazan folder za probu):

1. Otvori Claude Code u folderu projekta i reci: `Postavi git za ovaj projekat i napravi prvi commit. Objasni mi šta si uradio.`
2. Pokreni `/init` da dobiješ početni `CLAUDE.md`, pa dodaj svojim rečima opis proizvoda i bar jednu ključnu odluku (zamoli Claude-a da to upiše).
3. Iskopiraj prompt za merne instrumente iz ovog modula i pošalji ga. Ne prihvataj "gotovo je" — traži izlaz sve tri komande kao dokaz.
4. Reci: `Napravi GitHub repozitorijum i pošalji projekat tamo.` (Ako nemaš GitHub nalog, prvo ga napravi besplatno na github.com — obična registracija mejlom. Ako te pri prvom slanju zatraži povezivanje naloga, samo prati uputstva na ekranu.) Otvori link u browseru i uveri se da fajlovi stoje u sefu.
5. Za kraj, zatraži podešavanje GitHub Actions promptom iz prethodne sekcije, pa napravi sitnu izmenu i gledaj kako kontrolor radi svoj posao.

### Najčešće greške

1. **Odlaganje commit-a "dok ne bude savršeno".** Onda nešto pukne i nemaš snimak za povratak. Rešenje: commit posle svake celine koja radi, makar bila sitna.
2. **Preskakanje instrumenata jer "prvo hoću da vidim aplikaciju".** Bez instrumenata svaki sledeći korak gradi na nečemu što ne umeš da proveriš. Rešenje: prompt za instrumente ide pre prve funkcionalnosti, bez izuzetka.
3. **CLAUDE.md kao mrtvo slovo.** Generišeš ga jednom i nikad ne pipneš; posle dve nedelje laže. Rešenje: svaku važnu odluku odmah diktiraj u njega, ili je zabeleži porukom koja počinje sa `#`.
4. **Verovanje na reč umesto traženja dokaza.** "Sve provere prolaze" nije dokaz — izlaz komande jeste. Rešenje: uvek traži da ti Claude pokaže rezultat testova, linta i builda.
5. **Mešanje git-a i GitHub-a.** Misliš da je projekat "u oblaku" iako commit-i postoje samo lokalno. Rešenje: posle važnijih commit-a traži i slanje na GitHub ("pošalji izmene na GitHub").

### Kontrolna lista

- [ ] Projekat ima git i bar jedan commit
- [ ] Postoji GitHub repozitorijum i poslednje stanje je poslato u njega
- [ ] `/init` je pokrenut i `CLAUDE.md` postoji
- [ ] U `CLAUDE.md` su opis proizvoda, ključne odluke, konvencije i komande
- [ ] Testovi, lint i build postoje i sve tri provere prolaze (video si izlaz svojim očima)
- [ ] Komande za provere su upisane u `CLAUDE.md`
- [ ] GitHub Actions automatski pokreće provere pri svakoj izmeni
- [ ] Zabeležio si naviku (npr. porukom sa `#`) da se commit predlaže posle svake celine

### Proveri znanje

**1. Claude je upravo polomio funkcionalnost koja je juče radila. Šta tražiš?**
Da vrati projekat na poslednji commit u kom je sve radilo — prirodnim jezikom, npr. "vrati projekat na jučerašnje stanje". Zato commit-uješ često: vremenska mašina vredi onoliko koliko ima snimaka.

**2. Zašto se merni instrumenti podešavaju pre prve funkcionalnosti, a ne posle?**
Jer bez njih nemaš način da proveriš nijednu izmenu — gradio bi sprat po sprat bez ikakvog merenja temelja. Uz to, autonomni rad iz Modula 7 zahteva merljive uslove ("testovi prolaze"), koji bez instrumenata ne postoje.

**3. U čemu je razlika između provera koje pokrećeš u sesiji i CI-ja?**
Provere u sesiji pokrećeš ti (ili Claude na tvoj zahtev), dok radiš. CI (GitHub Actions) ih pokreće automatski pri svakoj izmeni u repozitorijumu — i kad ne gledaš. Prvo je instrument-tabla u kokpitu, drugo kontrola letenja koja proverava svaki let.
