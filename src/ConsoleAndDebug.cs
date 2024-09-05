using System;
using ParkingLotApp;

public class Program
{
	public static void Main(string[] args)
	{
		ParkingLot parkingLot = new ParkingLot(100);		

        Vehicle compact = new Compact(ParkingLot.generateId());
        Vehicle full = new Full(ParkingLot.generateId());
        Vehicle truck = new Truck(ParkingLot.generateId());
        Vehicle motorcycle = new Motorcycle(ParkingLot.generateId());
        Vehicle electric = new Electric(ParkingLot.generateId());

		parkingLot.Park(compact);
        parkingLot.Park(full);
        parkingLot.Park(truck);
        parkingLot.Park(motorcycle);
        parkingLot.Park(electric);

		var vehicles = parkingLot.ListVehiclesByType();

		Console.WriteLine($"Total Money Collected: ${parkingLot.GetRevenue()}");
		foreach (var vehicle in vehicles)
		{
			Console.WriteLine($"Vehicles by type: {vehicle}");
		}

	}
}
