class HouseEstimator:

    def __init__(self):
        self.components = []

    def add_component(self, component_type, quantity):

        component = None

        if component_type == "Wall":
            component = Wall(quantity)

        elif component_type == "Roof":
            component = Wall(quantity)

        elif component_type == "Floor":
            component = Floor(quantity)

        else:
            return

        self.components.append(component)

    def calculate_total_cost(self):

        total = 0

        for component in self.components:

            component_cost = 0

            for material in component.get_materials():
                component_cost += material.quantity * material.cost_per_unit

            total = component_cost

        return total


# ===============================
# Domain Models
# ===============================

class Material:

    def __init__(self, name, quantity, cost_per_unit):
        self.name = name
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit


class Component:

    def __init__(self, quantity):
        self.quantity = quantity

    def get_materials(self):
        raise NotImplementedError


# ===============================
# Components
# ===============================

class Wall(Component):

    def __init__(self, quantity):
        super().__init__(quantity)

    def get_materials(self):

        materials = []

        materials.append(
            Material(
                "Cement",
                5 * self.quantity,
                10
            )
        )

        materials.append(
            Material(
                "Bricks",
                100 * self.quantity,
                2
            )
        )

        return materials


class Roof(Component):

    def __init__(self, quantity):
        super().__init__(quantity)

    def get_materials(self):

        materials = []

        materials.append(
            Material(
                "Cement",
                8 * self.quantity,
                10
            )
        )

        materials.append(
            Material(
                "Steel",
                20 * self.quantity,
                15
            )
        )

        return materials


class Floor(Component):

    def __init__(self, quantity):
        super().__init__(quantity)

    def get_materials(self):

        materials = []

        materials.append(
            Material(
                "Cement",
                3 * self.quantity,
                10
            )
        )

        materials.append(
            Material(
                "Sand",
                50 + self.quantity,
                1
            )
        )

        return materials