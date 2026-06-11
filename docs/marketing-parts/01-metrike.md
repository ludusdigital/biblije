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
