import csv

classes = {
    "passeriformes": {
        "turdidae": ["bicthr", "amerob", "woothr", "veery", "swathr", "herthr", "gycthr", "thsh", "gcbi", "with", "blueb"],
        "regulidae": ["gocking"],
        "parulidae": ["grawar", "virwar", "yetwar", "yelwar", "woewar1", "towwar", "swawar", "prowar", "prawar", "pinwar", "orcwar", "kirwar", "kenwar", "herwar", "gowwar", "conwar", "cerwar", "buwwar", "btywar", "bkbwar", "tenwar", "naswar", "magwar", "btnwar", "bkpwar", "babwar", "macwar", "hoowar", "yerwar", "mouwar", "paalwar", "norwat", "wlswar", "canwar", "ovenbi1", "norpar", "comyel", "chswar", "camwar", "btbwar", "bawwar", "amered", "sbuf", "dewa", "zeep", "dbup", "bzwa", "mwar"],
        "icteridae": ["wesmea", "orcori", "easmea", "balori", "boboli"],
        "passerellidae": ["amtspa", "swaspa", "sonspa", "seaspa", "nstspa", "linspa", "larspa", "harspahenspa", "gocspa", "foxspa", "brespa", "vesspa", "fiespa", "lecspa", "clcspa", "graspa", "whcspa", "whtspa", "savspa", "daejun", "chispa", "cups", "swli", "sfhs", "hssp", "desp", "ccbrs"],
        "cardinalidae": ["sumtan", "paibun", "lazbun", "blugrb1", "dickci", "scatan", "indbun", "robgro", "bunt", "tana", "gros"],
        "calcariidae": ["snobun", "smilon", "laplon"],
        "motacillidae": ["sprpip", "amepip"],
        "corvidae": [],
        "alaudidae": ["horlar"],
        "bombycillidae": ["cedwax"],
        "sittidae": ["rebnut"]
    },
    "charadriiformes": {
        "charadriidae": ["amgplo", "killde", "bkbplo", "semplo"],
        "recurvirostridae": ["ameavo", "bknsti"],
        "Laridae": ["forter", "comter", "caster1", "blkski"],
        "scolopacidae": ["dunlin", "baisan", "wilsni1", "willet1", "whimbr", "sander", "lobdow", "lobcur", "lesyel", "solsan", "sposan", "shbdow", "leasan", "greyel", "uplsan"],
        "haematopodidae": ["blkoys", "ameoys"]
    },
    "pelecaniformes": {
        "ardeidae": ["triher", "ycnher", "greegr", "grbher3", "grnher", "amebit", "bcnher"]
    },
    "cuculiformes": {
        "cuculidae": ["bkbcuc", "yebcuc"]
    }
}

def find_species_info(target_input):
    for order, families in classes.items():
        for family, species_list in families.items():
            if target_input in species_list:
                return [target_input, family, order]
            elif target_input == family:
                return ["N/A", target_input, order]
    return ["N/A", "N/A", target_input]

target_input_1 = "ardeidae"
result_1 = find_species_info(target_input_1)

with open('TVILLE.csv', 'r') as f:
    with open('speciesoutput.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'Time Detected', 'Species', 'Family', 'Order'])
        
        for lines in csv.reader(f):
            if lines[5] != 'date':
                result = find_species_info(lines[3])
                csv_writer.writerow([lines[5], lines[9], result[0], result[1], result[2]])
        
    