## Dodaci

Ovo poglavlje je drugačije od ostalih: nema lekcija, nema vežbi, nema pitanja. Ovo je tvoj priručnik za svaki dan — mesto na koje se vraćaš kad ti zatreba komanda koje ne možeš da se setiš, šablon prompta koji ne želiš da pišeš iz nule, ili pojam koji ti je promakao. Slobodno ga odštampaj, zalepi pored monitora ili drži otvoren u drugom prozoru dok radiš.

---

## Dodatak A: Cheat-sheet komandi

Sve komande na jednom mestu. Komande koje počinju sa `claude` kucaš u terminal (program za kucanje komandi, detaljno u Modulu 2). Komande koje počinju kosom crtom (`/`) kucaš unutar razgovora sa Claude-om.

### Instalacija i pokretanje

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `npm install -g @anthropic-ai/claude-code` | Instalira Claude Code CLI verziju (zahteva Node.js); alternativa je desktop aplikacija | Jednom, pri postavljanju računara (Modul 2) |
| `claude` | Pokreće Claude Code iz foldera projekta | Svaki put kad počinješ rad na projektu |
| `claude --resume` / `claude --continue` | Nastavak ranije sesije | Kad si juče stao na pola posla i hoćeš da nastaviš tu gde si stao |
| `claude -p "..."` | Neinteraktivno pokretanje: jedan zadatak, bez interaktivnog razgovora | Za brze, jednokratne zadatke ili automatizaciju |

### Rad u sesiji

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/init` | Generiše `CLAUDE.md` sa opisom projekta, komandama i konvencijama | Jednom po projektu, na samom početku (Modul 3) |
| Poruka koja počinje sa `#` | Claude tu napomenu trajno beleži (memorija / `CLAUDE.md`) | Kad otkriješ pravilo koje Claude treba da pamti zauvek, npr. `# uvek piši poruke commit-a na srpskom` |
| `/clear` | Briše kontekst i počinje svežu sesiju | Kad prelaziš na potpuno novi zadatak ili je razgovor postao konfuzan |
| `/compact` | Sažima dugačak razgovor da oslobodi prostor | Kad je sesija duga, a želiš da nastaviš isti posao bez gubljenja niti |
| `Shift+Tab` | Kruži kroz režime rada, uključujući plan mode (Claude istražuje i predlaže plan, ne menja fajlove dok ne odobriš) | Pre svake veće izmene — prvo plan, pa rad (Modul 5) |
| `Esc` | Prekida Claude-a usred rada; odmah možeš da ga preusmeriš | Kad vidiš da je krenuo u pogrešnom pravcu — ne čekaj da završi |
| `/fewer-permission-prompts` | Analizira tvoj rad i predlaže listu bezbednih komandi za unapred odobrenje (čuva se u `.claude/settings.json`) | Kad te Claude prečesto pita za dozvole za iste, bezopasne stvari |

### Autonomni rad (detaljno u Modulu 7)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/goal <uslov>` | Claude radi turu za turom autonomno dok uslov nije ispunjen; posle svake ture mali brzi model (Haiku) ocenjuje da li uslov važi | Za zadatke sa jasnim, dokazivim ciljem, npr. „svi testovi prolaze" |
| `/goal` | Prikazuje status: uslov, broj tura, vreme, potrošnju tokena | Kad hoćeš da proveriš dokle je stigao |
| `/goal clear` | Prekida aktivni goal | Kad odustaješ ili menjaš cilj (novi goal i sam zamenjuje stari) |
| `/loop 5m <prompt>` | Ponavlja prompt na fiksni interval (jedinice: `s`, `m`, `h`, `d`) | Za periodične provere dok radiš nešto drugo |
| `/loop <prompt>` | Dinamički režim: Claude sam bira pauze (1–60 min) prema aktivnosti i može sam da završi petlju kad je posao gotov | Kad ne znaš tačan ritam, ali hoćeš da Claude prati posao |
| `/loop` | Podrazumevani prompt za održavanje sesije (nastavi nedovršeno, sredi PR); prilagođava se kroz `.claude/loop.md` | Kad hoćeš da Claude „dežura" nad projektom dok je sesija otvorena |
| `/schedule` | Routines: zakazani cloud agenti koji rade i kad je tvoj računar ugašen | Za redovne zadatke van sesije, npr. dnevni izveštaj (Modul 10) |

Napomena: `/loop` važi samo dok je sesija otvorena (najviše 7 dana) i ne radi kad je računar ugašen — za to postoji `/schedule`. `/goal` radi i neinteraktivno: `claude -p "/goal ..."`.

### Kvalitet i bezbednost (detaljno u Modulu 8)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/code-review` | Pregled trenutnih izmena koda; nivoi temeljnosti `low`/`medium`/`high`/`max` | Posle svake završene funkcionalnosti, pre spajanja izmena |
| `/code-review ultra` | Multi-agent pregled celog brancha u cloudu — najtemeljniji, dodatno se naplaćuje | Pred lansiranje ili pred veliku, rizičnu izmenu |
| `/security-review` | Bezbednosni pregled izmena na trenutnom branchu | Pre lansiranja i posle svake izmene koja dira lozinke, plaćanja ili podatke korisnika |
| `/simplify` | Pojednostavljuje i čisti izmenjeni kod (ne traži bagove) | Kad funkcionalnost radi, a hoćeš da kod ostane uredan i održiv |

### Ekosistem (detaljno u Modulu 12)

| Komanda | Šta radi | Kada je koristiš |
|---|---|---|
| `/vercel:bootstrap` | Postavlja projekat za rad sa Vercel-om (hosting, env varijable) — deo vercel plugin-a | Jednom, kad povezuješ projekat sa hostingom (Modul 9) |
| `/vercel:deploy` | Pravi preview deploy — probnu verziju na privatnom linku | Pre svakog objavljivanja: prvo proveriš na privatnom linku (Modul 9) |
| `/vercel:deploy prod` | Objavljuje u produkciju | Tek kad preview verzija radi besprekorno — nikad direktno u produkciju (Modul 9) |

### Korisni fajlovi koje vredi znati

| Fajl | Čemu služi |
|---|---|
| `CLAUDE.md` | Claude-ovo „dugoročno pamćenje" o projektu — učitava se na početku svake sesije |
| `.claude/settings.json` | Lista unapred dozvoljenih komandi (dozvole) |
| `.claude/loop.md` | Prilagođeni podrazumevani prompt za `/loop` |
| `docs/spec.md` | Tvoja specifikacija proizvoda (Modul 4) |

---

## Dodatak B: Šabloni promptova

Osam šablona za situacije koje se najčešće ponavljaju. Kopiraj, zameni sve što je u uglastim zagradama `[OVAKO]` svojim sadržajem, i pošalji. Logika iza svakog šablona objašnjena je u modulima na koje se odnose; ovde je samo „gotova jela".

### Šablon 1: Inicijalizacija novog projekta sa mernim instrumentima

Koristiš na samom početku, posle Modula 3. Posle ovog prompta ukucaj i `/init` da nastane `CLAUDE.md`.

```
Pravim novi projekat: [KRATAK OPIS PROIZVODA, npr. "veb aplikacija za zakazivanje termina u frizerskom salonu"].

Postavi temelje:
1. Inicijalizuj git repozitorijum i napravi prvi commit.
2. Postavi projekat koristeći [TEHNOLOGIJA, ili napiši: "predloži mi standardan, dobro podržan izbor tehnologija za ovakav proizvod i objasni ga laičkim jezikom pre nego što kreneš"].
3. Podesi tri merna instrumenta: testove, lint i build.
4. Pokreni sve tri komande i pokaži mi njihov izlaz kao dokaz da prolaze.

Ja nisam programer — kad god doneseš tehničku odluku, objasni mi je u jednoj rečenici.
```

### Šablon 2: Brainstorm koji te izaziva

Koristiš pre nego što napišeš i jedan red specifikacije (Modul 4). Poenta je da Claude bude kritičar, ne navijač.

```
Imam ideju za proizvod: [OPIS IDEJE U 2-3 REČENICE].

Budi mi kritičan sagovornik, ne navijač:
1. Postavi mi 10 najtežih pitanja na koja moram da imam odgovor pre nego što počnem.
2. Navedi 3 najverovatnija razloga zašto ova ideja može da propadne.
3. Predloži 2 alternativna ugla na isti problem koje možda nisam razmotrio.
4. Reci mi šta je NAJMANJA verzija ove ideje koja i dalje rešava stvarni problem.

Ne piši nikakav kod i ne menjaj nijedan fajl — ovo je samo razgovor. Pitanja mi postavljaj jedno po jedno i sačekaj moj odgovor.
```

### Šablon 3: Pisanje spec-a

Koristiš posle brainstorma, kad je ideja prečišćena (Modul 4).

```
Na osnovu našeg dosadašnjeg razgovora napiši specifikaciju proizvoda u fajl docs/spec.md.

Proizvod: [IME + JEDNA REČENICA ŠTA RADI]
Za koga je: [CILJNA GRUPA]
Glavni problem koji rešava: [PROBLEM]

Struktura dokumenta:
1. Problem i za koga ga rešavamo
2. MVP funkcionalnosti — najviše [BROJ, npr. 5], svaka opisana iz ugla korisnika ("korisnik može da...")
3. Šta svesno NIJE u MVP-u (i zašto)
4. Merljivi kriterijumi uspeha za svaku funkcionalnost

Pravila: piši jednostavnim srpskim jezikom, bez tehničkog žargona. Sve što ti je nejasno — pitaj me PRE pisanja, nemoj da pretpostavljaš.
```

### Šablon 4: Arhitektonska odluka (2 opcije + preporuka)

Koristiš kad treba doneti tehničku odluku, a nemaš tehničko znanje (Modul 5). Najbolje radi u plan mode-u.

```
Treba da odlučimo: [ODLUKA, npr. "gde i kako čuvamo podatke korisnika"].

Predstavi mi tačno 2 realne opcije. Za svaku:
- objasni je u jednom pasusu, kao da objašnjavaš nekome ko nikad nije programirao
- navedi najviše 3 prednosti i 3 mane
- reci šta znači za troškove (sada i kad poraste broj korisnika) i za održavanje

Na kraju daj svoju preporuku i JEDAN ključni razlog za nju.
Ne menjaj nijedan fajl dok ti ne kažem koju opciju biramo.
```

### Šablon 5: Feature ciklus (kontekst → zadatak → kriterijum → ograničenja)

Tvoj svakodnevni radni prompt (Modul 6). Ovo je formula koju ćeš koristiti najčešće.

```
KONTEKST: Radimo na projektu [IME]. Trenutno stanje: [ŠTA VEĆ POSTOJI I RADI, npr. "korisnik može da se registruje i prijavi"].

ZADATAK: Dodaj [FUNKCIONALNOST OPISANA IZ UGLA KORISNIKA — šta korisnik vidi i šta može da uradi].

KRITERIJUM USPEHA: Gotovo je tek kada [MERLJIV USLOV, npr. "korisnik može da rezerviše termin, dobije potvrdu na ekranu, i svi testovi prolaze"].

OGRANIČENJA:
- Ne diraj [DELOVI KOJE NE TREBA MENJATI, npr. "postojeću prijavu korisnika"].
- Postojeći testovi moraju i dalje da prolaze.
- Napiši testove i za novu funkcionalnost.
- Ako ti bilo šta nije jasno, pitaj me pre nego što kreneš.

Na kraju mi pokaži dokaz: izlaz testova i kratak opis šta si promenio.
```

### Šablon 6: /goal uslov

Koristiš za autonoman rad (Modul 7). Zapamti pravilo: uslov mora biti dokaziv kroz ono što Claude pokaže u razgovoru — „aplikacija je kvalitetna" kontrolor ne može da izmeri, „testovi prolaze" može.

```
/goal [MERLJIVO ZAVRŠNO STANJE, npr. "funkcionalnost rezervacije termina je implementirana"]. Provera: komanda `[TEST KOMANDA, npr. npm test]` izlazi bez ijedne greške i `[BUILD KOMANDA, npr. npm run build]` prolazi. Ograničenja: postojeći testovi se ne menjaju i ne brišu. Ako uslov nije ispunjen posle [BROJ, npr. 20] tura, stani i napiši šta te blokira.
```

### Šablon 7: Verifikacija sa dokazom

Koristiš kad Claude tvrdi da je nešto gotovo, a ti hoćeš dokaz, ne obećanje (princip iz Modula 1).

```
Tvrdiš da je [FUNKCIONALNOST] gotova. Dokaži mi to:

1. Pokreni sve testove i pokaži mi kompletan izlaz.
2. Pokreni aplikaciju i prođi kroz ovaj scenario kao korisnik: [KORACI, npr. "otvori početnu stranu, prijavi se kao test korisnik, rezerviši termin za sutra u 14h"]. Napravi screenshot svakog koraka.
3. Proveri i šta se dešava kad korisnik pogreši: [LOŠ SCENARIO, npr. "pokuša da rezerviše već zauzet termin"] — i to mi pokaži.

Ako bilo šta ne radi, nemoj da mi objašnjavaš zašto — popravi, pa ponovi ceo dokaz ispočetka. Ne prihvatam "trebalo bi da radi": samo izlaz komandi i screenshotove.
```

### Šablon 8: Priprema za lansiranje

Koristiš pred objavljivanje (Modul 9). Posle ovog prompta sam pokreni i `/security-review` i `/code-review` — to su tvoje nezavisne kontrole.

```
Pripremamo [IME PROJEKTA] za lansiranje. Prođi kroz ovu listu i za SVAKU stavku mi pokaži dokaz (izlaz komande, screenshot ili sadržaj fajla):

1. Build prolazi bez grešaka i upozorenja.
2. Svi testovi prolaze.
3. Nijedna tajna (lozinka, API ključ) nije upisana direktno u kod — sve je u env varijablama, a fajl sa tajnama je isključen iz git-a.
4. Aplikacija razumno reaguje na greške: [KLJUČNI LOŠI SCENARIO, npr. "pad veze sa bazom"] ne ruši ceo sajt nego prikazuje poruku.
5. Probaj aplikaciju na ekranu veličine telefona i pokaži mi screenshot.

Za svaku stavku koja NE prolazi: prvo mi reci šta si našao, predloži popravku, i sačekaj moje odobrenje pre menjanja.
```

---

## Dodatak C: Rečnik pojmova

Trideset pojmova koje ćeš sretati svakodnevno, objašnjenih bez žargona. Ako te neki pojam zanima dublje, pored njega stoji modul u kom se detaljno obrađuje.

**API** — način na koji programi pričaju jedni s drugima, kao konobar između tebe i kuhinje: ti naručiš, on prenese, kuhinja vrati jelo. Kad tvoja aplikacija „povlači podatke" od nekog servisa, radi to preko API-ja.

**auth (autentifikacija)** — sve oko provere ko je korisnik: registracija, prijava, lozinke, nalozi. Deo aplikacije koji odgovara na pitanje „ko si ti i šta smeš da vidiš".

**backend** — deo aplikacije koji korisnik ne vidi: radi na serveru, obrađuje podatke i logiku. Kuhinja restorana — gosti je ne vide, ali bez nje nema jela.

**backlog** — uredna lista svega što čeka da bude urađeno, poređana po važnosti. Tvoj „spisak želja" za proizvod (Modul 10).

**baza podataka** — organizovano skladište podataka tvoje aplikacije: korisnici, narudžbine, poruke. Zamisli digitalni arhivski ormar u kom svaka fioka ima svoje mesto i etiketu.

**branch (grana)** — paralelna kopija koda u git-u na kojoj možeš da eksperimentišeš bez diranja glavne verzije. Kad si zadovoljan, izmene se spajaju nazad.

**build** — proces „sklapanja" izvornog koda u verziju spremnu za rad. Ako build pukne, znaš da nešto fundamentalno ne valja — zato je jedan od tvoja tri merna instrumenta (Modul 3).

**CI (continuous integration)** — robot na GitHub-u koji automatski pokreće testove i provere pri svakoj izmeni koda. Tvoj kontrolor kvaliteta koji nikad ne spava (Modul 3).

**commit** — sačuvana „fotografija" stanja celog projekta u git-u, sa opisom šta je promenjeno. Tačka u istoriji na koju uvek možeš da se vratiš ako nešto krene naopako.

**deploy** — objavljivanje aplikacije na internet, da bude dostupna stvarnim korisnicima. Trenutak kad jelo izlazi iz kuhinje u salu (Modul 9).

**env varijabla** — podešavanje ili tajna (API ključ, lozinka za bazu) koja se čuva van koda, u posebnom fajlu ili na hosting servisu. Tajne nikad ne idu u kod, jer kod ide na GitHub.

**feature** — jedna funkcionalnost proizvoda iz ugla korisnika: „korisnik može da rezerviše termin". Osnovna jedinica posla u ritmu razvoja (Modul 6).

**frontend** — deo aplikacije koji korisnik vidi i koristi: ekrani, dugmad, forme, boje. Sala restorana, u kojoj gost provodi vreme.

**git** — program koji pamti kompletnu istoriju svih izmena koda. Vremenska mašina tvog projekta: u svakom trenutku znaš šta je promenjeno, kada, i možeš da se vratiš (Modul 3).

**kontekst** — sve što Claude „drži u glavi" tokom jedne sesije: razgovor, fajlove koje je pročitao, ono što je uradio. Ograničen je — zato postoje `/clear` i `/compact` (Modul 1).

**lint** — automatski lektor za kod: pronalazi stilske greške, nedoslednosti i sumnjiva mesta pre nego što postanu problemi. Drugi od tri merna instrumenta.

**log** — dnevnik onoga što se dešava u aplikaciji dok radi: ko se prijavio, šta je puklo i zašto. Prvo mesto na kom se traži uzrok problema (Modul 13).

**MVP (minimum viable product)** — najmanja verzija proizvoda koja rešava stvarni problem stvarnom korisniku. Sve preko toga je ukras koji čeka svoj red (Modul 4).

**plan mode** — režim rada u kom Claude istražuje i predlaže plan, ali ne menja nijedan fajl dok plan ne odobriš. Tvoja sigurnosna kočnica pre velikih izmena (Modul 5).

**PR (pull request)** — formalni predlog: „ove izmene želim da ubacim u glavnu verziju koda". Mesto gde se izmene pregledaju pre nego što budu prihvaćene.

**preview** — probna verzija sajta na privremenoj internet adresi, da izmene vidiš i isprobaš pre nego što odu u produkciju. Generalna proba pred premijeru.

**produkcija** — „prava" verzija aplikacije, ona koju koriste stvarni korisnici. Sve što dotiče produkciju zaslužuje dodatnu pažnju i dokaz da radi.

**prompt** — poruka, uputstvo ili zahtev koji daješ Claude-u. Kvalitet prompta direktno određuje kvalitet rezultata (Modul 11).

**refaktorisanje** — sređivanje koda iznutra bez promene onoga što korisnik vidi. Kao generalno raspremanje kuhinje: meni ostaje isti, ali se posle kuva brže i bezbednije.

**repo (repozitorijum)** — folder projekta pod nadzorom git-a; na GitHub-u dobija i svoju online kopiju. Kad neko kaže „pogledaj repo", misli na ceo projekat sa istorijom.

**sesija** — jedan razgovor sa Claude Code-om. Između sesija Claude ne pamti ništa, osim fajla `CLAUDE.md` i memorije — zato je `CLAUDE.md` toliko važan (Modul 1).

**stack** — skup tehnologija od kojih je proizvod sagrađen: jezik, framework, baza, hosting. Kao spisak materijala od kojih je sagrađena kuća.

**test** — automatska provera da određeni deo aplikacije radi kako treba. Sigurnosna mreža: kad Claude nešto menja, testovi javljaju ako je usput nešto pokvario. Najvažniji od tri merna instrumenta.

**token** — jedinica teksta (otprilike deo reči) kojom se meri koliko Claude čita i piše, pa i koliko rad košta. Zato `/goal` status prikazuje potrošnju tokena.

**UI (user interface)** — korisnički interfejs: sve vizuelno preko čega korisnik komunicira sa aplikacijom — dugmad, forme, raspored, boje.

---

Toliko od priručnika. Ako si stigao dovde čitajući redom — čestitam: prošao si ceo put od ideje do proizvoda na produkciji. Sada se vraćaj ovde po potrebi, a kada nešto krene naopako, Modul 13 te čeka. Srećno graditeljstvo.
