from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By
import unittest


class MenuPage(BasePage):
    # Icono Perfil
    icon_perfil = By.XPATH, "//button[@class='mat-focus-indicator mat-menu-trigger mat-flat-button mat-button-base mat-accent']"
    btn_cerrar_sesion = By.XPATH, "//button[@class='mat-focus-indicator ng-tns-c110-16 mat-raised-button mat-button-base mat-accent']"

    # Agencia >>
    btn_agencia = By.XPATH, "//button/span[contains(text(),'Ingresar')]"
    # btn_proyectos =By.XPATH,"//div[@class='mat-list-item-content']/div[text()=' Proyectos ']"
    btn_proyectos = By.ID, "PROJECTS"
    btn_RIA = By.ID, "RIA"
    btn_lotes = By.ID, "LOTES"
    btn_gestor_de_descargas = By.ID, "DOWNLOAD_MANAGER"
    btn_mis_datos = By.ID, "MY_INFO"
    btn_mi_cv = By.ID, "MY_CV"
    btn_mis_proyectos = By.ID, "MY_PROJECTS"
    btn_reportes = By.ID, "REPORTS"
    btn_notificaciones = By.ID, "NOTIFICATIONS"

    # Agencia >> Administrador >>
    btn_administrador = By.ID, "ADMIN"
    btn_usuarios = By.ID, "USERS"
    btn_roles = By.ID, "ROLES"
    btn_fondos = By.ID, "FUNDS"
    btn_instrumentos = By.ID, "INSTRUMENTS"
    btn_chequeos = By.ID, "CHECKS"
    btn_llamados = By.ID, "LLAMADOS"
    btn_formularios = By.ID, "FORMS"
    btn_formularios_de_evaluacion = By.ID, "FORMS"

    # Agencia >> Administrador>>ABMS
    btn_ABMS = By.ID, "ABMS"
    btn_areas_de_actuacion = By.ID, "ACTION_AREAS"
    btn_areas_alta_prioridad = By.ID, "HIGH_PRIORITY_AREAS"
    btn_areas_tematicas = By.ID, "THEMATIC_AREAS"
    btn_becas = By.ID, "SCHOLARSHIPS"
    btn_codigos = By.ID, "CODES"
    btn_carteras = By.ID, "PORTFOLIOS"
    btn_duracion = By.ID, "DURATION"
    btn_ejes = By.ID, "AXES"
    btn_lineas_de_accion = By.ID, "GUIDELINES"
    btn_funciones = By.ID, "FUNCTIONS"
    btn_nodos_region = By.ID, "REGION_NODE"
    btn_rubros_de_presupuesto = By.ID, "BUDGET_ITEMS"
    btn_nucleo_socio_productivos_estrategicos = By.ID, "STRATEGIC_SECTOR"
    btn_temas_de_interes = By.ID, "INTEREST_TOPICS"
    btn_terminos_y_condiciones = By.ID, "TERMS_AND_CONDITIONS"

    # Agencia >> evaluacion >>
    btn_evaluacion = By.ID, "EVALUATION"
    btn_banco_de_evaluacion = By.XPATH, "BANK_OF_EVALUATORS"
    btn_comisiones = By.XPATH, "COMMISSIONS"
    btn_grupos_expertos = By.XPATH, "EXPERT_GROUP"
    btn_buscar_cvar = By.XPATH, "SEARCH_CVAR"
    btn_asignacion_de_proyectos = By.XPATH, "COMMISSION_ASSIGNATION"
    btn_mis_evaluaciones = By.XPATH, "MY_ASSIGNATIONS"
    # Agencia >> evaluacion >>mis equipos
    btn_mis_equipos_coordinador = By.ID, "MY_TEAMS_COORDINATOR"
    btn_mis_equipos_cocoordinador = By.XPATH, "MY_TEAMS_COCOORDINATOR"

    # Icono Perfil
    def click_icon_perfil(self):
        self.click(self.icon_perfil)

    def click_btn_cerrar_sesion(self):
        self.click(self.btn_cerrar_sesion)

    # Agencia >>
    def click_btn_proyectos(self):
        self.click(self.btn_proyectos)

    def click_btn_RIA(self):
        self.click(self.btn_RIA)

    def click_btn_lotes(self):
        self.click(self.btn_lotes)

    def click_btn_gestor_de_descargas(self):
        self.click(self.btn_gestor_de_descargas)

    def click_btn_mis_datos(self):
        self.click(self.btn_mis_datos)

    def click_btn_mi_cv(self):
        self.click(self.btn_mi_cv)

    def click_btn_mis_proyectos(self):
        self.click(self.btn_mis_proyectos)

    def click_btn_reportes(self):
        self.click(self.btn_reportes)

    def click_btn_notificaciones(self):
        self.click(self.btn_notificaciones)

    # Agencia >> Administrador >>
    def click_btn_administrador(self):
        self.click(self.btn_administrador)

    def click_btn_usuarios(self):
        self.click(self.btn_usuarios)

    def click_btn_roles(self):
        self.click(self.btn_roles)

    def click_btn_fondos(self):
        self.click(self.btn_fondos)

    def click_btn_instrumentos(self):
        self.click(self.btn_instrumentos)

    def click_btn_chequeos(self):
        self.click(self.btn_chequeos)

    def click_btn_llamados(self):
        self.click(self.btn_llamados)

    def click_btn_formularios(self):
        self.click(self.btn_formularios)

    def click_btn_formularios_de_evaluacion(self):
        self.click(self.btn_formularios_de_evaluacion)

    # Agencia >> Administrador>>ABMS
    def click_btn_ABMS(self):
        self.click(self.btn_ABMS)

    def click_btn_areas_de_actuacion(self):
        self.click(self.btn_areas_de_actuacion)

    def click_btn_areas_alta_prioridad(self):
        self.click(self.btn_areas_alta_prioridad)

    def click_btn_areas_tematicas(self):
        self.click(self.btn_areas_tematicas)

    def click_btn_becas(self):
        self.click(self.btn_becas)

    def click_btn_codigos(self):
        self.click(self.btn_codigos)

    def click_btn_carteras(self):
        self.click(self.btn_carteras)

    def click_btn_duracion(self):
        self.click(self.btn_duracion)

    def click_btn_ejes(self):
        self.click(self.btn_ejes)

    def click_btn_lineas_de_accion(self):
        self.click(self.btn_lineas_de_accion)

    def click_btn_funciones(self):
        self.click(self.btn_funciones)

    def click_btn_nodos_region(self):
        self.click(self.btn_nodos_region)

    def click_btn_rubros_de_presupuesto(self):
        self.click(self.btn_rubros_de_presupuesto)

    def click_btn_nucleo_socio_productivos_estrategicos(self):
        self.click(self.btn_nucleo_socio_productivos_estrategicos)

    def click_btn_temas_de_interes(self):
        self.click(self.btn_temas_de_interes)

    def click_btn_terminos_y_condiciones(self):
        self.click(self.btn_terminos_y_condiciones)

    # Agencia >> evaluacion >>
    def click_btn_evaluacion(self):
        self.click(self.btn_evaluacion)

    def click_btn_banco_de_evaluacion(self):
        self.click(self.btn_banco_de_evaluacion)

    def click_btn_comisiones(self):
        self.click(self.btn_comisiones)

    def click_btn_grupos_expertos(self):
        self.click(self.btn_grupos_expertos)

    def click_btn_buscar_cvar(self):
        self.click(self.btn_buscar_cvar)

    def click_btn_asignacion_de_proyectos(self):
        self.click(self.btn_asignacion_de_proyectos)

    def click_btn_mis_evaluaciones(self):
        self.click(self.btn_mis_evaluaciones)

    # Agencia >> evaluacion >>mis equipos
    def click_btn_mis_equipos_coordinador(self):
        self.click(self.btn_mis_equipos_coordinador)

    def click_btn_mis_equipos_cocoordinador(self):
        self.click(self.btn_mis_equipos_cocoordinador)
