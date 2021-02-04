#!/usr/bin/python3

import sys
import csv
import re
import os
import gzip
from dataclasses import dataclass

# Model
@dataclass
class Candidatura:
    nombre_candidato: str
    num_candidatura: int
    es_suplente: bool
    nombre_partido: str
    abbr_partido: str
    fecha: str


def parse_file(file_name, date):
    new_party, party_name, party_abbr, is_alternate = True, None, None, False
    candidate_regex = re.compile(r"(\d+)\. (?:(?:Doña|Don) )?(.*)")
    with gzip.open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.decode('utf-8').strip().replace('\n', '')
            if new_party:
                party_info = line.split("(")
                party_name = party_info[0].strip()
                if len(party_info) > 1:
                    party_abbr = party_info[1].split(")")[0]
                new_party = False
            elif line == 'Suplentes':
                is_alternate = True
            elif line == "":
                new_party, party_name, party_abbr, is_alternate = True, None, None, False
            else:
                candidate = line
                candidate_info = candidate_regex.search(candidate)
                if candidate_info is None:
                    raise ValueError(candidate)
                candidate_info = candidate_info.groups()
                yield Candidatura(
                    nombre_partido=party_name,
                    nombre_candidato=candidate_info[1],
                    es_suplente=is_alternate,
                    abbr_partido=party_abbr,
                    num_candidatura=int(candidate_info[0]),
                    fecha=date
                )


def parse():
    writer = csv.DictWriter(sys.stdout, fieldnames=list(Candidatura.__annotations__.keys()))
    writer.writeheader()
    files_path = os.path.abspath(sys.argv[1])
    txt_path = os.path.join(files_path, 'txt')
    dates = read_info(files_path)
    for file in os.listdir(txt_path):
        if file.endswith(".gz"):
            for obj in parse_file(os.path.join(txt_path, file), dates[file]):
                writer.writerow(obj.__dict__)
                pass


def read_info(files_path):
    with open(os.path.join(files_path, 'info.csv')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        info = {}
        for row in csv_reader:
            info[(os.path.basename(row[0]).replace('%20', ' ').replace('.pdf', '.txt.gz')).lower()] = row[1]
    return info


if __name__ == '__main__':
    parse()

