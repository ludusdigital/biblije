## Modul 8: Kvalitet i bezbednost: poverenje se gradi proverom

Tvoj proizvod sada radi. Funkcionalnosti se ređaju, demo izgleda dobro, i prirodno je da poželiš da odmah lansiraš. Ali između "radi kod mene" i "spremno za prave korisnike" stoji jedan korak koji profesionalci nikad ne preskaču: nezavisna provera. Dobra vest, ne moraš da budeš programer da bi je sproveo. Claude Code ima ugrađene alate za pregled koda, a tvoj posao je isti kao posao dobrog direktora: da postavljaš prava pitanja i tražiš dokaze.

Zamisli to ovako: kad kupuješ stan, ne veruješ prodavcu na reč da su instalacije ispravne, dovedeš svog majstora da pregleda. `/code-review`, `/security-review` i `/simplify` su tvoji majstori za pregled. Razlika je u tome što su uvek dostupni i pregled traje minute, ne dane.

### Šta ćeš naučiti

- Kako da pokreneš `/code-review` i izabereš pravi nivo temeljnosti za situaciju
- Kada je `/security-review` obavezan, a ne opcioni
- Kako da čitaš nalaze pregleda iako ne razumeš kod, formula od tri pitanja
- Kako da "napadneš" sopstvenu aplikaciju pre nego što to uradi neko drugi
- Koje crvene zastavice u Claude-ovim odgovorima zahtevaju da odmah staneš

### /code-review: drugi par očiju za tvoj kod

Komanda `/code-review` pregleda izmene koje su trenutno u toku i traži greške: stvari koje će se pokvariti, ivične slučajeve koji nisu pokriveni, logiku koja ne radi ono što misliš da radi. To je kao lektor za kod, ne piše tekst umesto tebe, nego hvata ono što je autoru promaklo.

Postoje nivoi temeljnosti: `low`, `medium`, `high` i `max`. Niži nivoi su brži i fokusirani na najvažnije; viši nivoi pregledaju temeljnije. Praktično pravilo:

- **low/medium**, svakodnevni ritam, posle svake završene funkcionalnosti (vidi Modul 6). Brzo, hvata očigledne propuste.
- **high/max**, pre spajanja veće celine, posle autonomnog rada iz Modula 7, ili kad menjaš nešto osetljivo.
- **`/code-review ultra`**, za najvažnije prekretnice: pred lansiranje, posle velikog refaktorisanja (krupnog unutrašnjeg sređivanja koda koje ne menja ono što korisnik vidi, detaljno u Modulu 10). Ovo je multi-agent pregled celog brancha u oblaku, više nezavisnih pregledača radi paralelno, pa je najtemeljniji. Dodatno se naplaćuje i pokrećeš ga ti, svesno, ne usput.

```
/code-review high
```

Nemoj da pregledaš sve odjednom jednom mesečno. Mali, česti pregledi su kao pranje sudova posle svakog obroka, deset minuta dnevno umesto traume vikendom.

### /security-review: brava na vratima

`/code-review` traži greške; `/security-review` traži rupe kroz koje neko zlonameran može da uđe. Pregleda bezbednosne propuste u izmenama na trenutnom branchu (branch = paralelna verzija projekta na kojoj se izmene prave pre spajanja u glavnu, vidi rečnik u Dodatku C).

Dva trenutka kad je ova komanda **obavezna**, bez izuzetka:

1. **Pred lansiranje**, uvek, kao tehnički pregled pre registracije auta.
2. **Posle svake izmene koja dodiruje prijavu korisnika, plaćanja ili lične podatke.** Imejl adrese, lozinke, brojevi kartica, istorija korišćenja, sve su to podaci za koje si odgovoran i pravno i moralno.

```
/security-review
```

Trošak: nekoliko minuta. Trošak propusta: poverenje korisnika koje se ne vraća lako.

### /simplify: generalno spremanje

Kod vremenom raste i zapliće se, kao fioka u koju mesecima ubacuješ stvari "samo na trenutak". `/simplify` pojednostavljuje i čisti izmenjeni kod, uklanja dupliranje, skraćuje zaobilazne puteve. Važno: on **ne traži bagove**, za to je `/code-review`. Pokreći ga periodično, recimo posle svake zaokružene celine, čistiji kod znači da će svaka sledeća izmena biti brža i jeftinija.

### Kako čitaš nalaze kad nisi programer

Pregled će ti vratiti listu nalaza punu tehničkih izraza. Ne treba da ih razumeš na nivou koda, treba da doneseš odluku, a za odluku ti treba prevod. Za **svaki** nalaz traži tri stvari:

```
Za nalaz broj 2 iz pregleda:
1. Objasni mi prostim jezikom, bez žargona, šta je problem, kao da pričaš
   sa nekim ko nikad nije programirao.
2. Koliko je ozbiljno na skali 1-10? Šta je najgore što može da se desi
   ako ovo ne popravimo?
3. Predloži ispravku i reci koliko bi posla bilo. Ne menjaj ništa dok ne odobrim.
```

Sa ova tri odgovora odlučuješ kao direktor: ozbiljnost 8+ se rešava odmah, 4-7 ide u backlog (spisak budućih zadataka, vidi Modul 10), 1-3 možda nikad. Ti određuješ prioritete, Claude ti daje informacije za odluku.

### Igraj napadača pre napadača

Najbolji bezbednosni test koji možeš da uradiš besplatno: zamoli Claude-a da razmišlja kao neko ko želi da te ošteti.

```
Ponašaj se kao zlonameran korisnik moje aplikacije. Šta sve mogu da
zloupotrebim? Probaj da pristupiš tuđim podacima, da promeniš tuđe
sadržaje, da zaobiđeš prijavu, da pošalješ besmislene ili ogromne
podatke u forme. Za svaki uspešan "napad" pokaži mi tačno šta si
uradio i koji je dokaz da je uspeo.
```

Claude može da pokrene dev server i proveri ovo u pregledaču, da klikće, popunjava forme i pravi snimke ekrana. Ako "napad" uspe, imaćeš snimak ekrana ili log kao dokaz, a onda i jasan zadatak za ispravku.

### Princip dokaza i crvene zastavice

Iz Modula 1 znaš pravilo: **tvrdnja bez dokaza se ne računa.** "Popravio sam" ne znači ništa bez test rezultata, snimka ekrana ili loga. U kontekstu kvaliteta, ovo su tri crvene zastavice na koje reaguješ odmah:

❌ **"Gotovo je" bez dokaza.** Odgovor: "Pokaži mi rezultat testova / snimak ekrana ekrana / log koji to potvrđuje."

❌ **Test "popravljen" tako što je obrisan ili oslabljen.** Ako test ne prolazi, problem je u kodu, ne u testu. Ovo je kao da požarni alarm utišaš vađenjem baterije. Reci unapred:

```
Postojeće testove ne smeš da brišeš niti menjaš da bi prošli.
Ako test pada, popravi kod. Ako misliš da je sam test pogrešan,
stani i objasni mi zašto pre nego što ga diraš.
```

❌ **Upozorenja koja se ignorišu.** Kad build ili lint izbaci upozorenje (warning), a Claude kaže "to nije bitno, nastavljam", pitaj: "Objasni mi to upozorenje prostim jezikom i šta rizikujemo ako ga ostavimo."

✅ Zdrav obrazac izgleda ovako: izmena → testovi prolaze (vidiš rezultat) → `/code-review` → nalazi prevedeni i odlučeni → dokaz da ispravke rade.

### Vežba

1. Otvori terminal u folderu projekta i pokreni `claude`.
2. Pokreni `/code-review medium` nad trenutnim izmenama (ako nemaš sveže izmene, zamoli Claude-a da pregleda poslednju završenu funkcionalnost).
3. Izaberi jedan nalaz i postavi tri pitanja iz formule: prost jezik, ozbiljnost 1-10 + najgori scenario, predlog ispravke.
4. Odluči: popraviti odmah, backlog, ili ignorisati. Zapiši odluku i razlog.
5. Pokreni `/security-review`. Ako vrati nalaze, ponovi korak 3 za najozbiljniji.
6. Kopiraj prompt "zlonamernog korisnika" iz ovog modula i pusti Claude-a da napadne tvoju aplikaciju. Traži dokaz za svaki nalaz.
7. Za jednu odobrenu ispravku traži dokaz da radi: test rezultat ili snimak ekrana.

### Najčešće greške

1. **Pregled samo pred lansiranje.** Tada je nalaza previše i nastaje panika. *Rešenje:* mali pregled posle svake funkcionalnosti, `ultra` samo za prekretnice.
2. **Slepo odobravanje svih ispravki odjednom.** Ne znaš šta si odobrio ni zašto. *Rešenje:* nalaz po nalaz, tri pitanja, pa odluka.
3. **Ignorisanje nalaza jer "aplikacija radi".** To što vrata nisu obijena ne znači da brava valja. *Rešenje:* ozbiljnost 7+ rešavaš pre lansiranja, uvek.
4. **Prihvatanje "popravio sam testove" bez gledanja.** Možda su obrisani. *Rešenje:* traži da ti pokaže šta je tačno promenjeno i rezultat testova pre i posle.
5. **Preskakanje `/security-review` posle "male" izmene prijave ili plaćanja.** Male izmene prave velike rupe. *Rešenje:* pravilo je mehaničko, dira login/pare/lične podatke → pregled, bez razmišljanja.

### Kontrolna lista

- [ ] Posle svake završene funkcionalnosti pokrećem `/code-review` (low/medium)
- [ ] Pred veliku prekretnicu razmatram `/code-review ultra` (svestan da se dodatno naplaćuje)
- [ ] `/security-review` pokrećem pred lansiranje i posle svake izmene prijave, plaćanja ili ličnih podataka
- [ ] Za svaki nalaz tražim: prost jezik, ozbiljnost 1-10 + najgori scenario, predlog ispravke
- [ ] Ispravke odobravam pojedinačno, ne paušalno
- [ ] Bar jednom pred lansiranje pustio sam prompt "zlonamernog korisnika"
- [ ] Periodično pokrećem `/simplify` za čišćenje koda
- [ ] Ne prihvatam "gotovo je" bez test rezultata, snimka ekrana ili loga
- [ ] Proveravam da testovi nisu obrisani ili oslabljeni da bi "prošli"

### Proveri znanje

**1. Kada koristiš `/code-review medium`, a kada `/code-review ultra`?**

Medium za svakodnevni ritam posle svake funkcionalnosti, brz, fokusiran na najvažnije. Ultra za najvažnije prekretnice (pred lansiranje, posle velikog refaktorisanja), multi-agent pregled celog brancha u oblaku, najtemeljniji, dodatno se naplaćuje i pokrećeš ga ti.

**2. Koja tri pitanja postavljaš za svaki nalaz pregleda?**

(1) Objasni prostim jezikom šta je problem. (2) Koliko je ozbiljno na skali 1-10 i šta je najgore što može da se desi? (3) Koji je predlog ispravke? Tek onda odobravaš, ili šalješ u backlog.

**3. Claude kaže da je popravio bag i da sada svi testovi prolaze. Šta tražiš pre nego što prihvatiš?**

Dokaz: rezultat testova i pregled šta je tačno izmenjeno. Posebno proveravaš da nijedan test nije obrisan ili oslabljen, tvrdnja bez dokaza se ne računa.
