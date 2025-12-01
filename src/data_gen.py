import pandas as pd
import numpy as np
import uuid
import random

# Configuración de la Semilla para reproducibilidad (Importante para que siempre salga lo mismo)
np.random.seed(42)

def generate_data(n_users=10000):
    print(f"Generando datos para {n_users} usuarios simulados...")
    
    # 1. Variables Base
    data = {
        'user_id': [str(uuid.uuid4()) for _ in range(n_users)],
        'channel': np.random.choice(['Facebook', 'Google Ads', 'Organic', 'Referral'], n_users, p=[0.4, 0.3, 0.2, 0.1]),
        'device_os': np.random.choice(['Android', 'iOS'], n_users, p=[0.7, 0.3]), # Perú es mayormente Android
        'ab_group': np.random.choice(['Control', 'Variant'], n_users, p=[0.5, 0.5]) # 50/50 Split
    }
    
    df = pd.DataFrame(data)
    
    # 2. Simulación de Fricción (Aquí está la "magia" del negocio)
    # Definimos probabilidades de PASAR al siguiente paso.
    # NOTA: Estas reglas crean los patrones que luego analizarás.
    
    steps = []
    dni_times = []
    total_times = []
    is_converted_list = []
    
    for _, row in df.iterrows():
        step = 'Landing'
        dni_time = np.nan
        total_time = np.random.normal(30, 10) # Tiempo base de lectura landing
        
        # Logica de conversión por pasos (Funnel)
        
        # Paso 1: Landing -> Info Personal
        if np.random.random() < 0.85: 
            step = 'Personal_Info'
            total_time += np.random.normal(45, 15)
            
            # Paso 2: Info Personal -> DNI Scan (Aquí metemos el efecto del A/B Test)
            # Hipótesis: La Variante (Group B) facilita este paso.
            prob_pass_dni = 0.70 if row['ab_group'] == 'Control' else 0.78
            
            # Penalización técnica: Android es un poco más lento/falla más en cámaras viejas
            if row['device_os'] == 'Android':
                prob_pass_dni -= 0.05 
            
            if np.random.random() < prob_pass_dni:
                step = 'DNI_Scan'
                
                # Simulación de tiempo de escaneo
                # Android tarda más (fricción técnica)
                base_scan_time = 12 if row['device_os'] == 'iOS' else 18
                dni_scan_duration = max(2, np.random.normal(base_scan_time, 5))
                dni_time = dni_scan_duration
                total_time += dni_scan_duration
                
                # Paso 3: DNI Scan -> Contrato
                if np.random.random() < 0.90:
                    step = 'Contract'
                    total_time += np.random.normal(20, 5)
                    
                    # Paso 4: Contrato -> Success (Conversión Final)
                    if np.random.random() < 0.95:
                        step = 'Success'
                        total_time += 5 # click final
        
        steps.append(step)
        dni_times.append(np.round(dni_time, 2))
        total_times.append(np.round(total_time, 2))
        is_converted_list.append(1 if step == 'Success' else 0)

    # Asignar nuevas columnas al DF
    df['step_reached'] = steps
    df['dni_scan_duration'] = dni_times
    df['onboarding_duration'] = total_times
    df['is_converted'] = is_converted_list
    
    return df

if __name__ == "__main__":
    df_final = generate_data(10000)
    
    # Guardar en raw (Simulando la extracción de la BD)
    output_path = "data/raw/onboarding_ab_test_data.csv"
    
    # Asegúrate de crear la carpeta data/raw antes de correr esto, o dará error
    try:
        df_final.to_csv(output_path, index=False)
        print(f"✅ Éxito! Datos guardados en {output_path}")
        print(f"Total filas: {len(df_final)}")
        print(f"Tasa de conversión global simulada: {df_final['is_converted'].mean():.2%}")
    except OSError:
        print("❌ Error: No se encuentra la carpeta '../data/raw/'. Créala primero.")