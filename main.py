from fastapi import FastAPI
import swisseph as swe
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Swetha Jothidam Server Ready - Thirukanitham"}

@app.post("/api/jathagam")
def get_jathagam(data: dict):
    try:
        year = int(data.get('year', 1990))
        month = int(data.get('month', 1))
        day = int(data.get('day', 1))
        hour = int(data.get('hour', 12))
        minute = int(data.get('minute', 0))

        # Thirukanitham - Lahiri Ayanamsa
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        jd = swe.julday(year, month, day, hour + minute/60.0)

        planets = {}
        names = {0:"Sooriyan", 1:"Chandran", 2:"Sevvai", 3:"Budhan", 4:"Guru", 5:"Sukran", 6:"Sani"}
        for p_id in [0,1,2,3,4,5,6]:
            calc = swe.calc_ut(jd, p_id, swe.FLG_SIDEREAL)
            planets[names[p_id]] = calc[0]

        return {"success": True, "planets": planets, "ayanamsa": "Lahiri Thirukanitham"}
    except Exception as e:
        return {"success": False, "error": str(e)}
