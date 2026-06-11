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
