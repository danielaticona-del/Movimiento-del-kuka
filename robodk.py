from robodk import robolink, robomath
import time

RDK = robolink.Robolink()
robot = RDK.Item('KUKA KR 10 R1100-2')

# Activar herramienta
tool = RDK.Item("efector")
robot.setTool(tool)

# Coordenadas seteadas
xyzrpy = [600, 150, 300, 100, 2, 150]

# Convertir lista a pose válida para RoboDK
destino_pose = robomath.xyzrpw_2_pose(xyzrpy)

# Velocidad
robot.setSpeed(75)

print(f"Moviendo a destino: {xyzrpy} ...")
robot.MoveJ(destino_pose)   # Movimiento articulado seguro

llegada = 1
print(f"Robot llegó a la posición. llegada = {llegada}")
print("Robot permanece en esta posición.")
