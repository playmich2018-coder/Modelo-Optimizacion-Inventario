import pandas as pd
import numpy as np
import os

if not os.path.exists('historial_demanda.csv') or not os.path.exists('catalogo_proveedores.csv'):
    print("⚠️ Faltan los datos. Ejecuta primero: py generar_datos_inventario.py")
else:
    # 1. Cargar bases de datos
    df_demanda = pd.read_csv('historial_demanda.csv')
    df_catalogo = pd.read_csv('catalogo_proveedores.csv')

    # 2. Calcular estadísticas de demanda por producto (Promedio diario y Desviación)
    stats_demanda = df_demanda.groupby('Producto')['Demanda_Diaria'].agg(['mean', 'std']).reset_index()
    stats_demanda.columns = ['Producto', 'Demanda_Promedio_Diaria', 'Desviacion_Demanda']

    # 3. Unir con el catálogo de proveedores para cruzar los tiempos logísticos
    df_optimizacion = pd.merge(stats_demanda, df_catalogo, on='Producto')

    # 4. Parámetros financieros
    NIVEL_SERVICIO = 1.65 # Representa un 95% de confianza (evitar quiebres de stock)
    COSTO_MANTENIMIENTO = 0.20 # Asumimos que almacenar cuesta el 20% del valor del producto al año

    resultados = []

    # 5. Calcular EOQ (Cantidad a pedir) y ROP (Cuándo pedir)
    for index, row in df_optimizacion.iterrows():
        producto = row['Producto']
        D_anual = row['Demanda_Promedio_Diaria'] * 365 # Demanda total proyectada
        S = row['Costo_Pedido_Fijo_USD'] # Costo de flete/logística por cada pedido
        H = row['Costo_Unitario_USD'] * COSTO_MANTENIMIENTO # Costo de tener inventario quieto
        L = row['Tiempo_Entrega_Dias'] # Lead Time
        
        # Cantidad Económica de Pedido (EOQ)
        eoq = np.sqrt((2 * D_anual * S) / H)
        
        # Stock de Seguridad y Punto de Reorden (ROP)
        stock_seguridad = NIVEL_SERVICIO * row['Desviacion_Demanda'] * np.sqrt(L)
        rop = (row['Demanda_Promedio_Diaria'] * L) + stock_seguridad
        
        resultados.append({
            'Producto': producto,
            'Demanda_Promedio_Diaria': round(row['Demanda_Promedio_Diaria'], 1),
            'Stock_de_Seguridad': int(stock_seguridad),
            'Punto_de_Reorden_(ROP)': int(rop),
            'Cantidad_a_Pedir_(EOQ)': int(eoq)
        })

    # 6. Mostrar el Dashboard de Reabastecimiento
    df_resultados = pd.DataFrame(resultados)
    
    print("📦 REPORTE AUTOMATIZADO DE REABASTECIMIENTO (EOQ & ROP) 📦")
    print("-" * 75)
    for _, row in df_resultados.iterrows():
        print(f"🔹 {row['Producto']}:")
        print(f"   ⚠️ Alerta de pedido: Emitir orden al bajar a {row['Punto_de_Reorden_(ROP)']} unidades en bodega.")
        print(f"   🛒 Volumen de compra: Pedir exactamente {row['Cantidad_a_Pedir_(EOQ)']} unidades al proveedor.")
        print("-" * 75)

    # 7. Exportar el archivo final
    df_resultados.to_csv('reporte_reabastecimiento.csv', index=False)
    print("\n📁 Archivo gerencial exportado: 'reporte_reabastecimiento.csv'")