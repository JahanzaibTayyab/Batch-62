from typing import Dict,Union, Optional

my_dict: Dict[str, Union[str, list[str], int]] = {"name": "Mubarra", "age": 20, "courses": ["python", "nextjs"]}
print(my_dict)

dict1: Dict[str, Union[str, int, Optional[list[str]]]] = {"name": "Mubarra", "age": 20, "courses": None}


my_dict["name"].upper()
my_dict["courses"].append("django")

my_dict.get("name").upper()

my_dict.clear()
my_dict.fromkeys(["Mubarra", "python"])

my_dict["roll_no"] = "BS34"
