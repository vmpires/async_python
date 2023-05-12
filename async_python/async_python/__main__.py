import time
import asyncio
from faker import Faker

fake = Faker()

async def calculate_tax(value):
    print("Tax: ", value * 0.1)

async def calculate_worker_bonus(sales):
    for worker in sales:
        sale = sales[worker]
        print(worker, f"Bonus: {(sale * 0.05):.2f}")
        await asyncio.sleep(1)

async def closing():
    sales = {
        "Victor": fake.random_int(min=500, max=2000),
        "Jaci": fake.random_int(min=600, max=3000),
        "Lorenzo" :fake.random_int(min=1000, max=5000)
    }

    gross_value = fake.random_int(min=1000, max=10000)
    task1 = asyncio.create_task(calculate_worker_bonus(sales))
    task2 = asyncio.create_task(calculate_tax(gross_value))

    print("Gross Value: ", gross_value)
    print("\nIt's closed.")

    await task1, task2


if __name__ == "__main__":
    asyncio.run(closing())
