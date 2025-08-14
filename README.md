# ⚾ MLB Hall of Pretty Good

Search any MLB player since 1990 to see if they're eligible for the "Hall of Pretty Good"

**🌐 [Live Website](https://timmymatten.github.io/mlb_hall_of_good/)**

## What is the Hall of Pretty Good?

The Hall of Pretty Good celebrates MLB players who had solid, respectable careers but fell short of baseball's highest honors. Inspired by [@mlbhallofgood](https://www.instagram.com/mlbhallofgood/) on Instagram.

## Eligibility Criteria

To qualify for the Hall of Pretty Good, a player must meet **ALL** of these requirements:

- ⚾ **Career bWAR ≤ 38.6**
- 🏅 **No MVP Awards**
- 🏆 **No Cy Young Awards** 
- 🎖️ **Not in Hall of Fame**
- 📊 **Batting Average ≥ .200** (hitters only)
- 🎯 **Career Hits ≥ 1,000** (hitters only)
- ⏰ **Officially retired** or 3+ years inactive

## Examples

| Player | Status | Reason |
|--------|--------|--------|
| Hunter Pence | ✅ ELIGIBLE | 32.8 bWAR, no major awards |
| Derek Jeter | ❌ NOT ELIGIBLE | Hall of Famer, 71.3 bWAR |
| R.A. Dickey | ❌ NOT ELIGIBLE | Won 2012 Cy Young Award |
| Bobby Abreu | ✅ ELIGIBLE | 36.4 bWAR, solid career |

## Features

- 🔍 Search 1,900+ players since 1990
- 📊 Real career statistics from Baseball Reference
- 🏅 Accurate awards data (MVP, Cy Young, HOF)
- ⚡ Instant eligibility checking
- 📱 Mobile-friendly design

## Data Sources

- **Statistics**: Baseball Reference via [PyBaseball](https://github.com/jldbc/pybaseball)
- **Awards**: Comprehensive database of MLB award winners 1990-present

## How to Update Data

```bash
pip install pybaseball pandas
python get_baseball_data.py
```

## Credits

Inspired by [@mlbhallofgood](https://www.instagram.com/mlbhallofgood/) • Data from Baseball Reference

---

*Celebrating baseball's "pretty good" players since 1990* ⚾
