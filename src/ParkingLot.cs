using System;
using System.Collections.Generic;
using System.Linq;

namespace ParkingLotApp
{
		public class ParkingLot
		{
			private int LotSize { get; set; }
			private List<Vehicle> Vehicles = new List<Vehicle>();
			public decimal TotalRevenue { get; private set; }
			private static int id = 1;
			
			public ParkingLot(int lotSize)
			{
				LotSize = lotSize;
			}
			
			//Assuming no race-conditions to avoid using Threading.
			public static int generateId()
			{
				return id++;
			}

			public void Park(Vehicle vehicle)
			{
				if (Vehicles.Count >= 100)
				{
					throw new IndexOutOfRangeException("Cannot park: Lot is full.");
				}
				Vehicles.Add(vehicle);
				TotalRevenue += vehicle.CalculateCharge();
			}

			public void Unpark(int id)
			{
				var vehicle = Vehicles.FirstOrDefault(v => v.Id == id);
				if (vehicle != null)
				{
					Vehicles.Remove(vehicle);
				}
			}

			public decimal GetRevenue()
			{
				return TotalRevenue;
			}

			public decimal GetRevenueByVehicleType(Type vehicleType)
			{
				return Vehicles.Where(v => v.GetType() == vehicleType).Sum(v => v.CalculateCharge());
			}

			public List<Vehicle> ListVehicles()
			{
				return Vehicles;
			}

			public List<Vehicle> ListVehiclesByType()
			{
				return Vehicles.OrderBy(v => v.GetType().Name).ToList();
			}

			public List<Vehicle> ListVehiclesById()
			{
				return Vehicles.OrderBy(v => v.Id).ToList();
			}
		}
}
