# ============================================================
#   SIVA MedBot - Sistema Inteligente de Valoracion y
#   Analisis Medico
#   Materia: Knowledge Representation
#   Version 3.0 - Con indicador de intensidad
# ============================================================

INTENSIDAD_FACTOR = {
    "leve":     0.5,
    "moderado": 1.0,
    "intenso":  1.5
}

# ============================================================
#   BASE DE CONOCIMIENTO (15 enfermedades, 45+ sintomas)
# ============================================================

knowledge_base = {

    "resfriado": {
        "nombre": "Resfriado Comun",
        "tipo": "Respiratoria",
        "descripcion": "Infeccion viral leve del tracto respiratorio superior causada principalmente por rhinovirus.",
        "sintomas_clave": ["congestion_nasal", "estornudos"],
        "sintomas": {
            "congestion_nasal":     0.95,
            "estornudos":           0.90,
            "dolor_garganta":       0.80,
            "tos":                  0.70,
            "ronquera":             0.60,
            "lagrimeo":             0.55,
            "dolor_cabeza":         0.45,
            "fatiga":               0.40,
            "perdida_apetito":      0.35,
            "fiebre":               0.20,
            "dolor_muscular":       0.15,
            "nauseas":              0.10,
            "escalofrios":          0.15,
            "mucosidad":            0.85,
            "perdida_olfato":       0.40,
        },
        "tratamiento": ["Reposo", "Hidratacion", "Vitamina C", "Descongestionantes"],
        "cuando_ver_medico": "Si los sintomas duran mas de 10 dias o empeoran despues del dia 7."
    },

    "gripe": {
        "nombre": "Gripe / Influenza",
        "tipo": "Respiratoria",
        "descripcion": "Infeccion viral aguda del tracto respiratorio causada por el virus Influenza, mas grave que el resfriado.",
        "sintomas_clave": ["fiebre", "dolor_muscular", "escalofrios"],
        "sintomas": {
            "fiebre":               0.90,
            "tos":                  0.85,
            "dolor_muscular":       0.90,
            "fatiga":               0.85,
            "dolor_cabeza":         0.70,
            "escalofrios":          0.80,
            "congestion_nasal":     0.60,
            "perdida_apetito":      0.55,
            "dolor_garganta":       0.50,
            "nauseas":              0.30,
            "perdida_olfato":       0.20,
            "sarpullido":           0.05,
            "sudoracion_excesiva":  0.60,
            "debilidad_general":    0.80,
            "ronquera":             0.40,
        },
        "tratamiento": ["Reposo", "Hidratacion", "Antivirales", "Acetaminofen"],
        "cuando_ver_medico": "Si la fiebre supera 39.5 grados o dura mas de 5 dias."
    },

    "covid": {
        "nombre": "COVID-19",
        "tipo": "Respiratoria",
        "descripcion": "Enfermedad infecciosa causada por el coronavirus SARS-CoV-2.",
        "sintomas_clave": ["perdida_olfato", "tos", "fiebre"],
        "sintomas": {
            "fiebre":               0.85,
            "tos":                  0.90,
            "perdida_olfato":       0.95,
            "fatiga":               0.80,
            "dolor_cabeza":         0.70,
            "dolor_muscular":       0.60,
            "dificultad_respirar":  0.70,
            "dolor_garganta":       0.50,
            "nauseas":              0.40,
            "escalofrios":          0.50,
            "congestion_nasal":     0.40,
            "sarpullido":           0.10,
            "confusion_mental":     0.30,
            "dolor_pecho":          0.40,
            "debilidad_general":    0.70,
        },
        "tratamiento": ["Aislamiento", "Reposo", "Hidratacion", "Monitoreo de oxigeno"],
        "cuando_ver_medico": "Si tienes dificultad para respirar o saturacion de oxigeno menor a 94%."
    },

    "dengue": {
        "nombre": "Dengue",
        "tipo": "Viral",
        "descripcion": "Enfermedad viral transmitida por mosquitos Aedes aegypti.",
        "sintomas_clave": ["fiebre", "dolor_detras_ojos", "sarpullido"],
        "sintomas": {
            "fiebre":               0.95,
            "dolor_muscular":       0.90,
            "sarpullido":           0.85,
            "dolor_cabeza":         0.85,
            "dolor_detras_ojos":    0.90,
            "fatiga":               0.80,
            "nauseas":              0.70,
            "vomito":               0.60,
            "perdida_apetito":      0.65,
            "escalofrios":          0.50,
            "dolor_abdominal":      0.50,
            "moretones_faciles":    0.55,
            "dolor_garganta":       0.10,
            "tos":                  0.10,
            "congestion_nasal":     0.10,
        },
        "tratamiento": ["Hidratacion", "Reposo", "Acetaminofen", "Evitar aspirina"],
        "cuando_ver_medico": "Si presentas sangrado, vomito persistente o dolor abdominal intenso."
    },

    "amigdalitis": {
        "nombre": "Amigdalitis",
        "tipo": "Respiratoria",
        "descripcion": "Inflamacion de las amigdalas palatinas causada por bacterias o virus.",
        "sintomas_clave": ["dolor_garganta", "dificultad_tragar", "fiebre"],
        "sintomas": {
            "dolor_garganta":       0.99,
            "fiebre":               0.85,
            "dificultad_tragar":    0.90,
            "dolor_cabeza":         0.60,
            "fatiga":               0.65,
            "escalofrios":          0.55,
            "perdida_apetito":      0.60,
            "congestion_nasal":     0.30,
            "tos":                  0.35,
            "nauseas":              0.25,
            "dolor_muscular":       0.20,
            "ganglios_inflamados":  0.80,
            "ronquera":             0.50,
            "mal_aliento":          0.70,
            "sarpullido":           0.05,
        },
        "tratamiento": ["Antibioticos", "Reposo", "Liquidos frios", "Analgesicos"],
        "cuando_ver_medico": "Si tienes dificultad severa para respirar o tragar saliva."
    },

    "gastroenteritis": {
        "nombre": "Gastroenteritis",
        "tipo": "Digestiva",
        "descripcion": "Inflamacion del estomago e intestinos causada por virus, bacterias o parasitos.",
        "sintomas_clave": ["diarrea", "vomito", "nauseas"],
        "sintomas": {
            "nauseas":              0.95,
            "vomito":               0.90,
            "diarrea":              0.95,
            "dolor_abdominal":      0.90,
            "dolor_estomago":       0.90,
            "fiebre":               0.65,
            "fatiga":               0.70,
            "perdida_apetito":      0.80,
            "dolor_cabeza":         0.40,
            "escalofrios":          0.35,
            "dolor_muscular":       0.25,
            "distension_abdominal": 0.60,
            "sarpullido":           0.05,
            "tos":                  0.05,
            "acidez":               0.30,
        },
        "tratamiento": ["Hidratacion oral", "Reposo", "Dieta blanda", "Probioticos"],
        "cuando_ver_medico": "Si hay signos de deshidratacion severa o sangre en heces."
    },

    "migrana": {
        "nombre": "Migrana",
        "tipo": "Neurologica",
        "descripcion": "Trastorno neurologico caracterizado por dolor de cabeza intenso y pulsatil.",
        "sintomas_clave": ["dolor_cabeza", "sensibilidad_luz", "sensibilidad_sonido"],
        "sintomas": {
            "dolor_cabeza":         0.99,
            "nauseas":              0.80,
            "sensibilidad_luz":     0.90,
            "sensibilidad_sonido":  0.85,
            "vomito":               0.60,
            "fatiga":               0.65,
            "vision_borrosa":       0.55,
            "mareos":               0.60,
            "perdida_apetito":      0.50,
            "confusion_mental":     0.35,
            "fiebre":               0.03,
            "sarpullido":           0.01,
            "tos":                  0.01,
            "diarrea":              0.05,
            "dolor_muscular":       0.10,
        },
        "tratamiento": ["Analgesicos", "Reposo en oscuridad", "Evitar pantallas", "Triptanes"],
        "cuando_ver_medico": "Si el dolor es el peor de tu vida o viene con rigidez en el cuello."
    },

    "conjuntivitis": {
        "nombre": "Conjuntivitis",
        "tipo": "Ocular",
        "descripcion": "Inflamacion de la conjuntiva del ojo causada por virus, bacterias o alergias.",
        "sintomas_clave": ["ojos_rojos", "secrecion_ocular", "lagrimeo"],
        "sintomas": {
            "ojos_rojos":           0.99,
            "picazon_ojos":         0.95,
            "secrecion_ocular":     0.90,
            "lagrimeo":             0.85,
            "ojos_hinchados":       0.75,
            "sensibilidad_luz":     0.60,
            "vision_borrosa":       0.50,
            "dolor_cabeza":         0.30,
            "fiebre":               0.20,
            "fatiga":               0.15,
            "tos":                  0.05,
            "nauseas":              0.05,
            "sarpullido":           0.05,
            "congestion_nasal":     0.30,
            "dolor_garganta":       0.10,
        },
        "tratamiento": ["Colirios antibioticos", "Compresas frias", "Higiene ocular"],
        "cuando_ver_medico": "Si hay dolor intenso en el ojo o cambios severos en la vision."
    },

    "hipertension": {
        "nombre": "Hipertension Arterial",
        "tipo": "Cardiovascular",
        "descripcion": "Presion arterial cronicamente elevada que puede causar complicaciones graves.",
        "sintomas_clave": ["dolor_cabeza", "mareos", "vision_borrosa"],
        "sintomas": {
            "dolor_cabeza":         0.75,
            "mareos":               0.80,
            "vision_borrosa":       0.70,
            "fatiga":               0.65,
            "zumbido_oidos":        0.60,
            "dificultad_respirar":  0.55,
            "dolor_pecho":          0.50,
            "nauseas":              0.40,
            "palpitaciones":        0.60,
            "sangrado_nasal":       0.45,
            "confusion_mental":     0.35,
            "fiebre":               0.05,
            "tos":                  0.10,
            "sarpullido":           0.05,
            "escalofrios":          0.10,
        },
        "tratamiento": ["Medicacion antihipertensiva", "Dieta baja en sal", "Ejercicio moderado"],
        "cuando_ver_medico": "Si tienes dolor de pecho con mareos o presion mayor a 180/120."
    },

    "anemia": {
        "nombre": "Anemia",
        "tipo": "Hematologica",
        "descripcion": "Deficiencia de globulos rojos que reduce el oxigeno en la sangre.",
        "sintomas_clave": ["fatiga", "palidez", "mareos"],
        "sintomas": {
            "fatiga":               0.95,
            "palidez":              0.90,
            "mareos":               0.85,
            "dificultad_respirar":  0.75,
            "dolor_cabeza":         0.65,
            "vision_borrosa":       0.50,
            "perdida_apetito":      0.55,
            "palpitaciones":        0.65,
            "debilidad_general":    0.90,
            "manos_frias":          0.70,
            "fiebre":               0.10,
            "nauseas":              0.30,
            "escalofrios":          0.20,
            "tos":                  0.05,
            "sarpullido":           0.05,
        },
        "tratamiento": ["Suplementos de hierro", "Dieta rica en hierro", "Vitamina B12"],
        "cuando_ver_medico": "Si tienes fatiga extrema que no mejora con descanso o palpitaciones frecuentes."
    },

    "varicela": {
        "nombre": "Varicela",
        "tipo": "Dermatologica",
        "descripcion": "Infeccion viral altamente contagiosa causada por el virus varicela-zoster.",
        "sintomas_clave": ["sarpullido", "picazon", "fiebre"],
        "sintomas": {
            "sarpullido":           0.99,
            "picazon":              0.95,
            "fiebre":               0.85,
            "fatiga":               0.75,
            "perdida_apetito":      0.70,
            "dolor_cabeza":         0.60,
            "dolor_muscular":       0.50,
            "escalofrios":          0.55,
            "nauseas":              0.30,
            "dolor_garganta":       0.25,
            "tos":                  0.20,
            "vomito":               0.20,
            "ganglios_inflamados":  0.50,
            "ojos_rojos":           0.20,
            "congestion_nasal":     0.20,
        },
        "tratamiento": ["Antihistaminicos", "Aciclovir", "Calamina topica", "Reposo"],
        "cuando_ver_medico": "Si hay sarpullido en los ojos o dificultad para respirar."
    },

    "hepatitis": {
        "nombre": "Hepatitis",
        "tipo": "Hepatica",
        "descripcion": "Inflamacion del higado causada por virus, alcohol o medicamentos.",
        "sintomas_clave": ["piel_amarilla", "orina_oscura", "dolor_abdominal"],
        "sintomas": {
            "piel_amarilla":        0.95,
            "orina_oscura":         0.90,
            "fatiga":               0.90,
            "dolor_abdominal":      0.80,
            "nauseas":              0.80,
            "perdida_apetito":      0.85,
            "vomito":               0.65,
            "fiebre":               0.60,
            "dolor_muscular":       0.50,
            "dolor_cabeza":         0.40,
            "picazon":              0.60,
            "distension_abdominal": 0.55,
            "debilidad_general":    0.80,
            "escalofrios":          0.35,
            "sarpullido":           0.20,
        },
        "tratamiento": ["Reposo", "Hidratacion", "Evitar alcohol", "Medicacion antiviral"],
        "cuando_ver_medico": "Si hay coloracion amarilla de piel u ojos, acude de inmediato."
    },

    "apendicitis": {
        "nombre": "Apendicitis",
        "tipo": "Digestiva",
        "descripcion": "Inflamacion del apendice que puede volverse una emergencia medica.",
        "sintomas_clave": ["dolor_lado_derecho", "fiebre", "nauseas"],
        "sintomas": {
            "dolor_lado_derecho":   0.99,
            "fiebre":               0.85,
            "nauseas":              0.90,
            "vomito":               0.75,
            "dolor_abdominal":      0.95,
            "perdida_apetito":      0.90,
            "dolor_estomago":       0.85,
            "distension_abdominal": 0.70,
            "escalofrios":          0.60,
            "fatiga":               0.65,
            "estreñimiento":        0.40,
            "diarrea":              0.30,
            "debilidad_general":    0.60,
            "dolor_muscular":       0.20,
            "sudoracion_excesiva":  0.50,
        },
        "tratamiento": ["Cirugia de emergencia", "Antibioticos", "Hospitalizacion"],
        "cuando_ver_medico": "URGENTE: Acude de inmediato si tienes dolor intenso en lado derecho del abdomen."
    },

    "asma": {
        "nombre": "Asma",
        "tipo": "Respiratoria",
        "descripcion": "Enfermedad cronica que inflama y estrecha las vias respiratorias.",
        "sintomas_clave": ["silbido_al_respirar", "dificultad_respirar", "tos"],
        "sintomas": {
            "silbido_al_respirar":  0.95,
            "dificultad_respirar":  0.95,
            "tos":                  0.85,
            "dolor_pecho":          0.70,
            "fatiga":               0.65,
            "tos_nocturna":         0.80,
            "congestion_nasal":     0.45,
            "fiebre":               0.10,
            "sarpullido":           0.05,
            "nauseas":              0.10,
            "dolor_muscular":       0.15,
            "perdida_apetito":      0.25,
            "debilidad_general":    0.40,
            "escalofrios":          0.10,
            "ansiedad":             0.50,
        },
        "tratamiento": ["Broncodilatadores", "Corticosteroides inhalados", "Evitar desencadenantes"],
        "cuando_ver_medico": "Si el inhalador no alivia los sintomas en 20 minutos."
    },

    "bronquitis": {
        "nombre": "Bronquitis",
        "tipo": "Respiratoria",
        "descripcion": "Inflamacion de los tubos bronquiales que transportan aire a los pulmones.",
        "sintomas_clave": ["tos_persistente", "mucosidad", "dolor_pecho"],
        "sintomas": {
            "tos_persistente":      0.99,
            "mucosidad":            0.90,
            "dolor_pecho":          0.75,
            "fatiga":               0.70,
            "dificultad_respirar":  0.65,
            "silbido_al_respirar":  0.60,
            "fiebre":               0.40,
            "dolor_garganta":       0.45,
            "congestion_nasal":     0.40,
            "ronquera":             0.55,
            "dolor_muscular":       0.30,
            "dolor_cabeza":         0.35,
            "escalofrios":          0.30,
            "nauseas":              0.20,
            "perdida_apetito":      0.35,
        },
        "tratamiento": ["Reposo", "Hidratacion", "Broncodilatadores", "Humidificador"],
        "cuando_ver_medico": "Si la tos dura mas de 3 semanas o hay sangre al toser."
    },
}


# ============================================================
#   MOTOR DE INFERENCIA CON INTENSIDAD
# ============================================================

def analizar_sintomas(sintomas_usuario):
    # sintomas_usuario = { "fiebre": "intenso", "tos": "moderado", ... }

    resultados = []
    sintomas_set = set(sintomas_usuario.keys())

    for enfermedad_id, datos in knowledge_base.items():
        puntaje = 0.0
        sintomas_coincidentes = []
        sintomas_enfermedad = datos["sintomas"]
        sintomas_clave = datos.get("sintomas_clave", [])

        for sintoma, intensidad in sintomas_usuario.items():
            if sintoma in sintomas_enfermedad:
                factor = INTENSIDAD_FACTOR.get(intensidad, 1.0)
                puntaje += sintomas_enfermedad[sintoma] * factor
                sintomas_coincidentes.append({
                    "sintoma":    sintoma,
                    "intensidad": intensidad
                })

        if puntaje > 0:
            # Penalizacion por sintomas clave ausentes
            claves_ausentes = [c for c in sintomas_clave if c not in sintomas_set]
            penalizacion = len(claves_ausentes) * 0.3
            puntaje = max(0, puntaje - penalizacion)

            resultados.append({
                "id":                enfermedad_id,
                "nombre":            datos["nombre"],
                "tipo":              datos["tipo"],
                "descripcion":       datos.get("descripcion", ""),
                "puntaje":           round(puntaje, 2),
                "coincidentes":      sintomas_coincidentes,
                "tratamiento":       datos["tratamiento"],
                "cuando_ver_medico": datos.get("cuando_ver_medico", ""),
                "confianza":         calcular_confianza(puntaje)
            })

    resultados.sort(key=lambda x: x["puntaje"], reverse=True)
    return resultados[:5]


def calcular_confianza(puntaje):
    if puntaje >= 3.0:
        return "Alta"
    elif puntaje >= 1.5:
        return "Media"
    else:
        return "Baja"


# ============================================================
#   REGLAS HEURISTICAS
# ============================================================

def aplicar_heuristicas(sintomas_usuario, resultados):
    sintomas_set = set(sintomas_usuario.keys())

    for r in resultados:

        # Resfriado: sin fiebre o fiebre leve
        if r["id"] == "resfriado":
            if "fiebre" not in sintomas_set:
                r["puntaje"] += 0.5
            elif sintomas_usuario.get("fiebre") == "intenso":
                r["puntaje"] -= 0.8

        # Gripe: fiebre intensa diferencia de resfriado
        if r["id"] == "gripe":
            if sintomas_usuario.get("fiebre") == "intenso":
                r["puntaje"] += 0.7
            if sintomas_usuario.get("dolor_muscular") == "intenso":
                r["puntaje"] += 0.5

        # COVID: perdida de olfato es casi exclusiva
        if r["id"] == "covid" and "perdida_olfato" in sintomas_set:
            r["puntaje"] += 0.8

        # Dengue: dolor detras de ojos + fiebre
        if r["id"] == "dengue":
            if "dolor_detras_ojos" in sintomas_set and "fiebre" in sintomas_set:
                r["puntaje"] += 0.8
            if "fiebre" not in sintomas_set:
                r["puntaje"] -= 1.0

        # Migrana: penalizar si hay fiebre, bonus si sensibilidad luz+sonido
        if r["id"] == "migrana":
            if "fiebre" in sintomas_set:
                r["puntaje"] -= 0.8
            if "sensibilidad_luz" in sintomas_set and "sensibilidad_sonido" in sintomas_set:
                r["puntaje"] += 0.6
            if sintomas_usuario.get("dolor_cabeza") == "intenso":
                r["puntaje"] += 0.5

        # Conjuntivitis: ojos rojos es casi exclusivo
        if r["id"] == "conjuntivitis" and "ojos_rojos" in sintomas_set:
            r["puntaje"] += 0.7

        # Hepatitis: piel amarilla es casi exclusiva
        if r["id"] == "hepatitis" and "piel_amarilla" in sintomas_set:
            r["puntaje"] += 1.0

        # Apendicitis: dolor lado derecho intenso
        if r["id"] == "apendicitis":
            if "dolor_lado_derecho" in sintomas_set:
                r["puntaje"] += 1.0
            if sintomas_usuario.get("dolor_lado_derecho") == "intenso":
                r["puntaje"] += 0.5

        # Asma: silbido al respirar sin fiebre
        if r["id"] == "asma":
            if "silbido_al_respirar" in sintomas_set:
                r["puntaje"] += 0.7
            if "fiebre" not in sintomas_set:
                r["puntaje"] += 0.3

        # Bronquitis: tos persistente + mucosidad
        if r["id"] == "bronquitis":
            if "tos_persistente" in sintomas_set:
                r["puntaje"] += 0.8
            if "mucosidad" in sintomas_set:
                r["puntaje"] += 0.5

        # Varicela: sarpullido + picazon intensos
        if r["id"] == "varicela":
            if "sarpullido" in sintomas_set and "picazon" in sintomas_set:
                r["puntaje"] += 0.6

        r["puntaje"] = round(max(0, r["puntaje"]), 2)
        r["confianza"] = calcular_confianza(r["puntaje"])

    # Sintomas exclusivos: penalizar otras enfermedades
    sintomas_exclusivos = {
        "piel_amarilla":       "hepatitis",
        "dolor_lado_derecho":  "apendicitis",
        "perdida_olfato":      "covid",
        "dolor_detras_ojos":   "dengue",
        "silbido_al_respirar": "asma",
        "tos_persistente":     "bronquitis",
        "ojos_rojos":          "conjuntivitis",
    }

    enfermedades_prioritarias = set()
    for sintoma, enfermedad in sintomas_exclusivos.items():
        if sintoma in sintomas_set:
            enfermedades_prioritarias.add(enfermedad)

    if enfermedades_prioritarias:
        for r in resultados:
            if r["id"] not in enfermedades_prioritarias:
                r["puntaje"] = round(r["puntaje"] * 0.7, 2)
                r["confianza"] = calcular_confianza(r["puntaje"])

    resultados.sort(key=lambda x: x["puntaje"], reverse=True)
    return resultados


# ============================================================
#   FUNCION AUXILIAR
# ============================================================

def obtener_todos_sintomas():
    todos = set()
    for datos in knowledge_base.values():
        todos.update(datos["sintomas"].keys())
    return sorted(list(todos))