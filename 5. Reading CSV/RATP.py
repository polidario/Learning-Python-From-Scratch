# Read the CSV file using csv package and place the data in a class instaces
# with the following schema:
# - rank: int
# - network: string
# - name: string
# - number_of_users: int
# - connections: list[string]
# - City: string
# - district: int | None
import csv
from dataclasses import dataclass

FILE_PATH = "resources/RATP.csv"

@dataclass
class Station:
    rank: int
    network: str
    name: str
    number_of_users: int
    connections: list[str]
    city: str
    district: int | None

def read_csv(file_path: str) -> list[Station]:
    stations = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            station = Station(
                rank=int(row[0]),
                network=row[1],
                name=row[2],
                number_of_users=int(row[3]),
                connections=row[4].split(","),
                city=row[9],
                district=int(row[10]) if row[10] else None
            )
            stations.append(station)
    return stations

stations = read_csv(FILE_PATH)
print(stations[0])