# KingdomsAndWarfare

# How To

## Make a Unit

```
from KingdomsAndWarfare.Units.Unit import Unit
splonks = Unit("Splonks Infantry", "Splonks with knives.")
```

## Have a unit attack another unit

```
from random import randint
splonks.attack(target, randint(1,20), randint(1,20))
```

## Install

`pip install KingdomsAndWarfare`
https://pypi.org/project/KingdomsAndWarfare/

## Build and publish

`python -m build`
`twine upload dist/*`