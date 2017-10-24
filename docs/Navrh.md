# A Convergence Time Optimization Paradigm for OSPF based Networks Through SDN SPF Protocol
### Peter Kaňuch, Nikolas Janec
### Cvičiaci: Tomáš Boros, Utorok 19:00

## Úvod

Článok sa zaoberá porovnaním OSPF, pretože najčastejšie používaným protokolom vo firemných sieťach je  práve tento protokol a SDN sieťami s kontrolérom podporujúcim algoritmus Shortest Path First (SPF) pre určenie najkratšej cesty. Autori porovnávajú konvergencie časov napríklad pri výpadku linky medzi Softvérovo definovanými sieťami (SDN) a sieťami fungujúcimi s protokolom OSPF. Taktiež overujú aj Response time pre dané zariadenie. Svoje riešenie overili pomocou Mininetu pre SDN a pre overenie OSPF použili GNS3 s použitím CISCO ios pri rôznych veľkostiach topológií (10, 20, 30 switchov(SDN)/routerov(ios)).  

## Návrh zadania

V našom riešení sme sa rozhodli overiť nasledujúce výsledky ich práce:
1. Konvergenciu SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch
2. Konvergenciu OSPF siete na Cisco ios routroch
3. Response time SDN siete v mininete s pomocou kontroleru podporujúcim SPF algoritmu na OFswitchoch
4. Response time OSPF siete na Cisco ios routroch
5. Veľkosti topológií: 10, 20, 30 switchov(SDN)/routerov(ios)
6. Rôzne časy časovačov (dead interval, ...) protokolu OSPF 


##Použité nástroje:
1. Mininet
2. HP VAN SDN kontroler
3. GNS3
4. Cisco ios
5. Ubuntu 14.04 
6. Virtual Box 5.1.28
7. Nástroj hrping
8. Nástroj tcping 