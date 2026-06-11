## Poglavlje 4: Umetnost objašnjavanja i izvođenja

### Šta ćeš dobiti iz ovog poglavlja

- Test kojim proveravaš da li ti je analogija dobra ili samo zvuči lepo
- Šablon za imenovanje koncepata koji polaznici počnu da koriste sami
- Protokol za demonstraciju uživo i za namernu grešku pred grupom
- Lek protiv "prokletstva znanja" + formulu ritma za sesiju od 2,5 sata

Kurikulum ti je dizajniran (poglavlje 3). Sada dolazi zanat: kako stojiš pred ljudima i pretvaraš tehnički haos u "aha" momente. Ovo poglavlje je trening za šest konkretnih tehnika, svaka sa primerom iz tvog konteksta: objašnjavanje Claude Code-a ne-tehničkim ljudima.

### Tehnika 1: Analogija pre definicije

95% edukatora kreće od definicije: "Git je distribuirani sistem za kontrolu verzija." Tvoj polaznik, preduzetnik bez tehničkog iskustva, čuo je sedam stranih reči i isključio se. Top 5% prvo veže pojam za iskustvo koje polaznik VEĆ ima, pa tek onda lepi ime.

❌ "Commit je snimak stanja repozitorijuma u istoriji verzija."
✅ "Zamisli da pišeš važan dokument i svakih pola sata sačuvaš kopiju sa datumom. Ako nešto pokvariš, vratiš se na jučerašnju kopiju. To radi git, vremenska mašina za tvoj projekat. Svako 'sačuvaj kopiju' zove se commit."

Test dobre analogije nije "da li zvuči zgodno" nego: **da li polaznik iz analogije ume da PREDVIDI ponašanje sistema?** Pitaj: "Ako je commit snimak stanja, šta misliš, možeš li da se vratiš na bilo koji raniji snimak?" Ako odgovori tačno bez tvoje pomoći, analogija radi. Ako analogija navodi na pogrešna predviđanja, opasnija je od definicije, menjaš je.

Napravi rečnik analogija za svoj kurs, jedan red po pojmu:

| Pojam | Analogija | Test-pitanje za predviđanje |
|---|---|---|
| git | Vremenska mašina za projekat | "Možeš li da vidiš kako je projekat izgledao pre 3 dana?" |
| commit | Snimak stanja sa porukom | "Šta gubiš ako radiš 4 sata bez commit-a i pokvariš nešto?" |
| terminal | Razgovor sa računarom porukama umesto klikovima | "Ako pogrešno ukucaš komandu, šta očekuješ da se desi?" |
| deploy (objavljivanje) | Otvaranje radnje za mušterije, do tada radiš u magacinu | "Da li mušterije vide ono što menjaš pre objavljivanja?" |
| Claude Code | Izvođač radova kome opisuješ šta hoćeš, a on zida | "Šta se desi ako izvođaču daš nejasan opis?" |

### Tehnika 2: Imenuj obrazac i polaznici ga vide svuda

Kad obrascu daš ime, prestaje da bude magla i postaje alat. Umesto "uvek tražite od Claude-a da prvo objasni plan", nazovi to **"pravilo plana pre koda"**. Umesto "dobar prompt ima kontekst, zadatak i format", **"formula prompta: K-Z-F"**. Polaznici počnu da govore tvojim jezikom ("čekaj, nisam primenio pravilo plana"), a to je ujedno seme tvog imenovanog metoda, intelektualne svojine koju konkurencija ne kopira preko noći (detaljno u poglavlju 6).

Pravilo: ne uvodi više od 4 nova imenovana pojma po sesiji, radna memorija drži 4±1 elementa (Sweller, cognitive load theory). Manje imena, jača imena.

### Tehnika 3: Demonstracija uživo tuče savršen slajd

Slajd sa snimkom ekrana koda je predavanje, a predavanje je najmanje efikasna metoda učenja (Freeman et al., 2014). Demonstracija uživo, sa pravim čekanjem dok Claude Code generiše, sa pravim "hm, ovo nije ono što sam hteo", pokazuje polazniku kako stvarnost izgleda. To je prvi korak "ja radim → radimo zajedno → ti radiš" lestvice (gradual release): preskočiš li demonstraciju ili, češće, srednji korak vođene vežbe, polaznik se ruši na samostalnom radu.

Protokol za demo (drži ga otvoren pored sebe):

```
1. NAJAVA: "Sada ću da X. Gledajte šta kucam i šta se vraća."
2. NARACIJA: izgovaraj svaku odluku NAGLAS ("biram ovu opciju jer...")
3. ČEKANJE: dok alat radi, ne ćuti neprijatno, pitaj grupu
   "šta očekujete da se pojavi?"
4. REZULTAT: uporedi sa očekivanjem grupe, ne samo sa svojim
5. PONOVI KLJUČNI POTEZ: drugi prolaz, brže, bez naracije
```

### Tehnika 4: Namerna greška

Najbrže učenje u grupi dešava se kroz analizu grešaka, a ljudi uče kad smeju da pogreše javno bez posledica (Edmondson). Zato top 5% NAMERNO izaziva grešku pred svima: napiše nejasan prompt, dobije pogrešan rezultat, i smireno ga razreši. Time učiš dve stvari odjednom: oporavak od greške (veštinu koju polaznik sigurno treba) i poruku "greška je ovde normalna".

Skripta:

```
"Sad ću namerno da uradim ono što većina uradi prve nedelje."
[napravi grešku, npr. prompt bez konteksta: "napravi mi sajt"]
"Vidite šta se desilo. Da li je alat pokvaren? Ne, ja sam mu dao
loš nalog. Hajde da popravimo ZAJEDNO. Šta nedostaje u mom promptu?"
[grupa predlaže, ti kucaš njihove predloge]
"Zapamtite ovaj osećaj: greška nije zid, nego informacija."
```

Pravilo: jedna namerna greška po sesiji, uvek razrešena do kraja. Nikad ne glumi da ti se namerna greška "slučajno omakla", reci da je namerna, to gradi poverenje.

### Tehnika 5: Kalibracija krivine: lek za prokletstvo znanja

Ti više NE VIDIŠ šta je početniku teško. Za tebe je "otvori terminal" trivijalno; za tvog polaznika to je prva prepreka na kojoj odustane. To je prokletstvo znanja i ne leči se razmišljanjem, leči se testiranjem.

Lek: **probno predavanje jednoj osobi iz ciljne grupe pre svake nove lekcije.** Nađi jednog preduzetnika/kreativca, ne kolegu tehničara. Pusti ga da prati lekciju i zapisuj svako mesto gde: (1) pita "čekaj, šta je to?", (2) klikne pogrešno, (3) ćuti duže od 10 sekundi. Svaka od te tri tačke je rupa u lekciji, zakrpi je analogijom, demonstracijom ili dodatnim korakom PRE prave grupe. Većina edukatora lekciju prvi put isporuči plaćenoj grupi. Ti nemoj.

### Tehnika 6: Energija i ritam

Radna memorija je usko grlo (Sweller), dug monolog gomila opterećenje koje polaznik ne može da obradi, a aktivne metode tuku predavanje u meta-analizi 225 studija (Freeman et al., 2014). Zato sesija od 2,5 sata ne sme biti monolog sa pauzom. Formula bloka:

| Minuti | Aktivnost |
|---|---|
| 0-10 | Izlaganje + demo (ti radiš, naracija naglas) |
| 10-25 | Vođena vežba (radite zajedno, ti šetaš i gledaš ekrane) |
| 25-35 | Samostalan mini-zadatak (oni rade, ti ćutiš) |
| 35-40 | Razrešenje + 2 pitanja prisećanja iz PROŠLE sesije |

Šest ovakvih blokova = jedna radionica. Pitanja prisećanja na kraju bloka nisu ukras, to je vežbanje prisećanja i spacing u praksi (detaljno u poglavlju 2).

### Mentorski zadatak

Do kraja nedelje napravi i upotrebi tri stvari:

1. **Rečnik analogija**, tabela sa minimum 10 pojmova iz tvog kurikuluma (git, commit, terminal, deploy, odnosno objavljivanje, prompt, kontekst, repozitorijum, API, hosting, domen), svaki sa analogijom i test-pitanjem za predviđanje. Jedna strana.
2. **Probno predavanje**, održi modul 1 jednoj ne-tehničkoj osobi uživo ili preko poziva. Rezultat rada: lista svih tačaka zastoja (pitanja, pogrešni klikovi, tišine) sa zakrpom za svaku.
3. **Jedna isplanirana namerna greška**, napiši skriptu (šta kvariš, šta pitaš grupu, kako razrešavaš) za prvu radionicu.

### Pitanja za samoprocenu

1. Koju si analogiju poslednju upotrebio, i da li si je TESTIRAO pitanjem za predviđanje, ili samo zvuči lepo?
2. Koliko minuta u komadu pričaš na svojoj tipičnoj sesiji pre nego što polaznici nešto URADE? (Izmeri na snimku, ne po osećaju.)
3. Kada je poslednji put ne-tehnička osoba videla tvoju lekciju pre plaćene grupe? Šta je tačno zapelo?
4. Koja imena koncepata tvoji polaznici koriste spontano, bez tvog podsećanja? Ako nijedno, šta to govori?
5. Seti se poslednjeg puta kad ti je demo pukao uživo. Šta si tačno uradio i rekao u prvih 60 sekundi, od reči do reči? Da li je grupa videla kako grešku čitaš i rešavaš, ili si prešao na sledeću stvar?

### Crvene zastavice

- Slajdovi ti rastu, a demo vreme se smanjuje, kliziš ka predavanju, najmanje efikasnoj metodi koju koristiš jer je tebi najudobnija.
- Lekciju prvi put isporučuješ plaćenoj grupi, bez probnog predavanja, prokletstvo znanja ti piše kurikulum umesto tebe.
- Na grešku uživo reaguješ izvinjavanjem ili prikrivanjem, učiš grupu da je greška sramota, i psihološka sigurnost umire (Edmondson).
- Polaznici te citiraju rečima "ono kad si rekao da..." umesto imenom koncepta, obrasci ti nemaju imena, pa ih niko ne nosi kući.
