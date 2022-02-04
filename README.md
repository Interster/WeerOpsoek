# WeerOpsoek
Verkry die weer van 'n sekere gebied vanaf openweathermap.com deur 'n python intervlak.

Dit word gebruik om te bepaal of dit sin maak om die inverter op battery of lynkrag te hou.

Die volgende tutoriaal word gebruik om die toepassing te skryf:

https://realpython.com/build-a-python-weather-app-cli/



## Gebruik:

Sit 'n lêer genaamd secrets.ini met die openweathermap API key in die gebruikslêergids.



Sit volgende import in die kode:

```python
from WeerOpsoek import *
```



Gebruik nou die isBewolk() funksie wat True uitgee as dit bewolk is om te bepaal dat dit tyd is om terug te gaan na lynkrag met inverter.

