# collatz
Number tree calculator for [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) with python.

## Usage

```
from collatz import Collatz

c = Collatz()
c.start(7) # Returns Dict

{'Number': 7,  # Calculated number
'Tree': [22, 11.0, 34.0, 17.0, 52.0, 26.0, 13.0, 40.0, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0],  # Calculation result
'Step': 16,  # How many step taken
'Start Time': 257865.707277785,  # Calculation start time
'End Time': 257865.707365228,  # Calculation end time
'Calculated Time': 8.744301158003509e-05,  #  How much time take
'Recalculated': True  #  If calculation did twice it will not recalculate and return first cached result
}
```