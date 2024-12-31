# A Dictionary representing the three types of results
RESULTS_TYPE = {
    "PAX" : 1,
    "RAW" : 2,
    "LAP" : 3
}

# A Dictionary representing the possible attributes from the data tables.
RECORD_ATTRIBUTES = {
    ('paxPosition', 'classPosition', 'class', 'number', 'driver', 'car', 'total', 'factor', 'paxTime', 'diff', 'fromFirst') : 1,
    ('rawPosition', 'classPosition', 'class', 'number', 'driver', 'car', 'rawTime', 'diff', 'fromFirst') : 2,
    ('position', 'class', 'number', 'driver', 'car', 'color', 'run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'total', 'diff') : 3
}

# Represents the header that would be sent if the request was from a browser
BROWSER_REQ_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}