# Optimización de Onboarding Digital: Análisis de Fricción & A/B Testing

## 1.Contexto del Negocio
Para entender cómo se comporta un flujo digital, simulé un dataset de 10,000 usuarios que atraviesan por las principales etapas del proceso. La idea fue identificar:
* En qué pasos se produce mayor fricción,
* Qué segmentos presentan problemas particulares,
* Y si una variante del flujo normal (Variante) mejora la conversión frente al grupo original (Control).

## 2.Resultados Principales

### 2.1.Impacto de la Variante (Test A/B)
La Variante mostró una mejora clara frente al grupo control.
* **Conversión Control**: 48.6%
* **Conversión Variante:** 54.2%
* **Lift (incremento):** +11.6%
Se aplicó un test de Chi-Cuadrado para validar si la diferencia era producto del azar.
El p-value obtenido fue de `0.00000002`, suficientemente bajo para rechazar la hipótesis nula y concluir que la Variante genera un impacto real en la conversión.

### 2.2.Fricción técnica en Android  
En el evento de "escaneo del DNI" se observa una diferencia significativa por tipo de dispositivo:
* **Tiempo promedio Android:** 17.95s
* **Tiempo promedio iOS:** 11.84s
Se aplicó el T-test para comparar las medias entre ambos grupos, siendo el p-value cercano a 0, lo que confirma que la diferencia no es aleatoria: Android tiene un problema técnico evidenciado.

### 2.3.Evento crítico del funnel
La mayor caída en el funnel ocurre en la transición de "Información Personal" a "Escaneo de DNI", con una caída cercana al 30%:
* **Caída en SO Android:** 31.35%
* **Caída en SO iOS:** 26.43%
Este evento se convierte en un cuello de botella que concentra la mayor pérdida de usuarios antes de la verificación de identidad.

## 3.Stack Tecnológico
* **Python:** Para la simulación de datos y manipulación en general.
* **Pandas:** Para análisis del funnel y cálculos de conversión.
* **Scipy:** Pruebas de hipótesis estadísticas (Chi-Square & T-Test).

## 4.Estructura del Proyecto
* `src/data_gen.py`: Script de generación de datos que simula 10,000 usuarios con patrones de comportamiento y sesgos técnicos.
* `notebooks/`: Análisis exploratorio (EDA), construcción del funnel y validación estadística.

## 5.Recomendación Estratégica
1.  **Roll-out:** Desplegar la Variante dado el incremento consistente y validado de la conversión.
2.  **Ingeniería:** Revisar el módulo de escaneo en Android, ya que el tiempo adicional demuestra un problema técnico que podría afectar la experiencia.
3.  **Marketing:** Pausar temporalmente la inversión de pauta pagada (Ads) dirigida a dispositivos Android hasta corregir el bug para evitar desperdicio de presupuesto (CAC ineficiente).
4. **UX/UI:** Auditar la usabilidad del evento de "Información Personal". Se puede revisar los campos obligatorios, autocompletado y validaciones para reducir fricción antes del escaneo del DNI.