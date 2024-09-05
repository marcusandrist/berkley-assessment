using System;
using System.Collections.Generic;
using System.Linq;

namespace ParkingLotApp
{
		public abstract class Vehicle
		{
			public int Id { get; private set; }
			public int Wheels { get; protected set; }
			public decimal WheelPrice { get; }
			public decimal Surcharge { get; protected set; }

			public Vehicle(int id)
			{
				Id = id;
				WheelPrice = 5.00m;
			}

			public decimal CalculateCharge()
			{
				return (Wheels * WheelPrice) + Surcharge;
			}
		}

		public class Compact : Vehicle
		{
			public Compact(int id) : base(id)
			{
				Wheels = 4;
				Surcharge = 0.00m;
			}
		}

		public class Full : Vehicle
		{
			public Full(int id) : base(id)
			{
				Wheels = 4;
				Surcharge = 2.00m;
			}
		}

		public class Truck : Vehicle
		{
			public Truck(int id) : base(id)
			{
				Wheels = 4;
				Surcharge = 3.00m;
			}
		}

		public class Motorcycle : Vehicle
		{
			public Motorcycle(int id) : base(id)
			{
				Wheels = 2;
				Surcharge = 0.00m;
			}
		}

		public class Electric : Vehicle
		{
			public Electric(int id) : base(id)
			{
				Wheels = 4;
				Surcharge = 1.00m;
			}
		}
}
