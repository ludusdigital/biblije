## Poglavlje 10: Eksperimentalni pogon: nedeljni ritam rasta

Sve što si naučio u Delu II, PLG, petlje, organski, plaćeno oglašavanje, imejl, brend, lansiranja, proizvodi ideje. Ovo poglavlje ih pretvara u proces. Bez procesa, marketing solo osnivača je serija nasumičnih poteza vođenih raspoloženjem; sa procesom, to je mašina koja svake nedelje proizvodi naučene lekcije, a povremeno i pobedu.

Polazna istina dolazi iz objavljenih nalaza Ronija Kohavija (Microsoft) o eksperimentima: otprilike trećina eksperimenata poboljša metrike, trećina nema efekta, a trećina ih pogorša. Pročitaj to još jednom. I iskusni timovi sa ogromnim podacima pogode tek u trećini slučajeva. Ako ne meriš, ne znaš ni u kojoj si trećini, i statistički gledano, trećina tvojih „očiglednih poboljšanja" aktivno šteti proizvodu.

### Šta ćeš naučiti

- Kako da vodiš backlog ideja za rast i prioritizuješ ga ICE skorom
- Nedeljni ritam: 1-3 eksperimenta, petak retrospektiva, sledeći ciklus
- Disciplinu hipoteze: jedna hipoteza = jedna metrika odluke, zapisana unapred
- Zašto sa malim saobraćajem testiraš velike zamahe, a ne boju dugmeta
- Minimalni skup alata za analitiku koji ti treba da bi eksperimenti uopšte imali smisla

### Spisak ideja: gde žive ideje

Svako poglavlje Dela II ti je ostavilo kandidate za eksperimente: drugačiji aha-momenat u uvođenju korisnika (Poglavlje 3), nova petlja (Poglavlje 4), AEO stranica ili objava koju lično vodi osnivač (Poglavlje 5), novi ugao u testu plaćenog oglašavanja (Poglavlje 6), aktivaciona sekvenca (Poglavlje 7), lansiranje funkcionalnosti (Poglavlje 9). Te ideje ne sprovodiš redom kojim su ti pale na pamet, upisuješ ih u spisak ideja (backlog): jedan fajl (npr. `eksperimenti/backlog.md` u repozitorijumu, što postaje deo OS-a iz Poglavlja 12), jedna ideja po redu.

Pravilo: ideja bez hipoteze ne ulazi u spisak ideja. „Probaj TikTok" nije ideja. „Ako objavim 3 demo videa nedeljno, dobiću X registracija iz tog kanala za 30 dana" jeste.

### ICE: kako biraš šta ide prvo

Sean Ellis je za prioritizaciju eksperimenata definisao ICE skor: **Impact × Confidence × Ease**, svaka komponenta ocena 1-10.

| Komponenta | Pitanje | Primer ocene |
|---|---|---|
| Impact | Koliko pomera metriku ako uspe? | Promena cene: 9. Novi font na blogu: 1 |
| Confidence | Koliko dokaza imam da će uspeti? | Korisnici se žale na uvođenje korisnika u 5 imejlova: 8. „Imam osećaj": 2 |
| Ease | Koliko brzo i jeftino mogu da testiram? | Promena naslova prodajne stranice: 9. Novi sistem preporuka: 3 |

Pomnožiš, sortiraš spisak ideja opadajuće, uzmeš vrh. ICE nije nauka, to je brana protiv biranja eksperimenata po tome šta ti je zabavno. Confidence ocenjuj na osnovu signala (žalbe korisnika, podaci iz analitike, rezultati prethodnih eksperimenata), ne na osnovu entuzijazma.

### Nedeljni ritam rasta

Ritam je jednostavan i stane u jedan kalendarski blok:

1. **Ponedeljak (30 min):** pogledaj spisak ideja, izaberi 1-3 eksperimenta po ICE skoru. Solo? Jedan je sasvim dovoljno. Za svaki zapiši hipotezu, metriku odluke i trajanje, UNAPRED, u dnevnik eksperimenata.
2. **Utorak-četvrtak:** izvršavanje. Lansiraj eksperiment, ne diraj ga, ne „proviruj" u rezultate svaka dva sata da bi prekinuo čim izgleda dobro.
3. **Petak (30 min): retrospektiva.** Za svaki završeni eksperiment: da li je metrika odluke pomerena? Odluka: usvoji / odbaci / produži (samo ako je trajanje isteklo a podaci nedovoljni, ne zato što ti se rezultat ne sviđa). Zapiši lekciju. Lekcija često rodi 2-3 nove ideje, one idu u spisak ideja, i krug se zatvara.

Ovaj ritam je preteča autonomnog OS-a: u Poglavlju 12 ćeš videti kako agent preuzima pripremu ponedeljka i izveštaj petka, a ti ostaješ kapija za odluke.

### Disciplina hipoteze: jedna hipoteza, jedna metrika

Najčešći način na koji se osnivači lažu jeste pomeranje gola posle šuta. Gvozdeno pravilo discipline: jedna hipoteza = jedna metrika odluke, zapisana unapred. Menjanje hipoteze posle rezultata je samoobmana.

❌ „Testirao sam novi uvođenje korisnika. Konverzija u plaćeno nije porasla, ALI je vreme na sajtu duže, pa je uspeh!", metrika odluke promenjena naknadno; ovo nije eksperiment nego racionalizacija.

✅ „Hipoteza: skraćeni uvođenje korisnika (3 koraka umesto 7) podiže stopu dostizanja aha-momenta u prvih 24h. Metrika odluke: % novih korisnika koji dostignu aha-momenat u 24h. Trajanje: 2 nedelje. Sve ostalo što primetim je zanimljivost, ne odluka."

Sekundarne metrike smeš da gledaš, kao izvor novih hipoteza za spisak ideja, nikad kao zamenu za metriku odluke.

### Mali saobraćaj = veliki zamasi

Mali saobraćaj nema statističku snagu za sitne testove. Ako ti na prodajnu stranicu dođe 300 ljudi mesečno, razlika između plavog i zelenog dugmeta je nemerljiva, rezultat će biti šum, a ti ćeš iz šuma „pročitati" priču. Zato sa malim saobraćajem testiraš velike zamahe:

- **Poruka:** potpuno drugačiji ugao pozicioniranja (Poglavlje 2), ne sinonim u naslovu
- **Cena i paketi:** druga struktura cenovnika, najpotcenjenija poluga iz Poglavlja 1
- **Uvođenje korisnika tok:** drugačiji put do aha-momenta, ne redosled tooltipa
- **Kanal:** potpuno nov kanal, ne treća varijanta iste objave

Praktično pravilo: ako ne očekuješ da eksperiment pomeri metriku bar za dvocifren procenat, nemaš saobraćaj da ga izmeriš, vrati ga u spisak ideja za dan kad budeš imao više korisnika. I još jedno: sa malim brojevima često ne treba ni A/B test, sekvencijalno poređenje (2 nedelje stara verzija, 2 nedelje nova, ista sezona) plus razgovori sa korisnicima daju ti dovoljno signala za velike zamahe.

### Minimalni skup alata za analitiku

Bez merenja nema eksperimenta, ali ne treba ti analitika za velike sisteme. Minimum, opisan generički (alat biraš sam):

1. **Praćenje događaja ključnih akcija:** registracija, aha-momenat (definisan u Poglavlju 3), konverzija u plaćeno. Tri događaja su dovoljna za početak; svaki sledeći događaj dodaješ tek kad ti zatreba za konkretan eksperiment.
2. **UTM disciplina:** svaki link koji deliš nosi UTM parametre po istoj konvenciji (kanal/kampanja/sadržaj). Jedan dokument sa konvencijom, nula izuzetaka, inače ti je izveštaj o kanalima fikcija.
3. **Pitanje o izvoru:** polje „Kako si čuo za nas?" pri registraciji (praksa koju je popularizovao Refine Labs / Chris Walker). Nevidljive preporuke, privatne grupe, DM, usmeno, analitika ne vidi (Poglavlje 5), a ovo polje vidi.
4. **Kohortna zadržavanje korisnika, mesečno:** koliko korisnika iz svake mesečne kohorte ostaje aktivno posle 1, 2, 3 meseca. Ovo je jedini graf koji ti kaže da li eksperimenti na aktivaciji zaista deluju dugoročno.

### Dnevnik eksperimenata: šablon

Jedan fajl, append-only, svaki eksperiment jedan blok. Ovo je istovremeno tvoja memorija i ulaz za AI agente u Poglavlju 12 (prošireni šabloni u Dodacima, 14-dodaci.md):

```markdown
## EXP-014: Skraćeni uvođenje korisnika (3 koraka)
- Datum: 2026-06-15 → 2026-06-29
- Hipoteza: Smanjenje uvođenja korisnika sa 7 na 3 koraka podiže
  stopu dostizanja aha-momenta u prvih 24h.
- Metrika odluke: % novih korisnika sa aha-momentom u 24h
  (trenutno stanje: izmeri i upiši PRE starta)
- ICE: Impact 8 × Confidence 6 × Ease 7 = 336
- Trajanje: 2 nedelje (zapisano unapred, ne produžava se
  zbog "još malo pa će")
- Rezultat: [popuni posle isteka, broj, ne utisak]
- Odluka: usvoji / odbaci / produži
- Lekcija: [šta sad znaš što pre nisi znao + nove ideje za spisak ideja]
```

### Primena odmah

Napravi danas, za svoj proizvod (rok: 60 minuta):

1. Fajl `eksperimenti/log.md` sa šablonom iznad i fajl `eksperimenti/backlog.md`.
2. Prelistaj svoje beleške iz poglavlja 3-9 i upiši najmanje 6 ideja u spisak ideja, svaku kao hipotezu, ne kao „probaj X".
3. Daj ICE skor svim idejama i upiši prva 3 eksperimenta u dnevnik: hipoteza, metrika odluke, trajanje, kompletno popunjeno PRE nego što bilo šta lansiraš.

Rezultat rada: spisak sa 6+ ocenjenih ideja i dnevnik sa 3 spremna eksperimenta. Prvi lansiraj u ponedeljak.

### Najčešće greške

1. **Promena hipoteze posle rezultata.** „Nije pomerilo konverziju, ali je angažovanje bolji." Rešenje: metrika odluke se piše unapred i ne dira; sve ostalo su zanimljivosti za spisak ideja.
2. **Testiranje nijansi sa malim saobraćajem.** Boja dugmeta na 300 poseta mesečno je čitanje iz šuma. Rešenje: dvocifreni očekivani efekat ili eksperiment ide nazad u backlog.
3. **Prekidanje eksperimenta čim izgleda dobro (ili loše).** Rani rezultati su najnestabilniji. Rešenje: trajanje zapisano unapred; pre isteka se ne odlučuje.
4. **Pet eksperimenata paralelno na istoj metrici.** Ne znaš šta je pomerilo šta. Rešenje: 1-3 nedeljno, na različitim delovima levka.
5. **Eksperimenti bez loga.** Posle tri meseca ponavljaš već propali test. Rešenje: append-only log; petak retrospektiva je nepreskočiv sastanak, i kad si sam sa sobom.

### Kontrolna lista

- [ ] Postoji `eksperimenti/backlog.md`, svaka ideja formulisana kao hipoteza
- [ ] Svaka ideja ima ICE skor (Impact × Confidence × Ease)
- [ ] Postoji `eksperimenti/log.md` sa šablonom iz ovog poglavlja
- [ ] Svaki aktivan eksperiment ima JEDNU metriku odluke i trajanje zapisane unapred
- [ ] Nedeljni ritam u kalendaru: ponedeljak izbor (30 min), petak retrospektiva (30 min)
- [ ] Praćenje događaja radi za registraciju, aha-momenat i konverziju
- [ ] UTM konvencija dokumentovana i primenjuje se na svaki deljeni link
- [ ] Polje „Kako si čuo za nas?" postoji u registraciji
- [ ] Kohortna zadržavanje korisnika se gleda jednom mesečno
- [ ] Sa malim saobraćajem testiram velike zamahe (poruka, cena, uvođenje korisnika), ne nijanse
