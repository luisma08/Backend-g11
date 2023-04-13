function sumar(x, y) {
    return x + y;
}

function restar(x, y){
    return x - y;
}
// CALLBACKS
function operacion(funcion, parametro1, parametro2) {
    const resultado = funcion(parametro1, parametro2);
    console.log(resultado);
}

operacion(sumar, 1, 5);

operacion(restar, 10, 5);

operacion(
    (x, y) => {
        x * y;
    },
    5,
    6
);