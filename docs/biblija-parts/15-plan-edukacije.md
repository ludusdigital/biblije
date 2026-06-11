## Za predavače: kako iz ovog dokumenta izvesti kurs

Ovaj dokument je pisan da se čita samostalno, ali najbolje rezultate daje kad ga neko provede kroz njega uživo. Ako si predavač, mentor ili interni trener koji želi da od ovih petnaest poglavlja napravi kurs za ne-tehničke polaznike, ovo poglavlje je za tebe. Nije još jedan modul gradiva; ovo je plan časa.

Jedno pravilo iznad svih: **polaznici ne uče slušajući tebe, uče radeći pored tebe.** Svaka odluka u ovom planu, trajanje, redosled, struktura radionice, proizilazi iz tog pravila.

### Format kursa

- **6 radionica po 2 do 2,5 sata**, jednom nedeljno. Nedeljni razmak nije slučajan: polaznicima treba vreme između radionica da rade na završnom projektu i da se sapletu, jer se na sapletanju uči.
- **Uživo ili onlajn**, oba formata rade. Online zahteva da svaki polaznik deli ekran kad zapne; uživo zahteva da ti hodaš po sali i gledaš ekrane. U oba slučaja, predavač mora da vidi šta polaznik radi, ne samo da čuje šta kaže.
- **Završni projekat projekat** se proteže kroz ceo kurs: svaki polaznik bira svoj mali proizvod na drugoj radionici i lansira ga do šeste. Kurs bez kapstona je predavanje; kurs sa kapstonom je transformacija.
- Maksimalno **8–10 polaznika** po predavaču. Više od toga i nećeš stići da odglaviš svakoga ko zapne u samostalnom delu.

### Mapa radionica

| Radionica | Moduli | Cilj sa kojim svako odlazi kući |
|---|---|---|
| R1 | Moduli 0–2 | Mindset „ti si direktor" + postavka: **svi polaznici odu sa instaliranim i pokrenutim Claude Code-om** i prvim obavljenim razgovorom |
| R2 | Moduli 3–4 | Temelji (git, GitHub, `/init`) + specifikacija: **svako napiše `docs/spec.md` svoje ideje za završni projekat** |
| R3 | Moduli 5–6 | Plan mode + ritam razvoja: **svako izgradi prvu funkcionalnost uživo**, kroz ciklus plan → izvršenje → dokaz → commit |
| R4 | Moduli 7–8 | Autonomni rad (`/goal`, `/loop`) + kvalitet (`/code-review`, `/security-review`): svako pusti prvi autonomni zadatak sa zaštitnim ogradama |
| R5 | Moduli 9–10 | Lansiranje + život posle: **svako lansira preview verziju svog proizvoda** na javnu adresu |
| R6 | Moduli 11–13 | Majstorstvo promptovanja, ekosistem, dijagnostika problema + **prezentacije završnih projekata** |

Redosled ne menjaj. R1 mora da se završi instalacijom kod svih, polaznik koji ode kući bez radnog okruženja na drugoj radionici sedi i gleda, a posle treće odustaje. Zato u R1 planiraj duži samostalni blok i dođi spreman na uobičajene zastoje (Node.js verzije, prijava na nalog, antivirus koji blokira terminal).

### Struktura svake radionice

Svaka radionica prati isti ritam od četiri bloka:

1. **Demo uživo (20 min)**, ti radiš, oni gledaju. Ne slajdove: pravi projekat, pravi terminal, pravi promptovi. Razmišljaj naglas: „Sad ću tražiti plan pre izmena, jer ne želim da menja fajlove dok ne vidim kuda ide."
2. **Vežba zajedno (40 min)**, svi rade isti zadatak istovremeno, ti diktiraš tempo korak po korak. Niko ne ide dalje dok svi nisu prošli kontrolnu tačku („svi vidite zeleni test? idemo dalje").
3. **Samostalni zadatak (40 min)**, svako radi na svom završnom projektu, primenjujući ono iz vežbe. Ti kružiš i odglavljuješ. Ovde se gradivo pretvara u veštinu.
4. **Diskusija grešaka (20 min)**, svako podeli jednu stvar koja mu nije radila i kako ju je (ili nije) rešio.

Zašto je diskusija grešaka najvredniji deo? Iz tri razloga. Prvo, **greške su gradivo koje ne možeš isplanirati**, svaki polaznik udari u drugačiji zid, pa grupa za 20 minuta vidi osam različitih problema i osam oporavaka, što je više dijagnostičkog iskustva nego što bi sam skupio za mesec dana. Drugo, **normalizuje neuspeh**: ne-tehnički polaznici greške doživljavaju kao dokaz da „ovo nije za njih", kad čuju da je i najbolji u grupi zaglavio, taj strah nestaje, a baš taj strah je razlog broj jedan zašto ljudi odustanu. Treće, vežbaš ih u **jeziku dijagnoze** iz Modula 13: simptom → dijagnoza → lek. Insistiraj na formatu: „Šta si očekivao? Šta se desilo? Šta je bio dokaz? Šta si pokušao?", to je tačno onaj refleks koji im treba kad kurs prođe a tebe više nema pored.

### Završni projekat projekat

Svaki polaznik na R2 bira **mali, stvarni proizvod**: jedan problem, jedna ciljna grupa, jedna stvar koju aplikacija radi. Ne „platforma za fitnes" nego „stranica gde moji klijenti zakazuju termin i dobiju potvrdu imejlom". Pravilo iz Modula 4 ovde sprovedi nemilosrdno: ako spec ne staje na jednu stranu, projekat je prevelik za šest nedelja.

Tvoja najvažnija intervencija na R2 je rezanje obima. Polaznici će se opirati, svaki misli da je baš njegova treća funkcionalnost neophodna. Pomozi sebi promptom koji svi zajedno pokrenu nad svojim spec-om:

```
Pročitaj docs/spec.md. Ja imam 4 nedelje i radim sa Claude Code-om
po 3-4 sata nedeljno. Predloži šta da izbacim iz prve verzije da
proizvod ostane koristan, a obim realan. Budi nemilosrdan, za
svaku stavku koju zadržiš objasni zašto je nezamenljiva.
```

Stvarni proizvod znači: na kraju kursa postoji javna adresa, i bar jedna osoba koja nije polaznik ga je upotrebila. To je cilj prezentacija na R6, ne „pogledajte moj kod", nego „evo šta sam lansirao i evo šta je prvi korisnik rekao".

### Merljivi kriterijumi uspeha polaznika

Primeni princip iz Modula 1 na sopstveni kurs: uspeh se dokazuje, ne tvrdi. Polaznik je uspešno završio kurs ako:

- [ ] Ima projekat na GitHub-u sa istorijom commit-ova kroz sve nedelje kursa (ne jedan džinovski commit poslednje večeri)
- [ ] Projekat ima `CLAUDE.md` i `docs/spec.md` koje je sam pisao i menjao
- [ ] Bar jedna funkcionalnost je izgrađena kroz ciklus: plan mode → odobrenje → implementacija → dokaz (test ili snimak ekrana) → commit
- [ ] Pokrenuo je `/code-review` i `/security-review` i rešio bar jedan nalaz
- [ ] Proizvod je lansiran na javnu adresu (preview je dovoljan) i bar jedna spoljna osoba ga je koristila
- [ ] Na prezentaciji ume da odgovori: „šta bi sledeće dodao i kako bi to tražio od Claude-a", to pokazuje da je proces postao njegov

Primeti šta ovde nema: ni jedan kriterijum ne meri kvalitet koda. Polaznici nisu programeri i neće to postati za šest nedelja, mere se proces, dokazi i lansiran proizvod.

### Saveti za predavača

**Tri tačke zbunjenosti, i kako ih demonstrirati.** Iskustvo kaže da ne-tehnički polaznici zapinju na ista tri mesta:

1. **Terminal.** Crni prozor sa trepćućim kursorom je za mnoge prvi susret sa računarom bez ikona. Demistifikuj ga analogijom: terminal je šalter, umesto da hodaš po zgradi i tražiš pravu kancelariju (klikćeš po menijima), priđeš šalteru i kažeš tačno šta hoćeš. Demonstriraj sa tri bezopasne komande (`pwd`, gde sam, `ls`, šta je ovde, `cd`, idem tamo) i odmah pređi na poentu: čim pokrenu `claude`, dalje pričaju normalnim jezikom. Terminal je samo predvorje.
2. **Git.** Apstraktan je dok ga ne vide kao vremeplov. Demonstriraj uživo: napravi izmenu, commit-uj je, pa namerno „upropasti" fajl i vrati se na prethodno stanje. Taj jedan minut, „vidite, ništa nije izgubljeno", vredi više od pola sata teorije o granama. Poruka koju nosiš kroz ceo kurs: commit posle svakog koraka koji radi, jer je commit tačka na koju uvek možeš da se vratiš (detaljno u Modulu 3).
3. **Dozvole.** Kad Claude prvi put pita „da li smem da pokrenem ovu komandu?", polaznici se uplaše da su nešto pokvarili. Objasni unapred: to je sigurnosna provera, kao kad ti novi saradnik kaže „hoću da pošaljem ovaj imejl klijentu, jesi saglasan?", znak da sistem radi, ne da je nešto pošlo naopako. Pokaži kako odobravanje izgleda, šta znači lista dozvoljenih komandi u `.claude/settings.json`, i pomeni da skill `/fewer-permission-prompts` ume da predloži bezbednu listu (detaljno u Modulu 7).

**Namerno izazovi grešku uživo.** Ovo je najjači trik u tvom arsenalu. Negde u demou, najbolje na R3, namerno traži nešto dvosmisleno ili pusti da build pukne, pa pred svima prođi kroz oporavak: pročitaj poruku o grešci naglas, prevedi je na običan jezik, nalepi je Claude-u i traži dijagnozu, pritisni `Esc` ako je krenuo pogrešnim putem i preusmeri ga. Polaznici koji su videli predavača kako mirno izlazi iz greške ne paniče kad se njima desi, a desiće se iste večeri. Ako greška neće da se desi sama, izazovi je: traži funkcionalnost bez ikakvog konteksta („dodaj plaćanje") i pokaži zašto je rezultat loš, pa isti zahtev formuliši po formuli iz Modula 6 i pokaži razliku.

**Koristi šablone iz Dodatka B kao radne listove.** Ne teraj polaznike da promptove smišljaju iz glave dok su početnici, podeli šablone iz Dodatka B (odštampane ili kao fajl) i neka u samostalnom delu radionice popunjavaju praznine svojim projektom. Šablon za spec na R2, šablon za funkcionalnost na R3, šablon za `/goal` uslov na R4, kontrolna lista pre lansiranja na R5. Vremenom će šablone odbaciti sami, ali u prvim nedeljama, popunjavanje praznina pretvara paralizu pred praznim ekranom u rutinu.

I poslednji savet: vodi sopstveni završni projekat paralelno sa polaznicima. Predavač koji svake nedelje pokaže svoj napredak, svoje greške i svoje commit-ove nije autoritet koji priča o plivanju sa obale, on je u vodi, pored njih. To je ton celog ovog dokumenta, i ton koji kurs čini uspešnim.
