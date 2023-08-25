class Population:
    def __init__(self, year, population):
        self.year = year
        self.population = population


class Country:
    def __init__(self, name):
        self.name = name
        self.populations = []

    def add_population(self, population):
        self.populations.append(population)

    def calculate_growth_rate(self, start_year, end_year):
        start_pop = self.get_population(start_year)
        end_pop = self.get_population(end_year)
        growth_rate = ((end_pop - start_pop) / start_pop) * 100
        return growth_rate

    def get_population(self, year):
        for pop in self.populations:
            if pop.year == year:
                return pop.population
        return None

    def project_population(self, future_year, growth_rate):
        current_year = max(pop.year for pop in self.populations)
        current_pop = self.get_population(current_year)
        projected_pop = current_pop * (1 + growth_rate / 100) ** (future_year - current_year)
        return projected_pop

def main():
    print("Welcome to Population Analysis Tool")

    country_name = input("Enter country name: ")

    country = Country(country_name)

    while True:
        print("\nOptions:")

        print("1. Add Population Data")

        print("2. Calculate Growth Rate")

        print("3. Project Future Population")

        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            year = int(input("Enter year: "))

            population = int(input("Enter population: "))

            country.add_population(Population(year, population))

            print("Population data added successfully.")


        elif choice == "2":
            start_year = int(input("Enter start year: "))

            end_year = int(input("Enter end year: "))

            growth_rate = country.calculate_growth_rate(start_year, end_year)

            print(f"The average growth rate from {start_year} to {end_year} is {growth_rate:.2f}%.")


        elif choice == "3":
            future_year = int(input("Enter future year: "))

            growth_rate = float(input("Enter growth rate (%): "))

            projected_pop = country.project_population(future_year, growth_rate)

            print(f"The projected population in {future_year} is estimated to be {projected_pop:.0f}.")

            
        elif choice == "4":
            print("Exiting the Population Analysis Tool.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()