# Marketing Biblija za SaaS: od prvog korisnika do autonomnog marketinškog OS-a

## Uvod: marketing kao softver

### Šta ćeš naučiti

- Zašto se marketing danas gradi kao softver, sistem sa petljama, eksperimentima i automatizacijom, a ne niz kampanja
- Tri principa koja drže svako poglavlje ovog dokumenta i svaku odluku koju ćeš doneti
- Kako je dokument organizovan u tri dela i kojim redom da ga čitaš za svoju fazu
- Gde se ovaj dokument uklapa pored CLAUDE-CODE-BIBLIJE: jedan gradi proizvod, drugi ga prodaje

### Kome je ovo namenjeno

Ti si osnivač ili graditelj SaaS i digitalnih proizvoda. Proizvod praviš sam ili sa malim timom, verovatno uz Claude Code, po obrascima iz CLAUDE-CODE-BIBLIJE.md u ovom istom folderu. Nemaš marketinški tim. Nemaš budžet za agenciju. Imaš nešto vrednije: tehničku sposobnost da postaviš repozitorijum, fajlove i zakazane agente, i to je tačno ono što ovaj dokument pretvara u marketinšku prednost.

Ovo nije knjiga inspiracije. Ovo je operativni priručnik: svaki savet ima korak, alat, šablon ili primer. Ako negde piše brojka, ona dolazi iz javno citiranih izvora i nosi etiketu pouzdanosti, orijentir industrije, široko citirano, industrijska procena. Tamo gde pouzdanog podatka nema, nećeš dobiti izmišljeni procenat.

### Centralna teza: marketing kao softver

Većina osnivača marketing radi kao seriju nasumičnih događaja: objava kad se setiš, kampanja kad panika pritisne, lansiranje jednom pa tišina. Rezultat je predvidiv, nula složenog efekta, jer se ništa ne meri, ništa ne ponavlja i ništa ne gradi na prethodnom.

Marketing koji radi izgleda kao softver koji ti već pišeš:

| Softver | Marketing kao softver |
|---|---|
| Funkcije i moduli | Rast petlje i kanali (Deo II) |
| Testovi | Eksperimenti sa unapred zapisanom hipotezom i metrikom odluke (Poglavlje 10) |
| Monitoring i metrike | Kontrolna tabla: CAC, LTV, odlasci kupaca, NRR (Poglavlje 1) |
| Dokumentacija i konfiguracija | Brend priručnik kao mašinski čitljiv ustav brenda (Poglavlje 11) |
| CI/CD i cron poslovi | Autonomni marketinški OS: rutine, kapije, sigurnosni prekidač (Poglavlje 12) |

Krajnji cilj dokumenta je Deo III, marketinški operativni sistem koji radi sam: zakazani agenti pišu, analiziraju i predlažu, brend priručnik im je ustav, a ti si završna kapija koja odobrava. Ali do njega se ne preskače. Automatizovati možeš samo proces koji si bar jednom uspešno odradio ručno, automatizacija lošeg procesa samo brže proizvodi loš rezultat. Zato Deo I postavlja temelje, Deo II te tera da bar jedan motor rasta pokreneš rukama, i tek onda Deo III te procese pretvara u sistem.

### Tri principa koja drže ceo dokument

**1. Zadržavanje korisnika pre akvizicije.** Akvizicija u proizvod koji curi je sipanje vode u bure bez dna: svaki novi korisnik koga dovedeš i izgubiš košta te CAC, a vraća skoro ništa. Obrnuto, poboljšanje retencije deluje složeno (compounding) na sve ostale metrike, duži životni vek korisnika diže LTV, LTV podnosi veći CAC, veći CAC otvara kanale koji su konkurentima preskupi. Zato pre ijednog dinara u oglase ide pitanje: da li korisnici koji probaju proizvod ostaju? Formula i orijentiri u Poglavlju 1, aktivacija i time-to-value u Poglavlju 3.

**2. U AI eri sadržaj je komodifikovan, odbrambene prednosti koje konkurencija teško kopira su distribucija, brend, originalni podaci i ukus.** AI je prosečan tekst učinio besplatnim, pa generički blog bez ugla i podataka više ne donosi ništa, platforme i čitaoci ga ignorišu. Analize pokazuju da otprilike ~60% Google pretraga završi bez klika na rezultat (SparkToro/Similarweb analize, približno), a AI pregledi dodatno obaraju klikove na informativne upite. Vrednost se preselila u ono što se ne može generisati na zahtev: kanale koje poseduješ (lista imejl adresa, zajednica), brend koga se ljudi sete, podatke i istraživanja koje samo ti imaš, i ukus da prepoznaš šta je dobro. Ceo Deo II je izgrađen na ovoj realnosti, posebno Poglavlja 5, 7 i 8.

**3. Što se ne meri, ne postoji.** Objavljeni nalazi o eksperimentima u Microsoftu (Kohavi) su otrežnjujući: otprilike trećina eksperimenata poboljša metrike, trećina nema efekta, a trećina ih pogorša. Tvoja intuicija ti, dakle, u dve trećine slučajeva ili ne pomaže ili aktivno šteti, i bez merenja ne znaš ni u kojoj si trećini. Zato svaka aktivnost u ovom dokumentu ima metriku, svaki eksperiment unapred zapisanu hipotezu, a ceo sistem kontrolnu tablu (Poglavlje 1) i eksperimentalni pogon (Poglavlje 10).

### Mapa dokumenta

| Deo | Poglavlje | Tema |
|---|---|---|
| **I, TEMELJI** | 1. Ekonomija SaaS-a | CAC, LTV, odlasci kupaca, NRR, Rule of 40, glavna metrika, kontrolna tabla |
| | 2. Pozicioniranje i poruka | ICP, JTBD, Dunford metod, anatomija prodajne stranice |
| **II, MOTORI RASTA** | 3. Proizvod kao marketing | Aha-momenat, TTV, uvođenje korisnika, freemium vs probni period, PQL |
| | 4. Rast petlje | 4 tipa petlji sa studijama slučaja |
| | 5. Organski rast u AI eri | AEO/GEO, programski generisane SEO, vođeno lično od osnivača, zajednica, nevidljive preporuke |
| | 6. Plaćena akvizicija | Kada ima smisla, plaćeno oglašavanje kao laboratorija poruka |
| | 7. Imejl i životni ciklus korisnika | Najveći ROI kanal, aktivacione sekvence |
| | 8. Brend | 95-5 pravilo, prepoznatljivi elementi brenda, društveni dokaz |
| | 9. Lansiranja i momentum | Lista čekanja → beta → lansiranje → ritam funkcionalnosti |
| **III, SISTEM** | 10. Eksperimentalni pogon | ICE prioritizacija, nedeljni ritam, minimum analitike |
| | 11. Brend priručnik kao algoritam | Mašinski čitljiv ustav brenda (7 fajlova) |
| | 12. Autonomni marketinški OS | Arhitektura, repozitorijum, zakazane rutine (cron), kapije, sigurnosni prekidač |
| | 13. Plan uvođenja | Ručno → asistirano → autonomno za 12 nedelja |
| **DODACI** | 14. Dodaci | Rečnik i formule, šabloni, marketinški kalendar prve godine |

### Kako koristiti ovaj dokument

**Deo I, odmah i ceo.** Bez metrika ne znaš da li bilo šta radi; bez pozicioniranja ne znaš šta da kažeš. Ova dva poglavlja su preduslov za sve ostalo, bez obzira na proizvod i fazu.

**Deo II, biraj motore, ne čitaj kao roman.** Nijedan proizvod ne vozi svih sedam motora odjednom. Solo osnivač sa B2B alatom verovatno kreće od Poglavlja 3 (proizvod), 5 (organski) i 7 (imejl); proizvod sa prirodnom viralnošću od Poglavlja 4; proizvod pred lansiranjem od Poglavlja 9. Pročitaj uvodne sekcije svih poglavlja, pa duboko uđi u dva-tri koja odgovaraju tvom proizvodu i fazi.

**Deo III, tek kad bar jedan kanal radi ručno.** Pravilo je strogo namerno: OS automatizuje procese koje si dokazao rukama. Ako još nemaš kanal koji ručno donosi merljive rezultate, Deo III ti je mapa budućnosti, ne zadatak za ovu nedelju. Poglavlje 13 daje tačan 12-nedeljni put: ručno → asistirano → autonomno.

### Veza sa ostalim dokumentima u docs/

Ovaj dokument zatvara krug koji su otvorila prethodna dva:

- **CLAUDE-CODE-BIBLIJA.md**, kako se proizvod GRADI sa Claude Code-om: repozitorijum, agenti, obrasci razvoja.
- **TOP-5-EDUKATOR.md**, mentorski sloj za edukatora.
- **Marketing Biblija (ovaj dokument)**, kako se proizvod PRODAJE i RASTE, i kako se marketing pretvara u sistem koji radi sam: brend priručnik kao ustav, rutine kao radnici, ti kao završna kapija.

Isti princip koji ti je izgradio proizvod, fajlovi kao izvor istine, agenti kao izvršioci, ti kao arhitekta, sada gradi i njegov rast. Kreni od Poglavlja 1.


---

## Poglavlje 1: Ekonomija SaaS-a: metrike koje sve pokreću

Marketing bez metrika je trošenje para uz dobar osećaj. Pre nego što napišeš ijednu objavu ili pustiš ijedan oglas, moraš znati koliko te kupac košta, koliko vredi i da li ti biznis curi. Ovo poglavlje je rečnik i kontrolna tabla na koju se oslanja ostatak knjige, svaki kasniji kanal i petlja meri se brojkama odavde.

### Šta ćeš naučiti

- Definiciju, formulu i orijentir za svaku ključnu SaaS metriku, i koju odluku svaka od njih informiše
- Zašto je LTV:CAC ≥ 3:1 i period povrata CAC-a < 12 meseci minimum za zdrav biznis
- Kako da izabereš glavnu metriku (i kako da ne izabereš pogrešnu)
- Zašto je cenovnik najpotcenjenija poluga rasta, jača od akvizicije
- Kako da sastaviš sopstvenu kontrolnu tablu od 8 brojeva

### Prihod: MRR i ARR

**Definicija:** MRR (monthly recurring revenue) je mesečni ponavljajući prihod, zbir svih aktivnih pretplata svedenih na mesec. ARR = MRR × 12.

**Formula:** zbir mesečnih pretplata + (godišnje pretplate / 12). Jednokratne naplate NE ulaze.

**Odluka koju informiše:** da li rasteš i kojim tempom. MRR je puls biznisa, gledaš ga nedeljno, ne kvartalno.

### CAC: koliko te košta kupac

**Definicija:** CAC (customer acquisition cost) je prosečan trošak da dovedeš jednog kupca koji plaća.

**Formula:** CAC = ukupni troškovi prodaje i marketinga u periodu / broj novih kupaca u tom periodu. Solo osnivaču: uračunaj i vrednost svog vremena, inače se lažeš.

**Odluka:** koje kanale smeš da skaliraš. Kanal čiji CAC ne podnosi tvoj LTV se gasi ili ostaje laboratorija (detaljno u Poglavlju 6).

### LTV: koliko kupac vredi

**Definicija:** LTV (lifetime value) je ukupan profit koji prosečan kupac donese dok ne ode.

**Formula:** LTV ≈ prosečan mesečni prihod po nalogu × bruto marža / mesečna stopa odlazaka kupaca.

**Odluka:** gornja granica koliko smeš da platiš akviziciju. Bez LTV-a svaki budžet je nagađanje.

### LTV:CAC i period povrata CAC-a

**LTV:CAC ≥ 3:1**, orijentir industrije za zdrav SaaS. Ispod 3:1 trošiš previše na rast; znatno viši odnos može značiti da ima prostora da investiraš agresivnije.

**Period povrata CAC-a < 12 meseci**, orijentir za ranu fazu: za koliko meseci bruto marža od kupca vrati trošak njegove akvizicije. Formula: CAC / (mesečni prihod po kupcu × bruto marža).

**Odluka:** period povrata ti govori koliko ti je gotovine vezano u rastu. Solo osnivač bez investitora cilja što kraći period povrata, ti finansiraš sopstveni rast.

### Odlasci kupaca: rupa u buretu

**Definicija:** odlasci kupaca je procenat kupaca (ili prihoda) koji odu u periodu.

**Formula:** izgubljeni kupci u mesecu / kupci na početku meseca.

**Orijentiri** (industrijski preseci, jako variraju po segmentu):

| Segment | Tipičan odlasci kupaca |
|---|---|
| SMB SaaS | 3–7% mesečno |
| Mid-market | 1–2% mesečno |
| Enterprise | 5–10% godišnje |

**Odluka:** da li uopšte smeš da ulažeš u akviziciju. Akvizicija u proizvod koji curi je sipanje vode u bure bez dna, zadržavanje korisnika deluje složeno (compounding) na sve ostale metrike, pa popravka odlazaka kupaca pre skaliranja akvizicije nije opcija nego redosled.

### NRR: rast bez ijednog novog kupca

**Definicija:** NRR (net revenue zadržavanje) meri šta se dešava sa prihodom od postojećih kupaca: zadržavanje + nadogradnje − otkazi i smanjenja.

**Formula:** MRR od kohorte kupaca danas / MRR iste kohorte pre 12 meseci × 100.

**Orijentir:** NRR > 100% znači da postojeći kupci rastu brže nego što odlaze; najbolje javne SaaS kompanije tipično drže 110–130%.

**Odluka:** da li ti model ima ekspanziju (više sedišta, viši tier, usage). Ako je NRR strukturno ispod 100%, problem je u proizvodu ili cenovnik paketima, ne u marketingu.

### Rule of 40

**Definicija:** zbir stope rasta i profitne margine.

**Formula:** rast prihoda % + profitna margina % ≥ 40, standard zdravlja SaaS biznisa.

**Odluka:** balans rasta i održivosti. Ako rasteš 60% uz −30% marže, zbir 30 kaže: rast te košta previše.

### Aktivacija i TTV: samo definicija

**Aktivacija** je trenutak kad korisnik prvi put doživi stvarnu vrednost (aha-momenat). **TTV** (time-to-value) je vreme od registracije do tog trenutka, što kraće, to bolja aktivacija. Kako se aha-momenat nalazi i TTV skraćuje, detaljno u Poglavlju 3.

### Konverzioni rasponi: šta je "normalno"

Industrijski rasponi iz anketa OpenView / Lenny's Bilten:

| Model | Tipična konverzija u plaćeno |
|---|---|
| Freemium | 2–5% |
| Probni period bez kartice | ~8–12% |
| Probni period sa obaveznom karticom | 40%+ (ali drastično manje prijava) |

**Odluka:** izbor modela je razmena između širine vrha levka i kvaliteta dna, kartica unapred filtrira ozbiljne, freemium maksimizuje domet (puna analiza u Poglavlju 3).

### Prva metrika mladog proizvoda: Sean Ellis 40% test

Pre nego što meriš išta od gornjeg, izmeri usklađenost proizvoda i tržišta. Sean Ellis PMF test: pitaj aktivne korisnike "Kako biste se osećali da proizvod sutra nestane?" Ako bar 40% kaže **veoma razočarano** → signal usklađenosti proizvoda i tržišta. Ispod toga, marketing budžet je benzin u auto bez točkova, vrati se na proizvod i razgovore sa korisnicima.

```
Anketa (1 pitanje, alat: bilo koji form):
"Kako biste se osećali kada više ne biste mogli da koristite [proizvod]?"
( ) Veoma razočarano
( ) Donekle razočarano
( ) Ne bih bio/la razočaran/a
+ opciono: "Šta je glavna korist koju dobijate od proizvoda?"
```

### glavna metrika: jedan broj koji vodi sve

glavna metrika (koncept Sean Ellis / Amplitude) je jedna metrika koja spaja vrednost za korisnika i rast biznisa. Test izbora: ako ovaj broj raste, da li korisnici sigurno dobijaju više vrednosti I da li biznis sigurno raste? Oba uslova ili nije glavna metrika.

❌ "Broj registracija", raste i kad svi odu posle prvog dana; meri tvoj marketing, ne vrednost.
✅ "Broj korisnika koji su nedeljno aktivni i uradili ključnu akciju" (npr. nedeljno aktivni timovi koji su izvezli projekat), ne može da raste ako proizvod ne isporučuje vrednost.

Kako se bira: (1) definiši ključnu akciju u kojoj korisnik dobija vrednost, (2) dodaj frekvenciju koja odgovara prirodnoj upotrebi (dnevno/nedeljno/mesečno), (3) proveri da li korelira sa retencijom i prihodom. Sve eksperimente iz Poglavlja 10 meriš naspram nje.

### Pricing: najpotcenjenija poluga

ProfitWell (Patrick Campbell) analize: ulaganje u monetizaciju (cenovnik i pakovanje ponude) ima višestruko veći uticaj na rezultat od istog ulaganja u akviziciju. Logika je prosta, promena cene deluje na 100% kupaca odmah, novi kanal deluje na marginu novih.

Zato cenovnik nije "podesi i zaboravi":

1. **Revizija na kalendaru:** svaka 3 meseca pogledaj cene, pakete i NRR, stavi to u marketinški kalendar (Dodatak C).
2. **Šta tačno revidiraš:** vrednosna metrika (po čemu naplaćuješ, sedišta, upotreba, projekti), granice paketa (šta gura upgrade), nivo cene.
3. **Test:** podizanje cene samo za nove korisnike je najjeftiniji eksperiment sa najvećim dometom, jedna hipoteza, jedna metrika odluke, zapisana unapred (disciplina i Kohavijev nalaz o trećinama, Poglavlje 10), zato se meri, ne veruje.

### Kontrolna tabla osnivača

8 brojeva koje držiš na jednom mestu (tabela je dovoljan; automatizacija u Poglavlju 12):

| # | Metrika | Formula | Gde se meri | Koliko često |
|---|---|---|---|---|
| 1 | MRR | zbir mesečnih pretplata | naplata (Stripe/Paddle) | nedeljno |
| 2 | Novi kupci | broj novih plaćenih naloga | naplata | nedeljno |
| 3 | CAC | troškovi S&M / novi kupci | tabela (troškovi + naplata) | mesečno |
| 4 | Odlasci kupaca | izgubljeni / početni kupci | naplata | mesečno |
| 5 | LTV | prihod × marža / odlasci kupaca | tabela (izvedeno) | mesečno |
| 6 | LTV:CAC | LTV / CAC | tabela (izvedeno) | mesečno |
| 7 | NRR | MRR kohorte danas / pre 12m | naplata + tabela | kvartalno |
| 8 | glavna metrika | tvoja ključna akcija × aktivnost | analitika proizvoda | nedeljno |

### Primena odmah

Napravi fajl `metrike.md` (ili tabelu) sa gornjih 8 redova i upiši SVOJE brojeve za prošli mesec. Pravilo: gde nemaš podatak, upiši doslovno **NE MERIM**, bez ulepšavanja. Kolona sa "NE MERIM" je tvoj prvi spisak budućih zadataka: za svaku stavku zapiši šta ti treba da bi je merio (izveštaj naplate, događaj u analitici, polje u bazi) i rok od 2 nedelje. Rezultat rada: popunjena tabla + lista budućih zadataka. Ovaj fajl postaje deo marketinškog repozitorijuma u Poglavlju 12.

### Najčešće greške

1. **Meriš samo vrh levka** (posete, registracije) jer je lako. Rešenje: glavna metrika + odlasci kupaca pre svega, brojevi koji bole su brojevi koji vode.
2. **CAC bez sopstvenog vremena.** Solo osnivač "nema troškove" pa je CAC magično nula. Rešenje: uračunaj svoje sate po realnoj satnici.
3. **Skaliranje akvizicije pre popravke odlazaka kupaca.** Rešenje: dok je odlasci kupaca iznad orijentira za tvoj segment, budžet ide u retenciju i aktivaciju, ne u oglase.
4. **Pricing postavljen jednom, pre lansiranja, zauvek.** Rešenje: kvartalna revizija iz ovog poglavlja, monetizacija je jača poluga od akvizicije (ProfitWell nalaz).
5. **glavna metrika koja meri tebe, a ne korisnika** ("broj objava", "broj registracija"). Rešenje: test dva uslova, vrednost za korisnika I rast biznisa.

### Kontrolna lista

- [ ] Znam svoj MRR i proveravam ga nedeljno
- [ ] Izračunao sam CAC sa uračunatim sopstvenim vremenom
- [ ] Izračunao sam LTV i odnos LTV:CAC (cilj ≥ 3:1)
- [ ] Znam svoj mesečnu stopu odlazaka kupaca i gde je naspram orijentira za moj segment
- [ ] Sproveo sam Sean Ellis 40% test na aktivnim korisnicima
- [ ] Definisao sam glavnu metriku koja prolazi test dva uslova
- [ ] Kontrolna tabla od 8 metrika postoji kao fajl, sa spiskom stavki "NE MERIM"
- [ ] Kvartalna revizija cenovnika je u kalendaru


---

## Poglavlje 2: Pozicioniranje i poruka: za koga, za šta, naspram čega

### Šta ćeš naučiti

- Kako da definišeš ICP (ideal customer profile, profil idealnog kupca) operativno, uključujući i ko NIJE tvoj kupac
- Kako da JTBD intervjuom otkriješ pravu konkurenciju i okidač kupovine
- Dunford metod pozicioniranja u 5 koraka, pravim redosledom
- Kako da izgradiš messaging hijerarhiju: jedna tvrdnja, tri stuba, dokaz za svaki
- Anatomiju prodajne stranice koja konvertuje i zašto ti treba polje "Kako si čuo/la za nas?"

### Pozicioniranje je odluka, ne slogan

Najbolji proizvod sa nejasnom porukom gubi od prosečnog proizvoda sa jasnom. Pozicioniranje je odluka o kontekstu u kome mozak kupca smešta tvoj proizvod: za koga je, koji posao obavlja i naspram čega se poredi. Sve kanale iz Dela II (PLG, petlje, organski rast, plaćeno oglašavanje) gradićeš NA ovom temelju, ako je temelj mutan, svaki kanal će vraćati mutne rezultate, a metrike iz Poglavlja 1 nećeš umeti da protumačiš.

### ICP: operativna definicija, ne persona sa hobijima

Marketinška persona tipa "Marko, 34, product manager, voli planinarenje" je beskorisna, ne govori ti ništa što možeš da upotrebiš. Operativan ICP ima četiri komponente koje se proveravaju u stvarnosti:

| Komponenta | Pitanje | Primer (SaaS za fakturisanje freelancera) |
|---|---|---|
| Segment | Ko je, merljivo? | Solo freelancer u EU, 5+ klijenata, naplaćuje preko 2 valute |
| Problem | Šta ga boli, njegovim rečima? | "Pola dana mesečno gubim na fakture i jurenje uplata" |
| Okidač kupovine | Koji događaj ga tera da traži rešenje SADA? | Prva zakasnela uplata koju je primetio tek posle 30 dana |
| Pojilo | Gde se ti ljudi okupljaju? | Određeni subreddit, uske Slack/Discord zajednice, dva-tri biltena |

Jednako važno: **anti-ICP**, ko nije kupac. Agencija sa 20 zaposlenih nije kupac alata za solo freelancere, čak i ako se prijavi na probni period: tražiće funkcije koje ne planiraš, otkazaće pretplatu i iskriviti ti podatke. Zapiši anti-ICP eksplicitno, da bi smeo da kažeš "ne".

```
ICP ŠABLON (popuni za svoj proizvod)
Segment:           [merljiv opis, uloga, veličina, alat koji već koriste]
Problem:           [citat, njihovim rečima, iz intervjua ili foruma]
Okidač kupovine:   [konkretan događaj koji pokreće potragu]
Pojilo:            [3-5 mesta gde se okupljaju]
Anti-ICP:          [ko liči na kupca, a nije, i zašto]
```

### JTBD: kupac unajmljuje proizvod za posao

JTBD (jobs-to-be-done) kaže: kupac ne kupuje proizvod, on ga "unajmljuje" da obavi posao, i otpušta prethodno rešenje. Zato je najjače pitanje u intervjuu sa korisnikom:

```
"Šta si koristio pre, i šta te je nateralo da potražiš nešto drugo?"
```

Ovo jedno pitanje otkriva dve stvari koje ne možeš da izmisliš iz glave: **pravu konkurenciju** (često nije drugi SaaS, nego Excel, Google Docs, "platim studenta" ili "ništa, trpim") i **okidač kupovine** (konkretan momenat frustracije). Mini-skripta za 20-minutni intervju:

```
1. Šta si koristio pre i šta te je nateralo da tražiš drugo?
2. Opiši mi poslednji put kad te je taj problem koštao vremena/novca.
3. Šta si sve probao pre nego što si izabrao? Zašto si odbacio ostale?
4. Šta bi radio sutra da naš proizvod nestane?
5. Kako bi opisao proizvod kolegi u jednoj rečenici?
```

Odgovor na pitanje 5 ti često napiše hero naslov bolje nego ti sam. Uradi 5-10 ovakvih razgovora pre nego što pipneš prodajnu stranicu.

### Dunford metod: pozicioniranje u 5 koraka

Metod April Dunford radi zato što ide obrnutim redom od intuicije, kategoriju biraš POSLEDNJU, ne prvu:

1. **Konkurentske alternative**, šta bi kupac stvarno radio da ne postojiš? (uključi "ručno" i "ništa")
2. **Po čemu si jedinstven**, sposobnosti koje alternative dokazivo nemaju
3. **Vrednost**, šta te jedinstvenosti konkretno omogućavaju kupcu (ušteda, brzina, prihod)
4. **Kome je to najvažnije**, segment koji najviše mari za tu vrednost; ovo je tvoj ICP iz prethodnog koraka, sada proveren
5. **Kategorija**, tržišni okvir u kome je tvoja vrednost očigledna bez objašnjavanja

```
POZICIONA IZJAVA (rezultat 5 koraka)
Za [ICP iz koraka 4]
koji [problem + okidač],
[proizvod] je [kategorija iz koraka 5]
koja [vrednost iz koraka 3],
za razliku od [glavna alternativa iz koraka 1]
jer [jedinstvenost iz koraka 2].
```

Ova izjava nije javni tekst, to je interni dokument iz koga se izvodi sav javni tekst.

### Messaging hijerarhija: tvrdnja → stubovi → dokazi

Iz pozicione izjave gradiš hijerarhiju poruke:

```
GLAVNA TVRDNJA (1 rečenica, ishod za kupca)
├── Stub 1: [pod-tvrdnja]  → Dokaz: [brojka iz proizvoda / citat korisnika / demo]
├── Stub 2: [pod-tvrdnja]  → Dokaz: [...]
└── Stub 3: [pod-tvrdnja]  → Dokaz: [...]
```

Pravilo: tvrdnja bez dokaza je šum. Dokaz je merenje iz tvog proizvoda, citat stvarnog korisnika sa imenom, GIF koji pokazuje funkciju u 10 sekundi, ne pridev. Ova tri stuba postaju sekcije prodajne stranice, teme imejl sekvenci (Poglavlje 7) i uglovi za testove plaćenog oglašavanja (Poglavlje 6). Jedna hijerarhija, svi kanali.

### Anatomija prodajne stranice koja konvertuje

Above the fold (deo vidljiv bez skrolovanja) mora da odgovori na četiri stvari za nekoliko sekundi: **šta je ovo + za koga + dokaz + jedan poziv na akciju** (call to action, poziv na akciju). Jedan poziv na akciju, ne tri, svaki dodatni izbor deli pažnju. Jasnoća pobeđuje kreativnost, uvek:

❌ "Revolucija u produktivnosti"
✅ "Titluj video za 5 minuta umesto za 2 sata"

❌ "Pametnije fakturisanje za moderne timove"
✅ "Pošalji fakturu za 60 sekundi i vidi tačno kad je plaćena"

Loš naslov govori o proizvodu pridevima; dobar naslov imenuje posao (JTBD) i ishod, po mogućstvu sa pre/posle kontrastom. Ispod folda, redosled koji prati tok razmišljanja posetioca: tri stuba poruke sa dokazima → kako radi (3 koraka, vizuelno) → društveni dokaz (citati, logoi, recenzije) → cena ili FAQ → završni poziv na akciju, isti kao prvi.

### Polje "Kako si čuo/la za nas?"

Veliki deo B2B preporuka dešava se u kanalima koje analitika ne vidi, privatne Slack/WhatsApp grupe, DM-ovi, usmeno, odnosno nevidljive preporuke. Zato pri registraciji postavi obavezno otvoreno tekstualno polje "Kako si čuo/la za nas?", praksa koju je popularizovao Refine Labs (Chris Walker). Otvoreno polje, ne padajuća lista: "video sam thread na Redditu o titlovanju" vredi deset puta više od "Social". Kako te odgovore pretvaraš u odluke o kanalima, detaljno u Poglavlju 10.

### Primena odmah

Napravi fajl `docs/marketing/pozicioniranje.md` u repozitorijumu svog proizvoda sa četiri sekcije:

1. **Dunford 5 koraka**, popunjenih za tvoj proizvod, uključujući alternative "ručno" i "ništa"
2. **ICP + anti-ICP**, po šablonu iznad, sa bar jednim citatom iz stvarnog razgovora
3. **Messaging hijerarhija**, glavna tvrdnja + 3 stuba + dokaz za svaki (ako za stub nemaš dokaz, stub leti)
4. **Novi hero**, naslov, podnaslov i poziv na akciju prepravljeni po anatomiji iz ovog poglavlja

Test pre objave: pokaži hero osobi iz svog ICP-a na 5 sekundi, skloni ekran i pitaj "šta ovo radi i za koga je?". Ako ne ume da odgovori, piši ponovo. Ovaj fajl postaje direktan ulaz za brend priručnik u Poglavlju 11.

### Najčešće greške

1. **Pozicioniranje "za sve"**, kad se obraćaš svima, niko se ne prepozna. Rešenje: suzi na segment kome je vrednost najvažnija (Dunford korak 4); širićeš se kasnije.
2. **Kreće se od kategorije**, "mi smo AI platforma za X" pre nego što znaš alternative i jedinstvenost. Rešenje: kategorija je korak 5, ne korak 1.
3. **Hero kreativan, ne jasan**, igra reči koju razume samo autor. Rešenje: imenuj posao i ishod; kreativnost dolazi tek kad je jasnoća rešena.
4. **Tvrdnje bez dokaza**, "najbrži", "najjednostavniji" bez brojke ili citata. Rešenje: svaki stub dobija dokaz ili se briše.
5. **Pozicioniranje iz glave**, bez ijednog intervjua. Rešenje: 5-10 JTBD razgovora pre pisanja; pitanje "šta si koristio pre?" je obavezno.

### Kontrolna lista

- [ ] Uradio sam bar 5 JTBD intervjua i zapisao odgovore na "šta si koristio pre?"
- [ ] ICP definisan operativno: segment + problem + okidač + pojilo
- [ ] Anti-ICP eksplicitno zapisan
- [ ] Dunford 5 koraka popunjeni, kategorija izabrana poslednja
- [ ] Poziciona izjava napisana po šablonu
- [ ] Messaging hijerarhija: 1 tvrdnja + 3 stuba + dokaz za svaki stub
- [ ] Hero sekcija: šta je + za koga + dokaz + jedan poziv na akciju, prošla test od 5 sekundi
- [ ] Polje "Kako si čuo/la za nas?" (otvoren tekst, obavezno) dodato na registraciju
- [ ] Fajl `pozicioniranje.md` u repozitorijumu, spreman kao ulaz za brend priručnik (Poglavlje 11)


---

## Poglavlje 3: Proizvod kao marketing: PLG i aktivacija

Najjeftiniji marketinški kanal koji imaš je onaj koji već gradiš: sam proizvod. Rast vođen proizvodom (PLG) znači da proizvod preuzima posao marketinga i prodaje, korisnik se sam registruje, sam doživi vrednost, sam pozove kolege i sam plati. Slack, Dropbox, Calendly, Notion i Figma su rasli upravo ovako. Za tebe, solo osnivača bez budžeta, ovo je poglavlje sa najvećim povraćajem: svaka izmena ovde je kod koji možeš isporučiti danas, ne kampanja koju moraš platiti.

### Šta ćeš naučiti

- Zašto je aktivacija (drugo A iz AARRR mape) tačka najvećeg uticaja za mali tim
- Kako da nađeš svoj aha-momenat iz podataka, a ne iz mašte
- Kako da izmeriš TTV i skratiš ga sa tri konkretne tehnike
- Kako da izabereš freemium ili probni period na osnovu industrijskih brojki
- Kako da definišeš PQL pravilo koje ponašanje pretvara u signal za naplatu

### Gde PLG udara: aktivacija

AARRR okvir (poznat kao Pirate Metrics, Dave McClure) deli put korisnika na pet koraka: Akvizicija (kako te nađu), aktivacija (kako dožive vrednost), zadržavanje (kako ostaju), preporuka (kako te preporuče), prihod (kako plate). Većina osnivača troši energiju na prvo A, a curi im drugo. Aktivacija je trenutak kad se registracija pretvori u korisnika, i sve nizvodno (zadržavanje korisnika, preporuke, prihod) zavisi od nje. Rast petlje koje grade na ovome detaljno obrađuje Poglavlje 4; ovde popravljaš motor pre nego što sipaš gorivo.

### Aha-momenat: definiši ga iz podataka

Aha-momenat je akcija (ili prag akcija) posle koje korisnik po pravilu ostaje. Javno poznati primeri: Facebook je rano otkrio da korisnik koji doda 7 prijatelja za 10 dana ostaje; kod Slacka je tim koji pošalje ~2000 poruka praktično zadržan.

Tvoj aha-momenat ne pogađaš, izvodiš ga poređenjem ponašanja:

```
Procedura: nađi svoj aha-momenat (potrebna ti je samo analitika događaja)

1. Uzmi korisnike registrovane pre 30+ dana i podeli ih u dve grupe:
   ZADRŽANI  = aktivni i danas
   OTIŠLI    = nestali posle prve 1-2 nedelje
2. Za obe grupe izlistaj akcije iz PRVE 2 NEDELJE
   (kreirao projekat, pozvao kolegu, izvezao rezultat, povezao integraciju…)
3. Pitanje: šta su ZADRŽANI uradili rano, a OTIŠLI nisu?
4. Kandidat-akcije pretvori u hipotezu sa pragom i rokom:
   "Korisnik koji [akcija] bar [N puta] u prvih [X dana] ostaje."
5. Proveri na sledećoj kohorti registracija, pa tek onda gradi uvođenje korisnika oko toga.
```

Bitno: aha-momenat je korelacija koju tretiraš kao hipotezu, ne kao zakon. Testiraš je tako što uvođenje korisnika gura korisnike ka toj akciji, pa gledaš da li zadržavanje korisnika kohorte raste (disciplina eksperimenta, Poglavlje 10).

### TTV: izmeri, pa skraćuj

TTV (time-to-value) je vreme od registracije do prve stvarne vrednosti, što kraće, to bolja aktivacija. Prvo izmeri: timestamp registracije minus timestamp prve aha-akcije, medijana po kohorti. Ako je medijana "nikad" za većinu korisnika, to je tvoj problem broj jedan.

Tri tehnike skraćivanja, redom po snazi:

1. **Manje koraka podešavanja.** Svaki ekran između registracije i vrednosti je mesto odustajanja. Sve što nije neophodno za prvu vrednost, pomeri posle nje.
2. **Demo podaci.** Korisnik ne sme da gleda prazan ekran dok ne unese svoje podatke. Učitaj primer-projekat koji odmah pokazuje šta proizvod radi.
3. **Šabloni umesto praznog platna.** "Počni od nule" je za eksperte; novi korisnik bira između 3-5 gotovih šablona i menja, ne gradi.

❌ Registracija → izbor plana → podešavanje profila → pozovi tim → podesi integracije → prazan kontrolna tabla
✅ Registracija → šablon ili demo podaci → prva vrednost za 2 minuta → tek ONDA: "hoćeš da sačuvaš ovo? Podesi nalog."

### Uvođenje korisnika: vodič, ne tutorijal

Uvođenje korisnika (uvođenje novog korisnika) ima jedan zadatak: dovesti korisnika do aha-akcije najkraćim putem. Dva obrasca koja rade:

- **Checklist obrazac.** Vidljiva lista od 3-5 koraka sa progresom ("2/5 završeno"), gde je svaki korak akcija ka aha-momentu, ne tura kroz funkcije. Ljudi završavaju započete liste.
- **Empty states kao vodič.** Svaki prazan ekran je prilika: umesto "Nema podataka", piše šta korisnik dobija kad uradi akciju + dugme koje je pokreće odmah tu.

Princip iznad svega: **prva vrednost PRE traženja podešavanja.** Ne traži integracije, ne traži pozivanje tima, ne traži karticu, dok korisnik nije svojim očima video zašto bi se trudio.

### Freemium ili probni period: odluči brojkama

Freemium = besplatan plan zauvek, sa ograničenjima. Probni period = pun proizvod na ograničeno vreme. Industrijski rasponi iz anketa OpenView / Lenny's Bilten:

| Model | Konverzija u plaćeno | Broj prijava | Kada ima smisla |
|---|---|---|---|
| Freemium | tipično 2-5% | najveći | proizvod sa viralnom/mrežnom komponentom; besplatni korisnici su distribucija (Poglavlje 4) |
| Probni period bez kartice | ~8-12% | srednji | vrednost vidljiva za par dana; želiš širok ulaz uz pristojnu konverziju |
| Probni period sa karticom | 40%+ | drastično manji | uska, kvalifikovana publika koja zna šta hoće; spreman si da žrtvuješ obim za nameru |

Pravilo izbora: freemium biraj samo ako besplatan korisnik radi marketing za tebe (deli linkove, poziva tim, izlaže brend). Ako besplatni korisnici samo troše tvoje resurse i ne šire proizvod, probni period. Cena i pakovanje su posebna, potcenjena poluga (videti ProfitWell nalaz u Poglavlju 1).

### PQL: ponašanje kao signal za naplatu

PQL (product-qualified lead) je potencijalni kupac kvalifikovan ponašanjem u proizvodu, ne formularom. Umesto da pitaš "koliko je velika tvoja firma", gledaš šta su uradili. Primer pravila:

```
PQL pravilo (primer za kolaboracioni SaaS):
  nalog sa 3+ aktivna korisnika
  I 10+ kreiranih dokumenata u prvih 14 dana
  I udario u limit besplatnog plana bar jednom
  → spreman za razgovor o naplati / ponudu za nadogradnju u aplikaciji

Akcija kad se pravilo okine:
  - poruka u aplikaciji sa konkretnim limitom koji su dotakli
  - imejl osnivača (životni ciklus korisnika sekvenca, Poglavlje 7)
```

Tvoje PQL pravilo izvedi iz istog poređenja kohorti kao aha-momenat: šta su uradili nalozi koji su platili, pre nego što su platili?

### Zadržavanje korisnika: temelj na kome sve stoji

Akvizicija u proizvod koji curi je sipanje vode u bure bez dna. Poboljšanje retencije deluje složeno (compounding) na sve metrike, LTV raste, period povrata CAC-a se skraćuje, preporuke se množe. Brzi test temelja je Sean Ellis PMF test: ako bar 40% aktivnih korisnika kaže da bi bili "veoma razočarani" da proizvod nestane, imaš signal usklađenosti proizvoda i tržišta; ispod toga, popravljaj proizvod i aktivaciju pre nego što skaliraš bilo koji kanal iz Dela II.

### Primena odmah

Napravi fajl `docs/marketing/aktivacija.md` u repozitorijumu svog proizvoda sa tri stavke:

```
# Aktivacija: [proizvod], [datum]

## 1. Hipoteza aha-momenta
"Korisnik koji [akcija] bar [N puta] u prvih [X dana] ostaje."
Osnova: poređenje zadržanih vs otišlih iz poslednjih 30 dana (procedura iznad).

## 2. Trenutni TTV
Medijana vremena registracija → prva aha-akcija: ___
% korisnika koji NIKAD stignu do aha-akcije: ___

## 3. Jedna izmena uvođenja korisnika koja skraćuje TTV
Izmena: (npr. demo podaci umesto praznog ekrana)
Metrika odluke, zapisana UNAPRED: TTV medijana / % aktiviranih kohorte
Rok provere: +14 dana
```

Rezultat rada: popunjen fajl + isporučena izmena. Ovaj fajl kasnije postaje ulaz za dnevnik eksperimenata (Poglavlje 10) i za rutine marketinškog OS-a (Poglavlje 12).

### Najčešće greške

1. **Aha-momenat izmišljen u glavi, ne izveden iz podataka.** Rešenje: uvek poređenje kohorti zadržani vs otišli; bez analitike događaja nemaš PLG, imaš nadu.
2. **Uvođenje korisnika kao tura kroz funkcije.** Korisnika ne zanima gde je koje dugme, zanima ga njegov rezultat. Rešenje: svaki korak checkliste vodi ka aha-akciji ili leti napolje.
3. **Traženje podešavanja pre vrednosti.** Integracije, profil, kartica, sve posle prve vrednosti. Rešenje: pregledaj svoj tok registracije i prebroj ekrane pre prve vrednosti; cilj je da ih bude što manje.
4. **Freemium bez distribucione logike.** Besplatan plan koji nikoga ne dovodi je čist trošak. Rešenje: ili besplatni korisnici šire proizvod, ili pređi na probni period.
5. **Skaliranje akvizicije preko proizvoda koji curi.** Rešenje: prvo Sean Ellis test i retencione kohorte, pa tek onda budžet i kanali.

### Kontrolna lista

- [ ] Analitika događaja beleži ključne akcije korisnika (registracija, ključne akcije, poziv kolege, izvoz)
- [ ] Upoređene kohorte zadržanih i otišlih iz prve 2 nedelje
- [ ] Hipoteza aha-momenta zapisana u formatu "akcija × N × X dana"
- [ ] Izmerena medijana TTV i % korisnika koji nikad stignu do vrednosti
- [ ] Nijedan ekran podešavanja ne stoji pre prve vrednosti
- [ ] Prazan ekran zamenjen demo podacima ili šablonima
- [ ] Uvođenje korisnika checklist od 3-5 koraka vodi ka aha-akciji
- [ ] Odluka freemium vs probni period doneta po tabeli, ne po osećaju
- [ ] PQL pravilo definisano i okida konkretnu akciju (poruka u aplikaciji / imejl)
- [ ] Sean Ellis test poslat aktivnim korisnicima pre ulaganja u kanale rasta


---

## Poglavlje 4: Rast petlje: motor umesto levka

### Šta ćeš naučiti

- Zašto je levak (funnel) linearan trošak koji se prazni, a petlja motor koji se sam hrani
- Kako da AARRR mapom dijagnostikuješ gde ti rast curi pre nego što gradiš bilo šta novo
- Četiri tipa rast petlji, svaki sa studijom slučaja i skicom koraka koju možeš kopirati
- K-faktor formulu i realna očekivanja od viralnosti (spojler: K>1 skoro niko nema)
- Test od jednog pitanja za izbor PRVE petlje za tvoj proizvod

### Prvo dijagnoza: AARRR mapa

Pre nego što juriš novi kanal, utvrdi gde gubiš ljude koje već imaš. Dave McClure-ovi „pirate metrics" AARRR su dijagnostička mapa celog puta korisnika:

| Faza | Pitanje | Primer metrike |
|---|---|---|
| Acquisition | Kako ljudi saznaju za tebe? | posete → registracije |
| Activation | Da li brzo dožive vrednost? | % koji stigne do aha-momenta (Poglavlje 3) |
| Zadržavanje | Da li se vraćaju? | odlasci kupaca, nedeljna aktivnost |
| Preporuka | Da li dovode druge? | pozivnice po korisniku |
| Revenue | Da li plaćaju? | konverzija u plaćeno, MRR |

Pravilo dijagnoze: popravljaj fazu koja najviše curi, počev od dna. petlja preporuka na proizvodu sa lošom retencijom samo brže izbacuje korisnike iz bureta bez dna (detaljno u Poglavlju 3).

### Problem levka: linearan je i troši se

Levak ima jedan smer: sipaš pažnju na vrh (sadržaj, oglasi, lansiranje), deo iscuri na svakom koraku, i sledećeg meseca kreneš od nule. Svaki novi korisnik traži novi ulaz, rast je plaćen svaki put iznova.

Petlja (Reforge koncept) radi drugačije: **izlaz jednog ciklusa je ulaz sledećeg**. Korisnik koji prođe kroz proizvod proizvede nešto, pozivnicu, javni link, šablon, rezultat alata, što dovede sledećeg korisnika. Rast se slaže kao kamata na kamatu: isti mesečni napor daje sve veći rezultat, jer baza koja „vrti" petlju raste.

Postoje četiri tipa petlji koje SaaS realno može da pokrene.

### Tip 1: Viralna / petlja preporuka

**Studija slučaja (široko citirano):** Dropbox program preporuka, obe strane dobiju dodatni skladišni prostor (GB), i onaj ko poziva i onaj ko prihvati. Rast sa ~100.000 na ~4.000.000 korisnika za 15 meseci. Ključ: nagrada je u valuti proizvoda (prostor), pa privlači ljude koji proizvod stvarno žele, a ne lovce na keš.

Formula viralnosti, **K-faktor = broj pozivnica po korisniku × stopa konverzije pozivnice**. Primer računa: ako prosečan korisnik pošalje 2 pozivnice i svaka peta konvertuje, K = 2 × 0,2 = 0,4.

Realna očekivanja: K > 1 (samoodrživ viralni rast) je izuzetno redak. Ali i K od 0,3–0,5 značajno obara efektivni CAC, svaki plaćeni korisnik „besplatno" dovuče još pola korisnika.

```
SKICA: petlja preporuka
1. Korisnik doživi vrednost (aha-momenat)     → metrika: % aktiviranih
2. Proizvod ponudi pozivnicu u pravom trenutku → metrika: % koji pošalje
3. Primalac otvori namensku prodajnu stranicu   → metrika: CTR pozivnice
4. Primalac se registruje (obe strane nagrada) → metrika: konverzija pozivnice
5. Novi korisnik stigne do aha-momenta         → nazad na korak 1
```

### Tip 2: Upotreba kao distribucija

**Istorijski primer (široko citirano):** Hotmail 1996, potpis „P.S. I love you. Get your free e-mail at Hotmail" u svakom poslatom imejlu doveo je ~12 miliona korisnika za ~18 meseci. Sama upotreba proizvoda bila je reklama.

Moderni primeri: Calendly i Loom, svaki poslat link za zakazivanje i svaki podeljen snimak izlažu brend novim ljudima, i to u radnom kontekstu gde primalac ima isti problem. Korisnik ne mora ništa dodatno da uradi: distribucija je nusproizvod posla koji ionako radi.

Mini verzija za tvoj proizvod: **„powered by" bedž** na svemu što korisnik deli ili objavljuje (izveštaj, embed, javna stranica, izvezeni fajl), na besplatnom planu obavezan, na plaćenom opcioni. To je i blagi motiv za upgrade.

### Tip 3: Sadržajna / petlja sadržaja koji prave korisnici (UGC)

**Studije slučaja (široko citirano):** Notion i Figma, korisnici prave šablone i sadržaj zajednice (sadržaj koji prave korisnici (UGC, user-generated content), ne firma), objavljuju ih u galerijama i zajednici, a novi korisnici ih nalaze, registruju se da bi ih koristili, i vremenom naprave svoje. Zajednica postaje odbrambena prednost koju konkurencija ne može lako kopirati.

Uslov da radi: rezultat korisnikovog rada mora biti **koristan nekom drugom** (šablon, konfiguracija, radni tok, unapred podešen obrazac). Tvoj posao je da napraviš mesto za objavljivanje (galerija na sajtu), trenje objavljivanja svedeš na jedan klik i najbolje primerke aktivno promovišeš. Srodna mašina, programski generisane SEO stranice, detaljno u Poglavlju 5.

### Tip 4: Free-tool petlja

**Studija slučaja (široko citirano):** HubSpot Website Grader, besplatan alat koji rešava mali, konkretan problem (oceni mi sajt) i hrani glavni proizvod kao mamac za kontakt, odnosno besplatan sadržaj ili alat zbog kog neko ostavlja imejl. „Marketing kroz besplatan alat": alat se deli i linkuje sam, jer daje trenutnu vrednost bez registracije.

Za tebe kao graditelja ovo je najjeftinija petlja za pokretanje: mali alat (kalkulator, analizator, generator) koji rešava jedan korak problema tvog ICP-a (Poglavlje 2) je vikend projekta vredan posao, a most ka glavnom proizvodu („tvoj rezultat je X, glavni alat rešava i Y") ugrađuješ u sam rezultat.

| Petlja | Kako se širi | Uslov da radi | Glavna metrika |
|---|---|---|---|
| Preporuka | korisnik poziva korisnika | nagrada u valuti proizvoda, dobra zadržavanje korisnika | K-faktor |
| Upotreba = distribucija | proizvodov rezultat nosi brend | rezultat se prirodno deli s drugima | novi korisnici po podeljenom rezultatu |
| Sadržajna / UGC | korisnici prave sadržaj | rezultat koristan drugima + mesto objave | registracije iz galerije/zajednice |
| Free-tool | alat se deli i linkuje | trenutna vrednost bez registracije | korišćenja alata → registracije |

### Kako izabrati PRVU petlju

Ne biraš petlju koja ti se sviđa, nego onu koja **prirodno izvire iz načina na koji se proizvod već koristi**. Test od jednog pitanja:

> Da li rezultat korisnikovog rada u mom proizvodu neko drugi vidi?

- Vidi ga (link, dokument, embed, snimak) → upotreba-kao-distribucija + „powered by" bedž.
- Rezultat je ponovo upotrebljiv (šablon, unapred podešen obrazac, radni tok) → petlja sadržaja koji prave korisnici (UGC).
- Proizvod je bolji kad ga koristi više ljudi zajedno → preporuka.
- Ništa od toga → petlja besplatnog alata, jer jedina ne zavisi od postojećeg ponašanja, dograđuješ je sa strane.

❌ „Dodaćemo program preporuka jer je Dropbox tako porastao", na proizvodu koji se koristi solo i čiji rezultat niko ne vidi.
✅ „Naši korisnici svaki dan šalju klijentima izveštaje iz alata, stavljamo bedž sa linkom u podnožje izveštaja i merimo klikove."

### Primena odmah

Skiciraj jednu petlju za svoj proizvod i sačuvaj je kao `docs/marketing/petlja-01.md` u repozitorijumu. Šablon:

```markdown
# Petlja: [tip] za [proizvod]

Korak 1: [šta se desi]        → metrika: [šta meriš]
Korak 2: [šta se desi]        → metrika: ...
Korak 3: [šta se desi]        → metrika: ...
Korak 4: [novi korisnik ulazi] → nazad na korak 1

Najslabija karika: [korak koji se najverovatnije kida i zašto]
Prvi eksperiment: [najmanja izmena koja testira najslabiju kariku]
Bazna linija: [trenutne vrednosti metrika, pre ikakvih podsticaja]
```

Obavezno: svaki korak ima svoju metriku i događaj u analitici PRE nego što petlju pustiš. Petlja koju ne meriš po koracima je petlja kojoj ne znaš gde puca. Eksperimente nad njom vodi ritmom iz Poglavlja 10.

### Najčešće greške

1. **Preporuke pre zadržavanja korisnika.** Petlja na proizvodu koji curi samo brže razočara više ljudi. Rešenje: prvo aktivacija i zadržavanje korisnika (Poglavlje 3), pa tek onda pozivnice.
2. **Očekivanje K > 1.** Samoodrživa viralnost je izuzetno retka. Rešenje: planiraj petlju kao amortizer CAC-a (K 0,3–0,5 je odličan rezultat), ne kao jedini kanal.
3. **Nagrada u kešu umesto u proizvodu.** Keš privlači lovce na nagrade koji odu posle isplate. Rešenje: nagrada u valuti proizvoda (prostor, krediti, meseci plana), obostrana, Dropbox lekcija.
4. **Petlja bez merenja koraka.** Vidiš samo da „ne radi", ne i gde. Rešenje: događaj za svaki korak skice, pa popravljaj najslabiju kariku, jednu po jednu.
5. **Kopiranje tuđe petlje koja ne izvire iz tvog proizvoda.** Rešenje: test od jednog pitanja iznad, ako rezultat korisnika niko ne vidi, ne forsiraj deljenje, kreni od free-tool petlje.

### Kontrolna lista

- [ ] Prošao sam AARRR mapu i znam koja faza najviše curi
- [ ] Odgovorio sam na test: da li rezultat korisnikovog rada neko drugi vidi?
- [ ] Izabrao sam jedan tip petlje koji prirodno izvire iz upotrebe proizvoda
- [ ] Skicirao sam petlju u `docs/marketing/petlja-01.md` sa metrikom za svaki korak
- [ ] Označio sam najslabiju kariku i definisao prvi eksperiment za nju
- [ ] Svaki korak petlje ima događaj u analitici pre pokretanja
- [ ] Zabeležio sam baznu liniju metrika pre uvođenja podsticaja
- [ ] Ako radim preporuka: nagrada je obostrana i u valuti proizvoda


---

## Poglavlje 5: Organski rast u AI eri: budi citiran izvor

### Šta ćeš naučiti

- Zašto stara igra "rangiraj se i čekaj klik" slabi, i koja igra dolazi umesto nje
- AEO/GEO taktike: kako da postaneš izvor koji AI modeli i ljudi citiraju
- Kada programski generisane SEO i dalje radi (Zapier model) i kako da ga primeniš bez spama
- Founder-led marketing i javno građenje proizvoda: šta deliti, a šta ne
- Kako da uhvatiš nevidljive preporuke, najvredniji kanal koji ti analitika ne pokazuje

### Nova realnost: klik umire, citat raste

Prvo brojevi. Otprilike ~60% Google pretraga završava bez ijednog klika na rezultat (SparkToro/Similarweb analize, približno), korisnik dobije odgovor na samoj stranici pretrage. To su tzv. zero-click pretrage. AI Overviews (AI sažeci na vrhu Google rezultata) dodatno obaraju CTR informativnih upita, više studija iz 2024-25 pokazuje značajne padove.

Posledica je strukturna, ne kozmetička: ako ti je plan "napišem blog post, rangiram se, čekam klik", igraš igru čija se nagrada smanjuje. Nova igra glasi: **budi izvor koji AI i ljudi citiraju.** Kada ChatGPT, Perplexity ili AI Overview odgovara na pitanje iz tvoje kategorije, tvoj proizvod treba da bude deo odgovora, čak i kad klik nikad ne stigne.

Drugi pomak: AI je komodifikovao prosečan sadržaj. Tekst koji svako može da generiše za 30 sekundi vredi tačno toliko, nula. Vrednost se seli u distribuciju, brend, originalne podatke i ukus. Generički AI blog bez ugla i podataka platforme i čitaoci ignorišu. Zapamti to pre nego što pomisliš da je rešenje "50 AI tekstova mesečno".

### AEO/GEO: optimizacija za mašine koje odgovaraju

AEO/GEO (answer engine optimization / generative engine optimization) je disciplina pravljenja sadržaja koji AI sistemi mogu da razumeju, izvuku i citiraju. Konkretne poluge:

| Taktika | Šta konkretno radiš | Zašto radi |
|---|---|---|
| Jasne definicije pojmova | Na svakoj ključnoj stranici: pojam + definicija u 1-2 rečenice, odmah ispod naslova | AI modeli izvlače čiste, samostalne definicije |
| Strukturirani podaci | Schema.org oznake (FAQ, Product, HowTo) kao JSON-LD u `<head>` prodajne stranice i stranica dokumentacije; proveri Google Rich Results testom | Mašinski čitljiv kontekst o tome šta si i šta radiš |
| Originalni podaci | Mini-istraživanje koje samo ti imaš (vidi recept ispod) | Magnet za linkove i AI citate, niko drugi nema taj broj |
| Prisustvo na izvorima koje modeli čitaju | Dokumentacija, G2, Reddit, YouTube, uredno, ažurno, sa pravim imenom proizvoda | Modeli uče iz tih izvora; ako te tamo nema, ne postojiš |
| llms.txt | Fajl u root-u sajta koji AI alatima daje sažet, strukturisan pregled proizvoda (primer ispod) | Standard u nastajanju, jeftino za postaviti, postavi ga |

Za llms.txt ti ne treba ništa više od ovoga, običan markdown fajl na adresi `tvojsajt.com/llms.txt`:

```
# [Ime proizvoda]

> [Jedna rečenica: šta proizvod radi i za koga, npr. "Alat koji
> malim timovima automatski pravi izveštaje iz X podataka."]

## Dokumentacija
- [Vodič za početak](https://tvojsajt.com/docs/start): od registracije do prve vrednosti
## Cene
- [Pricing](https://tvojsajt.com/cenovnik): planovi i šta koji uključuje
## Use-case stranice
- [Use case](https://tvojsajt.com/use-case): za koga i koji problem rešava
```

Najjača poluga sa liste su **originalni podaci**. Recept za mini-istraživanje koje SaaS sa 50 korisnika može da napravi za jedan dan:

```
MINI-ISTRAŽIVANJE, recept:
1. Izvuci anonimizovan, agregiran podatak iz svog proizvoda
   (npr. "prosečno trajanje X kod naših korisnika", "najčešći Y po segmentu")
2. Ili anketiraj svoj ICP: 5 pitanja, 30-50 odgovora je dovoljno za ugao
3. Objavi kao stranicu sa: naslov sa brojem, metodologija (2 rečenice),
   1-2 grafikona, jasan zaključak u jednoj rečenici na vrhu
4. Distribuiraj: lični profil osnivača + relevantne zajednice + lista imejl adresa
```

Niko ne može da generiše tvoj podatak, to je jedini sadržaj imun na komodifikaciju.

### Programmatic SEO koji i dalje radi

Programmatic SEO znači automatski generisane stranice za long-tail upite (duge, specifične pretrage sa malo konkurencije). Kanonski primer: Zapier i hiljade stranica tipa "X + Y integracija", jedan od glavnih organskih kanala kompanije (široko citirano).

Model radi i u AI eri, ali samo uz etički test: **svaka stranica mora imati stvarnu vrednost za stvarnog korisnika.**

❌ 2.000 stranica "najbolji [alat] za [grad]" sa istim template tekstom i promenjenim imenom grada, spam koji pretrage i modeli prepoznaju i ignorišu.

✅ Stranica "[tvoj proizvod] + [konkretan alat]" koja sadrži: šta integracija tačno radi, 3 stvarna use-case-a, snimak ekrana podešavanja, ograničenja. Korisna i da Google ne postoji.

Test pre lansiranja: otvori 5 nasumičnih generisanih stranica. Da li bi svaku poslao korisniku kao odgovor na pitanje? Ako ne, ne objavljuj.

### Marketing koji vodi osnivač: lični profil > nalog firme

Algoritmi LinkedIn-a i X-a favorizuju lične profile, profil osnivača nosi domet koji nalozi kompanije nemaju. Za solo osnivača ovo je asimetrična prednost: nemaš marketinški tim, ali imaš nešto što korporacija ne može da kopira, proces iz prve ruke.

Build in public obrazac (graditi javno, primeri: Buffer, levelsio):

| Deli | Ne deli |
|---|---|
| Metrike sa kontekstom (MRR, odlasci kupaca, vidi Poglavlje 1) | Podatke korisnika, čak ni anonimne ako su prepoznatljivi |
| Lekcije iz neuspeha ("probao X, nije radilo, evo zašto") | Hvalisanje bez pouke ("rekordan mesec!") |
| Proces odluka (zašto si izabrao cenu, kanal, funkcionalnost) | Planove koje konkurencija može da pretekne pre tebe |
| Pitanja publici (stvarna, ne angažovanje-bait) | Generičke motivacione objave, to je AI flood u ljudskom obliku |

Format koji se ponavlja, šablon nedeljne objave:

```
[BROJ ili DOGAĐAJ iz ove nedelje]
[Šta sam očekivao vs. šta se desilo]
[Jedna lekcija u jednoj rečenici]
[Pitanje za čitaoce, opciono]
```

Jedan format, jedan kanal, svake nedelje. Doslednost tuče genijalnost, algoritam i publika nagrađuju ritam.

### Nevidljive preporuke i G2 higijena

Nevidljive preporuke = preporuke u kanalima koje analitika ne vidi: privatne Slack/WhatsApp grupe, DM-ovi, usmeno. Veliki deo B2B preporuka dešava se upravo tamo. Tvoja analitika će reći "direktan saobraćaj", a istina je da te je neko preporučio u grupi.

Operativno rešenje, pitanje o izvoru koje korisnik sam popunjava (praksa koju je popularizovao Refine Labs / Chris Walker): obavezno polje pri registraciji.

```
Pitanje u registracija formi (obavezno, slobodan unos):
"Kako si čuo/la za nas?"
```

Slobodan tekst, ne padajući meni, odgovori tipa "neko te pomenuo u Slack grupi za osnivače" vrede zlata i ne staju ni u jednu unapred ponuđenu opciju. Pregledaj odgovore jednom nedeljno; oni će ti pokazati koji kanal stvarno radi.

G2/Capterra higijena: B2B kupci konsultuju peer recenzije pre razgovora sa prodajom. Popunjen profil sa svežim recenzijama je higijena, ne opcija, i dodatno, to su izvori koje AI modeli čitaju (AEO efekat). Minimalan proces: posle svakog aha-momenta (Poglavlje 3) zamoli zadovoljnog korisnika za recenziju; cilj je stalan dotok, ne kampanja jednom godišnje.

```
ŠABLON MOLBE (poruka u aplikaciji ili imejl, odmah posle aha-momenta):
"Vidim da si upravo [konkretan rezultat, npr. poslao prvi izveštaj].
Ako ti je [proizvod] pomogao, recenzija na G2 nam znači više nego
što misliš, traje 3 minuta: [link]. Hvala!"
```

Zajednica kao dugoročnija odbrambena prednost koju konkurencija teško kopira (dbt, Notion, Figma) detaljnije je obrađena u Poglavlju 4.

### Primena odmah

Izaberi **jedan** organski kanal, ne tri, jedan, na osnovu toga gde tvoj ICP (Poglavlje 2) stvarno provodi vreme. Popuni i sačuvaj ovaj plan za narednih 30 dana:

```
ORGANSKI PLAN, 30 DANA
Kanal:           (npr. LinkedIn lični profil / programski generisane stranice / YouTube)
Zašto baš taj:   (gde je moj ICP, jedna rečenica, sa dokazom)
Format:          (npr. nedeljna build-in-public objava po šablonu iznad)
Ritam:           (npr. 2x nedeljno, ponedeljak i četvrtak)
Metrika uspeha:  (jedna! npr. broj registracijaa sa odgovorom "video objavu"
                  u pitanje o izvoru koje korisnik sam popunjava polju)
Datum provere:   (danas + 30 dana)
```

Rezultat rada: popunjen plan + postavljeno "Kako si čuo/la za nas?" polje u registracija formi. Bez tog polja nećeš znati da li plan radi.

### Najčešće greške

1. **Svi kanali odjednom.** Solo osnivač na LinkedIn-u, X-u, YouTube-u i blogu istovremeno = osrednji svuda. Rešenje: jedan kanal, 90 dana, pa tek onda odluka o drugom.
2. **AI flood generičkih tekstova.** Komodifikovan sadržaj ne donosi ništa, ni rang, ni citate, ni poverenje. Rešenje: manje komada, više originalnih podataka i ličnog ugla.
3. **Merenje samo klikova.** Nevidljive preporuke ne ostavlja trag u analitici, pa kanal izgleda "mrtav" iako dovodi najbolje korisnike. Rešenje: pitanje o izvoru koje korisnik sam popunjava polje, pregledano nedeljno.
4. **Objavljivanje sa naloga firme.** Algoritmi favorizuju lične profile; nalog firme bez lica dobija deo dometa. Rešenje: osnivač objavljuje lično, nalog firme deli i pojačava.
5. **Programmatic spam.** Hiljade template stranica bez vrednosti ubijaju kredibilitet celog domena. Rešenje: test "da li bih ovu stranicu poslao korisniku kao odgovor?" pre objave.

### Kontrolna lista

- [ ] Ključni pojmovi moje kategorije imaju jasnu definiciju (1-2 rečenice) na mom sajtu
- [ ] Schema.org strukturirani podaci postavljeni na prodajnoj stranici i stranicama dokumentacije
- [ ] llms.txt fajl postavljen u root sajta
- [ ] Definisano jedno mini-istraživanje sa podatkom koji samo ja imam (rok: ovaj mesec)
- [ ] G2/Capterra profil popunjen + proces za stalan dotok recenzija posle aha-momenta
- [ ] "Kako si čuo/la za nas?" polje (slobodan unos) u registracija formi
- [ ] Izabran JEDAN organski kanal, format i ritam, plan za 30 dana popunjen
- [ ] Lični profil osnivača aktivan sa nedeljnim build-in-public ritmom
- [ ] Ako radim programski generisane SEO: 5 nasumičnih stranica prošlo test stvarne vrednosti


---

## Poglavlje 6: Plaćena akvizicija: kada, gde i kako da ne izgoriš

Plaćeni oglasi su jedini kanal gde rezultat stiže za 48 sati, i jedini gde za 48 sati možeš spaliti mesečni budžet bez ijednog korisnika. Ovo poglavlje ti daje ekonomski test koji odlučuje da li uopšte smeš da uključiš plaćeno oglašavanje, i protokol koji garantuje da svaki potrošeni dinar vrati bar jednu naučenu lekciju.

### Šta ćeš naučiti

- Ekonomski preduslov: kako da pre prvog dinara znaš da li plaćeno oglašavanje ima smisla za tvoj proizvod
- Dve uloge plaćenog oglašavanja po fazi: laboratorija poruka (rano) vs kanal skaliranja (kasno)
- Koji kanal kada: Google Search, LinkedIn, Meta, i šta svaki od njih zapravo radi
- Kako AI menja kreativu, a šta ostaje ljudski posao
- Higijena merenja: UTM + pitanje o izvoru koje korisnik sam popunjava, jer pikseli ne vide nevidljive preporuke

### Ekonomski preduslov: jedinična ekonomija mora da radi PRE plaćenog oglašavanja

Plaćena akvizicija ima ekonomski smisao tek kad LTV:CAC podnosi trošak kanala (formula u Poglavlju 1). Orijentir industrije je LTV:CAC ≥ 3:1 i period povrata CAC-a ispod 12 meseci za ranu fazu. Ako ti je LTV 90 evra, a klik na ciljanu ključnu reč košta 3 evra uz konverziju prodajne stranice od par procenata, matematika ti je rekla "ne" pre nego što si otvorio nalog za oglase.

Praktičan test pre pokretanja, u tri reda:

```
Maksimalni dozvoljeni CAC = LTV / 3
Procena CAC kanala       = CPC / (konverzija prodajne stranice % × konverzija probni period→plaćeno %)
Odluka: procena CAC kanala < maksimalni dozvoljeni CAC?  DA → testiraj.  NE → ne diraj.
```

Za konverziju probni period→plaćeno koristi industrijske raspone iz Poglavlja 3 ako još nemaš svoje brojke (freemium→plaćeno tipično 2-5%, probni period bez kartice ~8-12%, rasponi iz anketa OpenView / Lenny's Bilten). Računaj sa pesimističnim krajem raspona. Ako i tada matematika prolazi, imaš zeleno svetlo za test, ne za skaliranje.

I još jedan strukturni razlog za oprez: CPC-ovi na velikim platformama godinama rastu. Biznis oslonjen isključivo na plaćeno oglašavanje postaje strukturno sve skuplji, svake godine plaćaš više za istog korisnika. Plaćeno oglašavanje uvek ide UZ organski motor iz Poglavlja 5, nikad umesto njega.

### Dve uloge plaćenog oglašavanja: laboratorija, pa tek onda mašina

U ranoj fazi plaćeno oglašavanje ne služi za skaliranje, služi kao laboratorija poruka. Za male pare brzo testiraš naslove, uglove i ICP hipoteze (ICP detaljno u Poglavlju 2), i dobijaš signal za tekst prodajne stranice, sadržaj i imejl sekvence. Organski kanal ti za istu lekciju traži nedelje; oglasi ti za 100-200 evra kažu koji ugao zaustavlja skrol.

| Faza | Uloga plaćenog oglašavanja | Budžet | Metrika uspeha |
|---|---|---|---|
| Pre PMF-a | Laboratorija poruka | Fiksan test budžet koji smeš da izgubiš | CTR i konverzija prodajne stranice po UGLU poruke |
| Posle PMF-a, LTV:CAC ≥ 3 | Kontrolisano skaliranje | Vezan za period povrata CAC-a | CAC po kanalu vs maksimalni dozvoljeni CAC |
| Uvek | Ponovno oglašavanje posetilaca | Mali, stalan | Konverzija vraćenih posetilaca |

Ključna mentalna promena: u laboratorijskoj fazi kupuješ podatke, ne korisnike. Ako test od 150 evra dokaže da ugao "uštedi 5 sati nedeljno" duplo nadmašuje ugao "platforma pokretana AI-em", to saznanje vredi više od 10 korisnika koje bi isti novac doneo, jer ga ugrađuješ u prodajnu stranicu, imejl i svaki budući oglas.

### Koji kanal kada

| Kanal | Šta radi | Kada ima smisla | Rizik |
|---|---|---|---|
| Google Search | Hvata POSTOJEĆU tražnju, ljudi već kucaju problem ili kategoriju | Kad za tvoju kategoriju postoji obim pretrage; bottom-funnel upiti ("alat za X") | Ako kategoriju niko ne traži, nema šta da uhvatiš |
| LinkedIn | B2B targeting po roli, industriji, veličini firme | B2B SaaS sa višim LTV-om koji podnosi skup klik; precizno gađanje ICP-a | Skupo po kliku, matematika iz prvog dela mora da prođe |
| Meta/Instagram | Širina + ponovno oglašavanje; stvara tražnju kod ljudi koji te nisu tražili | Vizuelni proizvodi, šira publika, ponovno oglašavanje posetilaca sajta | Hladan saobraćaj na demo-traffic kampanjama ume da bude skup za B2B nišu |

Pravilo izbora: ako tvoju kategoriju ljudi već guglaju, počni od Search-a, jer hvataš nameru koja postoji. Ako prodaješ nešto što ICP još ne zna da traži, Search ti ne pomaže; tu poruku prvo testiraš na Meta/LinkedIn, a tražnju dugoročno gradiš organskim motorom i brendom (95-5 pravilo u Poglavlju 8: ~95% kupaca kategorije nije aktivno na tržištu u datom trenutku, performance hvata samo onih 5% koji kupuju sada).

Ponovno oglašavanje je poseban slučaj: gađa ljude koji su već bili na sajtu, pa je gotovo uvek najjeftinija konverzija u nalogu. Uključi ga pre bilo koje hladne kampanje.

### Kreativa u AI eri: AI pravi varijante, ti praviš ugao

AI je komodifikovao prosečan sadržaj, to važi i za oglase. Generička AI varijanta bez ugla i podataka ne zaustavlja nikoga. Vrednost se selila u ono što AI ne može da izmisli umesto tebe: UGAO, uvid zašto bi tvoj ICP stao da skroluje.

Podela posla koja radi:

1. **Ti**: definiši 3 ugla iz stvarnih razgovora sa korisnicima, bol ("ručno radiš X svake nedelje?"), ishod ("Y za 10 minuta umesto 5 sati"), neprijatelj ("prestani da plaćaš za Z koji ne koristiš").
2. **AI**: za svaki ugao generiše 5-10 varijanti naslova i opisa. Šablon prompta:

```
Uloga: copywriter za B2B SaaS oglase.
Proizvod: [jedna rečenica]. ICP: [rola, kontekst, bol].
Ugao: [npr. "ishod, uštedi 5 sati nedeljno na X"].
Napiši 8 varijanti naslova (max 40 karaktera) + opisa (max 90)
za [kanal]. Bez superlativa, bez "revolucionarno", konkretan ishod
u svakom naslovu. Ton: [iz brend priručnika, Poglavlje 11].
```

3. **Ti opet**: izbaci sve što zvuči kao da je moglo biti oglas bilo kog konkurenta. Test ugla: da li bi tvoj ICP rekao "ovo je o meni"?

❌ "Revolucionarna AI platforma za produktivnost timova"
✅ "Tvoj tim i dalje ručno prepisuje podatke iz imejlova u tabele?"

Testiraj UGLOVE jedan protiv drugog, ne nijanse iste poruke. Mali budžet nema statističku snagu za razliku između dva slična naslova, ima je za razliku između dva različita ugla (disciplina eksperimenta i Kohavijev nalaz o trećinama, detaljno u Poglavlju 10; zato se sve meri).

### Higijena merenja: UTM + "Kako si čuo za nas?"

Dva sloja, oba obavezna:

**Sloj 1, UTM parametri.** Svaki plaćeni link nosi `utm_source`, `utm_medium`, `utm_campaign` i `utm_content` (u `utm_content` ide UGAO, da znaš koja poruka konvertuje, ne samo koji kanal):

```
https://tvojproizvod.com/?utm_source=linkedin&utm_medium=paid&utm_campaign=test-uglova-jun&utm_content=ugao-ishod-5h
```

**Sloj 2, pitanje o izvoru koje korisnik sam popunjava.** Veliki deo B2B preporuka dešava se u kanalima koje analitika ne vidi (privatne Slack/WhatsApp grupe, DM-ovi, usmeno), u Poglavlju 5 opisane kao nevidljive preporuke, detaljno u Poglavlju 5. Zato pri registraciji ide obavezno otvoreno polje "Kako si čuo za nas?" (praksa koju je popularizovao Refine Labs / Chris Walker). Pikseli će oglasu pripisati korisnika koji je za tebe čuo u Slack grupi pa te kasnije guglao, polje koje korisnik sam popunjava hvata istinu koju piksel ne vidi. Odluke o gašenju i skaliranju donosi tek presek oba sloja.

### Primena odmah

Napravi fajl `plan-placenog-oglasavanja.md` u svom marketinškom repozitorijumu (struktura repozitorijuma u Poglavlju 12) sa tri bloka, popunjena UNAPRED, pre nego što otvoriš nalog za oglase:

```markdown
# Plaćeno oglašavanje test plan: [proizvod], [datum]

## 1. Test budžet (novac koji smem da izgubim)
Ukupno: ___ EUR. Po uglu: ___ EUR. Trajanje: max ___ dana.

## 2. Tri ugla za test
- Ugao A (bol):        "..."
- Ugao B (ishod):      "..."
- Ugao C (neprijatelj): "..."
Svaki ugao = ista prodajna stranica, različit `utm_content`.

## 3. Kriterijum za gašenje testa (zapisan PRE pokretanja)
- Gasim ugao ako posle ___ EUR potrošnje ima 0 konverzija prodajne stranice.
- Gasim ceo test ako procena CAC > ___ EUR (= LTV/3) nakon celog budžeta.
- Pobednički ugao ulazi u: naslovni deo prodajne stranice, imejl sekvencu, sledeći test.
```

Rezultat rada: popunjen fajl + izračunat maksimalni dozvoljeni CAC iz svoje LTV brojke (Poglavlje 1). Bez ta dva, nalog za oglase ostaje zatvoren.

### Najčešće greške

1. **Plaćeno oglašavanje pre jedinične ekonomije.** Kupuješ korisnike skuplje nego što vrede i to zoveš "rast". Rešenje: test LTV/3 iz ovog poglavlja, ako ne prolazi sa pesimističnim brojkama, novac ide u organski motor i monetizaciju (ProfitWell analize: ulaganje u cenovnik ima višestruko veći uticaj od istog ulaganja u akviziciju).
2. **Kriterijum za gašenje testa se izmišlja posle rezultata.** "Hajde još malo, samo što nije proradilo", tako se topi budžet. Rešenje: kriterijum zapisan u fajlu PRE pokretanja; menjanje hipoteze posle rezultata je samoobmana.
3. **Testiranje nijansi umesto uglova.** Plava vs zelena pozadina na 50 klikova ne znači ništa. Rešenje: testiraj velike zamahe, različite uglove poruke, različite ICP hipoteze.
4. **Verovanje samo pikselima.** Oglas dobija kredit za korisnika koga ti je donela preporuka iz privatne grupe, pa skaliraš pogrešan kanal. Rešenje: polje koje korisnik sam popunjava pri registraciji + presek oba sloja pre odluke.
5. **Plaćeno oglašavanje kao zamena za organski.** CPC inflacija znači da isti budžet svake godine kupuje manje. Rešenje: plaćeno oglašavanje je pojačalo i laboratorija; motor su petlje (Poglavlje 4) i organski kanali (Poglavlje 5).

### Kontrolna lista

- [ ] Izračunat maksimalni dozvoljeni CAC (LTV/3) i procena CAC kanala sa pesimističnim konverzijama
- [ ] Definisan fiksan test budžet koji smeš da izgubiš u celosti
- [ ] Tri različita UGLA poruke (ne tri varijante istog), izvedena iz razgovora sa korisnicima
- [ ] Kriterijum za gašenje testa zapisan u `plan-placenog-oglasavanja.md` PRE pokretanja kampanje
- [ ] Svaki link nosi UTM parametre, ugao u `utm_content`
- [ ] Polje "Kako si čuo za nas?" aktivno pri registraciji
- [ ] Ponovno oglašavanje uključen pre hladnih kampanja
- [ ] Odluka o skaliranju donosi se tek kad presek UTM + podatak koji korisnik sam unosi potvrdi CAC ispod limita


---

## Poglavlje 7: Imejl i životni ciklus korisnika: kanal koji poseduješ

Svaki kanal iz prethodnih poglavlja ima gazdu koji nisi ti. Algoritam ti preko noći može uzeti organski domet, plaćeni kanali poskupljuju iz godine u godinu (Poglavlje 6), a pretraga bez klika (zero-click) jede klikove (Poglavlje 5). Imejl lista je jedini kanal koji POSEDUJEŠ: niko ti je ne može oduzeti, ne plaćaš zakup pažnje i sam biraš kad i kome šalješ. Po industrijskim procenama (Litmus/DMA), imejl vraća oko 36$ na svaki uloženi 1$, najviši povraćaj ulaganja (ROI) među marketinškim kanalima. Ali taj povraćaj ulaganja ne dolazi iz generičkog biltena, nego iz imejlova vezanih za ponašanje korisnika.

### Šta ćeš naučiti

- Zašto je imejl jedini kanal u tvom vlasništvu i šta to praktično znači
- Razliku između imejlova kroz životni ciklus korisnika i biltena, i zašto okidač po ponašanju pobeđuje okidač po kalendaru
- Kako da sastaviš aktivacionu sekvencu od 5 imejlova vezanu za aha-momenat svog proizvoda
- Tri dodatna toka kroz životni ciklus korisnika: sprečavanje odlazaka kupaca, povratak neaktivnih korisnika i istek probnog perioda
- Higijenska pravila koja čuvaju isporučivost i poverenje liste

### Imejl po ponašanju korisnika pobeđuje bilten

Bilten šalješ po kalendaru: svima isto, svakog utorka, bez obzira na to gde se korisnik nalazi. Imejl kroz životni ciklus korisnika (imejl vezan za fazu životnog ciklusa korisnika) šalješ po ponašanju: registrovao se, zapeo pre aha-momenta, prestao da koristi proizvod, ističe mu probni period. Industrijska procena povraćaja ulaganja od ~36$ na 1$ (Litmus/DMA) je prosek, tokovi kroz životni ciklus korisnika su deo koji taj prosek vuče naviše, jer stižu tačno u trenutku kad su relevantni.

| | Bilten | Imejl kroz životni ciklus korisnika |
|---|---|---|
| Okidač | kalendar (utorak, 10h) | ponašanje (registracija, zastoj, pad upotrebe) |
| Publika | svi isto | segment u konkretnoj fazi |
| Sadržaj | novosti, blog | sledeći korak ka vrednosti |
| Cilj | održavanje pažnje | pomeranje metrike (aktivacija, konverzija, zadržavanje korisnika) |
| Kad ga praviš | svake nedelje, ručno | jednom, pa radi sam |

Bilten nije zabranjen, koristan je za brend i memoriju (Poglavlje 8). Ali ako biraš gde ćeš prvo uložiti vreme kao solo osnivač: tokovi kroz životni ciklus korisnika se naprave jednom i rade godinama; bilten te svake nedelje čeka prazan.

### Aktivaciona sekvenca: 5 imejlova vezanih za aha-momenat

Aktivaciona (uvođenje korisnika) sekvenca je niz imejlova posle registracije čiji je jedini posao da korisnika dovede do aha-momenta koji si definisao u Poglavlju 3, trenutka kad proizvod isporuči prvu stvarnu vrednost. Sve drugo (funkcije, cene, priče) čeka.

Tri principa pre šablona:

1. **Dan 0 = jedan korak.** Imejl dobrodošlice ima JEDAN sledeći korak, ne turu kroz 15 funkcija. Što je kraći put do TTV (time-to-value), to bolja aktivacija, to je imejl-verzija onoga što uvođenje korisnika radi u proizvodu.
2. **Nudge (podsticaj) samo ako treba.** Imejl koji gura ka aha-momentu šalje se SAMO korisniku kod kog se aha nije desio. Okidač je ponašanje, ne kalendar. Korisniku koji je već stigao do vrednosti taj imejl je šum.
3. **Konverziju traži kad ponašanje pokaže spremnost.** Poziv na plaćanje ide kad korisnik pređe PQL prag (product-qualified lead, detaljno u Poglavlju 3), ne sedmog dana zato što je sedmi dan.

```
AKTIVACIONA SEKVENCA, ŠABLON (5 imejlova)

MEJL 1, Dobrodošlica
  Okidač: registracija (odmah, dan 0)
  Svrha:  jedan jedini sledeći korak ka aha-momentu
  Skica:  "Zdravo [ime], da bi [proizvod] imao smisla, uradi ovo
          jedno: [konkretan korak, npr. 'otpremi prvi video'].
          Traje [X] minuta. [Dugme: Uradi to sada]"
          Bez liste funkcija. Bez 'upoznaj naš tim'.

MEJL 2, Nudge ka aha-momentu
  Okidač: 48h od registracije I aha-momenat se NIJE desio
          (ako jeste, imejl se preskače)
  Svrha:  ukloniti prepreku, ne podsetiti na postojanje
  Skica:  "Video sam da si se registrovao, a nisi još [korak].
          Najčešći razlog je [prepreka X], evo kako se rešava
          za 2 minuta: [mini-uputstvo ili 60s video]."

MEJL 3, Društveni dokaz + use-case
  Okidač: aha-momenat se desio ILI dan 4 (šta pre nastupi)
  Svrha:  pokazati šta sledi posle prve vrednosti
  Skica:  "Evo kako [tip korisnika kao ti] koristi [proizvod]
          za [konkretan ishod]: [kratka priča sa brojkom ili
          citatom]. Tvoj sledeći korak: [use-case dubina]."

MEJL 4, Direktno pitanje (ton osnivača)
  Okidač: dan 6 I aha-momenat se NIJE desio
  Svrha:  saznati šta je zaustavilo korisnika; svaki odgovor
          je besplatno istraživanje za uvođenje korisnika
  Skica:  "Kratko pitanje, šta te je zaustavilo? Odgovori
          jednom rečenicom na ovaj imejl, čitam svaki odgovor., [tvoje ime, osnivač]"
          Običan tekst, bez dizajna, reply-to = tvoj inbox.

MEJL 5, Poziv na konverziju
  Okidač: PQL signal, ponašanje koje istorijski prethodi
          plaćanju (npr. [N] upotreba ključne funkcije,
          dostignut limit besplatnog plana)
  Svrha:  ponuditi plaćanje u trenutku dokazane vrednosti
  Skica:  "Iskoristio si [konkretna upotreba, broj iz njegovog
          naloga]. Na [plaćeni plan] dobijaš [1-2 stvari direktno
          vezane za njegovu upotrebu]. [Dugme: Pređi na Pro]"
```

Logika preskakanja (imejlovi 2 i 4 se šalju samo bez aha-momenta) je ono što sekvencu čini sistemom vezanim za životni ciklus korisnika, a ne kap-po-kap kampanjom po kalendaru. Svaki ozbiljniji imejl alat ovo podržava kroz uslovne grane ili zasnovane na događajima okidače, biraj alat koji prima događaje iz tvog proizvoda, ne samo datume.

### Ostali tokovi kroz životni ciklus korisnika (kratko)

| Tok | Okidač | Prvi potez |
|---|---|---|
| Odlasci kupaca-spasavanje | pad upotrebe (npr. aktivan korisnik 14 dana neaktivan) | check-in sa POMOĆI: "vidim da te nema, da li je [čest problem]? evo rešenja", ne popust odmah |
| Povratak neaktivnih korisnika | otkazana pretplata / istekao nalog, 30-60 dana kasnije | šta je novo od kad je otišao + jedan razlog za povratak; tek u drugom imejlu eventualna ponuda |
| Istek probnog perioda | 3 dana pre isteka probnog perioda | rezime vrednosti iz NJEGOVOG naloga ("obradio si X projekata") + šta gubi istekom + jedan poziv na akciju |

❌ Pad upotrebe → automatski imejl "Vrati se, evo 30% popusta!", učiš korisnike da je odlazak način da dobiju popust, a ne saznaješ zašto odlaze.
✅ Pad upotrebe → "Primetio sam da nisi koristio [proizvod] dve nedelje. Najčešće je razlog [X], evo kako se rešava. Ako je nešto drugo, odgovori na imejl." Popust je poslednja karta, ne prva.

Za tokove probnog perioda drži na umu industrijske raspone iz anketa (OpenView / Lenny's Bilten): probni period bez kartice konvertuje ~8-12%, sa obaveznom karticom 40%+ ali uz drastično manje prijava, istek probnog perioda sekvenca je poluga koja te raspone pomera, pa je meri kao eksperiment (Poglavlje 10).

### Higijena: pravila koja drže listu živom

- **Jedan poziv na akciju po imejlu.** Imejl sa tri dugmeta je imejl bez cilja. Ako ne možeš da kažeš koju JEDNU akciju imejl traži, ne šalji ga.
- **Tekst kao da piše čovek čoveku.** Običan tekst ili minimalan dizajn, prvo lice, kratke rečenice. Imejl koji liči na bilten se skenira; imejl koji liči na poruku se čita.
- **Lako odjavljivanje.** Vidljiv unsubscribe link u jednom kliku. Korisnik koji ne može da se odjavi klikne "spam", a to ubija isporučivost ka svima ostalima na listi.
- **Adresa za odgovor vodi u pravo sanduče.** Odgovori na imejlove kroz životni ciklus korisnika su najjeftinije istraživanje korisnika koje postoji, ne šalji sa adrese na koju korisnik ne može da odgovori.
- **Lista se gradi, ne kupuje.** Kupljena lista = spam prijave + uništen domen. Svaka adresa na listi je tu jer se sama prijavila.

### Primena odmah

Napiši svoju aktivacionu sekvencu od 5 imejlova po šablonu iznad. Rezultat rada: fajl `imejlovi/aktivaciona-sekvenca.md` u svom marketinškom repozitorijumu (struktura repozitorijuma u Poglavlju 12), gde za svaki imejl piše: okidač (konkretan događaj iz TVOG proizvoda, vezan za aha-momenat koji si definisao u Poglavlju 3), svrha u jednoj rečenici, naslov imejla, ceo tekst imejla i jedan poziv na akciju. Pravilo provere: za imejlove 2 i 4 mora pisati uslov preskakanja ("ne šalje se ako…"), a za imejl 5 konkretan PQL prag sa brojem. Ako aha-momenat i PQL prag još nemaš definisane, to je signal da se prvo vratiš na Poglavlje 3, ne da pišeš imejlove napamet.

### Najčešće greške

1. **Sekvenca po kalendaru umesto po ponašanju.** "Dan 1, dan 3, dan 7" svima isto, korisnik koji je već aktiviran dobija uputstva za početnike. Rešenje: svaki imejl posle dobrodošlice ima uslov ponašanja (poslat samo ako se X jeste/nije desilo).
2. **Tura kroz 15 funkcija u imejlu dobrodošlice.** Korisnik ne zapamti ništa i ne uradi ništa. Rešenje: dan 0 = jedan korak ka aha-momentu; sve ostalo dolazi kasnije, kad zasluži kontekst.
3. **Popust kao prvi odgovor na pad upotrebe.** Trenira korisnike na popuste i maskira pravi uzrok odlazaka kupaca. Rešenje: prvo check-in sa pomoći i pitanjem; popust tek kao poslednji korak povratak neaktivnih korisnika toka.
4. **Tri poziva na akciju i pet linkova po imejlu.** Klik se raspe, ne meriš ništa. Rešenje: jedan imejl = jedna akcija = jedno dugme; sve ostalo izbaci.
5. **No-reply adresa i sakriven unsubscribe.** Gubiš najjeftiniji povratna informacija kanal i skupljaš spam prijave. Rešenje: reply-to = tvoj inbox, odjava u jednom kliku u futeru.

### Kontrolna lista

- [ ] Imejl alat prima događaje iz proizvoda (zasnovane na događajima okidači, ne samo datumi)
- [ ] Aha-momenat i PQL prag definisani (Poglavlje 3) i prevedeni u konkretne događaje
- [ ] Aktivaciona sekvenca od 5 imejlova napisana u `imejlovi/aktivaciona-sekvenca.md`
- [ ] Imejlovi 2 i 4 imaju uslov preskakanja vezan za aha-momenat
- [ ] Imejl 5 ima konkretan PQL okidač sa brojem, ne "dan 7"
- [ ] Svaki imejl ima tačno jedan poziv na akciju
- [ ] Adresa za odgovore vodi u pravo sanduče; odjava je vidljiva u jednom kliku
- [ ] Odlasci kupaca-spasavanje tok postavljen: pad upotrebe → pomoć, ne popust
- [ ] Imejl o isteku probnog perioda koristi podatke iz korisnikovog naloga, ne generički tekst
- [ ] Konverzija svakog toka se meri i ulazi u dnevnik eksperimenata (Poglavlje 10)


---

## Poglavlje 8: Brend: odbrambena prednost koju konkurencija teško kopira u eri besplatnog sadržaja

### Šta ćeš naučiti

- Zašto je brend postao najvredniji marketinški resurs u AI eri
- Šta 95-5 pravilo znači za tvoj nedeljni marketinški raspored, i zašto verovatno radiš samo polovinu posla
- Kako da definišeš svoje prepoznatljive elemente brenda i održiš ih doslednim svuda
- Piramidu društvenog dokaza: koji dokazi vrede malo, koji vrede mnogo, i kako se penješ uz nju
- Kako solo osnivač gradi brend bez budžeta, sistemski, ne "kad stignem"

### Zašto brend, zašto sada

AI je komodifikovao prosečan sadržaj, pa se vrednost seli u ono što se ne može generisati na zahtev, distribuciju, originalne podatke, ukus i brend (detaljno u Poglavlju 5). Ovo poglavlje se bavi poslednjom, najtrajnijom stavkom sa tog spiska.

Brend je, operativno rečeno, **memorija**. Kad korisniku zatreba alat iz tvoje kategorije, koje ime mu prvo padne na pamet? Ako je odgovor "tvoje", pola prodaje je gotovo pre nego što je otvorio Google ili pitao AI asistenta. Byron Sharp (How Brands Grow) taj merljivi mehanizam razlaže na dve komponente:

1. **Mentalna dostupnost**, verovatnoća da te se kupac seti u trenutku potrebe.
2. **Fizička dostupnost**, koliko te je lako naći i kupiti kad te se seti (jasan domen, prisutnost na G2, dokumentacija koju AI modeli citiraju, veza sa Poglavljima 3 i 5).

Mali SaaS gotovo uvek ulaže sve u fizičku dostupnost (prodajnu stranicu, cenovnik, registracija) a ništa u mentalnu, greška koju ovo poglavlje ispravlja.

### 95-5 pravilo: dva posla marketinga

Istraživanje LinkedIn B2B Instituta i Ehrenberg-Bass instituta (95-5 pravilo): **otprilike 95% kupaca jedne kategorije NIJE aktivno na tržištu u datom trenutku.** Samo ~5% kupuje sada.

Posledica: marketing ima dva odvojena posla.

| | Posao 1: hvatanje (5%) | Posao 2: memorija (95%) |
|---|---|---|
| Publika | Aktivno traži rešenje sada | Imaće problem za 6-18 meseci |
| Alati | Prodajna stranica, cenovnik, search, ponovno oglašavanje, G2 profil | Sadržaj sa uglom, vođeno lično od osnivača objave, brend elementi, originalni podaci |
| Metrika | Konverzija, CAC | Brendirana pretraga, direktan saobraćaj, "Kako ste čuli za nas?" |
| Vremenski horizont | Ove nedelje | Ove godine |

Većina malih SaaS-ova radi isključivo Posao 1, i onda se čudi zašto CAC raste (inflacija plaćenih kanala, Poglavlje 6). Posao 2 je razlog što konkurent sa slabijim proizvodom dobija kupce "niotkuda": godinama je gradio memoriju, pa kupac koji uđe na tržište ide pravo kod njega.

Operativno pravilo: **u nedeljnom marketinškom rasporedu, bar polovina aktivnosti mora ciljati 95%**, sadržaj koji gradi prepoznatljivost, ne samo konverziju. Efekat meriš brendiranom pretragom, direktnim saobraćajem i poljem "Kako ste čuli za nas?" pri registraciji (pitanje o izvoru koje korisnik sam popunjava, Poglavlje 5).

### Prepoznatljivi elementi brenda: brend kao skup mašinski proverljivih pravila

Sharp-ov drugi ključni koncept: **prepoznatljivi elementi brenda**, prepoznatljivi elementi koje publika nauči da poveže s tobom. Za mali SaaS to su:

- **Ime**, uvek pisano isto, bez varijacija
- **Boja**, jedna primarna, korišćena svuda (ne "plava na sajtu, zelena na slajdovima")
- **Vizuelni potpis**, logo, tipografija, stil snimak ekranaova/ilustracija, šablon za slike objava
- **Glas i ton**, rečnik koji koristiš i rečnik koji izbegavaš, dužina rečenica, odnos prema čitaocu
- **Tagline / jednorečenična pozicija**, ista formulacija svuda (iz Poglavlja 2)

Ključna reč je **doslednost**: brend od pet dobrih elemenata koji se pojavljuju nedosledno gubi od brenda sa dva osrednja elementa koja se pojavljuju identično hiljadu puta, memorija se gradi ponavljanjem identičnog signala.

❌ Loše: logo u tri varijante boje, slogan koji se menja po inspiraciji, objave koje zvuče kao tri različite osobe.
✅ Dobro: ista boja, isti šablon, isti glas, svuda, od prodajne stranice do tiketa podrške.

U Poglavlju 11 ovi elementi postaju **mašinski čitljivi fajlovi brend priručnika** koje svaki AI agent učitava pre nego što napiše ijednu reč u tvoje ime, doslednost tada održava sistem, ali samo ako pravila ovde prvo zapišeš.

### Piramida društvenog dokaza

Poverenje se ne traži, ono se dokazuje, ali dokazi nisu jednako vredni:

| Nivo | Dokaz | Snaga | Primer |
|---|---|---|---|
| 1 (dno) | Logoi kupaca | Slaba, svi ih imaju | Traka logoa na prodajnoj stranici |
| 2 | Brojke korišćenja | Umerena | "12.000 timova koristi X" |
| 3 | Izjave sa imenom i licem | Dobra | Citat + ime + funkcija + fotografija |
| 4 (vrh) | Merljiva studija slučaja | Najjača | "Firma Y smanjila vreme obrade za 40%, evo kako" (ime, kontekst, broj, proces) |

Iznad cele piramide stoji oblik koji ne kontrolišeš direktno: **lična preporuka**. Nielsen ankete pokazuju da su preporuke ljudi koje poznaješ najpouzdaniji oblik "oglašavanja", veruje im ~88-92% ispitanika. Zato je vrhunski posao društvenog dokaza zapravo retencioni posao: proizvod koji oduševljava pravi preporuke koje nijedan budžet ne može kupiti (petlje preporuka, Poglavlje 4).

Kako se penješ uz piramidu:

```
PROCES: od korisnika do studije slučaja (15 min nedeljno)

1. OKIDAČ: pohvala (imejl, direktna poruka, podrška) ili merljiv rezultat
   u proizvodu.
2. PITAJ ISTOG DANA: "Smem li ovo da citiram javno, sa tvojim
   imenom?", pristanak u pisanoj formi.
3. PRODUBI jednim pitanjem: "Koji broj se promenio otkad
   koristiš proizvod?"
4. ZAPIŠI u dnevnik dokaza fajl: citat, ime, funkcija, firma, broj,
   datum, dozvola, link.
5. OBJAVI na prodajnoj stranici → posle 3-4 izjave istog tipa, najbolju
   razradi u studiju slučaja od 500 reči.
```

Higijena uz ovo: popunjen G2/Capterra profil sa svežim recenzijama, B2B kupci ih konsultuju pre razgovora sa bilo kim (Poglavlje 5). Posle svake uspešne interakcije zamoli za recenziju, sistemski, ne stidljivo.

### Brend bez budžeta: četiri poluge solo osnivača

Veliki brend budžet ne možeš kopirati. Ali četiri stvari velike firme po pravilu rade gore od tebe:

1. **Doslednost**, tebi ne treba odobrenje tri odeljenja da bi sve izgledalo i zvučalo isto. Definiši elemente brenda jednom (tabela ispod) i primenjuj ih svuda.
2. **Ugao koji samo ti imaš**, tvoje iskustvo, podaci iz proizvoda, specifičan stav o kategoriji. Originalno istraživanje ili podaci koje samo ti imaš su magnet za linkove i AI citate (Poglavlje 5).
3. **Javni dokazi korisnika**, piramida iznad, građena nedeljnim ritmom.
4. **Lice osnivača**, lični profil nosi domet koji nalozi kompanije nemaju (mehanika ličnog nastupa osnivača detaljno u Poglavlju 5). Tvoje lice i glas su prepoznatljiv element brenda koji konkurencija doslovno ne može kopirati.

Brend se ne gradi kampanjom nego ritmom: ista boja, isti glas, isti ugao, nova vrednost, svake nedelje, godinu dana. Dosadno za tebe, nezaboravno za tržište.

### Primena odmah

Napravi **inventar prepoznatljivih elemenata brenda** za svoj proizvod, direktan ulaz za brend priručnik u Poglavlju 11. Za svaki element oceni stanje: imam / nemam / nedosledno.

```markdown
# Inventar prepoznatljivih elemenata brenda: [proizvod], [datum]

| Element            | Stanje (imam/nemam/nedosledno) | Trenutna definicija | Akcija |
|--------------------|--------------------------------|---------------------|--------|
| Ime (pisanje)      |                                |                     |        |
| Primarna boja      |                                | hex:                |        |
| Logo + varijante   |                                |                     |        |
| Tipografija        |                                |                     |        |
| Vizuelni šablon objava |                            |                     |        |
| Glas i ton (3 prideva + 3 zabranjene reči) |        |                     |        |
| Tagline / pozicija (iz Poglavlja 2) |               |                     |        |
| Lice osnivača (foto, bio, profil) |                 |                     |        |

## Tačke kontakta za proveru doslednosti
- [ ] Prodajna stranica  - [ ] Proizvod (UI)  - [ ] Imejl potpis i sekvence
- [ ] Društveni profili (lični + nalog firme)  - [ ] G2/Capterra
- [ ] Dokumentacija  - [ ] Slajdovi/demo  - [ ] Support odgovori
```

Rezultat: fajl `inventar-elemenata-brenda.md` sa popunjenom tabelom i najviše 5 akcija za "nemam" i "nedosledno" stavke, rok dve nedelje.

### Najčešće greške

1. **Sav marketing cilja 5% koji kupuju sada.** Rešenje: nedeljni raspored deli pola-pola između konverzije i memorije; napredak meri signalima opisanim gore.
2. **Rebrendiranje iz dosade.** Tebi je tvoja boja i slogan dosadila posle šest meseci, tržište ih je tek počelo primećivati. Rešenje: elementi brenda se menjaju samo uz jak razlog (repozicioniranje iz Poglavlja 2), ne uz inspiraciju.
3. **Društveni dokaz zaglavljen na dnu piramide.** Traka logoa i ništa više. Rešenje: dnevnik dokaza proces iz ovog poglavlja, 15 minuta nedeljno, cilj jedna merljiva studija slučaja kvartalno.
4. **Izjave bez imena i broja.** "Odličan alat!, M.P." ne dokazuje ništa. Rešenje: bez imena, funkcije i po mogućstvu broja, ne objavljuj; radije jedna jaka izjava nego deset anonimnih.
5. **Brend tretiran kao dizajn, ne kao sistem.** Lep logo, a glas se menja iz objave u objavu. Rešenje: glas i ton su element istog ranga kao boja, definiši ih u inventaru, pa svaki sadržaj proveravaj prema njima.

### Kontrolna lista

- [ ] Razumem 95-5 podelu i moj nedeljni raspored ima aktivnosti za obe grupe
- [ ] Inventar prepoznatljivih elemenata brenda popunjen i spreman kao ulaz za brend priručnik (Poglavlje 11)
- [ ] Za svaki "nemam/nedosledno" element postoji akcija sa rokom
- [ ] Sve tačke kontakta proverene na doslednost (lista u šablonu iznad)
- [ ] Proof-log fajl postoji i ima proces: okidač → dozvola → broj → objava
- [ ] G2/Capterra profil popunjen, postoji ritam traženja recenzija
- [ ] Pratim brendiranu pretragu, direktan saobraćaj i "Kako ste čuli za nas?" kao signale mentalne dostupnosti (Poglavlje 5)


---

## Poglavlje 9: Lansiranja i momentum: serija, ne događaj

Najskuplja zabluda solo osnivača: "veliki dan lansiranja". Mesecima ćutiš, gradiš u tajnosti, pa jednog jutra objaviš, i ništa. Realnost je drugačija: lansiranje nije događaj, nego serija talasa pažnje koje sistematski praviš i hvataš. Lista čekanja → zatvorena beta → javno lansiranje → lansiranja funkcionalnosti kao stalni ritam. Svaki talas ima svoj posao i svoj rezultat rada za sledeći.

### Šta ćeš naučiti

- Zašto je lansiranje serija od četiri talasa, a ne jedan dan
- Kako da napraviš lista čekanja sa mehanikom preporuke koja sama raste
- Kako zatvorena beta proizvodi sirovinu za prodajnu stranicu (dokazi, izjave)
- Product Hunt mehaniku, i sistem koji hvata pažnju pre nego što ispari za ~48h
- Ritam lansiranja funkcionalnosti: kako svaku značajnu funkcionalnost pretvoriš u mini-lansiranje

### Talas 1: Lista čekanja: prodaja pre proizvoda

Stranica liste čekanja je najjeftiniji test tražnje koji postoji: jedna stranica, jedno obećanje, jedno polje za imejl. Ako ne možeš da nateraš ljude da ostave imejl za besplatnu stvar koja stiže, nećeš ih naterati ni da plate gotovu.

Operativni minimum:

1. **Stranica**, naslov po formuli iz Poglavlja 2 (problem + ishod, ne lista funkcionalnosti), jedno polje za imejl i jedan poziv na akciju, bez navigacije i distrakcija.
2. **mehanika preporuka za poziciju u redu**, posle prijave, korisnik dobija jedinstveni link: "Podeli i preskoči red." Svaka uspešna preporuka ga pomera napred. Ovo je ista logika obostranog interesa koju je Dropbox program preporuka pretvorio u udžbenički primer (Poglavlje 4), nagrada za obe strane, vezana za vrednost proizvoda. Kod liste čekanja je nagrada raniji pristup.
3. **Imejl od prvog dana**, lista čekanja bez komunikacije je groblje. Jedan imejl na 2-3 nedelje: napredak, snimak ekrana, pitanje. Detalji sekvenci u Poglavlju 7.

```
Šablon lista čekanja potvrde (imejl #1):

Predmet: Na listi si, pozicija #{{broj}}

Hvala što si se prijavio za {{proizvod}}.
Trenutno si #{{broj}} u redu.

Hoćeš ranije? Podeli svoj link, svaka prijava
preko njega te pomera napred:
{{referral_link}}

Sledeće 2 nedelje šaljem kratak update o napretku., {{ime osnivača}}
```

Podsetnik na K-faktor iz Poglavlja 4: broj pozivnica po korisniku × stopa konverzije pozivnice. Lista čekanja sa mehanikom preporuke je najlakše mesto da ga prvi put izmeriš, i K od 0,3–0,5 značajno obara efektivni CAC (orijentir industrije), jer deo liste stiže besplatno.

### Talas 2: Zatvorena beta: fabrika dokaza

Cilj bete nije "testiranje". Cilj bete su dve stvari: brz povratna informacija ciklus i **sirovina za javno lansiranje**, izjave, brojke, studije upotrebe.

- **Mali broj, idealni korisnici.** 10-30 ljudi koji tačno odgovaraju tvom ICP-u (Poglavlje 2). Ne 500 nasumičnih prijava, sa 500 ljudi ne možeš da razgovaraš, a razgovor je poenta.
- **Brz ciklus.** Nedeljni ritam: pusti verziju → posmatraj gde zapinju (TTV iz Poglavlja 3) → razgovor sa 3-5 korisnika → ispravi → ponovi.
- **Žetva dokaza.** Posle svake dobre reakcije, traži dozvolu da je citiraš. Konkretno pitanje daje konkretan citat:

```
❌ "Da li ti se sviđa proizvod?" → "Da, super je." (neupotrebljivo)
✅ "Šta si radio pre ovoga i koliko ti je trajalo?
    A sada?" → "Ranije sat vremena ručno, sada 10 minuta."
    (citat koji prodaje, ide direktno na prodajnu stranicu)
```

Beta je i trenutak za Sean Ellis PMF test (Poglavlje 1): pitaj korisnike koliko bi bili razočarani da proizvod nestane, ako bar 40% kaže "veoma razočaran", imaš signal da je vreme za javni talas. Ako nemaš, javno lansiranje će samo glasnije objaviti proizvod koji ne drži ljude.

### Talas 3: Javno lansiranje: Product Hunt mehanika i sistem koji hvata

Product Hunt (i slične platforme) je vredan špic pažnje za early-adopter, developersku i PM publiku. Ali ključna činjenica (industrijska procena): **bez sistema koji pažnju hvata, efekat ispari za ~48 sati.** Špic saobraćaja koji padne na nespremnu stranicu je potrošen metak.

Mehanika dana: prvi sati su kritični za momentum, rani angažman gura listing više, pa zagrej zajednicu unapred (lista čekanja, beta korisnici, tvoja mreža) da znaju da je dan D i gde da te nađu. Ne traži eksplicitno glasove po pravilima platforme, traži da pogledaju i prokomentarišu iskreno.

Sistem koji hvata (mora postojati PRE dana D):

| Element | Zašto | Provera |
|---|---|---|
| Uvođenje korisnika doteran | Špic saobraćaja × loš TTV = potrošeni posetioci | Novi korisnik stiže do aha-momenta bez tvoje pomoći (Poglavlje 3) |
| Prikupljanje imejl adresa na svakom koraku | Posetilac koji ode bez imejla je izgubljen zauvek | I oni koji se ne registruju mogu da ostave imejl (npr. za vodič/resurs) |
| Follow-up sekvenca spremna | Pažnja traje ~48h, odnos traje koliko ga lista nosi | Aktivaciona sekvenca iz Poglavlja 7 uključena za nove registracije |
| "Kako si čuo za nas?" polje | Lansiranje saobraćaj stiže kroz nevidljive preporuke koji analitika ne vidi (praksa pitanje o izvoru koje korisnik sam popunjava, Poglavlje 5) | Polje pri registraciji, odgovori se loguju |
| Founder prisutan ceo dan | Komentari i pitanja na listingu su deo listinga | Kalendar blokiran, odgovaraš u minutima |

### Talas 4: Ritam lansiranja funkcionalnosti: proizvod koji vidljivo živi

Posle javnog lansiranja, najveća greška je tišina. Svaka značajna funkcionalnost je mini-lansiranje sa tri obavezna dela:

1. **Objava**, kratka, sa vizuelnim dokazom (snimak ekrana, GIF, 30-sekundni snimak): šta sada možeš što juče nisi mogao.
2. **Imejl segmentu kome znači**, ne celoj listi. Funkcionalnost za timove ide korisnicima koji rade u timu; ostalima je šum koji troši poverenje.
3. **Dnevnik izmena zapis**, javna stranica "šta je novo". Niko je ne čita od korice do korice, ali svaki posetilac koji je otvori vidi: proizvod živi, neko ga aktivno gradi. To je marketing poruka sama po sebi, i hrana za AI pretrage koje citiraju izvore (Poglavlje 5).

```
Šablon mini-lansiranje funkcionalnosti objave:

[Problem u 1 rečenici, rečima korisnika]
[Šta smo izbacili, 1 rečenica]
[GIF/snimak ekrana pre → posle]
[1 rečenica: kome ovo menja dan]
[Link]
```

Ritam je važniji od veličine: mala funkcionalnost svake 2-3 nedelje gradi više momentuma nego mega-objava dvaput godišnje, svaka objava je nova prilika da te neko prvi put vidi (95-5 logika iz Poglavlja 8: većina publike danas ne kupuje, ali pamti ko se stalno pojavljuje).

### Lansiranje checklist tabela

| Faza | Zadaci |
|---|---|
| **Pre (2+ nedelje)** | Uvođenje korisnika testiran na 5 svežih ljudi; aktivaciona imejl sekvenca uključena; izjave iz bete na prodajnoj stranici; lista čekanja/beta lista obaveštena o datumu; "Kako si čuo za nas?" polje aktivno |
| **Na dan** | Objava rano ujutru po vremenu platforme; lična poruka listi i mreži; osnivač odgovara na svaki komentar; analitika i registracije se prate uživo |
| **Posle 48h** | Naknadni imejl svima koji su se registrovali a nisu aktivirani; zahvalnica zajednici sa brojkama; zabeleži: posete, registracije, aktivacije, izvore ("kako si čuo") |
| **Posle 2 nedelje** | Zadržavanje korisnika u kohorti lansiranja vs. ranije kohorte; razgovor sa 3-5 novih korisnika; odluka: šta je sledeći talas (mini-lansiranje funkcionalnosti) i datum |

### Primena odmah

Isplaniraj svoj sledeći talas, danas, u jednom fajlu `lansiranje-plan.md`:

- **Ako proizvod još nije javan:** napravi stranicu liste čekanja. Rezultat rada: objavljena stranica sa naslovom po formuli iz Poglavlja 2, imejl poljem, linkom za preporuku ("podeli → preskoči red") i šablonom prvog imejla (gore).
- **Ako je proizvod javan:** izaberi sledeću funkcionalnost vrednu mini-lansiranja. Rezultat rada: popunjen šablon objave, definisan segment liste koji dobija imejl, zapis u dnevniku izmena, i datum u kalendaru, najkasnije za 3 nedelje.

U oba slučaja prepiši lansiranje checklist tabelu u svoj fajl i popuni je svojim stavkama, to postaje šablon koji u Poglavlju 12 pretvaraš u rutinu marketinškog OS-a.

### Najčešće greške

1. **Lansiranje kao jedan dan.** Sva energija u dan D, posle tišina. → Rešenje: planiraj seriju, pre dana D znaj koji je sledeći talas i kada.
2. **Špic bez sistema koji hvata.** Product Hunt saobraćaj padne na sirov uvođenje korisnika i nestane za ~48h (industrijska procena). → Rešenje: tabela "sistem koji hvata" je uslov za objavu, ne opcija.
3. **Beta sa pogrešnim ljudima.** 300 nasumičnih testera, nula upotrebljivog povratnih informacija. → Rešenje: 10-30 ljudi iz ICP-a sa kojima stvarno razgovaraš svake nedelje.
4. **Lista čekanja koja ćuti.** Lista skupljena pa zaboravljena tri meseca, na dan lansiranja imejl stiže hladnoj publici. → Rešenje: kratko obaveštenje na 2-3 nedelje, kratak i konkretan.
5. **Objave o funkcionalnostima celoj listi.** Svako ažuriranje poslato svima → opadanje otvaranja, odjave. → Rešenje: segmentacija, imejl ide samo onima kojima funkcionalnost menja rad.

### Kontrolna lista

- [ ] Znam u kom sam talasu (lista čekanja / beta / javno lansiranje / ritam funkcionalnosti) i koji je sledeći
- [ ] Stranica liste čekanja ima mehaniku preporuke "podeli → preskoči red" i prvi imejl spreman
- [ ] Beta grupa je 10-30 ljudi iz ICP-a, sa nedeljnim povratna informacija ciklusom
- [ ] Imam bar 3 upotrebljiva citata/dokaza iz bete na prodajnoj stranici
- [ ] Sistem koji hvata je kompletan: uvođenje korisnika, prikupljanje imejl adresa, sekvenca naknadnih poruka, "kako si čuo za nas?"
- [ ] Datum javnog lansiranja je određen i zajednica zagrejana unapred
- [ ] Posle-lansiranje koraci (48h i 2 nedelje) su u kalendaru pre dana D
- [ ] Ritam mini-lansiranja funkcionalnosti definisan: objava + imejl segmentu + dnevnik izmena, bar jednom u 3 nedelje


---

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


---

## Poglavlje 11: Brend priručnik kao algoritam: ustav za mašine

### Šta ćeš naučiti

- Zašto je AI agent odličan izvršilac, a loš čuvar ukusa, i kako se to rešava tekstom, ne nadom
- Strukturu mašinski čitljivog brend priručnika: 7 markdown fajlova sa svrhom, sadržajem i primerom za svaki
- Zašto je `04-glas-i-ton.md` najvažniji fajl i zašto agenti uče iz ❌/✅ parova više nego iz prideva
- Test brend priručnika: kako za sat vremena saznaš gde ti je brend priručnik rupav
- Kako brend priručnik verzionišeš kroz git i pretvaraš svaku ispravku u novo pravilo

### Problem: agent bez ustava

Do sada si gradio motore rasta (Deo II) i eksperimentalni pogon (Poglavlje 10). Sledeći korak, autonomni marketinški OS iz Poglavlja 12, ne sme da krene bez ovog poglavlja. Razlog je jednostavan: AI agent izvršava savršeno i prosuđuje loše. Daj mu zadatak "napiši objavu o novoj funkciji" i dobićeš gramatički besprekoran tekst koji zvuči kao bilo koji SaaS na svetu, uzvičnici, "uzbuđeni smo", emoji raketa. Ne zato što je agent loš, nego zato što nema tvoj ukus. Ukus se ne prenosi telepatijom; prenosi se tekstom.

Princip već poznaješ iz gradnje proizvoda: CLAUDE.md je fajl koji se učitava na početku svake Claude Code sesije i daje agentu trajni kontekst o projektu. Brend priručnik je isti obrazac primenjen na marketing, folder fajlova koji svaka rutina, svaki agent i svaki prompt čita PRE nego što napiše ijednu reč u tvoje ime. Nije PDF za investitore. To je izvršna specifikacija brenda.

Praktična posledica: brend priručnik živi u repozitorijumu, pored koda, kao `brandbook/` folder. Za v1 ga slobodno napravi u repozitorijumu svog proizvoda; u Poglavlju 12 folder se seli (kopijom ili kao git submodule) u zasebni `marketing-os/` repozitorijum, putanja u promptovima je uvek `brandbook/`. Tamo svaka zakazana rutina počinje instrukcijom "pročitaj sve fajlove iz brandbook/ pre rada".

### Sedam fajlova

| Fajl | Svrha | Pitanje na koje odgovara |
|---|---|---|
| `01-identitet.md` | Ko smo | Kako brend "misli"? |
| `02-icp.md` | Za koga | Kome se obraćamo, a kome NE? |
| `03-pozicioniranje.md` | Šta tvrdimo | Koju poruku ponavljamo i čime je dokazujemo? |
| `04-glas-i-ton.md` | Kako zvučimo | Kako se ta poruka izgovara, po kanalu? |
| `05-zabranjeno.md` | Crvene linije | Šta se NIKAD ne kaže? |
| `06-zlatni-primeri.md` | Few-shot biblioteka | Kako izgleda "odlično" kod nas? |
| `07-vizuelni-standardi.md` | Kako izgledamo | Koji su naši prepoznatljivi elementi brenda? |

Primeri ispod koriste izmišljeni SaaS "Reportly" (automatski klijentski izveštaji za male agencije).

**01-identitet.md, misija, vrednosti, ličnost**

Sadrži misiju u jednoj rečenici, 3-5 vrednosti i ličnost brenda u 5 prideva. Ključno: svaki pridev MORA imati objašnjenje šta znači u praksi, sam pridev je beskoristan agentu ("profesionalan" za banku i za skejt brend znači suprotno).

```markdown
## Ličnost brenda (5 prideva)
1. Direktan, prva rečenica nosi poentu. Bez zagrevanja, bez "u današnjem svetu".
2. Konkretan, svaka tvrdnja ima broj, primer ili korak. "Štedi vreme" je zabranjeno; "izveštaj za 4 minuta umesto 3 sata" je dozvoljeno.
3. Smiren, ne vičemo. Nula uzvičnika u naslovima, maksimum jedan po tekstu.
4. Duhovit na svoj račun, šala ide na naš trošak ili na trošak problema, nikad na trošak korisnika ili konkurenta.
5. Tehnički pismen, ne pojednostavljujemo do netačnosti. Čitalac je pametan, samo nema vremena.
```

**02-icp.md, ko jeste i ko nije kupac**

Destilat ICP-a iz Poglavlja 2: segment, bolovi, rečnik kojim kupac sam opisuje problem (citati iz pravih razgovora), i, jednako važno, eksplicitna lista ko NIJE kupac. Anti-ICP sprečava agenta da širi poruku na publiku koja nikad neće platiti.

```markdown
## NIJE naš kupac
- Freelancer sa 1-2 klijenta (izveštaj mu ne treba, rešava ga imejlom)
- Enterprise agencija 50+ ljudi (traži SSO, procurement, custom ugovore, nemamo)
- Bilo ko kome je glavna želja "white-label kontrolna tabla", to ne gradimo (vidi 05-zabranjeno.md)
```

**03-pozicioniranje.md, izjava, stubovi, dokazi**

Poziciona izjava (Dunford format iz Poglavlja 2) plus tačno 3 stuba poruke. Svaki stub nosi tvrdnju i dokaze: brojku iz proizvoda, citat korisnika, demo link. Agent bez dokaza izmišlja, ovaj fajl mu daje municiju da ne mora.

```markdown
## Stub 2: Brzina do prvog izveštaja
Tvrdnja: prvi izveštaj pre nego što popiješ kafu.
Dokazi:
- medijan TTV novih naloga: 6 min (naša analitika, ažurirano 2026-05)
- citat: "Poslao sam klijentu izveštaj 10 minuta posle registracije.", Marko, osnivač agencije X
- demo snimak: /assets/demo-first-report.mp4
```

**04-glas-i-ton.md, najvažniji fajl**

Pravila glasa (rečenice kratke, aktivan rod, brojevi umesto prideva...) plus ono što stvarno radi: ❌/✅ parovi primera PO KANALU, minimum 3 para po kanalu. Agenti uče iz primera neuporedivo bolje nego iz opisa, par "loše → dobro" je najgušći format prenosa ukusa koji postoji. Isti sadržaj zvuči različito na LinkedInu, u imejlu i u poruci u aplikaciji, zato parovi idu po kanalu.

```markdown
## LinkedIn
❌ "Uzbuđeni smo što najavljujemo revolucionarnu novu funkciju! 🚀"
✅ "Klijent te pita 'šta ste radili ovog meseca?' u 16:55 petkom. Od danas: izveštaj u 3 klika."

❌ "Reportly je sveobuhvatno rešenje za reporting potrebe modernih agencija."
✅ "Pregledali smo 40 agencijskih izveštaja. 31 je imao copy-paste grafikon iz prošlog meseca. Evo zašto se to dešava."

❌ "Ne propustite naš webinar! Prijavite se odmah!"
✅ "U četvrtak pokazujem kako tri agencije rade mesečne izveštaje za pod 15 minuta. Snimak šaljem svima koji se prijave."

## Imejl (životni ciklus korisnika)
❌ Subject: "Bilten #14, novosti iz Reportly-ja"
✅ Subject: "Tvoj prvi izveštaj čeka na 80%"
(...minimum 3 para i ovde, pa za svaki sledeći kanal koji koristiš)
```

**05-zabranjeno.md, crvene linije**

Četiri liste: teme koje se ne diraju (politika, tuđi neuspesi...), fraze koje se ne koriste (tvoja lista klišea: "game-changer", "revolucionarno", "uzbuđeni smo"...), obećanja koja se ne daju (plan puta datumi, "nikad nećemo poskupeti", rezultati koje proizvod ne garantuje) i pravila o konkurenciji: konkurenta pominjemo samo činjenično i proverivo, nikad podrugljivo, nikad nagađanjem o njihovim manama. Ovo je fajl koji agent čita kao hard constraint, sve ostalo je stil, ovo je zakon.

```markdown
## Zabranjene fraze
- "game-changer"
- "uzbuđeni smo što najavljujemo"
- "revolucionarno" (i srodno: "disruptivno", "next-level")

## Obećanja koja se ne daju
- datumi iz plana razvoja ("stiže u junu")
- "nikad nećemo poskupeti"
```

**06-zlatni-primeri.md, biblioteka primera**

Deset najboljih komada marketinga koje si ikad napravio, objave, imejlovi, sekcije prodajne stranice, svaki sa jednom rečenicom ZAŠTO je dobar ("ovaj imejl je imao najviše odgovora jer postavlja jedno konkretno pitanje"). Ovo je biblioteka primera: agent imitira ono što vidi, pa mu pokaži najbolje. Fajl raste, svaki novi komad koji prebaci prosek ulazi unutra, najslabiji ispada. Deset je plafon: više primera razvodnjava signal.

```markdown
## Primer 3: imejl, najviše odgovora do sada
Subject: "Jedno pitanje pre nego što obrišeš nalog"
Telo: "Vidim da nisi napravio nijedan izveštaj. Šta te je zaustavilo?
Odgovori u jednoj rečenici, čitam svaki imejl."
ZAŠTO: postavlja jedno konkretno pitanje i ništa ne prodaje.
```

**07-vizuelni-standardi.md, prepoznatljivi elementi brenda**

Tekstualni zapis vizuelnog identiteta iz Poglavlja 8: hex kodovi boja i kada se koja koristi, fontovi po hijerarhiji, pravila slika (npr. "snimak ekrana proizvoda uvek u tamnom modu, bez okvira za prikaz"), logo pravila i šta se NE radi (gradijenti, generičke fotografije ljudi koji se rukuju). I generativni alati za slike primaju tekstualne instrukcije, ovaj fajl je njihov prompt-prefiks.

### Test brend priručnika

Brend priručnik nije gotov kad je napisan, nego kad prođe test:

1. Otvori svežu agentsku sesiju koja NIKAD nije videla tvoj marketing (bez istorije, bez memorije). Praktično: iskopiraj `brandbook/` u prazan folder van projekta i pokreni novu sesiju tamo, ili koristi `claude -p` sa eksplicitnim nalogom da čita samo `brandbook/`, sesija u tvom repozitorijumu bi povukla CLAUDE.md i memoriju, pa test ne bi bio slep.
2. Daj joj samo `brandbook/` folder i zadatak: "Napiši 3 objave za [kanal] o [funkciji X], strogo po brend priručniku."
3. Pročitaj rezultat sa jednim pitanjem: da li bih OVO potpisao i objavio bez izmena?

Ako ne bi, brend priručnik je rupav, ne agent. Svaka ispravka koju napraviš je dijagnoza: ispravio si uzvičnik → pravilo o uzvičnicima nije dovoljno jasno; ispravio si frazu → ona ide u `05-zabranjeno.md`; prepisao si celu rečenicu → original i tvoja verzija postaju novi ❌/✅ par u `04-glas-i-ton.md`. Ponavljaj ciklus dok dve od tri objave ne prolaze bez izmena. Tako brend priručnik uči, isto kao što CLAUDE.md raste sa svakom lekcijom iz koda.

### Verzionisanje: brend priručnik je živ dokument

Brend priručnik se menja, pozicioniranje se izoštrava, ICP se sužava, glas sazreva. Zato živi u gitu:

- Svaka izmena je commit sa porukom koja objašnjava ZAŠTO ("zabranjena fraza 'AI-powered', 3 korisnika u intervjuima rekla da zvuči prazno").
- `git log brandbook/` postaje istorija odluka o brendu, novi saradnik (ljudski ili mašinski) može da pročita ne samo pravila nego i njihovo poreklo.
- Veće zaokrete (novo pozicioniranje) radi kroz granu i pregledaj diff pre merge-a, kao i svaki kod.

### Primena odmah

Napravi `brandbook/` folder u repozitorijumu svog proizvoda i napiši v1 svih 7 fajlova, makar po pola strane svaki. Ne čekaj savršenstvo: pola strane pravila bolje je od nule. Redosled: kreni od `04-glas-i-ton.md` (uzmi 3 svoja stara teksta koja voliš i 3 koja ne voliš, to su ti prvi ❌/✅ parovi), pa `02-icp.md` i `03-pozicioniranje.md` (destiluj iz rada u Poglavlju 2), ostalo popuni za njima. Zatim sprovedi test: sveža sesija + brend priručnik + zadatak "3 objave". Svaku ispravku vrati u fajlove i commituj. Rezultat rada: `brandbook/` folder sa 7 fajlova u gitu + 3 test objave + bar 3 nova pravila/para nastala iz testa.

### Najčešće greške

1. **Pridevi bez operacionalizacije.** "Prijateljski, profesionalan, inovativan" ne znači ništa mašini (ni čoveku). Rešenje: svaki pridev dobija rečenicu "u praksi to znači..." i bar jedan ❌/✅ par.
2. **Brend priručnik kao PDF artefakt.** Napisan jednom, otvoren nikad. Rešenje: markdown u repozitorijumu, učitava se u svaku sesiju, menja se commitom, dokument koji se ne čita mašinski ne postoji za agente.
3. **Samo pozitivna pravila, bez zabrana.** Agent popunjava praznine generičkim SaaS govorom. Rešenje: `05-zabranjeno.md` sa konkretnom listom fraza, zabrane su izvršivije od preporuka.
4. **Preskočen test.** Brend priručnik proglašen gotovim bez provere na slepo. Rešenje: test sa 3 objave pre nego što ijedna rutina iz Poglavlja 12 krene da radi.
5. **Mrtva biblioteka primera.** `06-zlatni-primeri.md` napunjen jednom i zaboravljen, pa agent imitira tebe od pre godinu dana. Rešenje: mesečni ritual (uklopi ga u nedeljni pregled iz Poglavlja 10), najbolji novi komad ulazi, najslabiji izlazi.

### Kontrolna lista

- [ ] `brandbook/` folder postoji u repozitorijumu i pod gitom je
- [ ] Svih 7 fajlova napisano, minimum pola strane po fajlu
- [ ] Svaki od 5 prideva ličnosti ima objašnjenje "šta to znači u praksi"
- [ ] `02-icp.md` sadrži eksplicitnu "NIJE naš kupac" listu
- [ ] Svaki stub poruke u `03-pozicioniranje.md` ima bar 2 dokaza
- [ ] `04-glas-i-ton.md` ima minimum 3 ❌/✅ para za svaki kanal koji koristiš
- [ ] `05-zabranjeno.md` pokriva: teme, fraze, obećanja, govor o konkurenciji
- [ ] `06-zlatni-primeri.md` ima do 10 primera, svaki sa "zašto je dobar"
- [ ] Test sproveden: sveža sesija + brend priručnik + 3 objave
- [ ] Bar 2 od 3 test objave prolaze bez izmena (ili je iteracija u toku)
- [ ] Svaka ispravka iz testa vraćena u brend priručnik kao pravilo ili ❌/✅ par
- [ ] Commit poruke objašnjavaju ZAŠTO se pravilo menja


---

## Poglavlje 12: Autonomni marketinški OS: arhitektura i implementacija

Sve dosad, metrike, pozicioniranje, petlje, kanali, eksperimenti, brend priručnik, bili su delovi. Ovo poglavlje ih sklapa u mašinu. Autonomni marketinški OS je sistem u kom AI agenti po zakazanom rasporedu rade proizvodnju, analizu i nadzor; brend priručnik iz Poglavlja 11 im je ustav; a ti, čovek, držiš kapije objavljivanja. Ništa ne izlazi u javnost bez tvog potpisa. Ali sve PRE tog potpisa radi samo.

Da raščistimo odmah: ovo nije "AI radi marketing umesto tebe". To je preterana verzija koja se završava generičkim sadržajem koji platforme i čitaoci ignorišu (videli smo u Poglavlju 5, AI je komodifikovao prosečan sadržaj). Ovo je verzija praktičara: ti i dalje odlučuješ ŠTA i ZAŠTO; sistem radi rutinski deo KAKO, i to svakog dana, bez tvoje radne memorije kao uskog grla.

### Šta ćeš naučiti

- Arhitekturu OS-a od 5 komponenti: mozak, čula, ruke, srce, kapije
- Tačnu strukturu repozitorijuma `marketing-os/` koju kopiraš i koristiš
- Dva kompletna prompta rutina (nedeljni izveštaj metrika; nacrti objava) spremna za upotrebu
- Tabelu nivoa autonomije: šta agent sme sam, šta uz agent za proveru kvalitetaa, šta nikad bez tebe
- Sigurnosni prekidač, nedeljni pregled i metrike kojima meriš sam OS

### Arhitektura: organizam sa pet komponenti

OS najlakše razumeš kao organizam. Pet komponenti, svaka sa jednom odgovornošću:

| Komponenta | Analogija | Šta je u praksi |
|---|---|---|
| 1. MOZAK | dugoročna memorija i vrednosti | `brandbook/` + `strategija/`, fajlovi koje svaka rutina učitava PRVE |
| 2. ČULA | šta organizam opaža | `data/`, izveštaji metrika, analitika sajta, recenzije, pominjanja, konkurencija |
| 3. RUKE | šta proizvodi | agenti-rutine: nacrti objava i imejlova, SEO stranice, izveštaji, analize |
| 4. SRCE | ritam koji sve pokreće | cron raspored: `/schedule` rutine, GitHub Actions ili `claude -p` iz cron-a |
| 5. KAPIJE | svesna odluka | TI, jedina instanca koja pušta sadržaj u javnost |

**1. MOZAK, `brandbook/` + `strategija/`.** Brend priručnik (7 fajlova iz Poglavlja 11) definiše ko si, kako zvučiš i šta nikad ne radiš. `strategija/` dodaje ono što se menja kvartalno: ciljevi kvartala, tematski stubovi sadržaja (3-5 tema koje sistematski pokrivaš), ICP. Pravilo je isto kao CLAUDE.md obrazac iz razvoja softvera, fajl koji se učitava na početku svake sesije i daje agentu trajni kontekst. Zato SVAKI prompt rutine počinje istom rečenicom: "Prvo pročitaj sve fajlove u brandbook/ i strategija/." Bez toga dobijaš generičkog agenta sa amnezijom.

**2. ČULA, `data/`.** Fajlovi koje rutine pune i čitaju: nedeljni izvoz metrika (MRR, odlasci kupaca, aktivacija, kontrolna tabla iz Poglavlja 1), izvoz iz analitike sajta, nove G2/Capterra recenzije, pominjanja brenda, beleške o konkurenciji. Format: markdown ili CSV, jedan fajl po izvoru, sa datumom. Ako alat ima MCP konektor (Slack, Notion, Gmail…), agent može da čita direktno; ako nema, ti ili skripta jednom nedeljno ubacite izvoz u `data/`. Bitno je da čula postoje, agent koji ne vidi brojke piše napamet.

**3. RUKE, agenti-rutine.** Svaka rutina je jedan prompt sa jasnim ulazom (koje fajlove čita) i izlazom (koji fajl piše i gde). Rutine proizvode NACRTE i ANALIZE, nikad objave. Claude Code čita i piše fajlove, pokreće komande i koristi paralelne subagente, što znači da jedna rutina može npr. paralelno da analizira tri konkurenta pa spoji nalaze.

**4. SRCE, cron ritam.** Tri načina da rutina kuca:
- `/schedule`, Routines: zakazani agenti u oblaku koji rade po zakazanom rasporedu i kad ti je računar ugašen. Najjednostavniji put za solo osnivača.
- GitHub Actions, automatizacija vezana za repozitorijum: na svaki push/PR ili po zakazanom rasporedu. Prirodno ako ti marketing-os već živi na GitHubu.
- `claude -p "..."`, neinteraktivno pokretanje jednog zadatka, pozivaš ga iz bilo kog sistema za zakazano pokretanje (server, lokalni cron).
- Bonus za rad u sesiji: `/loop` ponavlja zadatak unutar otvorene sesije (fiksni interval ili dinamički), korisno za dan lansiranja, ne za trajni pogon.

Nedeljni raspored koji preporučujem kao polaznu tačku:

| Kad | Rutina | Prompt | Izlaz |
|---|---|---|---|
| pon 07:00 | Nedeljni izveštaj metrika + predlozi | Rutina 1 (niže) | `izvestaji/YYYY-MM-DD-nedeljni.md` |
| uto 08:00 | Nacrti sadržaja po planu sadržaja | Rutina 2 (niže) | 3 fajla u `content/nacrti/` |
| sre 09:00 | Competitor scan | Dodatak B9 | `data/konkurencija/YYYY-MM-DD.md` |
| čet 08:00 | Nacrti sadržaja (druga tura) | Rutina 2 (niže) | 3 fajla u `content/nacrti/` |
| pet 16:00 | Retrospektiva eksperimenata + predlozi za sledeću nedelju | Dodatak B10 | dopuna `eksperimenti/log.md` + predlozi u `eksperimenti/backlog.md` |
| 1. u mesecu | AEO provera citiranosti (Poglavlje 5) + pregled brend priručnika | Dodatak B11 | izveštaj + predlozi izmena brend priručnika |

**5. KAPIJE, ti.** Jedina komponenta koja ne može da se automatizuje, i to je namerno. Detalji u tabeli autonomije niže.

### Repo struktura

```
marketing-os/
├── brandbook/              # 7 fajlova iz Poglavlja 11, ustav
├── strategija/
│   ├── ciljevi-kvartala.md
│   ├── content-plan.md     # stubovi, formati, ritam
│   └── icp.md
├── data/                   # ČULA, rutine pune i čitaju
│   ├── metrike/            # nedeljni izvozi (MRR, odlasci kupaca, aktivacija…)
│   ├── analitika-sajta/
│   ├── recenzije/
│   ├── pominjanja/
│   └── konkurencija/
├── content/
│   ├── ideje/              # backlog ideja (ti + rutine dopisuju)
│   ├── nacrti/             # RUKE pišu ovde
│   ├── na-pregledu/        # prošlo agent za kontrolu brenda, čeka TEBE
│   ├── odobreno/           # tvoj potpis, spremno za objavu
│   ├── objavljeno/         # arhiva sa datumom i kanalom
│   └── imejls/             # životni ciklus korisnika sekvence (Poglavlje 7)
├── eksperimenti/
│   ├── backlog.md          # ICE backlog ideja (Poglavlje 10)
│   └── log.md              # hipoteze + rezultati (Poglavlje 10)
└── izvestaji/              # nedeljni i mesečni izveštaji
```

Folderi u `content/` su mašina stanja: fajl se kreće samo udesno (nacrti → na-pregledu → odobreno → objavljeno) i svaki prelaz ima jasnog vlasnika.

### Tok sadržaja: od nacrta do objave

1. **Rutina piše u `nacrti/`**, po planu sadržaja, sa zaglavljem sa metapodacima na početku fajla (datum, stub, kanal, ciljna metrika).
2. **Agent za kontrolu brenda**, drugi, nezavisan agent kao prva kontrola. Ocenjuje nacrt protiv brend priručnika (glas, zabranjene fraze, tvrdnje bez izvora, poziv na akciju) i vraća isključivo JSON sa ocenom i poljem `prolaz`, prompt je u Dodatku B4; agent za proveru kvaliteta sam ne pomera fajlove i ne prepravlja nacrt. Fajlove pomera omotač-rutina od par linija koja pozove B4 pa postupi po polju `prolaz`: `true` → premešta nacrt u `na-pregledu/` i upiše ocenu u metapodatke na početku fajla; `false` → fajl ostaje u `nacrti/` uz dopisan blok "Provera kvaliteta: razlozi", pa rutina sledeći put ima tu povratnu informaciju.
3. **TI pregledaš `na-pregledu/`**, čitaš, popravljaš ili odbijaš. Odobreno premeštaš u `odobreno/`. Ovo je kapija, nepreskočiva.
4. **Objava**, ručno ili kroz alat za zakazivanje objava, ali TEK posle tvog odobrenja. Fajl ide u `objavljeno/` sa datumom i linkom.

❌ Pogrešno: agent ima pristup nalozima i objavljuje direktno "jer je brže". Prvi halucinirani orijentir ili pogrešan ton u javnosti košta te više poverenja nego što su sve uštede vremena vredele.
✅ Ispravno: agent staje na `na-pregledu/`. Tvoj pregled traje 10 minuta dnevno, jer agent za proveru kvaliteta već odradi prvo sito.

### Rutina 1: nedeljni izveštaj metrika (kompletan prompt)

```
Prvo pročitaj sve fajlove u brandbook/ i strategija/.

Zatim pročitaj sve fajlove iz data/metrike/ i data/analitika-sajta/
za poslednjih 14 dana, i eksperimenti/backlog.md i eksperimenti/log.md.

Napiši nedeljni izveštaj u izvestaji/YYYY-MM-DD-nedeljni.md sa strukturom:

1. BROJKE: tabela ključnih metrika (glavna metrika, MRR, novi korisnici,
   aktivacija, odlasci kupaca), ova nedelja vs prošla, sa % promene.
   Koristi ISKLJUČIVO brojke iz data/ fajlova. Ako podatak nedostaje,
   napiši "nema podatka", NIKAD ne procenjuj napamet.
2. SIGNALI: 3 najvažnije promene i tvoja hipoteza zašto su se desile,
   svaka vezana za konkretan broj.
3. EKSPERIMENTI: status tekućih iz eksperimenti/log.md
   (hipoteza, metrika odluke, dosadašnji rezultat).
4. PREDLOZI: tačno 3 predloga za sledeću nedelju, svaki sa ICE ocenom
   (Impact × Confidence × Ease) i naznakom koji cilj iz
   strategija/ciljevi-kvartala.md podržava.

Ton: činjenično, bez ulepšavanja, loš broj je loš broj.
Tvoj posao se završava pisanjem fajla. Ne šalješ, ne objavljuješ ništa.
```

### Rutina 2: nacrti objava po planu sadržaja (kompletan prompt)

```
Prvo pročitaj sve fajlove u brandbook/ i strategija/.

Zatim pročitaj strategija/content-plan.md, content/ideje/
i poslednja 2 fajla iz izvestaji/ (za sveže brojke i uglove).

Napiši 3 nacrta objava za [kanal] po planu sadržaja:
- svaki nacrt pokriva DRUGI tematski stub iz plana
- svaki kreće od stvarnog podatka, primera ili lekcije iz izvestaji/
  ili data/, nijedan nacrt od opšteg znanja
- glas i format strogo po brandbook/ (ton, dužina, zabranjene fraze,
  struktura otvaranja)
- ako za neki stub nemaš stvaran podatak ili primer, NE piši taj
  nacrt, umesto njega dodaj stavku u content/ideje/ sa opisom
  šta nedostaje

Svaki nacrt sačuvaj kao poseban fajl u content/nacrti/
sa imenom YYYY-MM-DD-[stub]-[tema].md i poljima metapodataka na početku fajla:
kanal, stub, ciljna_metrika, izvor_podatka.

NIKAD ne objavljuj i ne šalji ništa, tvoj posao se završava
u content/nacrti/.
```

Oba prompta zakazuješ kroz `/schedule` (rade i kad je računar ugašen), GitHub Actions ili `claude -p` iz cron-a, sadržaj prompta je isti.

### Nivoi autonomije: šta sme samo, šta nikad

| Nivo | Šta obuhvata |
|---|---|
| POTPUNO SAMO | analiza podataka, izveštaji, nacrti sadržaja, monitoring (recenzije, pominjanja, konkurencija), interni predlozi |
| UZ QA AGENTA | meta opisi stranica, A/B varijante naslova, niske posledice, visok volumen |
| NIKAD BEZ ČOVEKA | javno objavljivanje bilo čega; odgovori na recenzije i krizne situacije; promene cena; bilo kakva obećanja korisnicima |

Logika je jednostavna: autonomija raste sa reverzibilnošću. Interni izveštaj sa greškom obrišeš; javno obećanje korisniku ne možeš. Pricing posebno, to je najpotcenjenija poluga rasta (ProfitWell analize, detaljno u Poglavlju 1) i upravo zato NIKAD nije agentova odluka.

### Sigurnosni prekidač i nedeljni pregled

**Sigurnosni prekidač.** Moraš moći da pauziraš sve rutine jednim potezom. Dva sloja:
1. Isključi zakazane rutine u `/schedule` (odnosno onemogući cron radni tok ako koristiš GitHub Actions).
2. Dodaj u svaki prompt prvu liniju odbrane: "Ako u korenu repozitorijuma postoji fajl `PAUZA`, odmah prekini bez pisanja ijednog fajla." Onda je `touch PAUZA` tvoje crveno dugme, radi čak i ako si negde zaboravio jedan zakazani posao.

Kada povlačiš dugme: agent počne da halucinira brojke, ton ode van brend priručnika dva puta zaredom, ili se desi bilo šta javno neprijatno. Pauziraj, ispravi uzrok u brend priručniku ili promptu, pa tek onda ponovo pusti.

**Nedeljni pregled (1 sat, npr. petak posle retrospektive).** Pregledaš: šta je OS proizveo, šta si odbio i, ključno, ZAŠTO si odbio. Svako "zašto" se vraća u brend priručnik kao novo pravilo: odbio si nacrt jer zvuči prodajno-napadno → u `brandbook/04-glas-i-ton.md` ide nova zabranjena konstrukcija sa ❌/✅ primerom. To je mehanizam učenja: OS koji posle svakog odbijanja postaje precizniji. Bez pregleda, odbijaš iste greške svake nedelje i sistem stagnira.

### Metrike samog OS-a

OS je proizvod, meri ga kao proizvod:

| Metrika | Šta govori | Trend koji želiš |
|---|---|---|
| Stopa prihvatanja nacrta | % nacrta koje odobriš bez većih izmena | raste iz nedelje u nedelju (dokaz da pregled-petlja radi) |
| Rezultati / nedelja | broj nacrta, izveštaja, analiza | stabilan i predvidiv, ne maksimalan |
| Tvoje vreme / nedelja | sati na pregled + pregled | pada ka ~1-2h, ne ka nuli |

Tvoje vreme ne ide na nulu namerno, kapija si ti. Ako padne na nulu, nemaš autonomni OS nego neispitan autopilot. I podsetnik: Kohavijev nalaz o trećinama (Poglavlje 10) važi i za predloge tvog OS-a, zato predlozi iz nedeljnog izveštaja idu u eksperiment-log sa metrikom odluke, ne pravo u realizaciju.

### Primena odmah

Postavi skeleton i pusti prvu rutinu, danas, za manje od sat vremena:

1. Napravi repozitorijum `marketing-os/` sa strukturom iz code bloka iznad (prazni folderi + `.gitkeep`).
2. Ubaci brend priručnik iz Poglavlja 11 u `brandbook/` i napiši `strategija/ciljevi-kvartala.md` (3 cilja, po jedna metrika svaki).
3. Ubaci u `data/metrike/` jedan ručni izvoz svojih trenutnih brojki (markdown tabela je dovoljna).
4. Preseli fajlove koje si već napravio kroz ranija poglavlja na njihova mesta u repozitorijumu:

| Fajl iz ranijeg poglavlja | Novo mesto u `marketing-os/` |
|---|---|
| `pozicioniranje.md` (Poglavlje 2) | `brandbook/03-pozicioniranje.md` |
| `metrike.md` (Poglavlje 1) | `data/metrike/` |
| `petlja-01.md` (Poglavlje 4) i `plan-placenog-oglasavanja.md` (Poglavlje 6) | `eksperimenti/` |
| `imejlovi/aktivaciona-sekvenca.md` (Poglavlje 7) | `content/imejls/` |
| `plan-12-nedelja.md` (Poglavlje 13) | koren repozitorijuma |

5. Zakaži Rutinu 1 (nedeljni izveštaj) kroz `/schedule` za ponedeljak 07:00, prompt prepiši doslovno odozgo.
6. Pusti je da radi nedelju dana. Ne diraj ništa.

**Rezultat rada:** repozitorijum + prvi automatski generisan `izvestaji/` fajl sledećeg ponedeljka. Tek kad izveštajna rutina radi pouzdano dve nedelje, dodaješ content rutinu, redosled uvođenja po nedeljama je tema Poglavlja 13.

### Najčešće greške

1. **Agent sa pristupom objavljivanju.** "Samo ovaj put direktno" je početak kraja, jedna halucinirana brojka u javnoj objavi ruši poverenje koje gradiš mesecima. Rešenje: tehnički onemogući, agent piše samo u repozitorijum, kredencijale za objavu drži van njegovog domašaja.
2. **Rutine bez mozga.** Prompt koji ne počinje čitanjem brend priručnika i strategije proizvodi generički sadržaj koji platforme i čitaoci ignorišu. Rešenje: prva rečenica svakog prompta je učitavanje konteksta, bez izuzetka.
3. **Sve rutine odjednom.** Šest rutina prve nedelje = šest izvora grešaka koje ne stižeš da pregledaš, pa odustaneš od celog sistema. Rešenje: jedna rutina, dve nedelje stabilnog rada, pa sledeća (plan u Poglavlju 13).
4. **Pregled se preskače.** Bez vraćanja "zašto sam odbio" u brend priručnik, stopa prihvatanja stoji u mestu i pregledanje te košta isto kao prve nedelje. Rešenje: pregled je zakazan blok u kalendaru, 1h, ne "kad stignem".
5. **OS bez čula.** Rutine koje ne čitaju sveže podatke iz `data/` pišu iz opšteg znanja, uglađeno, netačno, beskorisno. Rešenje: pravilo u promptu "ako podatak ne postoji u data/, napiši da nedostaje" + nedeljni ritual punjenja `data/`.

### Kontrolna lista

- [ ] Repo `marketing-os/` postoji sa svim folderima iz strukture (`brandbook/`, `strategija/`, `data/`, `content/`, `eksperimenti/`, `izvestaji/`)
- [ ] `brandbook/` i `strategija/` popunjeni; svaki prompt rutine ih učitava prvi
- [ ] `data/` ima bar jedan svež izvoz metrika (ne stariji od nedelju dana)
- [ ] Rutina 1 (nedeljni izveštaj) zakazana i proizvela bar jedan izveštaj
- [ ] Agent za kontrolu brenda stoji između `nacrti/` i `na-pregledu/`
- [ ] Nijedan agent nema kredencijale za objavljivanje, kapija si ti
- [ ] Sigurnosni prekidač testiran: `PAUZA` fajl + isključenje zakazanih rutina
- [ ] Nedeljni pregled (1h) u kalendaru; svako "zašto odbijeno" ide u brend priručnik
- [ ] Pratiš stopa prihvatanja, rezultat/nedelja i svoje vreme/nedelja


---

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


---

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
