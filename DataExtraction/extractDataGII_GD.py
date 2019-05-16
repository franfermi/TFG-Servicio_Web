#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import sys
import pandas as pd
import psycopg2

RESOURCE = './resources'
OUTPUT = './outputs/GUIAS_DOCENTES'

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

def insertarGD(guiaDocente, asignatura):

    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

    asignatura = asignatura.upper()
    url = guiaDocente

    sql_insert_query = """INSERT INTO "GuiasDocentes" VALUES(%s, %s)"""
    insert_tuple = (asignatura, url)
    result = cursor.execute(sql_insert_query, insert_tuple)

    connect_db.commit()
    print("Fila insertada correctamente")

def extractDataTeable_GuiaDocente(asignatura):

    asignatura = asignatura.upper()

    if asignatura == 'ALEM':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/1semestre/alemgii/!', asignatura)

    if asignatura == 'CA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/1semestre/clculogradoinformatica1718/!', asignatura)

    if asignatura == 'FS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/1semestre/etsiit_gii_fs_1718_funddelsoftwarev1/!', asignatura)

    if asignatura == 'FP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/1semestre/ficha_ginf_fp_2961115/!', asignatura)

    if asignatura == 'FFT':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/1semestre/guia_docente_fft_gii_17_18/!', asignatura)

    if asignatura == 'ES':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/2semestre/estadistica1/!', asignatura)

    if asignatura == 'IES':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/2semestre/ingenieria-empresa-y-sociedad/!', asignatura)

    if asignatura == 'LMD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/2semestre/logica-y-metodos-discretos/!', asignatura) 

    if asignatura == 'MP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/2semestre/metodologia-de-la-programacion/!', asignatura)

    if asignatura == 'TOC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/primero/2semestre/tecnologia-y-organizacion-de-los-computadores/!', asignatura)  

    if asignatura == 'PDOO':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/1semestre/etsiit_gii_pdoo_1718_progdisoo/!', asignatura)

    if asignatura == 'SCD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/1semestre/etsiit_gii_scd_1718_sistconcydistrib/!', asignatura)

    if asignatura == 'SO':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/1semestre/etsiit_gii_so_1718_sistemasoperativos/!', asignatura)

    if asignatura == 'ED':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/1semestre/ficha_ginf_ed_2961122/!', asignatura)

    if asignatura == 'EC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/1semestre/gii_estructura_computadores_20172018_firmada/!', asignatura)

    if asignatura == 'FIS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/2semestre/etsiit_gii_fis_1718_fundamentosis/!', asignatura)

    if asignatura == 'ALG':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/2semestre/ficha_ginf_alg_2961126/!', asignatura)

    if asignatura == 'FBD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/2semestre/ficha_ginf_fbd_2961128/!', asignatura)

    if asignatura == 'IA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/2semestre/ficha_ginf_ia_2961129/!', asignatura)

    if asignatura == 'AC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/segundo/2semestre/gii_arquitectura_computadores_20172018_firmada/!', asignatura)

    if asignatura == 'IG':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/comunes/etsiit_gii_ig_1718_informaticagrafica/!', asignatura)

    if asignatura == 'DDSI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/comunes/ficha_ginf_ddsi_2961132/!', asignatura)

    if asignatura == 'MC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/comunes/ficha_ginf_mc_2961131/!', asignatura)

    if asignatura == 'FR':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/comunes/gii_fr_20172018/!', asignatura)

    if asignatura == 'ISE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/comunes/gii_ingenieria_servidores_20172018_firmada/!', asignatura)

    if asignatura == 'AA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/computacionysistemasinteligentes/ficha_ginf_aa_296113c/!', asignatura)

    if asignatura == 'IC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/computacionysistemasinteligentes/ficha_ginf_ic_296113a/!', asignatura)

    if asignatura == 'MAC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/computacionysistemasinteligentes/ficha_ginf_mac_296113d/!', asignatura)

    if asignatura == 'MH':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/computacionysistemasinteligentes/ficha_ginf_mhe_296113e/!', asignatura)

    if asignatura == 'TSI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/computacionysistemasinteligentes/ficha_ginf_tsi_296113b/!', asignatura)

    if asignatura == 'DIU':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadelsoftware/etsiit_gii_diu_1718_disenodeinterfacesdeusuario/!', asignatura)

    if asignatura == 'DS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadelsoftware/etsiit_gii_ds1718_desarrollosoftware/!', asignatura)

    if asignatura == 'DSD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadelsoftware/etsiit_gii_dsd_1718_desarrollosistemasdistribuidos/!', asignatura)

    if asignatura == 'SG':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadelsoftware/etsiit_gii_sg_1718_sistemasgraficos/!', asignatura)

    if asignatura == 'SIBW':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadelsoftware/etsiit_gii_sibw_1718_sistemasweb/!', asignatura)

    if asignatura == 'ACAP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadecomputadores/gii_arquitecturas_comp_altas_pres_20172018firmada/!', asignatura)

    if asignatura == 'AS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadecomputadores/gii_arquitectura_sistemas_20172018_firmada/!', asignatura)

    if asignatura == 'DHD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadecomputadores/gii_desarrollo_hardware_digital_20172018_firmada/!', asignatura)

    if asignatura == 'SMP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadecomputadores/gii_sistemas_microprocesadores_20172018_firmada/!', asignatura)

    if asignatura == 'DSE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/ingenieriadecomputadores/guiadocente_2017_2018_diseaodesistemaselectronicosgii/!', asignatura)

    if asignatura == 'SIE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/sistemasdeinformacion/etsiit_gii_sie_1718_sistinfoempres/!', asignatura)

    if asignatura == 'SMD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/sistemasdeinformacion/etsiit_gii_smd_1718_sistemasmultidimensionales/!', asignatura)

    if asignatura == 'ABD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/sistemasdeinformacion/ficha_ginf_abd_296113t/!', asignatura)

    if asignatura == 'ISI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/sistemasdeinformacion/ficha_ginf_isinf_296113s/!', asignatura)

    if asignatura == 'PW':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/sistemasdeinformacion/ficha_ginf_pweb_296113q/!', asignatura)

    if asignatura == 'CUIA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/tecnologiasdelainformacion/ficha_ginf_cuia_296113w/!', asignatura)

    if asignatura == 'SMM':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/tecnologiasdelainformacion/ficha_ginf_sm_296113v/!', asignatura)

    if asignatura == 'TW':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/tecnologiasdelainformacion/ficha_ginf_tw_296113x/!', asignatura)

    if asignatura == 'SWAP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/tecnologiasdelainformacion/gii_servidores_web_altas_pres_20172018firmada/!', asignatura)

    if asignatura == 'TDRC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/tercero/tecnologiasdelainformacion/gii_tdrc_20172018/!', asignatura)

    if asignatura == 'NPI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/etsiit_gii_npi_1718_nuevosparadigmasdeinteraccion/!', asignatura)

    if asignatura == 'PL':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/etsiit_gii_pl_1718_procesadoresdelenguajes/!', asignatura)

    if asignatura == 'VC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/ficha_ginf_vc_296114b/!', asignatura)

    if asignatura == 'DGP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/etsiit_gii_dgp_1718_dirgestproy/!', asignatura)

    if asignatura == 'MDA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/etsiit_gii_mda_1718_metodologiasdesarrolloagiles/!', asignatura)

    if asignatura == 'DBA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/ficha_ginf_dbag_296114f/!', asignatura)

    if asignatura == 'CPD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/gii_centro_procesamiento_datos_20172018_firmada/!', asignatura)

    if asignatura == 'SE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/sistemas-empotrados/!', asignatura)

    if asignatura == 'TR':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/tecnologias-de-red/!', asignatura)

    if asignatura == 'BDD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/etsiit_gii_bdd_1718_basesdedatosdistr/!', asignatura)

    if asignatura == 'IN':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/ficha_ginf_in_296114k/!', asignatura)

    if asignatura == 'RI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/ficha_ginf_rinf_296114j/!', asignatura)

    if asignatura == 'DAI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/etsiit_gii_dai_1718_desapint/!', asignatura)

    if asignatura == 'IV':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/gii_infraestructura_virtual_20172018_firmada/!', asignatura)

    if asignatura == 'SPSI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/spsi/!', asignatura)

    if asignatura == 'PTC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/complementos/ficha_ginf_ptc_29611ad/!', asignatura)

    if asignatura == 'SS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/complementos/ficha_ginf_ss_29611ae/!', asignatura)

    if asignatura == 'TIC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/computacionysistemasinteligentes/complementos/ficha_ginf_tic_29611aa/!', asignatura)

    if asignatura == 'LP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/complementos/logica-y-programacion/!', asignatura)

    if asignatura == 'PGV':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/complementos/programacion-grafica-de-videojuegos/!', asignatura)

    if asignatura == 'SSO':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadelsoftware/complementos/seguridad-de-sistemas-operativos/!', asignatura)

    if asignatura == 'TE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/complementos/gii_tecnologias_emergentes_20172018_firmada/!', asignatura)

    if asignatura == 'II':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/ingenieriadecomputadores/complementos/informatica-industrial/!', asignatura)

    if asignatura == 'SIG':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/complementos/etsiit_gii_sig_1718_sistemasdeinformaciongeograficos/!', asignatura)

    if asignatura == 'GRD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/complementos/ficha_ginf_grd_29611dc/!', asignatura)

    if asignatura == 'RSC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/sistemasdeinformacion/complementos/ficha_ginf_rsc_29611de/!', asignatura)

    if asignatura == 'CRIM':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/complementos/ficha_ginf_crim_29611fc/!', asignatura)

    if asignatura == 'TID':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/tecnologiasdelainformacion/complementos/ficha_ginf_tid_29611fa/!', asignatura)

    if asignatura == 'CEGE':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/fci/creacion-de-empresas-y-gestion-emprendedora/!', asignatura)

    if asignatura == 'DI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/fci/derechoeinformatica/!', asignatura)

    if asignatura == 'EISI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/fci/etica-informatica-y-sociedad-de-la-informacion/!', asignatura)

    if asignatura == 'TFG':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/pfg/proyectofindegrado/!', asignatura)

    if asignatura == 'PRACTICAS DE EMPRESA':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/pe/practicasdeempresa/!', asignatura)

    if asignatura == 'CC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/computacionysistemasinteligentes/cc/!', asignatura)

    if asignatura == 'PLD':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/computacionysistemasinteligentes/ficha_ginf_plud_29611ab/!', asignatura)

    if asignatura == 'ROI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/computacionysistemasinteligentes/gii_ri_1718/!', asignatura)

    if asignatura == 'AO':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/ingenieriadelsoftware/etsiit_gii_ao_1718_animacionporordenador/!', asignatura)

    if asignatura == 'PPR':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/ingenieriadelsoftware/etsiit_gii_scd_1718_sistconcydistrib/!', asignatura)

    if asignatura == 'NTP':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/ingenieriadelsoftware/ficha_ginf_ntp_29611bd/!', asignatura)

    if asignatura == 'CII':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/ingenieriadecomputadores/circuitos-integrados-impresos/!', asignatura)

    if asignatura == 'MEI':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/ingenieriadecomputadores/guiamei_1718/!', asignatura)

    if asignatura == 'SCGC':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/sistemasdeinformacion/etsiit_gii_scgc_1718_gestioncontenidos/!', asignatura)

    if asignatura == 'PDIH':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/sistemasdeinformacion/gii_perifericos_disp_interfaz_20172018firmada/!', asignatura)

    if asignatura == 'PDM':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/tecnologiasdelainformacion/etsiit_gii_pdm_1718_programaciondispositivosmoviles/!', asignatura)

    if asignatura == 'RMS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/tecnologiasdelainformacion/gii_rms_20172018/!', asignatura)

    if asignatura == 'PDS':
        insertarGD('https://grados.ugr.es/informatica/pages/infoacademica/guias_docentes/curso_actual/cuarto/2semestre/tecnologiasdelainformacion/procesamientodigitaldeseaales/!', asignatura)

if __name__ == '__main__':
    if sys.argv[1:]:
        asignatura = sys.argv[1]
        extractDataTeable_GuiaDocente(asignatura)
    else:
        print('Error: indique la asignatura')
