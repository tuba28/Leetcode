import pandas as pd
from datetime import datetime

def calculate_average_speed(file_path, distance_km=250):  # Adjust distance as needed
    df = pd.read_csv(file_path)
    
    # Ensure timestamps are in datetime format
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
    print(f'Average Speed from Pune to Solapur: {avg_speed:.2f} km/h')
    return avg_speed

# Example usage
file_path = 'Feb_1-7_Pune-Solapur.csv'  # Update with actual file path
calculate_average_speed(file_path)
