#!/usr/bin/env python3
from models.base_model import BaseModel

base1 = BaseModel()
print(base1)
print(base1.id)
print(base1.created_at)
print(base1.updated_at)

print("----------------------------------------")

base2 = BaseModel()
print(base2)
print(base2.id)
print(base2.created_at)
print(base2.updated_at)