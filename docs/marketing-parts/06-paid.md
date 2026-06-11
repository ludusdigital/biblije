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
