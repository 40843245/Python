[print(f'at least {i} soldiers') for i in range(500, 1000) if i%3==2 and i%5==3 and i%7==2]
print("\n".join([f'at least {i} soldiers' for i in range(500, 1000) if i%3==2 and i%5==3 and i%7==2]))