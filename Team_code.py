# Python Script: Team Information + Favorite Gene DNA Sequence

team = [
    {
        "name": "Sweeta Selvan",
        "slack_username": "@sweeta",
        "country": "India",
        "hobby": "Watching films",
        "affiliation": "Student (Anna University, Chennai), UAA",
        "favorite_gene": {
            "gene_name": "TP53",
            "dna_sequence": "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACA"
        }
    },
    {
        "name": "Aditya Dash",
        "slack_username": "@aditya",
        "country": "India",
        "hobby": "Playing cricket",
        "affiliation": "Student (IIT Bhubaneswar)",
        "favorite_gene": {
            "gene_name": "BRCA1",
            "dna_sequence": "ATGGAAGTTGTCATTTTATAAAAAGGTTGCAAAATAATGTGGAAGAAAAAAAGCAGTGAACCTGTTGGTGATTTTGAAATGAGGAGGA"
        }
    },
    {
        "name": "Gloria Omogwigho Akpederi",
        "slack_username": "@gloria",
        "country": "Nigeria",
        "hobby": "Baking",
        "affiliation": "Student (University of Lagos)",
        "favorite_gene": {
            "gene_name": "ACE2",
            "dna_sequence": "ATGGAGAGCCCTGTTCACATCTCCTCCTGCTCTCCTGCTCCTGCTCCTGCTCCTGGAGGAGGAGATCTTCCTCCTGCTGCTCTGCCT"
        }
    },
    {
        "name": "Umunakwe Goodness",
        "slack_username": "@goodness",
        "country": "Nigeria",
        "hobby": "Reading novels",
        "affiliation": "Student (University of Nigeria, Nsukka)",
        "favorite_gene": {
            "gene_name": "HBA1",
            "dna_sequence": "ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGG"
        }
    }
]

# Print the information
for member in team:
    print(f"Name: {member['name']}")
    print(f"Slack Username: {member['slack_username']}")
    print(f"Country: {member['country']}")
    print(f"Hobby: {member['hobby']}")
    print(f"Affiliation: {member['affiliation']}")
    print(f"Favorite Gene: {member['favorite_gene']['gene_name']}")
    print(f"DNA Sequence: {member['favorite_gene']['dna_sequence']}")
    print("-" * 70)
