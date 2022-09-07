
# To declare static type data structures is needed to import 
from typing import Tuple, Dict, List

# Example of static type variables 
a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)

# Example of static type function
def suma(a: int, b: int) -> int :
	return a + b

# Delcare a list formed by integers
positives: List [int] = [1,2,3,4,5]

# Delcare a dictionary formed by string keys and integer values
users: Dict [str, int] = {
	"argentina": 1,
	"mexico": 34,
	"colombia": 45
}

# Delcare a list formed by dictionaries
countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]


CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]