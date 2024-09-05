using Xunit;
using ParkingLotApp;
using System;

namespace ParkingLotTests
{
	public class ParkingLotTests
	{
		private ParkingLot parkingLot;
		public Vehicle compact = new Compact(ParkingLot.generateId());
		public Vehicle full = new Full(ParkingLot.generateId());
		public Vehicle truck = new Truck(ParkingLot.generateId());
		public Vehicle motorcycle = new Motorcycle(ParkingLot.generateId());
		public Vehicle electric = new Electric(ParkingLot.generateId());

		[Fact]
		public void Singlular_CalculateCharge()
		{
			var compact = new Compact(1);
			var charge = compact.CalculateCharge();
			Assert.Equal(20.00m, charge);
		}
		
		public ParkingLotTests()
		{
			parkingLot = new ParkingLot(100);
		}

		[Fact]
		public void GenerateId_Returns_Unique()
		{
			Assert.NotEqual(motorcycle.Id, compact.Id);
			Assert.NotEqual(motorcycle.Id, truck.Id);
			Assert.NotEqual(compact.Id, truck.Id);
		}

		[Fact]
		public void TotalRevenue_Correct()
		{	
			parkingLot.Park(compact);
			parkingLot.Park(full);
			parkingLot.Park(truck);
			parkingLot.Park(motorcycle);
			parkingLot.Park(electric);
			Assert.Equal(96.00m, parkingLot.GetRevenue());
		}

		[Fact]
		public void RevenueByVehicleType_Singular_Correct()
		{
			parkingLot.Park(compact);
			parkingLot.Park(full);
			parkingLot.Park(truck);
			parkingLot.Park(motorcycle);
			parkingLot.Park(electric);
			Assert.Equal(20.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Compact)));
			Assert.Equal(22.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Full)));
			Assert.Equal(23.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Truck)));
			Assert.Equal(10.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Motorcycle)));
			Assert.Equal(21.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Electric)));
		}

		[Fact]
		public void RevenueByVehicleType_Many_Correct()
		{
			for (int i=0; i<13; i++) parkingLot.Park(compact);
			for (int i=0; i<22; i++) parkingLot.Park(full);
			for (int i=0; i<44; i++) parkingLot.Park(truck);
			for (int i=0; i<7; i++) parkingLot.Park(motorcycle);
			for (int i=0; i<9; i++) parkingLot.Park(electric);
			Assert.Equal(260.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Compact)));
			Assert.Equal(484.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Full)));
			Assert.Equal(1012.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Truck)));
			Assert.Equal(70.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Motorcycle)));
			Assert.Equal(189.00m, 
				parkingLot.GetRevenueByVehicleType(typeof(Electric)));
		}

		[Fact]
		public void ListVehicles_Count_Correct()
		{
			for (int i=0; i<13; i++) parkingLot.Park(truck);
			for (int i=0; i<22; i++) parkingLot.Park(motorcycle);
			Assert.Equal(35,
				parkingLot.ListVehicles().Count);

		}

		[Fact]
		public void ListVehicles_By_Type_Correct()
		{
			parkingLot.Park(compact);
			parkingLot.Park(full);
			parkingLot.Park(truck);
			parkingLot.Park(motorcycle);
			parkingLot.Park(electric);
			var vehicles = parkingLot.ListVehiclesByType();
			List<Vehicle> expectedOrder = new List<Vehicle>
			{
				compact,
				full,
				electric,
				motorcycle,
				truck	
			};
		}

		[Fact]
		public void ListVehicles_By_Id_Correct()
		{
			parkingLot.Park(electric);
			parkingLot.Park(full);
			parkingLot.Park(compact);
			bool isOrdered = true;
			var sortedVehicles = parkingLot.ListVehiclesById();
			for (int i = 0; i<sortedVehicles.Count-1; i++)
			{
				if (sortedVehicles[i].Id >= sortedVehicles[i+1].Id)
				{
					isOrdered = false;
				}
			}
			Assert.True(isOrdered);
		}		
	}
}
