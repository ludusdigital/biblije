## Poglavlje 13: Plan uvođenja: od ručnog do autonomnog za 12 nedelja

Sve do sada, metrike, pozicioniranje, petlje, brend priručnik, arhitektura OS-a, sklapa se ovde u jedan kalendar. Ovo poglavlje je tvoj plan implementacije: 12 nedelja, tri faze, merljive prekretnice. Gvozdeno pravilo koje drži ceo plan na okupu:

> **Automatizuje se SAMO proces koji si bar 10 puta uradio ručno i za koji postoji zapisan standard kvaliteta.** Automatizacija lošeg procesa proizvodi loš rezultat, samo brže i u većoj količini.

Zato faze idu ovim redom: prvo radiš rukama i zapisuješ, pa agent radi a ti pregledaš sve, pa tek onda agent radi sam uz tvoj pregled. Preskakanje faza nije ušteda vremena, to je proizvodnja generičkog AI sadržaja koji, kako smo videli u Poglavlju 5, platforme i čitaoci ignorišu.

### Šta ćeš naučiti

- Zašto se automatizuje samo proces koji si 10+ puta uradio ručno
- Šta tačno radiš svake od 12 nedelja, sa prekretnicom na kraju svake faze
- Kako se stopa prihvatanja meri i koristi kao kapija između faza
- Koje metrike čine tablu ključnih metrika OS-a, i zašto biznis metrike moraju biti u njoj
- Kako da napraviš sopstveni 12-nedeljni kalendar uvođenja

### Pregled tri faze

| Faza | Nedelje | Ko radi | Tvoja uloga | Prekretnica za prelaz |
|---|---|---|---|---|
| 1. Ručno | 1–4 | Ti | Izvršilac + pisac procedura | 4 nedelje doslednog ritma + brend priručnik je prošao test |
| 2. Asistirano | 5–8 | Agent (nacrti), ti (objava) | Recenzent 100% rezultata | Stopa prihvatanja ~80% za bar jedan tip sadržaja |
| 3. Autonomno | 9–12 | Cron rutine + agent za proveru kvaliteta | Nedeljni pregled + završna kapija | Stabilan rezultat, biznis metrike se pomeraju |

### Faza 1: Ručno (nedelje 1–4): radiš ti, ali zapisuješ kao mašina

Cilj faze nije volumen, nego **dokumentovan, ponovljiv proces**. Svaki korak koji uradiš, zapisuješ kao proceduru, jer te procedure u Fazi 2 doslovno postaju promptovi rutina.

**Nedelja 1:** Izaberi 1–2 kanala na osnovu svog ICP-a (kriterijumi u Poglavljima 5 i 6, gde tvoj kupac stvarno provodi vreme, ne gde je tebi zabavno). Postavi kontrolnu tablu metrika iz Poglavlja 1 (registracije, aktivacija, MRR, makar i ručno popunjavana tabela). Počni brend priručnik v1 po strukturi iz Poglavlja 11.

**Nedelje 2–4:** Radi kanale rukama, doslednim ritmom (npr. 3 objave + 1 duži sadržaj nedeljno). Posle SVAKOG izvršenog zadatka, dopuni proceduru. Format procedure:

```markdown
# PROCEDURA: nedeljna objava (tip: edukativni post)
Učestalost: 3x nedeljno (pon/sre/pet)
Ulaz: tema iz content/ideje/ + fajlovi brend priručnika

KORACI:
1. Pročitaj brend priručnik (glas, ICP, zabranjene fraze)
2. Izaberi temu, mora odgovarati na stvarno pitanje ICP-a,
   ne "šta bih ja voleo da pišem"
3. Nacrt: prva rečenica koja hvata pažnju, jedan konkretan uvid, bez pretrpavanja pozivima na akciju
4. Provera protiv ❌/✅ primera u brend priručniku
5. Objavi kroz alat za zakazivanje objava; zabeleži link u log

STANDARD KVALITETA (šta znači "dobro"):
- ❌ "AI menja sve. Evo 5 saveta..." (generično, bez ugla)
- ✅ "Probao sam X na sopstvenom proizvodu 3 nedelje. Evo brojki..."
   (konkretno, prvo lice, podaci)
```

Procedura bez sekcije "standard kvaliteta" je nepotpuna, agent u Fazi 2 ne može da pogodi šta ti znači "dobro" ako to nisi zapisao.

**Prekretnica Faze 1:** (a) 4 nedelje neprekinutog ritma objavljivanja, nijedna preskočena nedelja; (b) brend priručnik v1 prošao test iz Poglavlja 11 (agent iz hladnog starta proizvodi sadržaj koji prepoznaješ kao svoj); (c) svaki ponavljajući zadatak ima zapisanu proceduru sa standardom kvaliteta. Ako bilo šta od ovoga ne stoji, Faza 1 se produžava. Nema pregovora: ritam koji ne preživi 4 nedelje sa tobom za volanom neće preživeti ni sa agentom.

### Faza 2: Asistirano (nedelje 5–8): agent piše, ti pregledaš sve

Sada tvoje procedure postaju promptovi. Agent (npr. kroz `claude -p "..."` ili sesiju koja prvo čita brend priručnik po CLAUDE.md obrascu iz Poglavlja 11) proizvodi nacrte i analize po proceduri, **ti pregledaš 100% rezultata pre objave**. Ništa ne izlazi bez tvog odobrenja.

Ali konverzija nije doslovno prepisivanje. Pravilo: korake koji ostaju u repozitorijumu prepiši od reči do reči, a **svaki korak koji dira javnost zamenjuje se pisanjem fajla**. Na proceduri iz Faze 1 to znači da koraci 1–4 ostaju isti, a korak 5 se obavezno menja:

```markdown
❌ 5. Objavi kroz alat za zakazivanje objava; zabeleži link u log
✅ 5. Sačuvaj nacrt u content/nacrti/ sa metapodacima na početku fajla (datum,
      kanal, ciljna metrika) i STANI, objavu radi čovek
      posle kapije
```

Agent sa korakom "objavi" u promptu je najveća greška #1 iz Poglavlja 12, kapija "NIKAD ne objavljuj" važi i kad je prompt nastao iz tvoje sopstvene procedure.

Ključna metrika faze je **stopa prihvatanja**: procenat nacrta koji prolaze bez suštinskih izmena (kozmetička izmena reči se ne računa kao odbijanje; promena ugla, tona ili tvrdnje se računa). Meri ga po tipu sadržaja, u običnoj tabeli:

```markdown
# DNEVNIK PRIHVATANJA: nedelja 6
| Datum | Tip            | Prihvaćeno? | Razlog odbijanja → novo pravilo |
|-------|----------------|-------------|----------------------------------|
| 5.2.  | edukativni post| da          | nema izmene                         |
| 5.2.  | najava funkcionalnosti | ne          | previše superlativa → dodat ❌/✅ |
| 7.2.  | edukativni post| da          | nema izmene                         |
Nedeljni presek: edukativni 5/6 (83%), najave 1/3 (33%)
```

Pravilo petlje učenja: **svako odbijanje = novo pravilo ili ❌/✅ par u brend priručniku.** Ako odbiješ nacrt a ne zapišeš zašto, agent će istu grešku ponoviti, i to je tvoja greška, ne njegova. Brend priručnik raste kroz odbijenice; to mu je glavni mehanizam evolucije.

**Nedelje 5–6:** agent preuzima 1 tip sadržaja (onaj sa najzrelijom procedurom). **Nedelje 7–8:** dodaješ drugi i treći tip + analitičke zadatke (nedeljni izveštaj metrika, presek eksperimenata iz Poglavlja 10).

**Prekretnica Faze 2:** stopa prihvatanja ~80% za bar jedan tip sadržaja, mereno kroz bar dve uzastopne nedelje. Tip koji je na 50% ne prelazi dalje, vraća se u doradu procedure i brend priručnika.

### Faza 3: Autonomno (nedelje 9–12): rutine rade, ti pregledaš

Tipovi sadržaja koji su prešli prag od ~80% prelaze na zakazane rutine: `/schedule` (agenti u oblaku po zakazanom rasporedu, rade i kad je računar ugašen), GitHub Actions vezane za repozitorijum, ili `claude -p` iz bilo kog sistema za zakazano pokretanje, arhitektura, agent za proveru kvaliteta i sigurnosni prekidač su detaljno u Poglavlju 12. Svaka rutina prvo čita brend priručnik, proizvodi rezultat, agent za proveru kvaliteta ga proverava protiv standarda kvaliteta, pa tek onda ide ka objavi.

Ti se pomeraš sa pregleda svakog komada na **nedeljni pregled**: uzorak rezultata, dnevnik prihvatanja, kontrolna tabla ključnih metrika, izmene brend priručnika. Tvoje vreme se seli sa proizvodnje na strategiju, biranje eksperimenata, razgovore sa korisnicima, rad na cenovniku (po ProfitWell analizama i dalje najpotcenjeniju polugu, Poglavlje 1).

**Šta NIKAD ne prelazi u Fazu 3** (puna lista i obrazloženje u Poglavlju 12): odgovori nezadovoljnim korisnicima i krizna komunikacija, objave o ceni i pravne/finansijske tvrdnje, slanje na celu imejl listu, izjave u tvoje lično ime kao osnivača. Tu je čovek završna kapija, trajno.

### kontrolna tabla ključnih metrika OS-a

OS koji proizvodi sadržaj a ne pomera biznis metrike je pozorište, ne marketing. Zato tabla obavezno spaja operativne metrike OS-a sa biznis metrikama iz Poglavlja 1:

| Metrika | Faza 1 (početno stanje) | Cilj Faza 3 | Zašto |
|---|---|---|---|
| Tvoje vreme nedeljno na izvršenje | zabeleži stvarno (npr. 10–15h) | višestruko manje | Smisao OS-a |
| Stopa prihvatanja po tipu | početna vrednost | ~80%+ po autonomnom tipu | Kapija kvaliteta |
| Rezultati / nedelja | tvoj ručni ritam | isti ili veći, bez pada kvaliteta | Doslednost |
| Registracije / nedelja | početna vrednost iz tabele Poglavlja 1 | rast trenda | Da li mašina dovodi ljude |
| Aktivacija (TTV, aha-momenat) | početna vrednost | stabilna ili bolja | Da li dovodi PRAVE ljude |
| MRR | početna vrednost | rast trenda | Krajnji sud |

Ako posle 12 nedelja operativne metrike sijaju a registracije, aktivacija i MRR stoje, problem nije OS nego ulaz u njega: kanal, poruka ili pozicioniranje (vrati se na Poglavlja 2 i 5). Seti se Kohavijevog nalaza o trećinama (Poglavlje 10), zato se sve meri, pa i sam OS.

### Primena odmah

Napravi fajl `plan-12-nedelja.md` u svom marketinškom repozitorijumu, svoj kalendar uvođenja, danas:

```markdown
# 12-NEDELJNI PLAN UVOĐENJA: [tvoj proizvod]
Start: [datum] | Kanali (1-2): [iz Poglavlja 5/6, po ICP-u]

## FAZA 1 (ned. 1-4): RUČNO
N1: kanali izabrani, kontrolna tabla ključnih metrika postavljena, brend priručnik v1 započet
N2-4: ritam [X objava + Y dužih nedeljno], procedura po zadatku
PREKRETNICA: [ ] 4 ned. ritma [ ] test brend priručnika [ ] sve procedure

## FAZA 2 (ned. 5-8): ASISTIRANO
N5-6: agent preuzima [tip #1], dnevnik prihvatanja aktivan
N7-8: + [tip #2/#3] + nedeljni izveštaj metrika
PREKRETNICA: [ ] stopa prihvatanja ~80% za bar 1 tip, 2 ned. zaredom

## FAZA 3 (ned. 9-12): AUTONOMNO
N9-10: [tip #1] na zakazanu rutinu (cron) + agent za proveru kvaliteta
N11-12: nedeljni pregled ritam; lista "nikad autonomno" zalepljena
PREKRETNICA: [ ] stabilan rezultat [ ] registracije/MRR trend zabeležen

## TABLA KLJUČNIH METRIKA (popunjavaj nedeljno)
| Ned | Moje vreme | Prihvatanje | Rezultat | Registracije | Aktivacija | MRR |
```

Rezultat rada: popunjen plan sa stvarnim datumima i izabranim kanalima, prva nedelja već u toku.

### Najčešće greške

1. **Automatizacija pre 10 ručnih ponavljanja.** Proces koji nisi savladao rukama ne umeš ni da oceniš kad ga agent radi. Rešenje: broji ponavljanja u proceduri; ispod 10, ostaje ručno.
2. **Procedure bez standarda kvaliteta.** "Napiši post o X" nije procedura. Rešenje: svaka procedura mora imati sekciju sa ❌/✅ primerima, to je razlika između prompta i želje.
3. **Odbijanje nacrta bez zapisivanja razloga.** Agent ponavlja grešku, ti gubiš vreme, stopa prihvatanja stagnira. Rešenje: pravilo "nema odbijanja bez novog pravila u brend priručniku", bez izuzetka.
4. **Prelazak u Fazu 3 sa stopom prihvatanja od 50–60%.** Dobijaš autonomnu mašinu za osrednji sadržaj. Rešenje: prag je ~80% kroz dve uzastopne nedelje, po tipu, tip koji ne prelazi prag ostaje u Fazi 2.
5. **Slavljenje rezultata umesto ishoda.** "Objavili smo 40 komada ovog meseca" ne znači ništa ako registracije stoje. Rešenje: biznis metrike iz Poglavlja 1 su u tabli ključnih metrika od prvog dana, ne naknadno.

### Kontrolna lista

- [ ] Izabrana 1–2 kanala na osnovu ICP-a (ne na osnovu lične preferencije)
- [ ] kontrolna tabla ključnih metrika postavljena pre starta, sa početnim vrednostima (registracije, aktivacija, MRR)
- [ ] Svaki ponavljajući zadatak ima zapisanu proceduru sa standardom kvaliteta
- [ ] Brend priručnik v1 prošao test iz Poglavlja 11 pre kraja Faze 1
- [ ] 4 nedelje neprekinutog ručnog ritma, nijedna preskočena
- [ ] Dnevnik prihvatanja se vodi po tipu sadržaja od prvog dana Faze 2
- [ ] Svako odbijanje proizvelo novo pravilo ili ❌/✅ par u brend priručniku
- [ ] U Fazu 3 prešli samo tipovi sa ~80% stope prihvatanja kroz 2 uzastopne nedelje
- [ ] Lista "nikad autonomno" iz Poglavlja 12 zalepljena u repozitorijum i poštuje se
- [ ] Nedeljni pregled u kalendaru kao neprikosnoveni termin
- [ ] Posle 12 nedelja: poređenje biznis metrika sa početnim stanjem, OS sudi rezultat, ne volumen
