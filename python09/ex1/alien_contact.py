from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

# Inherit from BaseModel to create validated data
# classes.


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

# runs after Pydantic’s built-in validation
    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        # id starts with ac
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        # physical is verified
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        # telepathic has witnesses
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        # strong signal has message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should include received messages")
        return self


def display_contact(contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received!r}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-06-30T22:15:00",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    display_contact(contact)
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_BAD_001",
            timestamp=datetime.now(),
            location="Remote observatory",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.2,
            duration_minutes=20,
            witness_count=1,
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
