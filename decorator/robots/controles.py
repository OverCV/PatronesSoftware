from entidades import Robot


class ControlRobot:
    """
    Clase que controla el funcionamiento de un robot,
    permitiendo su uso y mostrando las funciones que tiene.
    """

    def usar_robot(self, robot: Robot):
        robot.funcionar()
        print(robot.descripcion_funciones())


if __name__ == "__main__":
    robot = Robot("1", True, True)
    control = ControlRobot()
    control.usar_robot(robot)
