def parse_logs(file_path):
    parsed_logs=[]
    
    with open(file_path,'r') as file:
        for log in file:
            parts=log.split()
            
            
            parsed_logs.append({
                "date" : parts[0],
                "time" : parts[1],
                "status" : parts[2],
                "user": parts[3].split('=')[1],
                "ip":parts[4].split('=')[1]
                })
    
    return parsed_logs