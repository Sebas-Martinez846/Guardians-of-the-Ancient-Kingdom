
import pytest
from personajes import  Guerrero, Mago, Arquero
from combate import Combate


# 1. Creación correcta de personajes válidos
def test_creacion_personajes():
    g = Guerrero("Thor", 100, 30, 20)
    m = Mago("Merlín", 80, 40, 10)
    a = Arquero("Robin", 90, 35, 15)
    assert g.nombre == "Thor"
    assert m.vida == 80
    assert a.defensa == 15


# 2. Rechazo de valores incorrectos (excepciones)
def test_valores_invalidos():
    with pytest.raises(ValueError):
        Guerrero("Invalido", 120, 20, 10)  # Vida > 100
    with pytest.raises(ValueError):
        Guerrero("Invalido", -5, 20, 10)   # Vida < 0
    with pytest.raises(ValueError):
        Mago("   ", 80, 20, 10)            # Nombre vacío
    with pytest.raises(ValueError):
        Guerrero("Invalido", 80, 0, 10)    # Ataque <= 0
    with pytest.raises(ValueError):
        Guerrero("Invalido", 80, 20, -1)   # Defensa < 0


# 3. Cálculo de daño específico por cada clase
def test_calculo_danio_habilidades():
    # Guerrero: 30 * 1.20 = 36 - 10 = 26
    g = Guerrero("Ares", 100, 30, 10)
    objetivo_g = Guerrero("Blanco1", 100, 10, 10)
    assert g.atacar(objetivo_g) == 26

    # Mago: ignora defensa = 40
    m = Mago("Strange", 100, 40, 10)
    objetivo_m = Guerrero("Blanco2", 100, 10, 20)
    assert m.atacar(objetivo_m) == 40

    # Arquero: (35 - 15) * 2 = 40
    a = Arquero("Legolas", 100, 35, 10)
    objetivo_a = Guerrero("Blanco3", 100, 10, 15)
    assert a.atacar(objetivo_a) == 40


# 4. Que la vida nunca quede negativa
def test_vida_no_negativa():
    herido = Guerrero("Debil", 10, 10, 0)
    danio_efectivo = herido.recibir_danio(50)
    assert danio_efectivo == 10
    assert herido.vida == 0
    assert not herido.esta_vivo()


# 5. Imposibilidad de atacar estando derrotado
def test_derrotado_no_puede_atacar():
    muerto = Guerrero("Caido", 0, 20, 10)
    vivo = Guerrero("Vivo", 100, 20, 10)
    with pytest.raises(ValueError):
        muerto.atacar(vivo)


# 6. Combate determina correctamente el resultado
def test_resultado_combate():
    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)
    combate = Combate(arthas, gandalf)
    combate.iniciar()
    assert combate.ganador == gandalf
    assert gandalf.vida == 2