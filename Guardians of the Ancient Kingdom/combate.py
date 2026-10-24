from personajes import Personaje

class Combate:
    def __init__(self, personaje1: Personaje, personaje2: Personaje):
        if not isinstance(personaje1, Personaje) or not isinstance(personaje2, Personaje):
            raise TypeError("Ambos contendientes deben ser instancias válidas de Personaje.")
        if personaje1 is personaje2:
            raise ValueError("Un personaje no puede combatir contra sí mismo.")
        if not personaje1.esta_vivo() or not personaje2.esta_vivo():
            raise ValueError("Ambos personajes deben estar vivos para iniciar un combate.")

        # Agregación: almacena referencias a los personajes ya creados
        self.p1 = personaje1
        self.p2 = personaje2
        self.atacante = personaje1
        self.defensor = personaje2
        self.ganador: Personaje | None = None
        self.empate: bool = False
        self.motivo_empate: str = ""

    def cambiar_turno(self):
        """Alterna el rol de atacante y defensor entre los dos participantes."""
        self.atacante, self.defensor = self.defensor, self.atacante

    def verificar_ganador(self) -> Personaje | None:
        """Determina si alguno de los personajes ha sido derrotado."""
        if not self.p1.esta_vivo() and self.p2.esta_vivo():
            self.ganador = self.p2
            return self.p2
        if not self.p2.esta_vivo() and self.p1.esta_vivo():
            self.ganador = self.p1
            return self.p1
        return None

    def mostrar_resultado(self):
        """Presenta el resultado final del combate en consola."""
        print("\n================ RESULTADO DEL COMBATE ================")
        if self.ganador:
            print(f"¡Ganador: {self.ganador.nombre}!")
            print(f"Estado final del ganador: {self.ganador}")
        elif self.empate:
            print(f"Combate finalizado en EMPATE: {self.motivo_empate}")
        print("=======================================================\n")

    def iniciar(self):
        """Ejecuta el ciclo de combate por turnos aplicando las reglas del sistema."""
        print("\n========== INICIO DEL COMBATE ==========")
        print(f"Contendiente 1: {self.p1}")
        print(f"Contendiente 2: {self.p2}")
        print("========================================\n")

        turno = 1
        ronda = 1
        max_rondas = 50

        while ronda <= max_rondas:
            # Bandera para medir el daño de la ronda completa (p1 y p2)
            dano_ronda = 0

            # --- Ataque del primer contendiente de la ronda ---
            dano1 = self.atacante.atacar(self.defensor)
            dano_ronda += dano1
            print(f"Turno {turno} | Atacante: {self.atacante.nombre} | Daño causado: {dano1}")
            print(f"         Estado: {self.defensor.nombre} queda con {self.defensor.vida} de vida.")

            if self.verificar_ganador():
                break

            turno += 1
            self.cambiar_turno()

            # --- Ataque del segundo contendiente de la ronda ---
            dano2 = self.atacante.atacar(self.defensor)
            dano_ronda += dano2
            print(f"Turno {turno} | Atacante: {self.atacante.nombre} | Daño causado: {dano2}")
            print(f"         Estado: {self.defensor.nombre} queda con {self.defensor.vida} de vida.")

            if self.verificar_ganador():
                break

            # Regla: Si ambos completan una ronda sin causarse daño -> Empate técnico
            if dano_ronda == 0:
                self.empate = True
                self.motivo_empate = "Empate técnico (ningún contendiente logró causar daño en la ronda)."
                break

            turno += 1
            self.cambiar_turno()
            ronda += 1

        # Regla: Si se completan 50 rondas sin vencedor -> Empate por límite
        if ronda > max_rondas and not self.ganador:
            self.empate = True
            self.motivo_empate = "Límite de 50 rondas alcanzado sin un vencedor."

        self.mostrar_resultado()