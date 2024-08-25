class Utilities:
    def __init__(self, electricity=True, water=True, gas=True, internet=True, cctv=True):
        self.electricity = electricity
        self.water = water
        self.gas = gas
        self.internet = internet
        self.cctv = cctv

    def __str__(self):
        return (f"UTILITIES - Electricity: {'Yes' if self.electricity else 'No'},\n"
                f"Water: {'Yes' if self.water else 'No'},\n"
                f"Gas: {'Yes' if self.gas else 'No'},\n"
                f"Internet: {'Yes' if self.internet else 'No'},\n"
                f"CCTV: {'Yes' if self.cctv else 'No'}")

    def fully_func(self):
        return all([self.electricity, self.water, self.gas, self.internet, self.cctv])


class Room:
    def __init__(self, square_meters, windows, doors):
        self.square_meters = square_meters
        self.windows = windows
        self.doors = doors

    def __str__(self):
        return (f"ROOMS - Area: {self.square_meters} sq.m,\n"
                f"Windows: {self.windows}, Doors: {self.doors}")


class Kitchen(Room):
    def __init__(self, square_meters, windows, doors, drawers_brand, color, table, fridge, bar, oven, sink, microwave,
                 air_ventilation, dish_machine, wash_machine_q_ty, wash_machine_brand, condition, tv):
        super().__init__(square_meters, windows, doors)
        self.drawers_brand = drawers_brand
        self.color = color
        self.table = table
        self.fridge = fridge
        self.bar = bar
        self.oven = oven
        self.sink = sink
        self.microwave = microwave
        self.air_ventilation = air_ventilation
        self.dish_machine = dish_machine
        self.wash_machine_q_ty = wash_machine_q_ty
        self.wash_machine_brand = wash_machine_brand
        self.condition = condition
        self.tv = tv

    def __str__(self):
        return (f"KITCHEN AREA: {self.square_meters} sq.m, kitchen complected with {self.color} color, {self.drawers_brand} drawer set.\n"
                f"Dining area: {self.table}.\n"
                f"Fridge: {self.fridge}, Bar: {self.bar},\n"
                f"Oven: {self.oven}, Sink: {self.sink}, Microwave: {self.microwave},\n"
                f"Air Ventilation: {self.air_ventilation}, Dish Machine: {self.dish_machine},\n"
                f"{self.wash_machine_q_ty} Washing Machine(s): {self.wash_machine_brand}, TV: {self.tv}.\n"
                f"Condition: {self.condition}.\n"
                f"Windows: {self.windows}, Doors: {self.doors}")


class Bathroom(Room):
    def __init__(self, square_meters, windows, doors, bathtub, shower, sink, has_toilet):
        super().__init__(square_meters, windows, doors)
        self.bathtub = bathtub
        self.shower = shower
        self.sink = sink
        self.has_toilet = has_toilet

    def __str__(self):
        return (f"BATHROOM: Area - {self.square_meters} sq.m,\n"
                f"Bathtub: {'Yes' if self.bathtub else 'No'}, Shower: {'Yes' if self.shower else 'No'},\n"
                f"Sink: {self.sink}, Toilet: {'Yes' if self.has_toilet else 'No'},\n"
                f"Windows: {self.windows}, Doors: {self.doors}")


class Bedroom(Room):
    def __init__(self, square_meters, windows, doors, bed_type, has_wardrobe):
        super().__init__(square_meters, windows, doors)
        self.bed_type = bed_type
        self.has_wardrobe = has_wardrobe

    def __str__(self):
        return (f"BEDROOM: Area - {self.square_meters} sq.m, Bed: {self.bed_type},\n"
                f"Wardrobe: {'Yes' if self.has_wardrobe else 'No'},\n"
                f"Windows: {self.windows}, Doors: {self.doors}")


class LivingRoom(Room):
    def __init__(self, square_meters, windows, doors, has_tv, sofa):
        super().__init__(square_meters, windows, doors)
        self.has_tv = has_tv
        self.sofa = sofa

    def __str__(self):
        return (f"LIVING ROOM: Area - {self.square_meters} sq.m, TV: {'Yes' if self.has_tv else 'No'},\n"
                f"Sofa: {self.sofa},\n"
                f"Windows: {self.windows}, Doors: {self.doors}")



class Apartment:
    def __init__(self, id_num, condition, rooms, square_meters, address, utilities):
        self.id_num = id_num
        self.condition = condition
        self.rooms = rooms
        self.square_meters = square_meters
        self.address = address
        self.utilities = utilities

    def __str__(self):
        room_details = '\n'.join([str(room) for room in self.rooms])
        return (f"Apartment ID: {self.id_num}, Address: {self.address},\n"
                f"Condition: {self.condition}, Total Rooms: {len(self.rooms)}.\n"
                f"General Area: {self.square_meters} sq.m\n"
                f"Rooms:\n{room_details}\n"
                f"{self.utilities}")

    def total_area(self):
        return sum(room.square_meters for room in self.rooms)

    def check_utilities(self):
        return self.utilities.fully_func()





utilities = Utilities(electricity=True, gas=True, water=True, internet=True)

kitchen = Kitchen(63, 3, 2, 'Trava', "Light Green", "White Table", "White Fridge", 'No Bar', "Zanussi Oven", "Himble Sink",
                  "Zanussi Microwave", "Factory Air Ventilation", "Zanussi Dish Machine", 1, "Zanussi",
                  "After Renovation", "Yes")
bathroom = Bathroom(26, 2, 2, bathtub=True, shower=True, sink="Marble", has_toilet=True)
living_room = LivingRoom(89, 3, 3, has_tv=True, sofa="L-shaped")
bedroom = Bedroom(56, 2, 2, 'King', has_wardrobe=True)

rooms = [kitchen, bathroom, bedroom, living_room]

apartment = Apartment("B500", "First Rent", rooms, 270, "42 St. George Street", utilities)

print(apartment)
print(f"Total Area: {apartment.total_area()} sq.m")
print(f"Utilities Fully Functioning: {'Yes' if apartment.check_utilities() else 'No'}")
