from datetime import datetime
from pydantic import BaseModel, Field, ValidationError

#   python3 -m venv .venv
#   source .venv/bin/activate
#   python -m pip install "pydantic>=2,<3"
#   python ex0/space_station.py

# ge = greater equal, le = lesser equal


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-06-30T12:00:00",
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Not operational"
    print(f"Status: {status}")
    print("=" * 40)

    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
