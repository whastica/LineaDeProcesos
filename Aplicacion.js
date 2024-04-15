class Aplicacion {
    constructor(tipoUsuario, funcionalidadesBasicas, plataforma, estiloInterfaz, lenguajeProgramacion, pruebas, tiendaApp, marketing) {
        this._tipoUsuario = tipoUsuario;
        this._funcionalidadesBasicas = funcionalidadesBasicas;
        this._plataforma = plataforma;
        this._estiloInterfaz = estiloInterfaz;
        this._lenguajeProgramacion = lenguajeProgramacion;
        this._pruebas = pruebas;
        this._tiendaApp = tiendaApp;
        this._marketing = marketing;
    }


    get tipoUsuario() {
        return this._tipoUsuario;
    }

    set tipoUsuario(value) {
        this._tipoUsuario = value;
    }

    get funcionalidadesBasicas() {
        return this._funcionalidadesBasicas;
    }

    set funcionalidadesBasicas(value) {
        this._funcionalidadesBasicas = value;
    }

    get plataforma() {
        return this._plataforma;
    }

    set plataforma(value) {
        this._plataforma = value;
    }

    get estiloInterfaz() {
        return this._estiloInterfaz;
    }

    set estiloInterfaz(value) {
        this._estiloInterfaz = value;
    }

    get lenguajeProgramacion() {
        return this._lenguajeProgramacion;
    }

    set lenguajeProgramacion(value) {
        this._lenguajeProgramacion = value;
    }

    get pruebas() {
        return this._pruebas;
    }

    set pruebas(value) {
        this._pruebas = value;
    }

    get tiendaApp() {
        return this._tiendaApp;
    }

    set tiendaApp(value) {
        this._tiendaApp = value;
    }

    get marketing() {
        return this._marketing;
    }

    set marketing(value) {
        this._marketing = value;
    }
}