from Bio import Entrez
Entrez.email = "miltul@utu.fi"

# how many hits for (complete) human p53 protein search
def searchEntrez(database, query):
    handle = Entrez.search(db=database, term=query)
    record = Entrez.read(handle)
    return record["Count"]

protein = searchEntrez("protein", "p53 AND human[Orgn]")
complete = searchEntrez("protein", "p53 AND human[Orgn] AND complete")

print protein, "hits found for protein p53 in human."

print complete, "hits found for complete protein p53 in human."
