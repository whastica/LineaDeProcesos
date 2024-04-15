class usuario {
    constructor(nombre, correo, nombreApp) {
        this._nombre = nombre;
        this._correo = correo;
        this._nombreApp = nombreApp;
    }


    get nombre() {
        return this._nombre;
    }

    set nombre(value) {
        this._nombre = value;
    }

    get correo() {
        return this._correo;
    }

    set correo(value) {
        this._correo = value;
    }

    get nombreApp() {
        return this._nombreApp;
    }

    set nombreApp(value) {
        this._nombreApp = value;
    }
}
