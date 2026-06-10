## Poglavlje 2: Nauka učenja — šest principa koje 95% ignoriše

### Šta ćeš dobiti iz ovog poglavlja

- Šest principa nauke učenja, svaki u formatu: nalaz → kako 95% greši → šta ti radiš sutra
- Pravilo 30/70 za strukturu svake radionice
- Copy-paste šablone: kviz za otvaranje sesije, struktura "ja → mi → ti" bloka, formula za feedback
- Severnjaču celog dizajna: Bloomov 2-sigma nalaz i kako mu se približavaš strukturom

Većina edukatora dizajnira programe na osnovu intuicije: "ovako su mene učili, ovako ću i ja". Problem je što intuicija o učenju sistematski greši — i to je merljivo. Ovo poglavlje ti daje šest principa sa naučnim utemeljenjem i, važnije, šest konkretnih tehnika koje primenjuješ na sledećoj radionici. Ne sledeće godine. Sledećoj.

### Princip 1: Aktivno učenje pobeđuje predavanje — pravilo 30/70

**Nalaz:** Meta-analiza 225 studija pokazala je da aktivne metode (vežbe, diskusija, rešavanje problema) značajno smanjuju stopu pada i podižu rezultate u odnosu na klasično predavanje. Predavanje je najmanje efikasna, a najčešće korišćena metoda (Freeman et al., 2014).

Brojka 30/70 nije iz studije — to je radna heuristika ovog priručnika, dovoljno gruba da je primeniš na plan radionice već sutra.

**Kako 95% greši:** Radionica od 2 sata = 100 minuta slajdova + 20 minuta "ima li pitanja?". Edukator se oseća produktivno jer je "pokrio gradivo". Polaznici klimaju glavom i ne umeju ništa novo.

**Tvoja primena sutra:** Pravilo 30/70 — maksimalno 30% vremena ti pričaš ili demonstriraš, minimalno 70% polaznici rade. Otvori plan svoje sledeće radionice i obeleži svaki blok slovom P (pričam) ili R (rade). Ako P blokovi prelaze trećinu, seci: svaki P blok duži od 10 minuta razbij ubacivanjem zadatka "sada ti — 5 minuta".

❌ "Sada ću vam pokazati još tri primera prompta..."
✅ "Pokazao sam jedan. Sledeća dva pišete vi — 7 minuta, pa poredimo."

### Princip 2: Prisećanje jača pamćenje više od ponavljanja

**Nalaz:** Aktivno prisećanje (kviz, vežba bez gledanja u materijal) jača dugoročno pamćenje znatno više od ponovnog čitanja ili gledanja istog sadržaja (Roediger & Karpicke, 2006).

**Kako 95% greši:** "Da se podsetimo šta smo radili prošli put" — i onda edukator SAM prepriča prošlu sesiju. Polaznici pasivno slušaju rezime i mozak ne radi ništa.

**Tvoja primena sutra:** Svaku radionicu otvori kvizom od 3 pitanja iz prošle sesije — polaznici odgovaraju PRE nego što im išta kažeš. Zatvori je zadatkom "uradi bez gledanja": jedna ključna radnja iz današnje sesije, bez beležaka i bez tvog ekrana.

```text
ŠABLON — otvaranje sesije (5 min, bez gledanja u materijale):
1. [Činjenica] Kojom komandom pokrećeš Claude Code u svom projektu?
2. [Proces] Kojim redosledom ideš od ideje do prvog radnog prototipa?
3. [Zašto] Zašto prvo pišemo CLAUDE.md, a ne odmah tražimo kod?

ŠABLON — zatvaranje sesije (10 min):
"Zatvorite beleške. Sami, od nule: [današnja ključna radnja].
Ko zaglavi — ruka gore, ali tek posle 3 minuta pokušaja."
```

### Princip 3: Raspoređeno ponavljanje umesto zbijenog bubanja

**Nalaz:** Gradivo raspoređeno kroz vreme pamti se bolje od zbijenog ponavljanja u jednom bloku (spacing effect).

**Kako 95% greši:** Svaka tema dobije svoju sesiju, "obradi se" jednom i nikad više ne pomene. Modul 3 je završen — prelazimo na modul 4. Posle šest nedelja polaznici se modula 1 sećaju maglovito.

**Tvoja primena sutra:** Napravi tabelu vraćanja koncepata. Za svaki ključni koncept iz tvog kurikuluma odredi u kojim sesijama se NAMERNO vraća — ne kao ponovno predavanje, nego kao pitanje u kvizu ili sastojak novog zadatka.

| Koncept | Uveden | Vraća se u kvizu | Vraća se u zadatku |
|---|---|---|---|
| CLAUDE.md kao kontekst | Sesija 1 | Sesije 2, 4 | Sesija 5 (kapstone setup) |
| Iterativni prompt (plan → kod → test) | Sesija 2 | Sesije 3, 5 | Svaka sesija od 3. nadalje |
| Deploy proces | Sesija 4 | Sesije 5, 6 | Sesija 6 (lansiranje) |

### Princip 4: Kognitivna opterećenost — radna memorija je usko grlo

**Nalaz:** Radna memorija drži oko 4±1 elementa istovremeno; sve preko toga se gubi (Sweller, cognitive load theory).

**Kako 95% greši:** Slajd sa 9 bullet-a, tri nova alata u jednoj sesiji, i samostalan zadatak odmah posle prvog objašnjenja. Polaznik nije glup — njegov bafer je pun.

**Tvoja primena sutra:** Tri rezna pravila za svaku sesiju:
1. **Male celine:** jedna sesija = jedan ishod koji se da izgovoriti u jednoj rečenici ("danas svako pokreće svoj prvi lokalni prototip").
2. **Čisti slajdovi:** maksimalno 4 elementa po slajdu. Sve "zanimljivo ali nebitno" briši — to je opterećenje, ne vrednost.
3. **Razrađen primer pre samostalnog zadatka (worked example):** prvo kompletno rešen primer korak po korak, pa tek onda sličan zadatak koji rade sami. Za ne-tehničke polaznike ovo je presudno — bez razrađenog primera, prazan terminal je zid.

### Princip 5: Namerna vežba + povratna informacija na zadatak

**Nalaz:** Napredak dolazi iz vežbe na ivici trenutne sposobnosti, sa neposrednom povratnom informacijom — ne iz ponavljanja onoga što već ide (Ericsson, deliberate practice). Povratna informacija je među najjačim pojedinačnim uticajima na učenje, ali samo kad je specifična, pravovremena i usmerena na zadatak, ne na ličnost (Hattie, Visible Learning).

**Kako 95% greši:** Svi dobiju isti zadatak (prelak za pola grupe, pretežak za drugu polovinu), a feedback stigne za nedelju dana u obliku "super ti je ovo, samo nastavi".

**Tvoja primena sutra:** Svaki zadatak pravi u dve verzije — osnovnu i "tik iznad" (ista vežba + jedan dodatni zahtev koji još nisu radili). Feedback daješ u toku same sesije, po formuli:

```text
FORMULA FEEDBACKA (na zadatak, nikad na ličnost):
1. ŠTA konkretno radi: "Tvoj prompt jasno definiše ulaz i izlaz."
2. ŠTA konkretno ne radi: "Ali ne kaže Claude-u šta da radi kad podatak fali."
3. SLEDEĆI korak: "Dodaj jednu rečenicu o ivičnom slučaju i pokreni ponovo."

❌ "Odlično ti ide!" / "Moraš se više potruditi."
✅ "Korak 2 ti je preskočen — vrati se na plan pre koda i probaj opet."
```

### Princip 6: "Ja → mi → ti" — i zašto preskakanje "mi" ubija samopouzdanje

**Nalaz:** Gradual release of responsibility: demonstracija (ja radim), pa vođena vežba (radimo zajedno), pa samostalan rad (ti radiš). Preskakanje srednjeg koraka je najčešća greška.

**Kako 95% greši:** Demonstracija pa odmah "sad vi sami". Polaznik koji prvi put vidi terminal ostane sam pred greškom koju ne ume da pročita, zaključi "ovo nije za mene" — i to je trenutak u kom gubiš completion rate (stopu završavanja programa). Tehnika izvođenja sve tri faze detaljno je u poglavlju 4; ovde je princip.

**Tvoja primena sutra:** Svaki novi koncept prolazi kroz sva tri bloka u ISTOJ sesiji:

```text
JA (10 min): radiš uživo, naglas komentarišeš ŠTA i ZAŠTO — uključujući
   i grešku koju namerno napraviš i razrešiš (psihološka sigurnost:
   polaznici vide da je greška normalan deo procesa, ne sramota).
MI (15 min): isti tip zadatka, ali polaznici diktiraju sledeći korak,
   a ti izvršavaš. "Šta sad kucamo? Zašto?" Niko ne sme da ćuti dva kruga.
TI (20 min): sličan zadatak, samostalno. Ti kružiš i daješ feedback
   po formuli iz principa 5.
```

### Severnjača: Bloomova 2 sigme

Prosečan polaznik sa kombinacijom 1-na-1 tutorstva i mastery learninga (ne prelaziš na sledeću celinu dok prethodna nije proverena, ne samo odslušana) postiže rezultat bolji od 98% polaznika klasične učionice (Bloom, 1984). Tutorstvo niko nije skalirao — ali tvoj posao kao dizajnera programa je da mu se PRIBLIŽIŠ strukturom: mastery kontrolne tačke na kraju svake celine (kviz + "uradi bez gledanja"), mentorske tačke (kratke individualne provere u kapstone fazi), i vršnjački feedback po formuli iz principa 5. Svaki od šest principa iznad je jedan korak ka tom efektu. Kako se to pretvara u dizajn celog programa od ishoda unazad — detaljno u poglavlju 3.

### Coaching zadatak

Do kraja nedelje imaš **revidiran plan jedne svoje radionice na jednoj strani**, koji sadrži:

1. Svaki blok obeležen P/R i odnos vremena ≤30/≥70 (princip 1)
2. Upisan kviz od 3 pitanja na otvaranju + "uradi bez gledanja" zadatak na zatvaranju (princip 2)
3. Tabelu vraćanja za 3 ključna koncepta (princip 3)
4. Za jedan novi koncept: razrađen primer + raspisan "ja → mi → ti" blok sa minutažom (principi 4 i 6)

Test prolaznosti: daj plan nekome ko nije bio na radionici — ako iz njega ne vidi šta polaznici RADE svakih 15 minuta, plan nije gotov.

### Pitanja za samoprocenu

1. U poglavlju 1 si izračunao odnos P/R svoje poslednje radionice. Koliki je taj odnos u planu koji si upravo revidirao — i koji P blok je bio najteže iseći?
2. Kada si poslednji put proverio šta polaznici pamte iz prethodne sesije — i kako tačno (kviz, zadatak, ili "ima li pitanja")?
3. Koji koncept iz tvog programa se pojavljuje samo jednom i nikad ne vraća? Šta očekuješ da polaznici znaju o njemu posle šest nedelja?
4. Navedi poslednji feedback koji si dao polazniku, od reči do reči. Da li sadrži konkretan sledeći korak, ili je ohrabrenje?
5. U poslednjoj sesiji sa novim konceptom — da li je postojala "mi" faza, ili si sa demonstracije skočio na "sad vi"?

### Crvene zastavice

- Praviš nove slajdove umesto novih vežbi — sadržaj raste, aktivnost stoji.
- "Nemamo vremena za kviz, moramo da pređemo gradivo" — pokrivanje gradiva ti je postalo važnije od toga da li je iko išta naučio.
- Feedback daješ tek posle sesije, mejlom, uopšteno — umesto u toku rada, na konkretan zadatak.
- Najbolji polaznici ti služe kao dokaz da metoda radi, dok tiha polovina grupe zaostaje — zadaci nisu kalibrisani tik iznad nivoa, nego za one kojima i ne trebaš.
