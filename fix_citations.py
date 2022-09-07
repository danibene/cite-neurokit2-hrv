import bibtexparser
from bibtexparser.bibdatabase import BibDatabase

with open("Exported Items.bib") as bibtex_file:
    bibtex_database = bibtexparser.load(bibtex_file)

unique_key = "ID"
for entry in bibtex_database.entries_dict:
    if unique_key in bibtex_database.entries_dict[entry].keys():
        print(bibtex_database.entries_dict[entry][unique_key])

remove_keys = ["url", "doi", "eprint", "file"]
keep_keys = []
with open("Exported Items.bib") as bibtex_file:
    bibtex_database = bibtexparser.load(bibtex_file)

new_entries = []
for entry in bibtex_database.entries:
    if "date" in entry.keys():
        entry["year"] = entry["date"].split("-")[0]
    if "year" in entry.keys():
        entry["year"] = entry["year"].split("-")[0]

        new_entry = entry
        new_entries.append(new_entry)

new_bibtex_database = BibDatabase()
new_bibtex_database.entries = new_entries

with open("new_bibtex.bib", "w") as bibtex_file:
    bibtexparser.dump(new_bibtex_database, bibtex_file)
    bibtexparser.dump(bibtex_database, bibtex_file)
