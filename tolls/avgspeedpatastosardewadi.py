import pandas as pd
from datetime import datetime

def calculate_average_speed(file_path, distance_km, vehicle_type = "All"):  
    df = pd.read_csv(file_path)
    if vehicle_type != "All":
        df = df[df["avc"]==vehicle_type]
    
    df['txnTime'] = pd.to_datetime(df['txnTime'])
    df = df.sort_values(by=['vehicleRegNo', 'txnTime'])
    
    travel_times = []
    vehicle_groups = df.groupby('vehicleRegNo')
    
    for vehicle, data in vehicle_groups:
        if len(data) >= 2:
            entry_time = data.iloc[0]['txnTime']
            exit_time = data.iloc[-1]['txnTime']
            travel_time = (exit_time - entry_time).total_seconds() / 3600  # Convert to hours
            
            if travel_time > 0:  # Avoid division by zero
                speed = distance_km / travel_time
                travel_times.append(speed)
    
    avg_speed = sum(travel_times) / len(travel_times) if travel_times else 0
    print(f'Average Speed from Patas to Sawaleshwar: {avg_speed:.2f} km/h for ' + vehicle_type + ' vehicle type.')
    return avg_speed

txn_file = "C:/Users/HP/Documents/GitHub/Leetcode/tolls/Feb_1-7_Pune-Solapur.csv"
speedanalysisfile = "C:/Users/HP/Documents/GitHub/Leetcode/tolls/Toll plaza list for speed analysis.xlsx"
dfsp = pd.read_excel(speedanalysisfile )
filter_dfsp = dfsp[dfsp["Corridor Name"]=="Pune - Solapur"]
filter_dfsp = filter_dfsp.dropna(subset=["prev toll plaza"])
distance_from_patas_to_sawaleshwar = filter_dfsp["prev toll plaza"].sum()
calculate_average_speed(txn_file,distance_from_patas_to_sawaleshwar, "VC5")
