from dataclasses import dataclass


@dataclass
class Driver:
    driver_id: str
    name: str
    phone_number: str
    license_number: str

    experience_years: int

    status: str
    driving_style: str