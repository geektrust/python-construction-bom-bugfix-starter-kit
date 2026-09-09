class Main:

    estimator = None

    @staticmethod
    def main(args):
        Main.estimator = HouseEstimator()

        for arg in args:
            Main.handle(arg)

    @staticmethod
    def handle(input_data):
        tokens = input_data.strip().split(" ")

        command = tokens[0]

        if command == "ADD_COMPONENT":
            component = tokens[1]
            quantity = int(tokens[2])

            Main.estimator.add_component(component, quantity)

        elif command == "TOTAL_COST":
            print(
                "Total Construction Cost: "
                + str(Main.estimator.calculate_total_cost())
            )

        else:
            print("INVALID_COMMAND")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise RuntimeError("No command line arguments passed")

    Main.main(sys.argv[1:])