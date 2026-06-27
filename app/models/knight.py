class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def apply_equipment(self, knight: dict) -> None:
        # apply armour
        knight["protection"] = 0
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

        # apply weapon
        knight["power"] += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += knight["potion"]["effect"][
                    "protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
