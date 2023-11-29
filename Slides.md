---
<!-- to see slides install: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode -->
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

using
# **NGINX**
as a 

reverse proxy
load balancer 
caching server


---

# Introductie

In deze demo gaan we kijken naar de mogelijkheden van NGINX als reverse proxy, load balancer en caching server.

---

# Maar wat is NGINX?

NGINX is een open source webserver en reverse proxy die veel gebruikt wordt in het bedrijfsleven. Het is een krachtig en veelzijdig stuk software dat kan worden gebruikt voor een breed scala aan toepassingen.



---

# Wat gaan we doen?
Korte introductie met de lesstof en daarna een demo.
In de demo zullen we de volgende stappen doorlopen:

- We zullen een eenvoudige NGINX configuratie maken die statische bestanden serveert;
- We zullen een reverse proxy implementeren die meerdere webservers aan 1 adress kan binden;
- We zullen een load balancing configuratie toevoegen aan de reverse proxy;
- We zullen een caching configuratie toevoegen aan 1 specifieke route.

---
# Reverse proxy
<!-- Een reverse proxy is een server die verzoeken van clients accepteert en deze doorstuurt naar een andere server. De reverse proxy kan worden gebruikt om een aantal voordelen te realiseren, zoals: -->
Primaire voordelen:
- Beveiliging: 
<!-- - de reverse proxy kan worden gebruikt om verzoeken te filteren of te beveiligen voordat ze worden doorgestuurd naar de backend server. -->
- Prestaties: 
<!-- - de reverse proxy kan worden gebruikt om verzoeken te cachen, waardoor de belasting van de backend server wordt verminderd. -->
- Load balancing: 
<!-- - de reverse proxy kan worden gebruikt om verzoeken over meerdere backend servers te verdelen, waardoor de prestaties en betrouwbaarheid worden verbeterd. -->
Nadelen?
- Single point of failure
<!-- - de reverse proxy kan een single point of failure worden, waardoor de betrouwbaarheid wordt verminderd. Hiermee wordt bedoeld dat als de reverse proxy uitvalt, de backend servers niet meer bereikbaar zijn. -->

---
# Load balancer
<!-- Een load balancer is een server die verzoeken van clients verdeelt over meerdere backend servers.Load balancers worden vaak gebruikt om de prestaties en betrouwbaarheid van webtoepassingen te verbeteren. -->
Opties: 
- nothing <!--Round-robin verdeling; verzoeken worden om de beurt naar de servers verdeeld. -->
- random <!-- Random verdeling; verzoeken worden willekeurig naar de servers verdeeld. -->
- least_conn <!-- Least_conn verdeling; verzoeken worden verdeeld op basis van het aantal actieve verbindingen of te wel, verzoeken worden naar de server met de minste actieve verbindingen verdeeld. -->
- ip_hash <!-- IP_hash verdeling; verzoeken worden verdeeld op basis van het IP-adres van de client; verzoeken van hetzelfde IP-adres worden naar dezelfde server verdeeld. --> 

Kunnen jullie voor en nadelen bedenken?
![bg left:40% 80%](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuKfCBialKd3EoKpDA-7Aoqz9LV39JqnnIin9p4jEBOA8E2KcPwVcfGId5fMb5XbY4JFYueAOeA2Reck7QW8o1ooDPXmX1KPS3a0sqAa0)

--- 
# Caching
Voordelen? <!-- aan hun zelf vragen-->

Nadelen? <!-- aan hun zelf vragen-->

![bg left:40% 80%](https://www.plantuml.com/plantuml/svg/ZL1BJiGm3Dtd5DPisC05MA2vYicuJKGQ5zkPSdmoiQ0KCH8xMy_lytnMGx6sbF00buopu0AMq40JRzf7Wgdm1Zm1Wj1x8pMm9DpcDD28CL70Q2mGIwPgOKMn7FEArU1Kvrm_Je0AOpg2Wpp0CHt1LunlL2-W95UISULZS1zuUd7DvwzWlKEUzbIGq1i8AJU9z0ZPOCkbW90rgRVLs0aU7Oljt6zU63RTpx7TRwo77BfoLVeTvCAaKDcwwfNkHNBDspu9B-Fg-890HVzM_7zGLze1tmyCht2_Mm-q-_ZVVg0XdFj1Myed)

<!-- ```plantuml
@startuml
' diagram that shows the flow of a request through the cache
actor client
participant "nginx" as nginx
participant "cache" as cache
participant "backend server" as server
client -> nginx: request
' if the cache has the resource, it will return it to the client
alt cache has resource
nginx -> cache: request
cache -> nginx: response
' if the cache does not have the resource, it will request it from the backend server
else cache does not have resource
nginx -> cache: request
cache -> server: request
server -> cache: response
cache -> nginx: response
end
nginx -> client: response


@enduml
``` -->


---
# Let's get started!