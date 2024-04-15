class Actividad {
    constructor(nombre, descripcion, roles, objetivo, artefactoEntrada, artefactoSalida) {
        this._nombre = nombre;
        this._descripcion = descripcion;
        this._roles = roles;
        this._objetivo = objetivo;
        this._artefactoEntrada = artefactoEntrada;
        this._artefactoSalida = artefactoSalida;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(value) {
        this._nombre = value;
    }

    get descripcion() {
        return this._descripcion;
    }

    set descripcion(value) {
        this._descripcion = value;
    }

    get roles() {
        return this._roles;
    }

    set roles(value) {
        this._roles = value;
    }

    get objetivo() {
        return this._objetivo;
    }

    set objetivo(value) {
        this._objetivo = value;
    }

    get artefactoEntrada() {
        return this._artefactoEntrada;
    }

    set artefactoEntrada(value) {
        this._artefactoEntrada = value;
    }

    get artefactoSalida() {
        return this._artefactoSalida;
    }

    set artefactoSalida(value) {
        this._artefactoSalida = value;
    }
}

