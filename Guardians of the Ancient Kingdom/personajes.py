"""
personajes.py
"""
from abc import ABC, abstractmethod
import math


class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        # Al asignar mediante self.nombre, self.vida, etc., se ejecutan los setters obligatoriamente
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self._nombre = valor.strip()

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        if not isinstance(valor, int) or valor < 0 or valor > 100:
            raise ValueError("La vida debe ser un número entero entre 0 y 100.")
        self._vida = valor

    @property
    def ataque(self) -> int:
        return self._ataque

    @ataque.setter
    def ataque(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ataque debe ser un número entero positivo.")
        self._ataque = valor

    @property
    def defensa(self) -> int:
        return self._defensa

    @defensa.setter
    def defensa(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La defensa debe ser un número entero no negativo.")
        self._defensa = valor

    def esta_vivo(self) -> bool:
        return self._vida > 0

    def recibir_danio(self, cantidad: int) -> int:
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("El daño debe ser un número entero no negativo.")
        danio_efectivo = min(self._vida, cantidad)
        self._vida -= danio_efectivo
        return danio_efectivo

    def __str__(self) -> str:
        return (f"[{self.__class__.__name__}] {self._nombre} | "
                f"Vida: {self._vida}/100 | Ataque: {self._ataque} | Defensa: {self._defensa}")

    def mostrar_estado(self) -> str:
        return str(self)

    def validar_ataque(self, objetivo: "Personaje"):
        """Validación que asegura que un derrotado no ataque."""
        if not self.esta_vivo():
            raise ValueError(f"{self._nombre} está derrotado y no puede atacar.")
        if not isinstance(objetivo, Personaje):
            raise TypeError("El objetivo debe ser una instancia de Personaje.")
        if objetivo is self:
            raise ValueError("Un personaje no puede atacarse a sí mismo.")
        if not objetivo.esta_vivo():
            raise ValueError(f"{objetivo.nombre} ya está derrotado.")

    @abstractmethod
    def atacar(self, objetivo: "Personaje") -> int:
        pass


class Guerrero(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self.validar_ataque(objetivo)
        ataque_potenciado = math.floor(self.ataque * 1.20)
        danio = max(0, ataque_potenciado - objetivo.defensa)
        return objetivo.recibir_danio(danio)


class Mago(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self.validar_ataque(objetivo)
        danio = self.ataque
        return objetivo.recibir_danio(danio)


class Arquero(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self.validar_ataque(objetivo)
        if self.ataque > objetivo.defensa:
            danio_base = self.ataque - objetivo.defensa
            danio = danio_base * 2
        else:
            danio = 0
        return objetivo.recibir_danio(danio)







