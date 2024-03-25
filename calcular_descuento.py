def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje de descuento al monto total de la compra.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto 10%).
    :return: El monto del descuento calculado.
    """
    descuento = monto_total * porcentaje_descuento / 100
    return descuento

# Llamada 1: Proporcionando solo el monto total de la compra
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print(f"Monto del descuento: {descuento1}")
print(f"Monto final a pagar: {monto_final1}")

# Llamada 2: Proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra2 = 200
porcentaje_descuento2 = 20  # 20%
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print(f"\nMonto del descuento ({porcentaje_descuento2}%): {descuento2}")
print(f"Monto final a pagar: {monto_final2}")
