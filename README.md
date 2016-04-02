## Overview

The script converts a Dutch numeral (for example: "tweehonderddrieenzeventig" or "160 duizend") to a number in digits (273 and 160000, respectively). This works for numbers up to "een biljard" (a quadrillion), but can easily be extended for even higher numbers. 

## Usage

```python
import num_to_int

n = num_to_int.number_finder("honderdvijfenzestig")
# 165

n = num_to_int.number_finder("160 miljoen")
# 160000000
```
