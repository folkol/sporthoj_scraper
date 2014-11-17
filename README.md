Scraper for exporting sporthoj blogs
------------------------------------
(This readme is in Swedish)

Min (manuella) test suite har varit:

1. "Kör utan att det smäller för dessa 5 bloggar"
2. "~5 random stickprover har varit ok"

Några kommentarer:
- Markupen är helt sanslöst dålig, så det har varit svårt att få ut strukturerad text
- Det enda som kommer med ur en bloggpost är div/table/p/li-taggar
- Det hade varit enklare att kollapsa all text ut varje post, men då hade det varit jävligt svårt att se om resultatet blev "ok"

Kör mig:

	pip install beautifulsoup4
    python scraper.py rockmorsanaventyr
    python scraper.py rockmorsan_del1
    python scraper.py rockmorsan_del2
    python scraper.py rockmorsan_del3
    python scraper.py rockmorsan
