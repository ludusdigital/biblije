# Marketing Biblija za SaaS — od prvog korisnika do autonomnog marketinškog OS-a

## Uvod: marketing kao softver

### Šta ćeš naučiti

- Zašto se marketing danas gradi kao softver — sistem sa petljama, eksperimentima i automatizacijom, a ne niz kampanja
- Tri principa koja drže svako poglavlje ovog dokumenta i svaku odluku koju ćeš doneti
- Kako je dokument organizovan u tri dela i kojim redom da ga čitaš za svoju fazu
- Gde se ovaj dokument uklapa pored CLAUDE-CODE-BIBLIJE: jedan gradi proizvod, drugi ga prodaje

### Kome je ovo namenjeno

Ti si osnivač ili graditelj SaaS i digitalnih proizvoda. Proizvod praviš sam ili sa malim timom — verovatno uz Claude Code, po obrascima iz CLAUDE-CODE-BIBLIJE.md u ovom istom folderu. Nemaš marketinški tim. Nemaš budžet za agenciju. Imaš nešto vrednije: tehničku sposobnost da postaviš repo, fajlove i zakazane agente — i to je tačno ono što ovaj dokument pretvara u marketinšku prednost.

Ovo nije knjiga inspiracije. Ovo je operativni priručnik: svaki savet ima korak, alat, šablon ili primer. Ako negde piše brojka, ona dolazi iz javno citiranih izvora i nosi etiketu pouzdanosti — orijentir industrije, široko citirano, industrijska procena. Tamo gde pouzdanog podatka nema, nećeš dobiti izmišljeni procenat.

### Centralna teza: marketing kao softver

Većina osnivača marketing radi kao seriju nasumičnih događaja: objava kad se setiš, kampanja kad panika pritisne, launch jednom pa tišina. Rezultat je predvidiv — nula složenog efekta, jer se ništa ne meri, ništa ne ponavlja i ništa ne gradi na prethodnom.

Marketing koji radi izgleda kao softver koji ti već pišeš:

| Softver | Marketing kao softver |
|---|---|
| Funkcije i moduli | Growth petlje i kanali (Deo II) |
| Testovi | Eksperimenti sa unapred zapisanom hipotezom i metrikom odluke (Poglavlje 10) |
| Monitoring i metrike | Kontrolna tabla: CAC, LTV, churn, NRR (Poglavlje 1) |
| Dokumentacija i konfiguracija | Brandbook kao mašinski čitljiv ustav brenda (Poglavlje 11) |
| CI/CD i cron poslovi | Autonomni marketinški OS: rutine, kapije, kill-switch (Poglavlje 12) |

Krajnji cilj dokumenta je Deo III — marketinški operativni sistem koji radi sam: zakazani agenti pišu, analiziraju i predlažu, brandbook im je ustav, a ti si završna kapija koja odobrava. Ali do njega se ne preskače. Automatizovati možeš samo proces koji si bar jednom uspešno odradio ručno — automatizacija lošeg procesa samo brže proizvodi loš rezultat. Zato Deo I postavlja temelje, Deo II te tera da bar jedan motor rasta pokreneš rukama, i tek onda Deo III te procese pretvara u sistem.

### Tri principa koja drže ceo dokument

**1. Retencija pre akvizicije.** Akvizicija u proizvod koji curi je sipanje vode u bure bez dna: svaki novi korisnik koga dovedeš i izgubiš košta te CAC, a vraća skoro ništa. Obrnuto, poboljšanje retencije deluje složeno (compounding) na sve ostale metrike — duži životni vek korisnika diže LTV, LTV podnosi veći CAC, veći CAC otvara kanale koji su konkurentima preskupi. Zato pre ijednog dinara u oglase ide pitanje: da li korisnici koji probaju proizvod ostaju? Formula i orijentiri u Poglavlju 1, aktivacija i time-to-value u Poglavlju 3.

**2. U AI eri sadržaj je komodifikovan — moat su distribucija, brend, originalni podaci i ukus.** AI je prosečan tekst učinio besplatnim, pa generički blog bez ugla i podataka više ne donosi ništa — platforme i čitaoci ga ignorišu. Analize pokazuju da otprilike ~60% Google pretraga završi bez klika na rezultat (SparkToro/Similarweb analize, približno), a AI pregledi dodatno obaraju klikove na informativne upite. Vrednost se preselila u ono što se ne može generisati na zahtev: kanale koje poseduješ (email lista, zajednica), brend koga se ljudi sete, podatke i istraživanja koje samo ti imaš, i ukus da prepoznaš šta je dobro. Ceo Deo II je izgrađen na ovoj realnosti — posebno Poglavlja 5, 7 i 8.

**3. Što se ne meri, ne postoji.** Objavljeni nalazi o eksperimentima u Microsoftu (Kohavi) su otrežnjujući: otprilike trećina eksperimenata poboljša metrike, trećina nema efekta, a trećina ih pogorša. Tvoja intuicija ti, dakle, u dve trećine slučajeva ili ne pomaže ili aktivno šteti — i bez merenja ne znaš ni u kojoj si trećini. Zato svaka aktivnost u ovom dokumentu ima metriku, svaki eksperiment unapred zapisanu hipotezu, a ceo sistem kontrolnu tablu (Poglavlje 1) i eksperimentalni pogon (Poglavlje 10).

### Mapa dokumenta

| Deo | Poglavlje | Tema |
|---|---|---|
| **I — TEMELJI** | 1. Ekonomija SaaS-a | CAC, LTV, churn, NRR, Rule of 40, north star, kontrolna tabla |
| | 2. Pozicioniranje i poruka | ICP, JTBD, Dunford metod, anatomija landing stranice |
| **II — MOTORI RASTA** | 3. Proizvod kao marketing | Aha-momenat, TTV, onboarding, freemium vs trial, PQL |
| | 4. Growth petlje | 4 tipa petlji sa studijama slučaja |
| | 5. Organski rast u AI eri | AEO/GEO, programmatic SEO, founder-led, community, dark social |
| | 6. Plaćena akvizicija | Kada ima smisla, paid kao laboratorija poruka |
| | 7. Email i lifecycle | Najveći ROI kanal, aktivacione sekvence |
| | 8. Brend | 95-5 pravilo, distinctive assets, social proof |
| | 9. Lansiranja i momentum | Waitlist → beta → launch → feature ritam |
| **III — SISTEM** | 10. Eksperimentalni pogon | ICE prioritizacija, nedeljni ritam, analytics minimum |
| | 11. Brandbook kao algoritam | Mašinski čitljiv ustav brenda (7 fajlova) |
| | 12. Autonomni marketinški OS | Arhitektura, repo, cron rutine, kapije, kill-switch |
| | 13. Plan uvođenja | Ručno → asistirano → autonomno za 12 nedelja |
| **DODACI** | 14. Dodaci | Rečnik i formule, šabloni, marketinški kalendar prve godine |

### Kako koristiti ovaj dokument

**Deo I — odmah i ceo.** Bez metrika ne znaš da li bilo šta radi; bez pozicioniranja ne znaš šta da kažeš. Ova dva poglavlja su preduslov za sve ostalo, bez obzira na proizvod i fazu.

**Deo II — biraj motore, ne čitaj kao roman.** Nijedan proizvod ne vozi svih sedam motora odjednom. Solo osnivač sa B2B alatom verovatno kreće od Poglavlja 3 (proizvod), 5 (organski) i 7 (email); proizvod sa prirodnom viralnošću od Poglavlja 4; proizvod pred lansiranjem od Poglavlja 9. Pročitaj uvodne sekcije svih poglavlja, pa duboko uđi u dva-tri koja odgovaraju tvom proizvodu i fazi.

**Deo III — tek kad bar jedan kanal radi ručno.** Pravilo je strogo namerno: OS automatizuje procese koje si dokazao rukama. Ako još nemaš kanal koji ručno donosi merljive rezultate, Deo III ti je mapa budućnosti, ne zadatak za ovu nedelju. Poglavlje 13 daje tačan 12-nedeljni put: ručno → asistirano → autonomno.

### Veza sa ostalim dokumentima u docs/

Ovaj dokument zatvara krug koji su otvorila prethodna dva:

- **CLAUDE-CODE-BIBLIJA.md** — kako se proizvod GRADI sa Claude Code-om: repo, agenti, obrasci razvoja.
- **TOP-5-EDUKATOR.md** — coaching sloj za edukatora.
- **Marketing Biblija (ovaj dokument)** — kako se proizvod PRODAJE i RASTE, i kako se marketing pretvara u sistem koji radi sam: brandbook kao ustav, rutine kao radnici, ti kao završna kapija.

Isti princip koji ti je izgradio proizvod — fajlovi kao izvor istine, agenti kao izvršioci, ti kao arhitekta — sada gradi i njegov rast. Kreni od Poglavlja 1.
