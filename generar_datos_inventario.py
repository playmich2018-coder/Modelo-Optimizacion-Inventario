import pandas as pd
import numpy as np

# 1. Configuración base
np.random.seed(42)
dias_historial = 365
productos = ['Cafe_Grano_1kg', 'Vasos_Descartables_8oz', 'Leche_Almendra_1L', 'Azucar_Blanca_500g', 'Jarabe_Vainilla']

# 2. Generar histórico de demanda diaria
fechas = pd.date_range(start="2025-09-01", periods=dias_historial, freq='D')
datos = []

for fecha in fechas:
    for producto in productos:
        # Simulamos demanda con diferentes volúmenes operativos
        if producto == 'Cafe_Grano_1kg':
            demanda = np.random.poisson(lam=15)
        elif producto == 'Vasos_Descartables_8oz':
            demanda = np.random.poisson(lam=200)
        elif producto == 'Leche_Almendra_1L':
            demanda = np.random.poisson(lam=30)
        elif producto == 'Azucar_Blanca_500g':
            demanda = np.random.poisson(lam=5)
        else:
            demanda = np.random.poisson(lam=3)
        
        datos.append([fecha, producto, demanda])

df_demanda = pd.DataFrame(datos, columns=['Fecha', 'Producto', 'Demanda_Diaria'])
df_demanda.to_csv('historial_demanda.csv', index=False)

# 3. Crear catálogo de proveedores (Tiempos de entrega y Costos)
catalogo = pd.DataFrame({
    'Producto': productos,
    'Costo_Unitario_USD': [12.5, 0.05, 2.5, 0.8, 4.0],
    'Tiempo_Entrega_Dias': [3, 7, 2, 5, 10], # Lead Time (Lo que tarda el proveedor en llegar)
    'Costo_Pedido_Fijo_USD': [20, 15, 25, 10, 15] # Costo logístico por emitir una orden
})
catalogo.to_csv('catalogo_proveedores.csv', index=False)

print("✅ Éxito: Se generó 'historial_demanda.csv' (365 días de operación).")
print("✅ Éxito: Se generó 'catalogo_proveedores.csv' (Condiciones logísticas).")