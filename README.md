# 📦 Optimización de Inventario y Punto de Reorden

## 📖 ¿Para qué sirve y por qué utilizarlo?
La gestión científica de inventarios evita los dos grandes enemigos de la rentabilidad: el quiebre de stock (pérdida de ventas) y el sobrestock (dinero inmovilizado).
1. **Prevención de Quiebres:** Calcula matemáticamente el momento exacto para pedir a los proveedores (Punto de Reorden) considerando la volatilidad de la demanda y los tiempos de entrega.
2. **Minimización de Costos Logísticos:** Determina el tamaño de lote ideal (Cantidad Económica de Pedido) que equilibra el costo de emitir una orden y el costo de almacenamiento.
3. **Automatización de Compras:** Transforma la intuición operativa en un modelo estadístico y financiero.

## 🎯 Objetivo del Proyecto
Desarrollar un sistema de recomendación de reabastecimiento que analice el historial de demanda diaria y las condiciones logísticas del catálogo de proveedores para emitir alertas automatizadas de compra.

## 🛠 Metodología y Tecnologías
Se combinaron técnicas de estadística descriptiva con modelos clásicos de Investigación de Operaciones.
* **Modelos Matemáticos:** Cantidad Económica de Pedido (EOQ) y Punto de Reorden (ROP) con cálculo dinámico de Stock de Seguridad.
* **Nivel de Servicio (Z):** Configurado al 95% de confianza (1.65) para garantizar disponibilidad en picos de demanda.
* **Librerías:** Pandas, NumPy.

## 🧠 Resultados y Aplicación de Negocio
El sistema procesó 365 días de demanda simulada para 5 productos clave. Logró generar un dashboard logístico que indica a la operación exactamente *cuándo* y *cuánto* pedir de cada insumo. Para insumos de alta rotación (como vasos de 8oz), el algoritmo determinó un punto de reorden de 1,465 unidades y un volumen de compra optimizado de 14,807 unidades, asegurando la continuidad del servicio minimizando el costo de inventario.