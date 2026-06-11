## Modul 6: Ritam razvoja: funkcionalnost po funkcionalnost

Stigao si do srca cele metodologije. Sve do sada, okruženje, temelji, specifikacija, plan, bila je priprema. Odavde pa do lansiranja, 80% tvog vremena provodi se u jednom istom ciklusu koji se ponavlja za svaku funkcionalnost (jednu zaokruženu stvar koju proizvod radi, npr. "kontakt forma" ili "prijava korisnika"). Kad taj ciklus uđe u ruke, razvoj prestaje da bude haos i postaje zanat: predvidiv, miran, merljiv.

Zamisli ga kao pranje veša. Ne ubacuješ sve odjednom u mašinu, sortiraš, opereš jednu turu, proveriš da li je čisto, složiš, pa tek onda sledeća tura. Jedna funkcionalnost = jedna tura.

### Šta ćeš naučiti

- Ciklus od 7 koraka koji ponavljaš za svaku funkcionalnost, od prazne sesije do potvrde da sve radi
- Zašto svaka funkcionalnost zaslužuje svežu sesiju (`/clear`) i šta se dešava kad to preskočiš
- Kako da tražiš dokaz umesto obećanja, snimak ekrana, test, log
- Formulu savršenog prompta: KONTEKST → ZADATAK → KRITERIJUM PRIHVATANJA → OGRANIČENJA
- Kompletan, stvaran primer jednog ciklusa koji možeš da kopiraš i prilagodiš

### Ciklus od 7 koraka

**Korak 1: `/clear`, sveža sesija za svaku funkcionalnost.** Sesija je jedan razgovor sa Claude-om, a kontekst je njegova radna memorija u tom razgovoru (detaljno u Modulu 1). Kad u istoj sesiji nakupiš tri funkcionalnosti, dve ispravke i jedan eksperiment, ta memorija se zatrpa, Claude počinje da meša stare zahteve sa novima, kao konobar koji pamti porudžbine celog dana umesto samo tvog stola. Zato: nova funkcionalnost, nova sesija. Ne brini za "zaboravljanje", sve trajno važno živi u `CLAUDE.md` i u tvojim fajlovima sa specifikacijom, a oni se učitavaju iznova.

**Korak 2: Plan mode za sve što nije trivijalno.** Plan mode je režim u kom Claude istražuje projekat i predlaže plan, ali ne menja nijedan fajl dok ti plan ne odobriš. Uključuješ ga prečicom `Shift+Tab` ili jednostavno napišeš: "prvo napravi plan, ne menjaj ništa dok ne odobrim". Pravilo palca: ako funkcionalnost dira više od jednog fajla ili uvodi nešto novo (bazu, plaćanje, slanje imejlova), plan mode. Ako je sitnica ("promeni boju dugmeta"), preskoči. Kako da čitaš i izazivaš predloženi plan naučio si u Modulu 5.

**Korak 3: Implementacija.** Odobriš plan i pustiš Claude-a da radi. Tvoj posao nije da razumeš svaki red koda, nego da pratiš da li se drži plana. Ako vidiš da skreće, `Esc` ga prekida usred rada i odmah možeš da ga preusmeriš, to nije nepristojno, to je upravljanje.

**Korak 4: Verifikacija u pregledaču, traži dokaz.** Ovo je korak koji početnici najčešće preskaču, a najviše vredi. Claude ume da pokrene dev server (lokalnu, probnu verziju tvoje aplikacije na tvom računaru), klikće po njoj, popunjava forme i pravi snimke ekrana. Nikad ne prihvataj "implementirano je" kao kraj, to je obećanje, ne dokaz.

```
Pokreni dev server, otvori stranicu /kontakt u pregledaču, popuni formu
probnim podacima i pošalji je. Napravi snimak ekrana forme pre slanja i
snimak ekrana poruke o uspehu posle slanja. Pokaži mi oba.
```

**Korak 5: `/code-review`.** Pre nego što izmene proglasiš gotovim, pusti pregled koda: `/code-review` pregleda trenutne izmene i prijavi probleme. Ima nivoe temeljnosti (low/medium/high/max), za svakodnevni rad srednji nivo je sasvim dovoljan. Šta znače nalazi i kada da posegneš za `/security-review`, detaljno u Modulu 8.

**Korak 6: Commit.** Commit je snimak stanja projekta u git-u, kao "sačuvaj igru" u video igrici: tačka kojoj uvek možeš da se vratiš (osnove git-a su u Modulu 3). Jedna funkcionalnost = jedan commit (ili nekoliko manjih, ali nikad "sve od prošle nedelje odjednom").

```
Napravi commit ovih izmena sa jasnom porukom na srpskom koja opisuje
šta funkcionalnost radi, i pošalji na GitHub.
```

**Korak 7: `/loop` za praćenje CI-ja.** CI (continuous integration) je automatska kontrola kvaliteta na GitHub-u koja posle svakog slanja koda sama pokreće testove (podesio si je u Modulu 3). Umesto da sediš i osvežavaš stranicu, zaduži Claude-a: `/loop 5m proveri status CI provera za poslednji commit; ako je nešto palo, ispravi i pošalji ponovo`. Petlja ponavlja prompt na zadati interval i prekida se sa `Esc`. Više o autonomnom radu i zaštitnim ogradama, Modul 7.

I onda? `/clear` i sledeća funkcionalnost. To je ceo ritam.

### Formula savršenog prompta

Svaki dobar radni prompt ima četiri dela. Zapamti ih kao K-Z-K-O.

**1. KONTEKST, gde Claude treba da gleda.** Ne prepričavaj specifikaciju, uputi ga na nju:

```
Pročitaj docs/spec.md, sekciju "Kontakt forma".
```

**2. ZADATAK, šta se pravi.** Jedna jasna rečenica, jedna funkcionalnost. Ako u zadatku stoji veznik "i" između dve različite stvari, verovatno su to dva ciklusa.

**3. KRITERIJUM PRIHVATANJA, "gotovo je kad…".** Ovo je najmoćniji deo i najčešće izostavljen. Bez njega Claude sam odlučuje šta znači "gotovo", a njegova definicija i tvoja se retko poklapaju. Kriterijum mora biti proverljiv:

❌ `Napravi lepu kontakt formu.` (šta je "lepo"? kad je gotovo?)
✅ `Gotovo je kad: forma na /kontakt prima ime, imejl i poruku; posle slanja poruka se vidi u bazi; korisnik dobije potvrdu na ekranu; npm run build prolazi bez grešaka.`

**4. OGRANIČENJA, šta NE dirati.** Claude je vredan i ponekad "usput" sredi i ono što nisi tražio. Ogradi teren:

```
Ne diraj postojeću stranicu /cenovnik ni navigaciju. Ne uvodi nove
biblioteke bez pitanja. Postojeći testovi moraju i dalje da prolaze.
```

### Kompletan primer: kontakt forma koja čuva poruke u bazu

Prođimo ceo ciklus na stvarnoj funkcionalnosti, prompt po prompt.

**1.** Ukucaj `/clear`. Prazna tabla.

**2.** Plan (Shift+Tab za plan mode, pa):

```
Pročitaj docs/spec.md, sekciju "Kontakt forma". Napravi plan za kontakt
formu na stranici /kontakt: polja ime, imejl i poruka, čuvanje poruka
u našu bazu, potvrda korisniku posle slanja, jasna poruka ako nešto
pođe po zlu. Gotovo je kad poslata poruka postoji u bazi i korisnik
vidi potvrdu. Ne diraj ostale stranice i ne uvodi nove biblioteke bez
pitanja. Objasni mi plan jezikom za nekoga ko ne programira.
```

**3.** Pročitaj plan, postavi pitanja ("šta se desi ako neko pošalje prazan imejl?"), odobri. Claude implementira.

**4.** Dokaz:

```
Pokreni dev server i verifikuj u pregledaču: popuni formu na /kontakt
podacima "Marko Marković, marko@test.com, Probna poruka" i pošalji.
Napravi snimak ekrana potvrde. Zatim mi pokaži da ta poruka stvarno
postoji u bazi. Probaj i slanje prazne forme, snimak ekrana poruke
o grešci.
```

Pogledaj snimke ekrana svojim očima. Ti si poslednja kontrola.

**5.** `/code-review`, pa zamoli Claude-a da ispravi ono što pregled nađe i ponovi verifikaciju iz koraka 4 ako je menjao logiku.

**6.** Commit:

```
Napravi commit sa porukom "Dodaj kontakt formu sa čuvanjem poruka
u bazu" i pošalji na GitHub.
```

**7.** `/loop 5m proveri da li su CI provere za poslednji commit prošle; ako je nešto palo, ispravi uzrok i pošalji ponovo`. Kad CI pozeleni, `Esc`, pa `/clear`, i sledeća tura veša.

### Vežba

1. Otvori svoj `docs/spec.md` (napravio si ga u Modulu 4) i izaberi najmanju nezapočetu funkcionalnost sa liste.
2. Napiši na papiru ili u beležnici njegova četiri dela: kontekst, zadatak, kriterijum prihvatanja, ograničenja. Ne preskači kriterijum!
3. Ukucaj `/clear`, uđi u plan mode (`Shift+Tab`) i pošalji svoj prompt.
4. Prođi svih 7 koraka do kraja, uključujući snimak ekrana kao dokaz i commit.
5. Na kraju zapiši: koji korak ti je bio najneprirodniji? Njega sledeći put radi prvo.

### Najčešće greške

1. **Nastavljanje u istoj sesiji ceo dan.** Simptom: Claude "meša" stare i nove zahteve, vraća izmene koje si već odbacio. Rešenje: `/clear` posle svake završene funkcionalnosti; ako sesija mora da bude duga, `/compact` da sažme razgovor.
2. **Prihvatanje "gotovo je" bez dokaza.** Claude može iskreno da veruje da nešto radi, i da greši. Rešenje: uvek traži snimak ekrana, izlaz testova ili log; korak 4 nije opcioni.
3. **Prompt bez kriterijuma prihvatanja.** Dobiješ nešto, ali ne ono što si hteo, pa kreće prepravljanje u krug. Rešenje: pre slanja prompta dopiši rečenicu koja počinje sa "Gotovo je kad…".
4. **Tri funkcionalnosti u jednom promptu.** Plan postane ogroman, verifikacija nemoguća, a kad nešto pukne ne znaš šta je krivac. Rešenje: jedan ciklus = jedna funkcionalnost; ostalo ide u backlog (listu čekanja, Modul 10).
5. **Commit "kad se nakupi".** Posle nedelju dana imaš planinu izmena i nijednu sigurnu tačku za povratak. Rešenje: commit je korak 6 svakog ciklusa, ne mesečna proslava.

### Kontrolna lista

- [ ] Počeo sam rad na funkcionalnosti sa `/clear`, u svežoj sesiji
- [ ] Za netrivijalnu funkcionalnost koristio sam plan mode i odobrio plan pre izmena
- [ ] Moj prompt ima sva četiri dela: kontekst, zadatak, kriterijum prihvatanja, ograničenja
- [ ] Video sam dokaz da funkcionalnost radi (snimak ekrana, test, log), ne samo tvrdnju
- [ ] Pokrenuo sam `/code-review` i razrešio nalaze
- [ ] Napravio sam commit sa jasnom porukom i poslao na GitHub
- [ ] CI provere su zelene (pratio sam ih kroz `/loop` ili proverio ručno)

### Proveri znanje

**1. Zašto se svaka funkcionalnost radi u svežoj sesiji?**
Zato što se kontekst (radna memorija razgovora) vremenom zatrpa starim zahtevima i eksperimentima, pa Claude počinje da ih meša sa novim zadatkom. `/clear` daje čistu tablu, a trajno znanje ostaje u `CLAUDE.md` i fajlovima projekta.

**2. Koja su četiri dela formule savršenog prompta i koji se najčešće zaboravlja?**
Kontekst (gde da gleda), zadatak (šta se pravi), kriterijum prihvatanja ("gotovo je kad…") i ograničenja (šta ne dirati). Najčešće se zaboravlja kriterijum prihvatanja, a bez njega Claude sam definiše "gotovo".

**3. Šta je prihvatljiv dokaz da funkcionalnost radi, a šta nije?**
Prihvatljivo: snimak ekrana iz pregledača, izlaz testova, zapis u bazi, log. Neprihvatljivo: rečenica "implementirano je", to je obećanje, a ti tražiš dokaz koji možeš da vidiš svojim očima.
