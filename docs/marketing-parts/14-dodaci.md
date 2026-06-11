## Dodatak A: Rečnik i formule metrika

Ovo je referentna kartica celog dokumenta. Kad ti u nedeljnom izveštaju iskoči metrika koju ne pamtiš, pogledaj ovde, ne u Google. Sve brojke nose etiketu pouzdanosti; gde univerzalne brojke nema, piše zašto je nema.

### Tabela metrika

| Metrika | Formula / definicija | Orijentir | Detaljno u |
|---|---|---|---|
| **MRR** | Mesečni ponavljajući prihod (zbir svih aktivnih pretplata, svedeno na mesec) | Nema orijentir, definiciona metrika; prati trend, ne apsolutni broj | Poglavlje 1 |
| **ARR** | Godišnji ponavljajući prihod ≈ MRR × 12 | Nema orijentir, definiciona metrika | Poglavlje 1 |
| **CAC** | Ukupni troškovi prodaje i marketinga u periodu / broj novih kupaca u periodu | Sam po sebi ništa ne znači, čitaj ga samo u odnosu na LTV i period povrata | Poglavlja 1 i 6 |
| **LTV** | Prosečan prihod po nalogu × bruto marža / stopa odlazaka kupaca | Nema univerzalan broj, zavisi od segmenta i cene | Poglavlje 1 |
| **LTV:CAC** | LTV / CAC | ≥ 3:1 (orijentir industrije za zdrav SaaS) | Poglavlje 1 |
| **Period povrata CAC-a** | CAC / mesečna bruto marža po kupcu | < 12 meseci (orijentir za ranu fazu) | Poglavlje 1 |
| **Odlasci kupaca** | Izgubljeni kupci (ili prihod) u periodu / kupci (prihod) na početku perioda | Industrijski preseci, jako variraju po segmentu: SMB SaaS 3–7% mesečno; mid-market 1–2% mesečno; enterprise tipično 5–10% godišnje | Poglavlje 1 |
| **NRR** | MRR od kohorte kupaca danas / MRR iste kohorte pre 12 meseci × 100 (razloženo: početni MRR + ekspanzija − kontrakcija − odlasci kupaca, kroz početni MRR) | > 100% = rast bez ijednog novog kupca; najbolje javne SaaS kompanije tipično 110–130% | Poglavlje 1 |
| **Rule of 40** | Stopa rasta % + profitna margina % | ≥ 40 (standard zdravlja SaaS biznisa) | Poglavlje 1 |
| **glavna metrika** | Jedna metrika koja spaja vrednost za korisnika i rast biznisa (koncept Sean Ellis / Amplitude) | Nema broj, test je kvalitativan: da li raste SAMO kad korisnik dobija vrednost | Poglavlje 1 |
| **TTV (time-to-value)** | Vreme od registracije do prve stvarne vrednosti | Nema univerzalnu brojku, kraće je uvek bolje; meriš svoj trend | Poglavlje 3 |
| **Aktivacija** | % novih korisnika koji dostignu TVOJ aha-momenat | Aha-prag definišeš sam iz podataka; javno poznati primeri: Facebook „7 prijatelja za 10 dana", Slack ~2000 poslatih poruka | Poglavlje 3 |
| **Konverzija free→plaćeno** | Plaćeni / ukupno registrovani | Industrijski rasponi (ankete OpenView / Lenny's Bilten): freemium 2–5%; probni period bez kartice ~8–12%; probni period sa karticom 40%+ ali uz drastično manje prijava | Poglavlje 3 |
| **PQL** | Potencijalni kupac kvalifikovan ponašanjem u proizvodu, ne formularom | Nema orijentir, definicija je tvoja lista ponašanja (npr. aktiviran + dostigao limit plana) | Poglavlje 3 |
| **K-faktor** | Broj pozivnica po korisniku × stopa konverzije pozivnice | K > 1 = samoodrživ viralni rast (izuzetno redak); već K od 0,3–0,5 značajno obara efektivni CAC | Poglavlje 4 |
| **Sean Ellis PMF test** | % aktivnih korisnika koji bi bili „veoma razočarani" da proizvod nestane | ≥ 40% = signal usklađenosti proizvoda i tržišta | Poglavlja 1 i 3 |
| **Stopa prihvatanja OS-a** | Prihvaćeni nacrti agenata / ukupno predloženih nacrta na ljudskoj kapiji | Nema spoljnog orijentira, interni trend koji treba da raste iz nedelje u nedelju; pad = pogledaj brend priručnik, ne agenta | Poglavlje 12 |

### Mini-rečnik termina

| Termin | Značenje u jednoj rečenici |
|---|---|
| Odlasci kupaca | Stopa odliva kupaca ili prihoda. |
| Funnel | Levak: put od prvog kontakta do plaćanja. |
| Freemium | Trajno besplatan plan kao ulaz u proizvod. |
| Probni period | Vremenski ograničen probni period punog proizvoda. |
| Uvođenje korisnika | Vođenje novog korisnika do prve vrednosti. |
| Zadržavanje | Zadržavanje: koliko korisnika ostaje aktivno kroz vreme. |
| PLG | Product-led rast, proizvod je glavni kanal akvizicije, konverzije i širenja. |
| AEO/GEO | Optimizacija da te AI odgovori citiraju, ne samo da se rangiraš (Poglavlje 5). |
| Nevidljive preporuke | Preporuke u kanalima koje analitika ne vidi (DM, privatne grupe), zato pitanje o izvoru koje korisnik sam popunjava. |
| ICE | Impact × Confidence × Ease, prioritizacija eksperimenata (Sean Ellis). |
| prepoznatljivi elementi brenda | Prepoznatljivi elementi brenda: ime, boja, vizuelni potpis, glas (Byron Sharp, Poglavlje 8). |
| Imejl kroz životni ciklus korisnika | Imejl vezan za ponašanje korisnika, ne za kalendar (Poglavlje 7). |

---

## Dodatak B: Šabloni

Sve ispod je copy-paste materijal. Prilagodi `[PLACEHOLDER]` mesta i kreni, nemoj nedelju dana „doterivati" šablon pre prve upotrebe.

### B1. Skelet brend priručnika (7 fajlova)

Struktura i namena fajlova detaljno su objašnjeni u Poglavlju 11, imena ispod su ista, jedan na jedan. Napravi folder `brandbook/` u marketinškom repozitorijumu i popuni:

```
--- FILE: brandbook/01-identitet.md ---
# Identitet
- Proizvod: [IME], [JEDNA REČENICA ŠTA RADI]
- Misija: [ZAŠTO POSTOJIMO, BEZ PATETIKE]
- glavna metrika: [METRIKA], [ZAŠTO BAŠ ONA]
- Poslovni model: [freemium / probni period / prodaja]
- Ličnost brenda u 3-5 prideva: [SVAKI SA OBJAŠNJENJEM ŠTA ZNAČI U PRAKSI]

--- FILE: brandbook/02-icp.md ---
# Kome prodajemo
- ICP: [ULOGA] u [TIP FIRME], koji pokušava [JTBD, POSAO KOJI OBAVLJA]
- Bol koji rešavamo: [KONKRETAN BOL, REČIMA KUPCA]
- Anti-ICP (kome NE prodajemo): [LISTA, agenti ovo poštuju]

--- FILE: brandbook/03-pozicioniranje.md ---
# Pozicioniranje i dokazi
- Kategorija: [KAKO KUPAC ZOVE OVU VRSTU ALATA]
- Glavna alternativa: [ŠTA KUPAC RADI DANAS UMESTO NAS]
- Diferencijator: [ŠTA IMAMO ŠTO ALTERNATIVA NEMA]
- Glavna poruka (jedna rečenica): [PORUKA]
- Tri potporne tvrdnje, SVAKA sa dokazom: [BROJKA SA IZVOROM /
  ODOBREN TESTIMONIJAL / LINK NA STUDIJU SLUČAJA]
- PRAVILO: agent ne sme izmisliti nijednu brojku van ovog fajla.

--- FILE: brandbook/04-glas-i-ton.md ---
# Glas i ton
- Glas u 3 prideva: [NPR. direktan, konkretan, bez preterivanja]
- Pišemo: [LICE, DUŽINA REČENICA, PRIMERI DA/NE]
- Zabranjene reči i fraze: [LISTA, npr. "revolucionarno", "game-changer"]
- ❌/✅ parovi po kanalu: [LOŠ I DOBAR PASUS ZA SVAKI KANAL, MIN. 3 PARA]

--- FILE: brandbook/05-zabranjeno.md ---
# Crvene linije (šta agent NE sme)
- Ne objavljuje ništa bez ljudske kapije.
- Ne pominje konkurente po imenu bez odobrenja.
- Ne obećava funkcije koje ne postoje.
- Ne odgovara na [OSETLJIVE TEME, LISTA].
- Eskalacija: ako nije siguran → piše u [KANAL/FAJL] i staje.

--- FILE: brandbook/06-zlatni-primeri.md ---
# Zlatni primeri (biblioteka primera)
- [3-5 NAJBOLJIH OBJAVA/TEKSTOVA, CELI, SA NAPOMENOM ZAŠTO SU DOBRI]
- Dopunjavaš posle svakog teksta koji ispadne odličan, fajl raste.

--- FILE: brandbook/07-vizuelni-standardi.md ---
# Vizuelni standardi (prepoznatljivi elementi brenda)
- Boje: [HEX KODOVI + GDE SE KOJA KORISTI]
- Tipografija: [FONTOVI]
- Vizuelni potpis: [ŠTA SE PONAVLJA NA SVAKOM MATERIJALU]
- Šta NIKAD ne radimo vizuelno: [LISTA]
```

### B2. Prompt rutine: nedeljni izveštaj metrika

Zakaži kao `/schedule` rutinu (npr. ponedeljak 07:00), radi i kad je računar ugašen. Po istom CLAUDE.md obrascu, rutina prvo čita brend priručnik. Putanje prate strukturu repozitorijuma `marketing-os/` iz Poglavlja 12; B2 je skraćena varijanta Rutine 1 iz tog poglavlja, koristi jednu od dve, putanje su iste.

```
Ti si marketinški analitičar za [PROIZVOD]. Radiš u ovom repozitorijumu.

1. Pročitaj sve fajlove u brandbook/ (kontekst, ne menjaj ih).
2. Učitaj ovonedeljni izvoz iz data/metrike/ (najnoviji fajl;
   polja: datum, posete, registracije, aktivirani, plaćeni,
   MRR, odlasci kupaca, izvor-atribucije).
3. Uporedi sa prethodnom nedeljom: registracije, aktivacija %, 
   free→plaćeno %, MRR, odlasci kupaca, top 3 odgovora na "Kako ste čuli za nas?".
4. Označi svaku promenu veću od [PRAG]% kao ANOMALIJU sa hipotezom uzroka.
5. Napiši izveštaj u izvestaji/YYYY-MM-DD-nedeljni.md:
   - 5 brojeva u tabeli (sada vs. prošla nedelja)
   - anomalije + hipoteze
   - JEDNA preporučena akcija za ovu nedelju
6. Ne menjaj nijedan drugi fajl. Ne donosi odluke, predlažeš.
```

### B3. Prompt rutine: nacrti sadržaja

Takođe `/schedule` rutina ili `claude -p "..."` iz cron-a. Ključno: piše u `content/nacrti/`, nikad ne objavljuje, objavu radi čovek kroz alat za zakazivanje objava. B3 je skraćena varijanta Rutine 2 iz Poglavlja 12, koristi jednu od dve, putanje su iste.

```
Ti si pisac sadržaja za [PROIZVOD]. Radiš u ovom repozitorijumu.

1. OBAVEZNO prvo pročitaj ceo brandbook/, glas i ton (04),
   crvene linije (05) i zlatni primeri (06) su zakon.
   Brojke samo iz dokaza u 03-pozicioniranje.md.
2. Pročitaj strategija/content-plan.md i content/ideje/
   i uzmi prve [N] neobrađene teme.
3. Za svaku temu napiši nacrt u content/nacrti/{DATUM}-{slug}.md
   sa headerom:
   kanal: [blog/bilten/social]
   cilj: [metrika koju gađa]
   poziv_na_akciju: [jedan poziv na akciju]
4. Format po kanalu: [TVOJA PRAVILA, dužina, struktura, primeri].
5. Označi temu u content/ideje/ kao "nacrt spreman".
6. NIKAD ne objavljuj i ne šalji ništa. Nacrt čeka ljudsku kapiju.
```

### B4. Prompt agent za kontrolu brenda

Pokreći kao pomoćnog agenta nad svakim nacrtom pre ljudske kapije, jeftin filter koji ti štedi vreme na kapiji.

```
Ti si kontrola brenda kontrolor. Ulaz: putanja do nacrta u content/nacrti/.

1. Pročitaj ceo brandbook/ i zatim nacrt.
2. Oceni nacrt 1-10 po dimenzijama:
   - glas (poklapanje sa 04-glas-i-ton.md, uključujući zabranjene reči)
   - icp_fit (da li govori ICP-u iz 02-icp.md, ne "svima")
   - dokazi (SVAKA brojka mora postojati u 03-pozicioniranje.md)
   - granice (nijedno kršenje 05-zabranjeno.md)
   - struktura (format kanala iz headera nacrta)
3. Vrati ISKLJUČIVO JSON:
   { "ocena_ukupno": X, "prolaz": true/false,
     "dimenzije": {...}, "razlozi": ["..."], "predlozi": ["..."] }
4. prolaz = true samo ako je svaka dimenzija ≥ 8 i nema kršenja granica.
5. Ne prepravljaj nacrt sam, vraćaš razloge, autor ispravlja.
```

### B5. Dnevnik eksperimenata

Kanonski je blok-format iz Poglavlja 10 (jedan `## EXP-XXX` blok po eksperimentu u `eksperimenti/log.md`; ideje čekaju u `eksperimenti/backlog.md`); tabela ispod je kompaktna varijanta istog dnevnika za pregled, jedan red = jedan eksperiment. Hipoteza i metrika odluke upisuju se UNAPRED, menjanje posle rezultata je samoobmana (Poglavlje 10). Podsetnik zašto dnevnik postoji: Kohavijev nalaz o trećinama (Poglavlje 10).

```
| ID | Datum | Hipoteza (unapred) | Metrika odluke (unapred) | I | C | E | ICE | Trajanje | Rezultat | Odluka | Naučeno |
|----|-------|--------------------|--------------------------|---|---|---|-----|----------|----------|--------|---------|
| E-001 | [DATUM] | Ako [PROMENA], onda [METRIKA] raste za [X], jer [RAZLOG] | [JEDNA metrika + prag odluke] | 7 | 6 | 8 | 336 | [2 ned.] | [BROJKE] | [usvoji/odbaci/ponovi] | [JEDNA rečenica] |
```

### B6. Lansiranje checklist

Za svako lansiranje iz serije (Poglavlje 9), ne samo „veliki dan".

```
T-14 dana:
- [ ] Lista čekanja ili prodajna stranica je živa, prikupljanje imejl adresa radi (test prijavom)
- [ ] mehanika preporuka za poziciju u redu uključena
- [ ] Uvođenje korisnika izglancano: TTV izmeren, aha dostižan bez pomoći
- [ ] Dokazi u 03-pozicioniranje.md ažurirani (sveže brojke/testimonijali za copy)
T-1 dan:
- [ ] Svi materijali prošli kontrola brenda (B4) i ljudsku kapiju
- [ ] Imejl sekvenca (B7) aktivna za nove registracije
T-dan:
- [ ] Objave po kanalima (zakazane kroz alat za zakazivanje objava)
- [ ] Osnivač lično odgovara na komentare ceo dan (vođeno lično od osnivača)
T+2 dana:
- [ ] Ponovno oglašavanje i poruka za nastavak imejl aktivni, hvataju saobraćaj posle
      špica (pažnja ispari za ~48h, industrijska procena za Product Hunt)
- [ ] Upis u dnevnik eksperimenata: šta je lansiranje donelo po metrici odluke
```

### B7. Aktivaciona imejl sekvenca (skica)

Pet imejlova, svaki vezan za ponašanje, ne za kalendar, životni ciklus korisnika, ne bilten (Poglavlje 7).

```
1. Dobrodošlica + JEDAN sledeći korak
   Okidač: registracija (odmah). Svrha: skratiti TTV, jedan link
   ka prvoj akciji, bez ture kroz sve funkcije.
2. Gurni ka aha-momentu
   Okidač: 48h od registracije bez dostignutog aha-praga (Poglavlje 7).
   Svrha: ukloniti konkretnu prepreku ("Zapeo si kod [KORAK]?
   Evo 60-sek rešenja").
3. Use-case proširenje
   Okidač: aha dostignut. Svrha: pokazati drugi posao koji proizvod
   obavlja, produbljivanje navike.
4. Društveni dokaz + nadogradnja
   Okidač: PQL signal (npr. dostignut limit besplatnog plana).
   Svrha: dokaz iz 03-pozicioniranje.md + jasan razlog za plaćeni plan.
5. Istek/odluka
   Okidač: 3 dana pre isteka probnog perioda (ili 14. dan freemium-a bez
   konverzije), kao u tabeli tokova iz Poglavlja 7. Svrha: rezime
   vrednosti KOJU JE KORISNIK VEĆ DOBIO (njegove brojke iz
   proizvoda) + poziv na akciju.
```

### B8. Pitanje o izvoru koje korisnik sam popunjava

Obavezno polje pri registraciji, jedini pouzdan pogled u nevidljive preporuke (praksa koju je popularizovao Refine Labs / Chris Walker; Poglavlje 5). Otvoreno polje, ne padajuća lista (Poglavlja 2 i 5): odgovori tipa „neko te pomenuo u Slack grupi" ne staju ni u jednu unapred ponuđenu opciju.

```
Kako si čuo/čula za nas? (obavezno, slobodan unos)
[____________________________________________]
```

Kategorisanje radiš NAKNADNO, pri nedeljnom pregledu odgovora, nikako kao opcije u formi. Polazne kategorije za kodiranje:

```
- Preporuka kolege ili prijatelja
- Google / pretraga
- AI asistent (ChatGPT, Claude, Perplexity...)
- Društvene mreže (koja)
- YouTube / podcast
- Zajednica ili forum (Reddit, Slack/Discord grupa...)
- Blog ili članak
- Ostalo
```

### B9. Prompt rutine: competitor scan

Sreda u nedeljnom rasporedu iz Poglavlja 12. Skelet, dopuni listu konkurenata i izvore.

```
Ti si tržišni analitičar za [PROIZVOD]. Radiš u ovom repozitorijumu.

1. Prvo pročitaj sve fajlove u brandbook/ i strategija/ (kontekst).
2. Pročitaj prethodne nalaze iz data/konkurencija/.
3. Za svakog konkurenta sa liste [KONKURENTI]: proveri javne promene,
   cene, nove funkcije, poruke na sajtu, nove recenzije.
4. Zapiši nalaze u data/konkurencija/YYYY-MM-DD.md: šta je novo od
   prošlog skena, šta je pretnja, šta prilika, uz izvor za svaku
   tvrdnju; tvrdnja bez izvora se ne upisuje.
5. Ne menjaš nijedan drugi fajl i ne objavljuješ ništa.
```

### B10. Prompt rutine: retrospektiva eksperimenata

Petak u nedeljnom rasporedu iz Poglavlja 12. Radi nad logom i backlogom iz B5/Poglavlja 10.

```
Ti si analitičar rasta za [PROIZVOD]. Radiš u ovom repozitorijumu.

1. Prvo pročitaj sve fajlove u brandbook/ i strategija/.
2. Pročitaj eksperimenti/log.md i eksperimenti/backlog.md.
3. Za svaki eksperiment kome je isteklo trajanje: uporedi rezultat sa
   metrikom odluke (upisanom unapred) i predloži odluku:
   usvoji / odbaci / produži, sa obrazloženjem u jednoj rečenici.
4. Dopiši predlog u kolone Rezultat/Odluka/Naučeno u eksperimenti/log.md;
   konačnu odluku potvrđuje čovek.
5. Predloži tačno 3 eksperimenta za sledeću nedelju iz backloga,
   sortirano po ICE skoru.
6. Ne pokrećeš nijedan eksperiment i ne objavljuješ ništa, predlažeš.
```

### B11. Prompt rutine: mesečna AEO provera + pregled brend priručnika

Prvi dan u mesecu po rasporedu iz Poglavlja 12. AEO/GEO pojmovi i higijena su u Poglavlju 5.

```
Ti si AEO kontrolor za [PROIZVOD]. Radiš u ovom repozitorijumu.

1. Prvo pročitaj sve fajlove u brandbook/ i strategija/.
2. Za [N] tipičnih upita našeg ICP-a (iz strategija/icp.md) proveri
   da li nas AI odgovori citiraju, ko jeste citiran i sa kojim izvorom.
3. Proveri AEO higijenu iz Poglavlja 5: definicione stranice,
   strukturirani podaci, svežina G2/recenzija profila.
4. Napiši izveštaj u izvestaji/YYYY-MM-aeo.md: citiranost, promene
   od prošlog meseca, 3 predloga.
5. Predloži izmene brend priručnika kao listu u istom izveštaju,
   NE menjaš fajlove u brandbook/ sam; izmene potvrđuje čovek.
6. Ne objavljuješ ništa.
```

---

## Dodatak C: Marketinški kalendar prve godine SaaS proizvoda

Ovo je podrazumevani plan, pomeraj ga po svojoj realnosti, ali ne preskači redosled: temelji pre kanala, kanal pre sistema, sistem pre autonomije. Detaljna OS tranzicija (ručno → asistirano → autonomno) razrađena je u Poglavlju 13.

| Kvartal | Fokus | Zadaci (3–5) | Prekretnica |
|---|---|---|---|
| **Q1, Temelji** | Pozicioniranje, merenje, prvi korisnici | 1. Pozicioniranje i poruka po metodu iz Poglavlja 2 (ICP, JTBD, glavna alternativa). 2. Prodajna stranica sa prikupljanjem imejl adresa + pitanjem o izvoru koje korisnik sam popunjava (B8). 3. Kontrolna tabla metrika iz Poglavlja 1 (makar ručni CSV). 4. Lista čekanja sa mehanikom preporuke → zatvorena beta. 5. 10+ razgovora sa beta korisnicima, zapisano rečima kupca. | Beta korisnici aktivni; definisan aha-momenat i izmeren TTV; Sean Ellis test poslat (cilj: signal ka 40% „veoma razočaranih") |
| **Q2, Prvi kanal + lansiranje** | Jedan kanal do ponovljivosti, javno lansiranje, prva petlja | 1. Izaberi JEDAN primarni kanal (Poglavlja 5–6) i objavljuj nedeljnim ritmom. 2. Javno lansiranje po kontrolnoj listi B6 (lista čekanja → dan lansiranja → T+48h sistem). 3. Aktivaciona imejl sekvenca B7 uživo. 4. Dizajniraj prvu petlju rasta iz Poglavlja 4 (npr. upotreba-kao-distribucija ili preporuka). 5. Pokreni dnevnik eksperimenata (B5), minimum 1 eksperiment nedeljno. | Lansiranje izvršeno; prvi plaćeni kupci; jedan kanal sa ponovljivim dotokom registracija; petlja v1 u proizvodu |
| **Q3, OS faza 1–2** | Marketing repozitorijum + asistirani agenti (ručno → asistirano) | 1. Postavi marketinški repozitorijum i popuni svih 7 fajlova brend priručnika (B1). 2. Uključi nedeljni izveštaj metrika kao `/schedule` rutinu (B2). 3. Uključi rutinu nacrta sadržaja (B3) + agent za kontrolu brenda (B4), sve kroz ljudsku kapiju. 4. Počni da meriš stopu prihvatanja OS-a (Dodatak A). 5. AEO/GEO higijena iz Poglavlja 5: definicije, strukturirani podaci, G2/recenzije profil. | OS faza 2 živa: agenti predlažu, ti odobravaš; stopa prihvatanja se meri i raste iz nedelje u nedelju |
| **Q4, OS faza 3 + drugi kanal + cenovnik** | Delimična autonomija, diverzifikacija, monetizacija | 1. OS faza 3 za niskorizične rutine (izveštaji, interni nacrti) uz sigurnosni prekidač iz Poglavlja 12; objave i dalje kroz kapiju. 2. Dodaj DRUGI kanal tek sad, prvi mora raditi bez tebe. 3. eksperiment sa cenovnikom i pakovanjem ponude: po ProfitWell analizama, ulaganje u monetizaciju ima višestruko veći uticaj od istog ulaganja u akviziciju. 4. Godišnji presek: LTV:CAC (cilj ≥ 3:1, orijentir industrije), period povrata (< 12 meseci, orijentir za ranu fazu), odlasci kupaca vs. preseci segmenta. 5. Plan za godinu 2 na osnovu dnevnika eksperimenata, ne osećaja. | OS radi nedeljni ciklus sa minimalnim tvojim vremenom; dva kanala; eksperiment sa cenovnikom završen sa odlukom u logu |

Tri pravila koja kalendar drže na okupu:

1. **Ne dodaješ kanal dok prethodni ne radi ponovljivo.** Dva polu-kanala su gora od jednog celog, i agenti u Q3 nemaju šta da sistematizuju ako proces ne postoji.
2. **Sve brojke teku u jedan dnevnik.** Dnevnik eksperimenata (B5) + nedeljni izveštaj (B2) su memorija sistema; bez njih Q4 odluke donosiš napamet.
3. **Autonomija se zarađuje, ne uključuje.** Redosled faza iz Poglavlja 13 nije birokratija, stopa prihvatanja ti govori kad je agent spreman za sledeći stepen slobode.
