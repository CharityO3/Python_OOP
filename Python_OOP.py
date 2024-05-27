import csv
import matplotlib.pyplot as plt


def read_population_data(file_name):
  """
  Extracts the population data from the data.csv file and return a dictionary with the following structure: {"Africa": {"population":[100, 200, 300], years: [1990, 2000, 2010]}.
  
  """

  out_put = {}

  with open(file_name, "r") as csv_file:
    reader = csv.DictReader(csv_file)  # we will like the data as a dictionary
    for line in reader:
      continent = line["continent"]
      year = int(line["year"])
      population = int(line["population"])
      if continent not in out_put:
        out_put[continent] = {"population": [], "years": []}

      out_put[continent]["population"].append(population)
      out_put[continent]["years"].append(year)

  return out_put


def generate_plot_population_per_continent(population_dictionary):
  """
  Generates a plot of the population per continent from a dictionary and returns a plot per continent.
  """
  for continent in population_dictionary:
    year = (population_dictionary[continent]["years"])
    population = (population_dictionary[continent]["population"])
    plt.plot(year, population, label=continent, marker="o", alpha=0.5)
  plt.title("Internet User Population Per Continent", fontweight="bold")
  plt.xlabel("Year", fontweight="bold")
  plt.ylabel("Population (in billion users)", fontweight="bold")
  plt.legend()
  plt.grid(True)
  plt.show()


file_name = "data.csv"

# Displays internet population in a plot
population_per_continent = read_population_data(file_name)
generate_plot_population_per_continent(population_per_continent)
