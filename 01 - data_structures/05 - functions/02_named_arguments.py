def save_car(brand, model, year, plate):
    # save car in database...
    print(f"Car inserted successfully! {brand}/{model}/{year}/{plate}")


save_car("Fiat", "Palio", 1999, "ABC-1234")
save_car(brand="Fiat", model="Palio", year=1999, plate="ABC-1234")
save_car(**{"brand": "Fiat", "model": "Palio", "year": 1999, "plate": "ABC-1234"})