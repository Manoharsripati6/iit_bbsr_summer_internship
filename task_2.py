import json
"""
Task 2 File handeling
    ● Read a text file containing log entries as below: (if data not given generate random data)
    INFO User logged in
    ERROR Database timeout
    WARNING Memory usage high
    ERROR Invalid credentials
    Write a script that :
    ● Count occurrences of each log type.
    ● Save the results into a JSON file.
    ● Print the most frequent log type.
"""

def format_log(d : dict)->None:
    sorted_log = dict(sorted(d.items(), key=lambda x: x[1],reverse=True))
    
    with open("log.json", "w") as f:
        json.dump(sorted_log, f, indent=4)
    max_key = next(iter(sorted_log))
    print("Max Log Details")
    print(f"log : {max_key}, occurrence {sorted_log[max_key]}")



if __name__ == "__main__":
    with open("log.txt","r") as f:
        data = f.read().splitlines() #file reading

    file_log={} #logs dictionaries

    for i in data:
        log=i.split() #
        if log[0] in file_log:
            file_log[log[0]]+=1
        else:
            file_log[log[0]]=1
    format_log(file_log)