import random

#respuestas aleatorias (bola8)
def random_ball() -> str:
	respuestas = [
		"si",
		"no",
		"tal vez",
		"nunca",
		"siempre"
	]

	return random.choice(random_ball);

def random_color() -> str:
	colores = [
		"azul",
		"amarillo",
		"blanco",
		"rojo",
		"morado",
		"verde",
		"marron",
		"naranja",
	] 
	return random.choice(colores);


def test() -> None:

	assert str, type(random_ball());
	assert str, type(random_color());
