# A Convergence Time Optimization Paradigm for OSPF based Networks Through SDN SPF Protocol
### Peter Kaňuch, Nikolas Janec
### Cvičiaci: Tomáš Boros, Utorok 19:00

## Úvod

Článok sa zaoberá porovnaním OSPF, pretože najčastejšie používaným protokolom vo firemných sieťach je  práve tento protokol a SDN sieťami s kontrolérom podporujúcim algoritmus Shortest Path First (SPF) pre určenie najkratšej cesty. Autori porovnávajú konvergencie časov napríklad pri výpadku linky medzi Softvérovo definovanými sieťami (SDN) a sieťami fungujúcimi s protokolom OSPF. Taktiež overujú aj Response time pre dané zariadenie. Svoje riešenie overili pomocou Mininetu pre SDN a pre overenie OSPF použili GNS3 s použitím CISCO ios pri rôznych veľkostiach topológií (10, 20, 30 switchov(SDN)/routerov(ios)).  

## Analýza

### SDN siete

Software-Defined Networks (SDN) je centralizovaná topológia architektúry. 

![SDN](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/sdn-architecture.png)

SDN architektúra sa skladá z:
- Aplikačná vrstva - ponúka služby pre virtualizáciu, smerovanie, firewall, ...
- Control vrstva - pozostáva z kontrolera, ktorý jednak komunikuje s aplikáciami cez rozhranie, ale aj priamo s fyzickou vrstvou (infraštruktúrou).
- Vrstva infraštruktúry 

Základ v SDN tvorí virtualizácia. Dovoľuje, aby softvér bežal nezávisle od hardvéru.

### Protokol OpenFlow

Komunikačný protokol pre SDN siete, ktorý umožňuje priamu interakciu kontrolera s fyzickými zariadeniami. Je štandard, ktorý dovoľuje vzdialene konfigurovať zariadenia od rôznych výrobcov. 
Taktiež umožňuje úpravusmerovacích tabuliek pomocou pridávania rôznych pravidiel. 

### Mininet

Mininet je virtuálna sieť pre simuláciu SDN sieti. Napodobňuje kompletnú sieť zariadení ako hosty, prepínače a jednotlivé prepojenia medzi nimi. 
Dokáže simulovať sieť pomocou virtualizácie založeniej na procesoch.
Taktiež podporuje protokol OpenFlow. 
![SDN](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/img/HPVAN.jpg)
[comment]: <> (https://github.com/mininet/mininet)

### HP VAN SDN

HP VAN SDN kontrolér je softvér, ktorý poskytuje centrálny bod pre správu sieti podporujúce protokol OpenFlow. Taktiež poskytuje rozhranie pre vývoj Java aplikácií inými vývojarmi. Je navrhnutý najmä pre fungovanie v dátových centrách.
[comment]: <> (https://www.sdxcentral.com/products/hp-virtual-application-networks-van-sdn-controller/)

## Návrh zadania

V našom riešení sme sa rozhodli overiť nasledujúce výsledky ich práce:
1. Konvergenciu SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch
2. Konvergenciu OSPF siete na Cisco ios routroch
3. Response time SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch
4. Response time OSPF siete na Cisco ios routroch
5. Veľkosti topológií: 10, 20, 30 switchov(SDN)/routerov(ios)
6. Rôzne časy časovačov (dead interval, ...) protokolu OSPF 


## Použité nástroje:
1. Mininet
2. HP VAN SDN kontroler
3. GNS3
4. Cisco ios
5. Ubuntu  
6. Virtual Box
7. Nástroj hrping
8. Nástroj tcping 