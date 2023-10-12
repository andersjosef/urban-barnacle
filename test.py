import json

ordbok = {
    1: {
        "0, 0": {
            "upper":[["1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "5, 8"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "4, 8"]],
            "under":[["1, 1", "2, 6", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "2, 6", "1, 4"], 
                     ["3, 3", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "2, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 6", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 15", "1, 4", "2, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["4, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 2", "1, 4", "1, 4", "1, 4", "1, 4", "2, 6", "1, 4", "1, 4", "3, 5", "4, 6", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 3", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "3, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 2", "1, 4", "1, 4", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"]
                     ],
            "enemies": [
                {"pos": (7, 7),
                 "members": ["mage", "mage"]}
            ]
        },
        "0, 1": {
            "upper":[["1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "1, 8", "5, 8"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "1, 0"], 
                     ["0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "0, 8", "4, 8"]],
            "under":[["1, 1", "2, 6", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "2, 6", "1, 4"], 
                     ["3, 3", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "2, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 6", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 15", "1, 4", "2, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["4, 15", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 2", "1, 4", "1, 4", "1, 4", "1, 4", "2, 6", "1, 4", "1, 4", "3, 5", "4, 6", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 3", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "3, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["3, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 2", "1, 4", "1, 4", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["2, 1", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"], 
                     ["1, 1", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4", "3, 5", "1, 4", "1, 4", "1, 4", "1, 4", "1, 4"]
                     ],
            "enemies": [
                {"pos": (8, 2),
                 "members": ["knight", "mage"]}
            ]
        }
        } 

}

with open("data/maps/test.json", "w") as outfile:
    json.dump(ordbok, outfile)