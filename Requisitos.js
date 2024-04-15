class Requisitos {
    constructor(publico, funcionalidadesBasicas, funcionalidadesAvanzadas, plataforma, estiloInterfaz, pruebasBeta, marketing) {
        this.publico = publico;
        this.funcionalidadesBasicas = funcionalidadesBasicas;
        this.funcionalidadesAvanzadas = funcionalidadesAvanzadas;
        this.plataforma = plataforma;
        this.estiloInterfaz = estiloInterfaz;
        this.pruebasBeta = pruebasBeta;
        this.marketing = marketing;
    }

    getPublico() {
        return this.publico;
    }

    setPublico(publico) {
        this.publico = publico;
    }

    getFuncionalidadesBasicas() {
        return this.funcionalidadesBasicas;
    }

    setFuncionalidadesBasicas(funcionalidadesBasicas) {
        this.funcionalidadesBasicas = funcionalidadesBasicas;
    }

    getFuncionalidadesAvanzadas() {
        return this.funcionalidadesAvanzadas;
    }

    setFuncionalidadesAvanzadas(funcionalidadesAvanzadas) {
        this.funcionalidadesAvanzadas = funcionalidadesAvanzadas;
    }

    getPlataforma() {
        return this.plataforma;
    }

    setPlataforma(plataforma) {
        this.plataforma = plataforma;
    }

    getEstiloInterfaz() {
        return this.estiloInterfaz;
    }

    setEstiloInterfaz(estiloInterfaz) {
        this.estiloInterfaz = estiloInterfaz;
    }

    getPruebasBeta() {
        return this.pruebasBeta;
    }

    setPruebasBeta(pruebasBeta) {
        this.pruebasBeta = pruebasBeta;
    }

    getMarketing() {
        return this.marketing;
    }

    setMarketing(marketing) {
        this.marketing = marketing;
    }
}
