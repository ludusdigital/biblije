## Poglavlje 11: Brandbook kao algoritam — ustav za mašine

### Šta ćeš naučiti

- Zašto je AI agent odličan izvršilac, a loš čuvar ukusa — i kako se to rešava tekstom, ne nadom
- Strukturu mašinski čitljivog brandbooka: 7 markdown fajlova sa svrhom, sadržajem i primerom za svaki
- Zašto je `04-glas-i-ton.md` najvažniji fajl i zašto agenti uče iz ❌/✅ parova više nego iz prideva
- Test brandbooka: kako za sat vremena saznaš gde ti je brandbook rupav
- Kako brandbook verzionišeš kroz git i pretvaraš svaku ispravku u novo pravilo

### Problem: agent bez ustava

Do sada si gradio motore rasta (Deo II) i eksperimentalni pogon (Poglavlje 10). Sledeći korak — autonomni marketinški OS iz Poglavlja 12 — ne sme da krene bez ovog poglavlja. Razlog je jednostavan: AI agent izvršava savršeno i prosuđuje loše. Daj mu zadatak "napiši objavu o novoj funkciji" i dobićeš gramatički besprekoran tekst koji zvuči kao bilo koji SaaS na svetu — uzvičnici, "uzbuđeni smo", emoji raketa. Ne zato što je agent loš, nego zato što nema tvoj ukus. Ukus se ne prenosi telepatijom; prenosi se tekstom.

Princip već poznaješ iz gradnje proizvoda: CLAUDE.md je fajl koji se učitava na početku svake Claude Code sesije i daje agentu trajni kontekst o projektu. Brandbook je isti obrazac primenjen na marketing — folder fajlova koji svaka rutina, svaki agent i svaki prompt čita PRE nego što napiše ijednu reč u tvoje ime. Nije PDF za investitore. To je izvršna specifikacija brenda.

Praktična posledica: brandbook živi u repou, pored koda, kao `brandbook/` folder. Za v1 ga slobodno napravi u repou svog proizvoda; u Poglavlju 12 folder se seli (kopijom ili kao git submodule) u zasebni `marketing-os/` repo — putanja u promptovima je uvek `brandbook/`. Tamo svaka cron rutina počinje instrukcijom "pročitaj sve fajlove iz brandbook/ pre rada".

### Sedam fajlova

| Fajl | Svrha | Pitanje na koje odgovara |
|---|---|---|
| `01-identitet.md` | Ko smo | Kako brend "misli"? |
| `02-icp.md` | Za koga | Kome se obraćamo, a kome NE? |
| `03-pozicioniranje.md` | Šta tvrdimo | Koju poruku ponavljamo i čime je dokazujemo? |
| `04-glas-i-ton.md` | Kako zvučimo | Kako se ta poruka izgovara, po kanalu? |
| `05-zabranjeno.md` | Crvene linije | Šta se NIKAD ne kaže? |
| `06-zlatni-primeri.md` | Few-shot biblioteka | Kako izgleda "odlično" kod nas? |
| `07-vizuelni-standardi.md` | Kako izgledamo | Koji su naši distinctive assets? |

Primeri ispod koriste izmišljeni SaaS "Reportly" (automatski klijentski izveštaji za male agencije).

**01-identitet.md — misija, vrednosti, ličnost**

Sadrži misiju u jednoj rečenici, 3-5 vrednosti i ličnost brenda u 5 prideva. Ključno: svaki pridev MORA imati objašnjenje šta znači u praksi — sam pridev je beskoristan agentu ("profesionalan" za banku i za skejt brend znači suprotno).

```markdown
## Ličnost brenda (5 prideva)
1. Direktan — prva rečenica nosi poentu. Bez zagrevanja, bez "u današnjem svetu".
2. Konkretan — svaka tvrdnja ima broj, primer ili korak. "Štedi vreme" je zabranjeno; "izveštaj za 4 minuta umesto 3 sata" je dozvoljeno.
3. Smiren — ne vičemo. Nula uzvičnika u naslovima, maksimum jedan po tekstu.
4. Duhovit na svoj račun — šala ide na naš trošak ili na trošak problema, nikad na trošak korisnika ili konkurenta.
5. Tehnički pismen — ne pojednostavljujemo do netačnosti. Čitalac je pametan, samo nema vremena.
```

**02-icp.md — ko jeste i ko nije kupac**

Destilat ICP-a iz Poglavlja 2: segment, bolovi, rečnik kojim kupac sam opisuje problem (citati iz pravih razgovora), i — jednako važno — eksplicitna lista ko NIJE kupac. Anti-ICP sprečava agenta da širi poruku na publiku koja nikad neće platiti.

```markdown
## NIJE naš kupac
- Freelancer sa 1-2 klijenta (izveštaj mu ne treba — rešava ga mejlom)
- Enterprise agencija 50+ ljudi (traži SSO, procurement, custom ugovore — nemamo)
- Bilo ko kome je glavna želja "white-label dashboard" — to ne gradimo (vidi 05-zabranjeno.md)
```

**03-pozicioniranje.md — izjava, stubovi, dokazi**

Poziciona izjava (Dunford format iz Poglavlja 2) plus tačno 3 stuba poruke. Svaki stub nosi tvrdnju i dokaze: brojku iz proizvoda, citat korisnika, demo link. Agent bez dokaza izmišlja — ovaj fajl mu daje municiju da ne mora.

```markdown
## Stub 2: Brzina do prvog izveštaja
Tvrdnja: prvi izveštaj pre nego što popiješ kafu.
Dokazi:
- medijan TTV novih naloga: 6 min (naša analitika, ažurirano 2026-05)
- citat: "Poslao sam klijentu izveštaj 10 minuta posle registracije." — Marko, osnivač agencije X
- demo snimak: /assets/demo-first-report.mp4
```

**04-glas-i-ton.md — najvažniji fajl**

Pravila glasa (rečenice kratke, aktivan rod, brojevi umesto prideva...) plus ono što stvarno radi: ❌/✅ parovi primera PO KANALU, minimum 3 para po kanalu. Agenti uče iz primera neuporedivo bolje nego iz opisa — par "loše → dobro" je najgušći format prenosa ukusa koji postoji. Isti sadržaj zvuči različito na LinkedInu, u emailu i u in-app poruci, zato parovi idu po kanalu.

```markdown
## LinkedIn
❌ "Uzbuđeni smo što najavljujemo revolucionarnu novu funkciju! 🚀"
✅ "Klijent te pita 'šta ste radili ovog meseca?' u 16:55 petkom. Od danas: izveštaj u 3 klika."

❌ "Reportly je sveobuhvatno rešenje za reporting potrebe modernih agencija."
✅ "Pregledali smo 40 agencijskih izveštaja. 31 je imao copy-paste grafikon iz prošlog meseca. Evo zašto se to dešava."

❌ "Ne propustite naš webinar! Prijavite se odmah!"
✅ "U četvrtak pokazujem kako tri agencije rade mesečne izveštaje za pod 15 minuta. Snimak šaljem svima koji se prijave."

## Email (lifecycle)
❌ Subject: "Newsletter #14 — novosti iz Reportly-ja"
✅ Subject: "Tvoj prvi izveštaj čeka na 80%"
(...minimum 3 para i ovde, pa za svaki sledeći kanal koji koristiš)
```

**05-zabranjeno.md — crvene linije**

Četiri liste: teme koje se ne diraju (politika, tuđi neuspesi...), fraze koje se ne koriste (tvoja lista klišea: "game-changer", "revolucionarno", "uzbuđeni smo"...), obećanja koja se ne daju (roadmap datumi, "nikad nećemo poskupeti", rezultati koje proizvod ne garantuje) i pravila o konkurenciji: konkurenta pominjemo samo činjenično i proverivo, nikad podrugljivo, nikad nagađanjem o njihovim manama. Ovo je fajl koji agent čita kao hard constraint — sve ostalo je stil, ovo je zakon.

```markdown
## Zabranjene fraze
- "game-changer"
- "uzbuđeni smo što najavljujemo"
- "revolucionarno" (i srodno: "disruptivno", "next-level")

## Obećanja koja se ne daju
- datumi sa roadmape ("stiže u junu")
- "nikad nećemo poskupeti"
```

**06-zlatni-primeri.md — few-shot biblioteka**

Deset najboljih komada marketinga koje si ikad napravio — objave, mejlovi, landing sekcije — svaki sa jednom rečenicom ZAŠTO je dobar ("ovaj mejl je imao najviše odgovora jer postavlja jedno konkretno pitanje"). Ovo je few-shot biblioteka: agent imitira ono što vidi, pa mu pokaži najbolje. Fajl raste — svaki novi komad koji prebaci prosek ulazi unutra, najslabiji ispada. Deset je plafon: više primera razvodnjava signal.

```markdown
## Primer 3 — email, najviše odgovora do sada
Subject: "Jedno pitanje pre nego što obrišeš nalog"
Telo: "Vidim da nisi napravio nijedan izveštaj. Šta te je zaustavilo?
Odgovori u jednoj rečenici — čitam svaki mejl."
ZAŠTO: postavlja jedno konkretno pitanje i ništa ne prodaje.
```

**07-vizuelni-standardi.md — distinctive assets**

Tekstualni zapis vizuelnog identiteta iz Poglavlja 8: hex kodovi boja i kada se koja koristi, fontovi po hijerarhiji, pravila slika (npr. "screenshot proizvoda uvek u tamnom modu, bez mockup okvira"), logo pravila i šta se NE radi (gradijenti, stock fotografije ljudi koji se rukuju). I generativni alati za slike primaju tekstualne instrukcije — ovaj fajl je njihov prompt-prefiks.

### Test brandbooka

Brandbook nije gotov kad je napisan, nego kad prođe test:

1. Otvori svežu agentsku sesiju koja NIKAD nije videla tvoj marketing (bez istorije, bez memorije). Praktično: iskopiraj `brandbook/` u prazan folder van projekta i pokreni novu sesiju tamo, ili koristi `claude -p` sa eksplicitnim nalogom da čita samo `brandbook/` — sesija u tvom repou bi povukla CLAUDE.md i memoriju, pa test ne bi bio slep.
2. Daj joj samo `brandbook/` folder i zadatak: "Napiši 3 objave za [kanal] o [funkciji X], strogo po brandbooku."
3. Pročitaj rezultat sa jednim pitanjem: da li bih OVO potpisao i objavio bez izmena?

Ako ne bi — brandbook je rupav, ne agent. Svaka ispravka koju napraviš je dijagnoza: ispravio si uzvičnik → pravilo o uzvičnicima nije dovoljno jasno; ispravio si frazu → ona ide u `05-zabranjeno.md`; prepisao si celu rečenicu → original i tvoja verzija postaju novi ❌/✅ par u `04-glas-i-ton.md`. Ponavljaj ciklus dok dve od tri objave ne prolaze bez izmena. Tako brandbook uči — isto kao što CLAUDE.md raste sa svakom lekcijom iz koda.

### Verzionisanje: brandbook je živ dokument

Brandbook se menja — pozicioniranje se izoštrava, ICP se sužava, glas sazreva. Zato živi u gitu:

- Svaka izmena je commit sa porukom koja objašnjava ZAŠTO ("zabranjena fraza 'AI-powered' — 3 korisnika u intervjuima rekla da zvuči prazno").
- `git log brandbook/` postaje istorija odluka o brendu — novi saradnik (ljudski ili mašinski) može da pročita ne samo pravila nego i njihovo poreklo.
- Veće zaokrete (novo pozicioniranje) radi kroz granu i pregledaj diff pre merge-a, kao i svaki kod.

### Primena odmah

Napravi `brandbook/` folder u repou svog proizvoda i napiši v1 svih 7 fajlova — makar po pola strane svaki. Ne čekaj savršenstvo: pola strane pravila bolje je od nule. Redosled: kreni od `04-glas-i-ton.md` (uzmi 3 svoja stara teksta koja voliš i 3 koja ne voliš — to su ti prvi ❌/✅ parovi), pa `02-icp.md` i `03-pozicioniranje.md` (destiluj iz rada u Poglavlju 2), ostalo popuni za njima. Zatim sprovedi test: sveža sesija + brandbook + zadatak "3 objave". Svaku ispravku vrati u fajlove i commituj. Deliverable: `brandbook/` folder sa 7 fajlova u gitu + 3 test objave + bar 3 nova pravila/para nastala iz testa.

### Najčešće greške

1. **Pridevi bez operacionalizacije.** "Prijateljski, profesionalan, inovativan" ne znači ništa mašini (ni čoveku). Rešenje: svaki pridev dobija rečenicu "u praksi to znači..." i bar jedan ❌/✅ par.
2. **Brandbook kao PDF artefakt.** Napisan jednom, otvoren nikad. Rešenje: markdown u repou, učitava se u svaku sesiju, menja se commitom — dokument koji se ne čita mašinski ne postoji za agente.
3. **Samo pozitivna pravila, bez zabrana.** Agent popunjava praznine generičkim SaaS govorom. Rešenje: `05-zabranjeno.md` sa konkretnom listom fraza — zabrane su izvršivije od preporuka.
4. **Preskočen test.** Brandbook proglašen gotovim bez provere na slepo. Rešenje: test sa 3 objave pre nego što ijedna rutina iz Poglavlja 12 krene da radi.
5. **Mrtva few-shot biblioteka.** `06-zlatni-primeri.md` napunjen jednom i zaboravljen, pa agent imitira tebe od pre godinu dana. Rešenje: mesečni ritual (uklopi ga u nedeljni pregled iz Poglavlja 10) — najbolji novi komad ulazi, najslabiji izlazi.

### Kontrolna lista

- [ ] `brandbook/` folder postoji u repou i pod gitom je
- [ ] Svih 7 fajlova napisano, minimum pola strane po fajlu
- [ ] Svaki od 5 prideva ličnosti ima objašnjenje "šta to znači u praksi"
- [ ] `02-icp.md` sadrži eksplicitnu "NIJE naš kupac" listu
- [ ] Svaki stub poruke u `03-pozicioniranje.md` ima bar 2 dokaza
- [ ] `04-glas-i-ton.md` ima minimum 3 ❌/✅ para za svaki kanal koji koristiš
- [ ] `05-zabranjeno.md` pokriva: teme, fraze, obećanja, govor o konkurenciji
- [ ] `06-zlatni-primeri.md` ima do 10 primera, svaki sa "zašto je dobar"
- [ ] Test sproveden: sveža sesija + brandbook + 3 objave
- [ ] Bar 2 od 3 test objave prolaze bez izmena (ili je iteracija u toku)
- [ ] Svaka ispravka iz testa vraćena u brandbook kao pravilo ili ❌/✅ par
- [ ] Commit poruke objašnjavaju ZAŠTO se pravilo menja
