"""
Sprint 7 - Python para automatización de pruebas
Ejercicios de práctica trabajados durante el sprint.

Autor: Camilo González
Descripción:
    Colección organizada de ejercicios sobre tipos de datos, estructuras,
    control de flujo, funciones y validaciones con assert.

Nota:
    Los ejemplos son ejercicios educativos. Algunos utilizan datos
    simulados de Urban Routes.
"""

# ============================================================
# 1. BOOLEANOS Y OPERADORES DE COMPARACIÓN
# ============================================================

temperature = 20
print("Temperatura dentro del límite:", temperature <= 20)

# Comparaciones: ==, !=, >, <, >=, <=
status_code = 204
print("Código exitoso:", 200 <= status_code <= 299)


# ============================================================
# 2. LISTAS
# ============================================================

vehicles = ["taxi", "moto", "bici", "scooter"]
print("Tercer vehículo:", vehicles[2])

vehicles[2] = "bici eléctrica"
print("Lista actualizada:", vehicles)

vehicles = ["taxi", "moto", "bici", "scooter", "scooter"]
vehicles.append("patín")
vehicles.pop(0)
vehicles.append("camioneta")
print("Cantidad de scooters:", vehicles.count("scooter"))

# Slices
vehicles = ["taxi", "moto", "bici", "scooter", "patín", "camioneta"]
print("Primeros dos:", vehicles[0:2])
print("Desde el cuarto:", vehicles[3:])
print("Elementos en posiciones alternas:", vehicles[::2])

# Ordenamiento e inversión
prices = [180, 200, 150, 220, 170]
print("Precios ascendente:", sorted(prices))
print("Precios descendente:", sorted(prices, reverse=True))
print("Orden inverso (sin ordenar):", list(reversed(prices)))


# ============================================================
# 3. DICCIONARIOS
# ============================================================

trip = {
    "destination": "Airport",
    "options": ["taxi", "scooter"],
    "coupon": "WELCOME"
}
print("Destino:", trip["destination"])
print("Primera opción:", trip["options"][0])
print("Cupón:", trip.get("coupon"))

trip["payment_method"] = "card"
trip["cost"] = 350
trip.pop("coupon", None)
trip["end_point"] = trip.pop("destination")
print("Configuración del viaje:", trip)


# ============================================================
# 4. CONDICIONALES Y OPERADORES LÓGICOS
# ============================================================

driver_status = "available"

if driver_status == "available":
    print("Conductor disponible")
elif driver_status == "busy":
    print("Conductor ocupado")
else:
    print("Estado de conductor desconocido")

distance = 12
price = 15

if distance > 10 and price == 15:
    print(True)
else:
    print(False)

status_code = 500
if status_code == 200:
    print("PASS")
else:
    print("FAIL")


# ============================================================
# 5. BUCLES FOR Y WHILE
# ============================================================

drivers = ["Ana", "Luis", "Sofía"]
driver_count = 0

for driver in drivers:
    print("Conductor asignado:", driver)
    driver_count += 1

print("Total de conductores:", driver_count)

trip_states = [
    "en curso", "pausado", "finalizado",
    "en curso", "pausado", "en curso"
]
in_progress = 0
paused = 0

for state in trip_states:
    if state == "en curso":
        in_progress += 1
    if state == "pausado":
        paused += 1

print("Viajes en curso:", in_progress)
print("Viajes pausados:", paused)

# range()
for number in range(1, 6):
    print("Número:", number)

# while
passengers = 0
capacity = 5

while passengers < capacity:
    passengers += 1
    print("Pasajeros actuales:", passengers)

# continue, break y pass
trip_states = ["en curso", "cancelado", "pausado", "cancelado", "finalizado"]
for state in trip_states:
    if state == "cancelado":
        continue
    print("Procesando viaje:", state)

remaining_distances = [12, 7, 5, 0, 3, 8]
for remaining_distance in remaining_distances:
    print("Distancia restante:", remaining_distance)
    if remaining_distance == 0:
        print("Viaje completado. Deteniendo revisión...")
        break

# pass como marcador de posición
trip_states = ["completo", "", "completo"]
for state in trip_states:
    if state == "":
        pass
    else:
        print("Procesando viaje:", state)


# ============================================================
# 6. OPERADORES DE PERTENENCIA: in / not in
# ============================================================

trip_states = ["completado", "en curso", "cancelado", "error"]
invalid_states = ["pendiente", "error"]

for state in trip_states:
    if state not in invalid_states:
        print("Estado válido:", state)
    else:
        print("Estado no válido encontrado:", state)

payment_methods = ["tarjeta", "efectivo", "paypal"]
if "tarjeta" not in payment_methods:
    print("Advertencia: falta el método de pago 'tarjeta'.")

messages = ["Tu pago fue exitoso", "Viaje confirmado"]
for message in messages:
    if "pago" not in message:
        print("Advertencia: el mensaje no contiene la palabra 'pago'.")

trip_config = {"origen": "Aeropuerto", "destino": "Hotel", "hora": "10:30"}
if "ruta" not in trip_config:
    print("Advertencia: falta la clave 'ruta'.")


# ============================================================
# 7. FUNCIONES INTEGRADAS Y TIPOS DE DATOS
# ============================================================

numbers = [4, 8, 2, 10]
print("Cantidad:", len(numbers))
print("Mínimo:", min(numbers))
print("Máximo:", max(numbers))
print("Suma:", sum(numbers))
print("Tipo:", type(numbers))

passengers_as_text = "4"
print("Tipo de passengers_as_text:", type(passengers_as_text))

# Validación explícita del tipo (sin detener el resto del archivo)
if not isinstance(passengers_as_text, int):
    print("Data type error!")
else:
    print("Data type OK")


# ============================================================
# 8. FUNCIONES, PARÁMETROS Y ARGUMENTOS
# ============================================================

def mostrar_banner():
    """Muestra el mensaje general de inicio."""
    print("Urban Routes — Pruebas iniciadas")


def mostrar_banner_para(suite):
    """Muestra un banner para el módulo recibido."""
    print("Urban Routes — " + suite + " pruebas iniciadas")


def confirmar_viaje(nombre, destino):
    """Muestra la confirmación de un viaje."""
    print(nombre + ", tu viaje hacia " + destino + " está confirmado")


mostrar_banner()
mostrar_banner_para("Viajes")
mostrar_banner_para("Pagos")
confirmar_viaje("Camilo", "Londres")


# ============================================================
# 9. VALORES DE RETORNO: return
# ============================================================

times = {
    "Airport": 40,
    "Downtown": 25,
    "University": 30,
    "Mall": 20
}


def calculate_time(trip_name, delay):
    """Devuelve el tiempo estimado más el retraso."""
    total_time = times[trip_name] + delay
    return total_time


trip_time = calculate_time("Airport", 15)
print("Stored value:", trip_time)

fares = {
    "Airport": 350,
    "Downtown": 200,
    "University": 180,
    "Mall": 220
}


def calculate_discounted_fare(trip_name, discount):
    """Devuelve la tarifa después de aplicar el descuento."""
    final_price = fares[trip_name] - discount
    return final_price


print("Tarifa con descuento:", calculate_discounted_fare("University", 30))


def calculate_fare(base, surcharge):
    """Devuelve la tarifa base más el recargo."""
    total = base + surcharge
    return total


fare = calculate_fare(200, 50)
fare_with_tip = fare + 20
print("Tarifa final con propina:", fare_with_tip)


# ============================================================
# 10. ASSERT: VALIDACIÓN DE RESULTADOS
# ============================================================

def calcular_costo(distancia, tarifa):
    """Calcula el costo de un viaje."""
    return distancia * tarifa


costo_viaje = calcular_costo(10, 20)
assert costo_viaje > 0, "El costo del viaje debe ser mayor que 0"
assert costo_viaje == 200, "El costo calculado no coincide con el esperado"
print("Costo validado:", costo_viaje)

taxi_capacity = 4
scooter_capacity = 1

assert taxi_capacity > 0, "La capacidad del taxi debe ser mayor que 0"
assert scooter_capacity != taxi_capacity, (
    "La capacidad del scooter no debe ser igual a la del taxi"
)

# Validación del código HTTP de ejemplo
status_code = 200
assert status_code == 200, "El código de respuesta no es 200"
print("Validaciones assert completadas.")


# ============================================================
# 11. EJERCICIOS DE REPASO DEL SPRINT
# ============================================================

# Obtener un elemento de una lista mediante su índice
completed_trips = ["TR-102", "TR-205", "TR-330"]
print("Segundo viaje completado:", completed_trips[1])

# Obtener un valor de un diccionario mediante su clave
eta_by_zone = {
    "Downtown": 8,
    "Airport": 15,
    "University": 12
}
print("ETA Airport:", eta_by_zone["Airport"])

# Contar tiempos de respuesta mayores a 500
response_times = [120, 640, 510, 200, 999]
slow_count = 0

for response_time in response_times:
    if response_time > 500:
        slow_count += 1

print("Respuestas mayores a 500 ms:", slow_count)


def is_success(status_code):
    """Devuelve True para códigos HTTP entre 200 y 299."""
    if status_code >= 200 and status_code <= 299:
        return True
    else:
        return False


status_code = 204
print("¿Respuesta exitosa?:", is_success(status_code))

print("\nFin de los ejercicios del Sprint 7.")
