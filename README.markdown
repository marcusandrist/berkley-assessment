# Parking Lot Program

Marcus Andrist 09/05/2024
Coding interview solution for WR Berkley
> (requires dotnet 8 + python3)

## Details

The codebase uses a makefile format:
- "**make**" will run python unittests and dotnet XUnit tests using only built-ins
- "**make coverage**" will **INSTALL** coverage (Python PIP package)

### Vehicle Types

- **Compact**
- **Full**
- **Truck**
- **Motorcycle**
- **Electric**

### Features

The program supports the following actions:

- **Get total money collected**
- **Get total money collected by vehicle type**
- **List all vehicles**
- **List vehicles ordered by type**
- **List vehicles ordered by ID**
- **Park a vehicle**
- **Un-park a vehicle**

### Pricing Structure

- **Wheel Rate:** $5.00 per wheel
- **Surcharges:**
  - Electric: $1.00
  - Full: $2.00
  - Truck: $3.00
