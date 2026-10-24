from personajes import Guerrero, Mago, Arquero
from combate import Combate


def ejecutar_pruebas():
    print("=================================================================")
    print("   GUARDIANS OF THE ANCIENT KINGDOM - CASOS DE PRUEBA DEL SISTEMA")
    print("=================================================================\n")

    # -------------------------------------------------------------------------
    # Caso 1: Creación correcta de los tres tipos de personajes
    # -------------------------------------------------------------------------
    print(">>> Caso 1: Creación correcta de los tres tipos de personajes")
    g = Guerrero("Thor", 100, 30, 15)
    m = Mago("Merlín", 90, 35, 10)
    a = Arquero("Legolas", 85, 40, 12)


    print(f"  [OK] Creado: {g}")
    print(f"  [OK] Creado: {m}")
    print(f"  [OK] Creado: {a}")

    # -------------------------------------------------------------------------
    # Caso 2: Rechazo de personajes con vida superior a 100 o negativa
    # -------------------------------------------------------------------------
    print("\n>>> Caso 2: Rechazo de personajes con vida superior a 100 o negativa")
    try:
        Guerrero("Invalido1", 120, 20, 10)
        print("  [FALLO] No se rechazó vida superior a 100.")
    except ValueError as e:
        print(f"  [OK] Rechazado vida > 100: {e}")

    try:
        Guerrero("Invalido2", -10, 20, 10)
        print("  [FALLO] No se rechazó vida negativa.")
    except ValueError as e:
        print(f"  [OK] Rechazado vida < 0: {e}")

    # -------------------------------------------------------------------------
    # Caso 3: Rechazo de nombres vacíos
    # -------------------------------------------------------------------------
    print("\n>>> Caso 3: Rechazo de nombres vacíos")
    try:
        Mago("   ", 80, 25, 10)
        print("  [FALLO] No se rechazó nombre en blanco.")
    except ValueError as e:
        print(f"  [OK] Rechazado nombre vacío: {e}")

    # -------------------------------------------------------------------------
    # Caso 4: Rechazo de ataques y defensas inválidos
    # -------------------------------------------------------------------------
    print("\n>>> Caso 4: Rechazo de ataques y defensas inválidos")
    try:
        Guerrero("SinAtaque", 80, 0, 10)
        print("  [FALLO] No se rechazó ataque <= 0.")
    except ValueError as e:
        print(f"  [OK] Rechazado ataque <= 0: {e}")

    try:
        Guerrero("DefensaNegativa", 80, 20, -5)
        print("  [FALLO] No se rechazó defensa negativa.")
    except ValueError as e:
        print(f"  [OK] Rechazada defensa < 0: {e}")

    # -------------------------------------------------------------------------
    # Caso 5: Aplicación correcta de la habilidad del Guerrero (Golpe poderoso)
    # Ataque: 30 -> +20% = 36. Defensa enemigo: 10. Daño esperado = 26.
    # -------------------------------------------------------------------------
    print("\n>>> Caso 5: Habilidad del Guerrero (Golpe poderoso: +20% ataque)")
    guerrero_prueba = Guerrero("Ares", 100, 30, 10)
    objetivo_g = Guerrero("SacoBoxeo1", 100, 10, 10)
    dano_g = guerrero_prueba.atacar(objetivo_g)
    print(f"  Daño infligido: {dano_g} (Esperado: 26)")
    print(f"  Vida restante del objetivo: {objetivo_g.vida}/100 (Esperado: 74)")

    # -------------------------------------------------------------------------
    # Caso 6: Aplicación correcta del ataque del Mago (Hechizo penetrante)
    # Ataque: 40. Defensa enemigo: 20 (se ignora). Daño esperado = 40.
    # -------------------------------------------------------------------------
    print("\n>>> Caso 6: Habilidad del Mago (Hechizo penetrante: ignora defensa)")
    mago_prueba = Mago("Dr. Strange", 100, 40, 10)
    objetivo_m = Guerrero("SacoBoxeo2", 100, 10, 20)
    dano_m = mago_prueba.atacar(objetivo_m)
    print(f"  Daño infligido: {dano_m} (Esperado: 40)")
    print(f"  Vida restante del objetivo: {objetivo_m.vida}/100 (Esperado: 60)")

    # -------------------------------------------------------------------------
    # Caso 7: Aplicación correcta del disparo crítico del Arquero
    # Ataque: 35. Defensa enemigo: 15. Daño base = 20. Crítico duplicado = 40.
    # -------------------------------------------------------------------------
    print("\n>>> Caso 7: Habilidad del Arquero (Disparo crítico: duplica daño base)")
    arquero_prueba = Arquero("Robin Hood", 100, 35, 10)
    objetivo_a = Guerrero("SacoBoxeo3", 100, 10, 15)
    dano_a = arquero_prueba.atacar(objetivo_a)
    print(f"  Daño infligido: {dano_a} (Esperado: 40)")
    print(f"  Vida restante del objetivo: {objetivo_a.vida}/100 (Esperado: 60)")

    # -------------------------------------------------------------------------
    # Caso 8: Imposibilidad de tener vida negativa
    # -------------------------------------------------------------------------
    print("\n>>> Caso 8: Imposibilidad de tener vida negativa")
    objetivo_vulnerable = Guerrero("Debil", 15, 10, 0)
    dano_recibido = objetivo_vulnerable.recibir_danio(50)
    print(f"  Tenía 15 de vida y recibió 50 de daño.")
    print(f"  Daño efectivo: {dano_recibido} | Vida final: {objetivo_vulnerable.vida} (Esperado: 0)")

    # -------------------------------------------------------------------------
    # Caso 9: Imposibilidad de atacar estando derrotado
    # -------------------------------------------------------------------------
    print("\n>>> Caso 9: Imposibilidad de atacar estando derrotado")
    guerrero_vivo = Guerrero("Vivo", 100, 20, 10)
    try:
        objetivo_vulnerable.atacar(guerrero_vivo)
        print("  [FALLO] Un personaje derrotado pudo atacar.")
    except ValueError as e:
        print(f"  [OK] Rechazado ataque de personaje derrotado: {e}")

    # -------------------------------------------------------------------------
    # Caso 10 y 11: Combate completo e Identificación correcta del ganador
    # Simulación exacta del ejemplo de la guía: Arthas (Guerrero) vs Gandalf (Mago)
    # -------------------------------------------------------------------------
    print("\n>>> Casos 10 y 11: Ejecución de un combate completo y ganador")
    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)
    combate_oficial = Combate(arthas, gandalf)
    combate_oficial.iniciar()

    # -------------------------------------------------------------------------
    # Caso 12: Finalización de un combate sin daño mediante empate técnico
    # Dos guerreros cuyo ataque potenciado no supera la defensa rival
    # -------------------------------------------------------------------------
    print(">>> Caso 12: Finalización de combate sin daño (Empate técnico)")
    tanque1 = Guerrero("Muralla 1", 50, 10, 50)
    tanque2 = Guerrero("Muralla 2", 50, 10, 50)
    combate_empate = Combate(tanque1, tanque2)
    combate_empate.iniciar()


if __name__ == "__main__":
    ejecutar_pruebas()