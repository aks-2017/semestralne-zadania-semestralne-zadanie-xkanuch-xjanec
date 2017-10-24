# A Convergence Time Optimization Paradigm for OSPF based Networks Through SDN SPF Protocol
### Peter Kaňuch, Nikolas Janec
### Cvičiaci: Tomáš Boros, Utorok 19:00

## Úvod

Článok sa zaoberá porovnaním OSPF, pretože najčastejšie používaným protokolom vo firemných sieťach je  práve tento protokol a SDN sieťami s kontrolérom podporujúcim algoritmus Shortest Path First (SPF) pre určenie najkratšej cesty. Autori porovnávajú konvergencie časov napríklad pri výpadku linky medzi Softvérovo definovanými sieťami (SDN) a sieťami fungujúcimi s protokolom OSPF. Taktiež overujú aj Response time pre dané zariadenie. Svoje riešenie overili pomocou Mininetu pre SDN a pre overenie OSPF použili GNS3 s použitím CISCO ios pri rôznych veľkostiach topológií (10, 20, 30 switchov(SDN)/routerov(ios)).  

## Analýza

### SDN siete

Software-Defined Networks (SDN) je centralizovaná topológia architektúry [^4]. 

![SDN](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/sdn-architecture.png "SDN architektúra")

SDN architektúra sa skladá z:
- Aplikačná vrstva - ponúka služby pre virtualizáciu, smerovanie, firewall, ...
- Control vrstva - pozostáva z kontrolera, ktorý jednak komunikuje s aplikáciami cez rozhranie, ale aj priamo s fyzickou vrstvou (infraštruktúrou).
- Vrstva infraštruktúry 

Základ v SDN tvorí virtualizácia. Dovoľuje, aby softvér bežal nezávisle od hardvéru [^5].

### Protokol OpenFlow

Komunikačný protokol pre SDN siete, ktorý umožňuje priamu interakciu kontrolera s fyzickými zariadeniami. Je štandard, ktorý dovoľuje vzdialene konfigurovať zariadenia od rôznych výrobcov [^3]. 
Taktiež umožňuje úpravusmerovacích tabuliek pomocou pridávania rôznych pravidiel. 

### Mininet

Mininet [^1] je virtuálna sieť pre simuláciu SDN sieti. Napodobňuje kompletnú sieť zariadení ako hosty, prepínače a jednotlivé prepojenia medzi nimi. 
Dokáže simulovať sieť pomocou virtualizácie založeniej na procesoch.
Taktiež podporuje protokol OpenFlow. 

### HP VAN SDN

HP VAN SDN kontrolér [^2] je softvér, ktorý poskytuje centrálny bod pre správu sieti podporujúce protokol OpenFlow. Taktiež poskytuje rozhranie pre vývoj Java aplikácií inými vývojarmi. Je navrhnutý najmä pre fungovanie v dátových centrách.

![HPVAN](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/HPVAN.jpg "HP VAN Controller")

### OSPF – Open Shortest Path First

Je dynamický smerovací protokol, ktorý sa používa v rámci jedného autonómneho systému (IGP). Patrí do skupiny Link-state protokolov vďaka čomu smerovač vo firemnej sieti pozná:
- Všetky ostatné smerovače
- Vzájomné prepojenia medzi smerovačmi
- Všetky koncové aj prepojovacie siete
- Ceny všetkých rozhraní

Po kompletnom prešírení informácii o celej topológii všetkým smerovačom v tejto sieti si smerovače vypočítajú najkratšiu cestu do každého vrcholu použitím, napríklad Dijkstrovým algoritmom. 
V OSPF protokole sa stretneme s dôležitými pojmami:
Pre identifikáciu a ohodnotenie (cena, IP adresa...) rozhrania/linky smerovača – Link, Link-state, Link-state ID, Link ID. Na identifikáciu smerovača vo vnútornej sieti – Router ID. V rámci firemnej sieti môžeme mať definované rôzne oblasti (arey), kde smerovače v konkrétnej oblasti poznajú celú topológiu len tejto oblasti. Pričom každá oblasť musí mať spojenie s backbone  oblasťou. OSPF sa skladá z troch štruktúr:
1.	Tabuľka susedov –informácie o známych susedov
2.	Topologická databáza – informácie o všetkých smerovačoch a ich pripojených sieťach v danej oblasti ale taktiež aj informácie o sieťach v iných oblastiach
3.	Smerovacia tabuľka – obsahuje next-hop na najkratšej ceste pre každú známu sieť

Pre vytvorenie susedstva v OSPF medzi dvoma smerovačmi je potrebné splniť nasledujúce kritéria:
- Obe rozhrania musia byť v rovnakej podsieti
- Hello a Dead interval časovaču musí byť zhodný na oboch rozhraniach
- Obe rozhrania musia byť v rovnakej oblasti
- V prípade, že je nastavená autentifikácia tak na oboch rozhraniach musí byť rovnaká

Nadviazanie susedstva prebieha buď automaticky (multicast adresa) alebo manuálne (unicast adresa). Poslednou najdôležitejšou častou v OSPF sú správy, ktoré sú rôznych typov:
Hello - Objavovanie susedných smerovačov
- Database Description (DBD) – porovnanie topologických informácii
- Link State Request (LSR) - požiadavka na zaslanie topologickej informácie
- Link State Update (LSU) – odpoveď na LSR v ktorej sa nachádzajú topologické informácie(LSA)
- Link State Acknowledgement (LSAck) - potvrdenie prijatia LSU
- Link State Advertisement (LSA) - dátová štruktúra, v ktorej sa nachádza jedna konkrétna topologická informácia ako ID smerovača a informácie o všetkých jeho priamo pripojených sieti v danej oblasti (LSU môže obsahovať viac LSA)

Konvergencia v OSPF sieťach sa skladá z dvoch častí a to detekciou zmien v topológii a následne prepočítanie trasy. OSPF môže zmenu v sieti zistiť dvomi spôsobmi a to zmenou stavu na fyzickom rozhraní, kde sa LSA odosiela okamžite alebo potom vypršaním dead časovača (4x hello správa) čo spôsobuje pomalšiu konvergenciu tá sa dá zrýchliť znížením hello časovača no v tomto prípade musíme dávať pozor aby sme nenastavili príliš nízku hodnotu čo by spôsobilo obrovské zlyhania.
Prepočet trasy vykoná každý smerovač po zistení zlyhania. Na všetky smerovače v oblasti OSPF sa odosiela LSA , ktorá signalizuje zmenu topológie. To spôsobí, že smerovače môžu prepočítať všetky svoje trasy pomocou algoritmu Djikstra (SPF). Toto je náročná úloha pre procesor, čo pri obrovských sieťach s často padajúcimi spojeniami môže spôsobiť preťaženia procesora na smerovači.  Preto sa zaviedoli spf časovače spf-delay (5 sekúnd) a spf-holdtime (10 sekúnd), ktoré zabezpečia „dýchací“ priestor pre procesor na smerovači. Je tiež možné naplánovať spúšťanie SPF ihneď po zaplavení informácií LSA, čo však môže potenciálne spôsobiť nestabilitu.


| Timers        | Time          |
| ------------- |:-------------:|
| ip ospf hello-interval      | 10 sec / 30 sec | 
| ip ospf dead-interval     | 40 sec / 120 sec (4 x hello)     |
| ip ospf retransmit-interval | 5 sec      |
| ip ospf transmit-delay |	1 sec |
| timers spf spf-delay |	5 sec |
| timers spf spf-holdtime |	10 sec |
| LSA Generation Interval |	0.5 sec |

[^1]: https://github.com/mininet/mininet
[^2]: https://www.sdxcentral.com/products/hp-virtual-application-networks-van-sdn-controller/
[^3]: https://www.sdxcentral.com/sdn/definitions/what-is-openflow/
[^4]: https://www.opennetworking.org/sdn-definition/
[^5]: https://www.networkcomputing.com/cloud-infrastructure/7-essentials-software-defined-networking/1672824201

## Návrh zadania

V našom riešení sme sa rozhodli overiť nasledujúce výsledky ich práce:
1. Konvergenciu SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch

![SDN](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/SDN-convergence.PNG "SDN Convergence")

2. Konvergenciu OSPF siete na Cisco ios routroch

![OSPF](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/OSPF-convergence.PNG "OSPF Convergence")

3. Response time SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch
4. Response time OSPF siete na Cisco ios routroch
5. Veľkosti topológií: 10, 20, 30 switchov(SDN)/routerov(ios)

![TOPOLOGY](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/topology.PNG "Príklad topológie")

6. Rôzne časy časovačov (dead interval, ...) protokolu OSPF 

#### HP VAN kontroler

V zadaní vytvoríme automatický deployovací skript pre nainštalovanie daného kontrolera na serveri.

#### Vytvorenie topológie

Pre vytvorenie jednotlivých veľkostí topológií a ich konfiguráciu vytvoríme buildovacie skripty pre SDN siete. Pre OSPF podporujúce siete vytvoríme konfiguračné súbory pre jednotlivé zariadenia v sieti.

#### Testovanie

Vytvoríme skripty pre automatické testovanie jednotlivých vykonaných meraní, a to pre merania času konvergencie a pre meranie času odozvy daného zariadenia pri zlyhaní jednotlivých liniek.

## Použité nástroje:
1. Mininet
2. HP VAN SDN kontroler
3. GNS3
4. Cisco ios
5. Ubuntu  
6. Virtual Box
7. Nástroj hrping
8. Nástroj tcping 
9. Python