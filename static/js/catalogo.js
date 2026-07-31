

window.onload = function () {

    const btnTodos = document.getElementById("btnTodos");
    const btnArabes = document.getElementById("btnArabes");
    const btnDisenador = document.getElementById("btnDisenador");

    const arabes = document.getElementById("arabes");
    const disenador = document.getElementById("disenador");

    btnTodos.onclick = function () {
        arabes.style.display = "block";
        disenador.style.display = "block";
    };

    btnArabes.onclick = function () {
        arabes.style.display = "block";
        disenador.style.display = "none";
    };

    btnDisenador.onclick = function () {
        arabes.style.display = "none";
        disenador.style.display = "block";
    };

};