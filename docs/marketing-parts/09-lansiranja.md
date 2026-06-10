## Poglavlje 9: Lansiranja i momentum — serija, ne događaj

Najskuplja zabluda solo osnivača: "veliki dan lansiranja". Mesecima ćutiš, gradiš u tajnosti, pa jednog jutra objaviš — i ništa. Realnost je drugačija: lansiranje nije događaj, nego serija talasa pažnje koje sistematski praviš i hvataš. Waitlist (lista čekanja) → zatvorena beta → javni launch → feature lansiranja kao stalni ritam. Svaki talas ima svoj posao i svoj deliverable za sledeći.

### Šta ćeš naučiti

- Zašto je lansiranje serija od četiri talasa, a ne jedan dan
- Kako da napraviš waitlist sa referral mehanikom koja sama raste
- Kako zatvorena beta proizvodi sirovinu za landing stranicu (dokazi, izjave)
- Product Hunt mehaniku — i sistem koji hvata pažnju pre nego što ispari za ~48h
- Feature launch ritam: kako svaki značajan feature pretvoriš u mini-lansiranje

### Talas 1: Waitlist — prodaja pre proizvoda

Waitlist stranica je najjeftiniji test tražnje koji postoji: jedna stranica, jedno obećanje, jedno polje za email. Ako ne možeš da nateraš ljude da ostave email za besplatnu stvar koja stiže, nećeš ih naterati ni da plate gotovu.

Operativni minimum:

1. **Stranica** — naslov po formuli iz Poglavlja 2 (problem + ishod, ne feature lista), jedno CTA polje za email, bez navigacije i distrakcija.
2. **Referral mehanika za poziciju u redu** — posle prijave, korisnik dobija jedinstveni link: "Podeli i preskoči red." Svaka uspešna preporuka ga pomera napred. Ovo je ista logika obostranog interesa koju je Dropbox referral program pretvorio u udžbenički primer (Poglavlje 4) — nagrada za obe strane, vezana za vrednost proizvoda. Kod waitliste je nagrada raniji pristup.
3. **Email od prvog dana** — lista čekanja bez komunikacije je groblje. Jedan mejl na 2-3 nedelje: napredak, screenshot, pitanje. Detalji sekvenci u Poglavlju 7.

```
Šablon waitlist potvrde (email #1):

Predmet: Na listi si — pozicija #{{broj}}

Hvala što si se prijavio za {{proizvod}}.
Trenutno si #{{broj}} u redu.

Hoćeš ranije? Podeli svoj link — svaka prijava
preko njega te pomera napred:
{{referral_link}}

Sledeće 2 nedelje šaljem kratak update o napretku.
— {{ime osnivača}}
```

Podsetnik na K-faktor iz Poglavlja 4: broj pozivnica po korisniku × stopa konverzije pozivnice. Waitlist sa referral mehanikom je najlakše mesto da ga prvi put izmeriš — i K od 0,3–0,5 značajno obara efektivni CAC (orijentir industrije), jer deo liste stiže besplatno.

### Talas 2: Zatvorena beta — fabrika dokaza

Cilj bete nije "testiranje". Cilj bete su dve stvari: brz feedback ciklus i **sirovina za javni launch** — izjave, brojke, studije upotrebe.

- **Mali broj, idealni korisnici.** 10-30 ljudi koji tačno odgovaraju tvom ICP-u (Poglavlje 2). Ne 500 random prijava — sa 500 ljudi ne možeš da razgovaraš, a razgovor je poenta.
- **Brz ciklus.** Nedeljni ritam: pusti verziju → posmatraj gde zapinju (TTV iz Poglavlja 3) → razgovor sa 3-5 korisnika → ispravi → ponovi.
- **Žetva dokaza.** Posle svake dobre reakcije, traži dozvolu da je citiraš. Konkretno pitanje daje konkretan citat:

```
❌ "Da li ti se sviđa proizvod?" → "Da, super je." (neupotrebljivo)
✅ "Šta si radio pre ovoga i koliko ti je trajalo?
    A sada?" → "Ranije sat vremena ručno, sada 10 minuta."
    (citat koji prodaje — ide direktno na landing)
```

Beta je i trenutak za Sean Ellis PMF test (Poglavlje 1): pitaj korisnike koliko bi bili razočarani da proizvod nestane — ako bar 40% kaže "veoma razočaran", imaš signal da je vreme za javni talas. Ako nemaš, javni launch će samo glasnije objaviti proizvod koji ne drži ljude.

### Talas 3: Javni launch — Product Hunt mehanika i sistem koji hvata

Product Hunt (i slične platforme) je vredan špic pažnje za early-adopter, developersku i PM publiku. Ali ključna činjenica (industrijska procena): **bez sistema koji pažnju hvata, efekat ispari za ~48 sati.** Špic saobraćaja koji padne na nespremnu stranicu je potrošen metak.

Mehanika dana: prvi sati su kritični za momentum — rani angažman gura listing više, pa zagrej zajednicu unapred (waitlist, beta korisnici, tvoja mreža) da znaju da je dan D i gde da te nađu. Ne traži eksplicitno glasove po pravilima platforme — traži da pogledaju i prokomentarišu iskreno.

Sistem koji hvata (mora postojati PRE dana D):

| Element | Zašto | Provera |
|---|---|---|
| Onboarding doteran | Špic saobraćaja × loš TTV = potrošeni posetioci | Novi korisnik stiže do aha-momenta bez tvoje pomoći (Poglavlje 3) |
| Email capture na svakom koraku | Posetilac koji ode bez emaila je izgubljen zauvek | I oni koji se ne registruju mogu da ostave email (npr. za vodič/resurs) |
| Follow-up sekvenca spremna | Pažnja traje ~48h, odnos traje koliko ga lista nosi | Aktivaciona sekvenca iz Poglavlja 7 uključena za nove registracije |
| "Kako si čuo za nas?" polje | Launch saobraćaj stiže kroz dark social koji analitika ne vidi (praksa self-reported attribution, Poglavlje 5) | Polje pri registraciji, odgovori se loguju |
| Founder prisutan ceo dan | Komentari i pitanja na listingu su deo listinga | Kalendar blokiran, odgovaraš u minutima |

### Talas 4: Feature launch ritam — proizvod koji vidljivo živi

Posle javnog lansiranja, najveća greška je tišina. Svaki značajan feature je mini-launch sa tri obavezna dela:

1. **Objava** — kratka, sa vizuelnim dokazom (screenshot, GIF, 30-sekundni snimak): šta sada možeš što juče nisi mogao.
2. **Email segmentu kome znači** — ne celoj listi. Feature za timove ide korisnicima koji rade u timu; ostalima je šum koji troši poverenje.
3. **Changelog zapis** — javna stranica "šta je novo". Niko je ne čita od korice do korice, ali svaki posetilac koji je otvori vidi: proizvod živi, neko ga aktivno gradi. To je marketing poruka sama po sebi — i hrana za AI pretrage koje citiraju izvore (Poglavlje 5).

```
Šablon feature mini-launch objave:

[Problem u 1 rečenici, rečima korisnika]
[Šta smo izbacili — 1 rečenica]
[GIF/screenshot pre → posle]
[1 rečenica: kome ovo menja dan]
[Link]
```

Ritam je važniji od veličine: mali feature svake 2-3 nedelje gradi više momentuma nego mega-objava dvaput godišnje — svaka objava je nova prilika da te neko prvi put vidi (95-5 logika iz Poglavlja 8: većina publike danas ne kupuje, ali pamti ko se stalno pojavljuje).

### Launch checklist tabela

| Faza | Zadaci |
|---|---|
| **Pre (2+ nedelje)** | Onboarding testiran na 5 svežih ljudi; aktivaciona email sekvenca uključena; izjave iz bete na landing stranici; waitlist/beta lista obaveštena o datumu; "Kako si čuo za nas?" polje aktivno |
| **Na dan** | Objava rano ujutru po vremenu platforme; lična poruka listi i mreži; founder odgovara na svaki komentar; analitika i registracije se prate uživo |
| **Posle 48h** | Follow-up mejl svima koji su se registrovali a nisu aktivirani; zahvalnica zajednici sa brojkama; zabeleži: posete, registracije, aktivacije, izvore ("kako si čuo") |
| **Posle 2 nedelje** | Retencija launch kohorte vs. ranije kohorte; razgovor sa 3-5 novih korisnika; odluka: šta je sledeći talas (feature mini-launch) i datum |

### Primena odmah

Isplaniraj svoj sledeći talas — danas, u jednom fajlu `launch-plan.md`:

- **Ako proizvod još nije javan:** napravi waitlist stranicu. Deliverable: live stranica sa naslovom po formuli iz Poglavlja 2, email poljem, referral linkom ("podeli → preskoči red") i šablonom prvog mejla (gore).
- **Ako je proizvod javan:** izaberi sledeći feature vredan mini-launcha. Deliverable: popunjen šablon objave, definisan segment liste koji dobija email, changelog zapis — i datum u kalendaru, najkasnije za 3 nedelje.

U oba slučaja prepiši launch checklist tabelu u svoj fajl i popuni je svojim stavkama — to postaje šablon koji u Poglavlju 12 pretvaraš u rutinu marketinškog OS-a.

### Najčešće greške

1. **Lansiranje kao jedan dan.** Sva energija u dan D, posle tišina. → Rešenje: planiraj seriju — pre dana D znaj koji je sledeći talas i kada.
2. **Špic bez sistema koji hvata.** Product Hunt saobraćaj padne na sirov onboarding i nestane za ~48h (industrijska procena). → Rešenje: tabela "sistem koji hvata" je uslov za objavu, ne opcija.
3. **Beta sa pogrešnim ljudima.** 300 random testera, nula upotrebljivog feedbacka. → Rešenje: 10-30 ljudi iz ICP-a sa kojima stvarno razgovaraš svake nedelje.
4. **Waitlist koja ćuti.** Lista skupljena pa zaboravljena tri meseca — na dan lansiranja mejl stiže hladnoj publici. → Rešenje: update na 2-3 nedelje, kratak i konkretan.
5. **Feature objave celoj listi.** Svaki update svima → opadanje otvaranja, odjave. → Rešenje: segmentacija — email ide samo onima kojima feature menja rad.

### Kontrolna lista

- [ ] Znam u kom sam talasu (waitlist / beta / javni launch / feature ritam) i koji je sledeći
- [ ] Waitlist stranica ima referral mehaniku "podeli → preskoči red" i prvi mejl spreman
- [ ] Beta grupa je 10-30 ljudi iz ICP-a, sa nedeljnim feedback ciklusom
- [ ] Imam bar 3 upotrebljiva citata/dokaza iz bete na landing stranici
- [ ] Sistem koji hvata je kompletan: onboarding, email capture, follow-up sekvenca, "kako si čuo za nas?"
- [ ] Datum javnog lansiranja je određen i zajednica zagrejana unapred
- [ ] Posle-launch koraci (48h i 2 nedelje) su u kalendaru pre dana D
- [ ] Feature mini-launch ritam definisan: objava + email segmentu + changelog, bar jednom u 3 nedelje
