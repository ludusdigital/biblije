## Modul 4: Od ideje do specifikacije

Najskuplja greška u pravljenju digitalnog proizvoda nije bag u kodu. Najskuplja greška je savršeno izgraditi pogrešnu stvar. Možeš imati besprekoran kod, prelep dizajn i brz sajt, ako rešava problem koji niko nema, potrošio si mesece ni na šta. Zato pre prvog reda koda dolazi nešto mnogo važnije: razgovor sa samim sobom o tome šta zapravo praviš. A Claude je, kada ga pravilno usmeriš, odličan sagovornik za taj razgovor.

### Šta ćeš naučiti

- Kako da nateraš Claude-a da tvoju ideju napadne, a ne da ti tapše po ramenu
- Kako da definišeš problem, ciljnu grupu i ključnu vrednost u jednoj rečenici
- Šta je MVP i kako da nemilosrdno isečeš sve što nije neophodno za prvu verziju
- Kako da napišeš `docs/spec.md`, dokument koji postaje ustav tvog projekta
- Kako da spec koristiš kao trajnu referencu u svakoj budućoj sesiji

### Zašto moraš da tražiš kritiku (i zašto je nećeš dobiti besplatno)

Claude je sam od sebe uslužan. Ako mu kažeš "imam ideju za aplikaciju koja povezuje vlasnike pasa sa šetačima", on će ti vratiti entuzijastičan odgovor, listu funkcionalnosti i predlog kako da počneš. To prija, i to je zamka. Dobio si navijača, a tebi treba đavolji advokat.

Kritiku moraš eksplicitno da tražiš. Kao kada prijatelja pitaš "kako ti se čini moj poslovni plan?", dobićeš "super zvuči!". Ali ako pitaš "šta je najslabija tačka ovog plana i zašto bi propao?", dobićeš odgovor koji vredi. Isto važi za Claude-a.

Evo prompta koji možeš da iskopiraš i prilagodiš:

```
Imam ideju za proizvod: [opiši ideju u 2-3 rečenice].

Nemoj da me hvališ i nemoj da budeš ljubazan. Ponašaj se kao
iskusan investitor koji je video stotine propalih projekata:

1. Postavi mi 10 najtežih pitanja o ovoj ideji.
2. Reci mi šta je najrizičnije, gde će najverovatnije pući.
3. Reci mi šta bi izbacio iz prve verzije i zašto.
4. Reci mi ko već rešava ovaj problem i zašto bi neko prešao kod mene.

Budi direktan. Više mi vredi neprijatna istina sada nego
propao projekat za šest meseci.
```

Odgovori na tih deset pitanja, pisano, ozbiljno. Ako na tri pitanja nemaš odgovor, nisi spreman da gradiš. To nije poraz; to je jeftino otkriće. Upravo si uštedeo mesece.

Ako koristiš plugin-ove (detaljno u Modulu 12), `product-management` plugin ima skill `brainstorm` koji vodi ovakav razgovor strukturirano. Ali i običan prompt iznad radi posao.

### Tri rečenice koje moraš da znaš napamet

Pre nego što napišeš spec, moraš da umeš da odgovoriš na tri pitanja, svako u jednoj rečenici:

1. **Problem**: Šta tačno boli koga? ("Frilenseri gube sate mesečno na ručno pisanje faktura.")
2. **Ciljna grupa**: Ko je taj kome je dovoljno hitno da plati ili promeni naviku? ("Frilenseri u Srbiji koji izdaju 5-20 faktura mesečno.")
3. **Ključna vrednost**: Zašto baš tvoje rešenje, u jednoj rečenici koju razume tvoja tetka? ("Faktura gotova za 30 sekundi, automatski u skladu sa domaćim propisima.")

Ako ne umeš da ih izgovoriš bez "i još...", "a takođe...", "pa zavisi...", ideja još nije sazrela. Vrati se na brainstorm.

### MVP: prvo skejtbord, ne polu-automobil

MVP (Minimum Viable Product, najmanji upotrebljiv proizvod) je prva verzija koja rešava srž problema, i ništa više. Klasična analogija: ako praviš prevozno sredstvo, MVP nije šasija automobila bez točkova, to je polu-automobil koji ne vozi i nikome ne koristi. MVP je skejtbord: ružan, jednostavan, ali te već danas preveze od tačke A do tačke B. Sledeća verzija je trotinet, pa bicikl, pa tek onda auto. U svakom koraku korisnik dobija nešto što radi.

Za rezanje MVP-a iskoristi Claude-a kao nemilosrdnog urednika:

```
Evo liste svih funkcionalnosti koje zamišljam: [nalepi listu].

Za svaku stavku odgovori: da li korisnik može da dobije osnovnu
vrednost proizvoda BEZ nje? Ako može, predloži da je izbacimo
iz prve verzije. Cilj je da prva verzija ima najviše 3 ključne
funkcionalnosti. Budi brutalan.
```

Pravilo palca: ako prvu verziju ne možeš da opišeš u jednoj rečenici i ne vidiš je gotovu za par nedelja rada, još uvek nisi dovoljno sekao.

### Pisanje `docs/spec.md`: ustav tvog projekta

Sada sve to pretačeš u jedan fajl: `docs/spec.md` (folder `docs` u tvom projektu, fajl u Markdown formatu, običan tekst sa naslovima, isti format kao `CLAUDE.md` iz Modula 3). Ovo je dokument kome se i ti i Claude vraćate kad god se pojavi dilema "a da dodamo i ovo?".

Struktura koja se pokazala dobrom:

```
# Specifikacija: [ime proizvoda]

## Problem
Jedna do tri rečenice: šta boli, koga i koliko.

## Korisnik
Ko je ciljna grupa. Konkretno: "frilenseri u Srbiji koji...",
ne "svi koji žele...".

## Ključna vrednost
Jedna rečenica koju razume laik.

## Funkcionalnosti
### Mora (MVP)
- [funkcionalnost 1, jedna rečenica šta korisnik može da uradi]
- [funkcionalnost 2]
- [funkcionalnost 3]

### Trebalo bi (verzija 2)
- [stvari koje su važne, ali ne za prvi dan]

### Kasnije (možda nikad)
- [ideje koje su zanimljive, ali ih svesno odlažeš]

## Šta NIJE u MVP-u
Eksplicitna lista. Npr: "Nema mobilne aplikacije. Nema više
jezika. Nema timskih naloga."

## Kriterijumi uspeha
Merljivo: "Korisnik kreira prvu fakturu za manje od 60 sekundi."
"10 ljudi koristi proizvod nedeljno mesec dana posle lansiranja."
```

Sekcija "Šta NIJE u MVP-u" je možda i najvrednija. Ona štiti od tebe samog, od trenutka u tri ujutru kad pomisliš "a da ubacim i čet?". Piše crno na belo: ne, ne sada.

Ne moraš spec da pišeš sam. Daj Claude-u beleške sa brainstorma i zatraži da ti sastavi prvi nacrt po ovoj strukturi, pa ga ti doteraj. Ti si urednik i potpisnik, Claude je pisar.

### Spec kao trajna referenca

Setimo se Modula 1: Claude ne pamti ništa između sesija (osim `CLAUDE.md` i memorije). Tvoj spec je način da svaka nova sesija počne sa istim razumevanjem proizvoda. Navika koja se isplati:

```
Pročitaj docs/spec.md pa mi reci kako sledeća funkcionalnost
koju planiramo utiče na ono što tamo piše.
```

Možeš i da zamoliš Claude-a da u `CLAUDE.md` doda napomenu da spec uvek pročita na početku rada, ili jednostavno pošalji poruku koja počinje sa `#`, čime Claude tu napomenu trajno zabeleži.

### Primer dijaloga iz prakse

**Ti:**

```
Imam ideju: aplikacija u koju ubaciš video, ona ga automatski
transkribuje i iseče tišine i poštapalice. Za male kreatore
sadržaja. Postavi mi 10 najtežih pitanja i reci šta bi izbacio
iz prve verzije.
```

**Claude (skraćeno):** "Pitanje 3: CapCut i Descript već rade nešto slično, zašto bi neko prešao kod tebe? Pitanje 7: obrada videa je skupa, ko plaća server dok je proizvod besplatan? Iz prve verzije bih izbacio: izvoz u više formata, timsku saradnju i mobilnu verziju. Zadržao bih samo: upload, transkripciju i automatsko sečenje tišina."

**Ti reaguješ:** Na pitanje 3 imaš odgovor, tvoja aplikacija radi odlično za srpski jezik, što veliki alati ne pokrivaju. To ide u spec pod "Ključna vrednost". Na pitanje 7 nemaš odgovor, beležiš ga kao rizik koji ćeš istražiti pre lansiranja. Predlog rezanja prihvataš i MVP postaje tri funkcionalnosti.

Vidiš mehaniku: Claude izaziva, ti odlučuješ. Ti si direktor (Modul 0), on je oštrouman savetnik.

### Vežba

1. Uzmi svoju ideju (ili izmisli jednu za vežbu, npr. aplikacija za deljenje troškova na putovanjima).
2. Otvori sesiju u Claude Code-u u folderu projekta i nalepi "đavolji advokat" prompt sa početka modula, sa svojom idejom.
3. Pisano odgovori na svih 10 pitanja. Za ona na koja nemaš odgovor, napiši "RIZIK: nemam odgovor", to su ti domaći zadaci.
4. Zatraži MVP rezanje promptom iz ovog modula. Cilj: najviše 3 funkcionalnosti u "Mora".
5. Zatraži od Claude-a: "Na osnovu ovog razgovora napiši nacrt `docs/spec.md` po sledećoj strukturi: problem, korisnik, ključna vrednost, funkcionalnosti (mora / trebalo bi / kasnije), šta NIJE u MVP-u, kriterijumi uspeha."
6. Pročitaj nacrt rečenicu po rečenicu. Sve sa čime se ne slažeš, ispravi ili izbaci. Ovo je tvoj dokument.
7. Sačuvaj fajl i potvrdi da postoji: zatraži od Claude-a da ti prikaže sadržaj `docs/spec.md`.

### Najčešće greške

1. **Tražiš mišljenje, a ne kritiku.** "Šta misliš o ovoj ideji?" donosi pohvale. Rešenje: uvek eksplicitno traži najteža pitanja, rizike i razloge za neuspeh, kao u promptu iz ovog modula.
2. **MVP od deset funkcionalnosti.** "Sve je neophodno" znači da nisi odlučio šta je srž. Rešenje: za svaku stavku pitaj "može li korisnik da dobije osnovnu vrednost bez ovoga?", ako može, seci.
3. **Spec napisan pa zaboravljen.** Posle dve nedelje gradiš nešto čega u spec-u nema. Rešenje: svaku sesiju počni sa "pročitaj `docs/spec.md`", a svaku novu ideju propusti kroz pitanje "da li ovo menja spec?".
4. **Ciljna grupa "svi".** Proizvod za sve je proizvod ni za koga. Rešenje: suzi dok ne zaboli, "frilenseri u Srbiji sa 5-20 faktura mesečno" je dobro; "ljudi koji rade" nije.
5. **Kriterijumi uspeha bez brojeva.** "Korisnici su zadovoljni" se ne može izmeriti. Rešenje: broj, vreme ili procenat, "prva faktura za manje od 60 sekundi" (princip merljivosti iz Modula 1).

### Kontrolna lista

- [ ] Claude mi je postavio 10 teških pitanja i odgovorio sam na svako (ili zabeležio rizik)
- [ ] Problem, ciljnu grupu i ključnu vrednost umem da kažem u po jednoj rečenici
- [ ] MVP ima najviše 3 funkcionalnosti pod "Mora"
- [ ] `docs/spec.md` postoji i sadrži svih šest sekcija, uključujući "Šta NIJE u MVP-u"
- [ ] Kriterijumi uspeha su merljivi (broj, vreme, procenat)
- [ ] Znam da svaku sledeću sesiju počinjem sa "pročitaj `docs/spec.md`"

### Proveri znanje

**1. Zašto moraš eksplicitno da tražiš kritiku od Claude-a?**

Zato što je Claude sam od sebe uslužan i podržavajući, na neutralno pitanje vratiće ohrabrenje, a ne analizu rizika. Kritiku, teška pitanja i razloge za neuspeh dobijaš samo ako ih izričito zatražiš.

**2. Šta znači analogija "prvo skejtbord, ne polu-automobil"?**

Prva verzija proizvoda treba da bude mala ali upotrebljiva, da već danas rešava srž problema (skejtbord vozi), umesto da bude nedovršen komad velike vizije koji nikome ne koristi (polu-automobil ne vozi).

**3. Čemu služi sekcija "Šta NIJE u MVP-u" i kako spec koristiš u budućim sesijama?**

Ta sekcija je pisana brana protiv širenja obima, kada dođe iskušenje da dodaš novu funkcionalnost, dokument te podseća da je svesno odložena. Spec koristiš tako što svaku novu sesiju počneš sa "pročitaj `docs/spec.md`", jer Claude ne pamti prethodne razgovore.
