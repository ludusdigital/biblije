## Modul 5: Planiranje i arhitektura: odlučivanje bez tehničkog znanja

Imaš specifikaciju iz Modula 4. Sledeći refleks većine ljudi je: "Hajde, Claude, pravi!" Sačekaj. Pre nego što se zida kuća, arhitekta donese nacrt na sto. Ti ga pogledaš, postaviš pitanja, tražiš izmene, i tek kad ti potpišeš, počinje gradnja. U ovom modulu učiš upravo to: kako da budeš investitor koji pametno odobrava nacrte, iako sam nikad nije držao mistriju.

### Šta ćeš naučiti

- Šta je plan mode i zašto je tvoj najvažniji zaštitni mehanizam
- Formulu za donošenje tehničkih odluka bez tehničkog znanja: 2 opcije + preporuka + razmena
- Četiri zlatna pitanja koja postavljaš pre svake važne odluke
- Kako da kažeš Claude-u za šta optimizuješ, i zašto bez toga on samo pogađa
- Standardni početni tehnološki skup (Next.js + Supabase + Vercel) objašnjen jezikom prodavnice, a ne programera

### Plan mode: nacrt pre zidanja

Plan mode je poseban režim rada u kom Claude **istražuje i predlaže, ali ništa ne menja**. Čita tvoje fajlove, razmišlja, piše plan, i čeka tvoje odobrenje. Tek kad kažeš "može", kreće da menja kod.

Zašto je ovo važno baš tebi, kao netehničkoj osobi? Zato što je čitanje plana na srpskom jeziku nešto što TI umeš da proceniš. Kod možda ne razumeš, ali rečenicu "napravićemo stranicu za prijavu pa tek onda plaćanje", razumeš savršeno. Plan mode premešta odluku na teren gde si ti jak.

Uključuje se prečicom `Shift+Tab` (ona kruži kroz režime rada, pa pritiskaj dok ne vidiš plan mode). A ako prečicu zaboraviš, dovoljno je da napišeš:

```
Prvo napravi plan, ne menjaj ništa dok ne odobrim.
```

Pravilo palca: sve što je veće od sitne ispravke teksta zaslužuje plan. Plan je jeftin, pet minuta čitanja. Pogrešno izgrađen temelj je skup, dani vraćanja unazad.

### Formula odlučivanja: 2 opcije + preporuka + razmena

Tokom planiranja Claude će nailaziti na raskrsnice: koju bazu podataka, koji način prijave korisnika, gde čuvati slike. Ako ga pustiš, odlučiće sam, i to često sasvim dobro. Ali ti si direktor, i direktor odlučuje o stvarima koje koštaju novac i vreme. Zato uvedi kućno pravilo:

```
Za svaku važnu tehničku odluku u ovom projektu:
1. Ponudi mi tačno 2 opcije.
2. Reci koju TI preporučuješ.
3. Objasni razmena (šta dobijam, šta žrtvujem) jezikom za nekoga
   ko nije programer, bez žargona, sa poređenjem iz svakodnevnog života.
```

*Razmena* je razmena: svaki izbor nešto daje i nešto uzima. Jeftiniji lokal je dalje od centra. Brži auto troši više. Ne postoji opcija bez cene, postoji samo cena koju nisi video. Tvoj posao nije da znaš tehnologije; tvoj posao je da tražiš da ti cena bude pokazana.

Dve opcije, ne pet. Sa pet opcija se davi i iskusan inženjer; sa dve opcije i jasnom preporukom, odluka traje dva minuta.

### Četiri zlatna pitanja

Kad ti Claude ponudi opcije, ova četiri pitanja postavljaš uvek, nauči ih napamet, kao pin kod:

```
1. Šta je rizik ovog izbora? Šta najgore može da se desi?
2. Šta je teže promeniti kasnije, opciju A ili opciju B?
3. Koliko me ovo košta mesečno, danas i kad budem imao 1.000 korisnika?
4. Šta bi TI izabrao za ovaj konkretan projekat i zašto?
```

Drugo pitanje je najvrednije. Neke odluke su tapete, promeniš ih za popodne. Druge su nosivi zidovi, menjaš ih rušenjem pola kuće. Boja dugmeta je tapeta. Izbor baze podataka je bliže nosivom zidu. Kad znaš šta je zid, znaš gde da uložiš pažnju, a gde da odlučiš za trideset sekundi i ne osvrćeš se.

### Reci za šta optimizuješ

Ovo je rečenica koju većina početnika nikad ne izgovori, a menja sve. Claude ne zna da li praviš prototip za vikend ili sistem za banku, ako mu ne kažeš, **pogađa**. Isti zadatak ima tri različita dobra odgovora u zavisnosti od cilja:

- **Brzina do prvog korisnika**, najjednostavnije što radi, gotovi servisi, minimalno podešavanja.
- **Skala**, izdrži rast, čak i ako je početak sporiji i skuplji.
- **Trošak**, što bliže nuli mesečno, čak i po cenu ručnog rada.

Zato svaki plan počni ovako:

```
Kontekst: ovo je MVP, optimizujem za brzinu do prvog korisnika.
Budžet je do 20 evra mesečno. Skala me sada ne zanima, ako proizvod
uspe, prepravićemo. Predlaži najjednostavnija rešenja koja rade.
```

❌ "Napravi mi aplikaciju za rezervacije.", Claude pogađa tvoje prioritete.
✅ "Napravi plan za MVP aplikacije za rezervacije. Optimizujem za brzinu lansiranja, budžet 20 €/mesečno, jedan grad, do 50 korisnika u prva tri meseca.", Claude bira ciljano.

### Standardni početni tehnološki skup: izlog, magacin i lokal

*Tehnološki skup* je skup tehnologija od kojih je proizvod sagrađen, kao spisak materijala za kuću. Za prvi proizvod ne moraš da istražuješ: postoji proverena kombinacija koju koristi ogroman broj malih timova, pa je i Claude odlično poznaje.

- **Next.js**, *izlog i unutrašnjost prodavnice*. Ono što korisnik vidi i sa čim klikće: stranice, dugmad, forme.
- **Supabase**, *magacin sa katancem*. Tu žive podaci (korisnici, narudžbine, sadržaj) i sistem za prijavljivanje, ko sme da uđe i šta sme da vidi.
- **Vercel**, *lokal koji iznajmljuješ*. Tvoja prodavnica mora negde fizički da stoji da bi je ljudi posetili; Vercel je adresa na internetu gde tvoja aplikacija živi, sa kirijom koja je za početak nula ili sitna.

Zašto baš ovo? Sve troje ima besplatan početni nivo, međusobno se lepo uklapaju, a za Vercel i Supabase postoje i plugin-ovi za Claude Code (detaljno u Modulu 12; lansiranje na Vercel obrađuje Modul 9). Ako Claude predloži nešto drugo i laički ti obrazloži zašto je za tvoj slučaj bolje, saslušaj ga, zato i postavljaš zlatna pitanja. Ali teret dokazivanja je na alternativi, ne na standardu.

### Odluke upiši u CLAUDE.md: ili ne postoje

Claude između sesija ne pamti ništa osim fajla `CLAUDE.md` (i memorije). Odluka doneta u razgovoru, a nezapisana, sutra je, nepostojeća. Nova sesija će istu raskrsnicu rešiti iznova, možda drugačije, i dobićeš proizvod koji se sam sa sobom svađa.

Zato se svaka usvojena odluka odmah zapisuje. Možeš da zamoliš Claude-a:

```
Usvojili smo odluke: Next.js + Supabase + Vercel, optimizujemo za brzinu
do prvog korisnika, budžet 20 €/mesečno. Upiši ovo u CLAUDE.md u sekciju
"Arhitektonske odluke", sa jednom rečenicom obrazloženja po odluci.
```

Ili iskoristi prečicu: poruka koja počinje sa `#` se trajno beleži u memoriju/CLAUDE.md. O ulozi `CLAUDE.md` kao "radne sveske" projekta detaljno smo pričali u Modulu 1 i Modulu 3.

### Vežba

1. Otvori terminal u folderu svog projekta i pokreni `claude`.
2. Uključi plan mode prečicom `Shift+Tab` (ili napiši: "prvo plan, ništa ne menjaj dok ne odobrim").
3. Nalepi prompt, prilagodi svojoj specifikaciji iz Modula 4:

```
Pročitaj docs/spec.md. Predloži arhitekturu za MVP. Kontekst:
optimizujem za brzinu do prvog korisnika, budžet 20 €/mesečno,
nisam programer. Za svaku važnu odluku daj 2 opcije, svoju
preporuku i razmena objašnjen laički.
```

4. Za svaku raskrsnicu u planu postavi bar dva od četiri zlatna pitanja. Posebno: "Šta je teže promeniti kasnije?"
5. Kad si zadovoljan, odobri plan i traži da se usvojene odluke upišu u `CLAUDE.md`.
6. Pokreni `/clear` pa pitaj: "Koje su arhitektonske odluke ovog projekta?" Ako Claude odgovori tačno, zapisivanje radi.

### Najčešće greške

1. **Preskakanje plana jer "žuri mi se".** Pet minuta čitanja plana štedi dane prepravki. Rešenje: plan mode kao podrazumevani početak za svaku veću izmenu.
2. **Klimanje glavom na plan koji ne razumeš.** Ako ne umeš da prepričaš plan prijatelju, nisi ga odobrio, samo si kliknuo. Rešenje: "Objasni mi tačku 3 kao da imam petnaest godina."
3. **Nisi rekao za šta optimizuješ.** Claude tada pogađa, često ka složenijem rešenju nego što ti treba. Rešenje: rečenica o cilju i budžetu na početku svakog planiranja.
4. **Odluke ostale u razgovoru, ne u `CLAUDE.md`.** Sledeća sesija kreće od nule i odlučuje drugačije. Rešenje: nijedna rasprava se ne završava bez upisa usvojenog zaključka.
5. **Egzotičan tehnološki skup jer je "najnoviji".** Za novu tehnologiju ima manje primera, pa i Claude i ti češće lutate. Rešenje: standardni tehnološki skup dok ne postoji konkretan, laički objašnjen razlog za izuzetak.

### Kontrolna lista

- [ ] Znam da uključim plan mode (`Shift+Tab` ili rečenicom) i kad da ga koristim
- [ ] Svaku važnu odluku tražim kao: 2 opcije + preporuka + razmena laički
- [ ] Četiri zlatna pitanja znam napamet
- [ ] Claude-u sam rekao za šta optimizujem (brzina / skala / trošak) i koliki je budžet
- [ ] Razumem analogiju: Next.js = izlog, Supabase = magacin, Vercel = lokal
- [ ] Usvojene odluke su upisane u `CLAUDE.md` i provereno preživljavaju `/clear`

### Proveri znanje

**1. Šta plan mode radi, a šta ne radi?**
Claude istražuje projekat i predlaže plan, ali ne menja nijedan fajl dok plan ne odobriš. Uključuje se prečicom `Shift+Tab` ili jednostavnim zahtevom u poruci.

**2. Zašto je pitanje "šta je teže promeniti kasnije" vrednije od "šta je bolje"?**
Zato što razdvaja tapete od nosivih zidova: odluke koje se lako menjaju donosi brzo i bez griže savesti, a pažnju i pitanja ulaže u one koje bi kasnije zahtevale rušenje pola proizvoda.

**3. Zašto odluke moraju u `CLAUDE.md`, a ne samo u razgovor?**
Claude između sesija ne pamti razgovore, na početku svake sesije učitava samo `CLAUDE.md` (i memoriju). Nezapisana odluka za sutrašnju sesiju ne postoji, pa bi istu dilemu mogao da reši drugačije i unese nedoslednost u projekat.
