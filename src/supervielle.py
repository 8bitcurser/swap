from re import search

from src.bank import Bank


Supervielle = Bank(
    name='supervielle',
    key='Concepto',
    concepts_map = {
        'Acreditación Cheque Dep.48 Hs.': {
            'id': 1,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
                'imp_debitos': None,
            }
        },
        'COMIS.TRANSFERENCIAS': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'percep_iibb':0.001,
                'imp_debitos': None,
            }
        },
        'COMISIONES DATANET': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'imp_debitos': None,
            }
        },
        'CRED BCA ELECTR INTERBANC EXEN': {
            'id': 12,
            'taxes': {}
        },
        'CRED BCA ELECTRONICA INTERBANC': {
            'id': 12,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
                'imp_debitos': None,
            }
        },
        'Cobro Percepción IIBB': {
            'id': 3,
            'taxes': {}
        },
        'Comisión Consulta Cámara': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'imp_debitos': None,
            }
        },
        'Comisión Mantenimiento Cuenta': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'percep_iva_3': 0.03,
                'percep_iibb':0.001,
                'imp_debitos': None,
            }
        },
        'Comisión Riesgo Contigente': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'imp_debitos': None,
            }
        },
        'Contras.Ints.Sobreg.': {
            'id': 6,
            'taxes': {
                'iva_10.5': 0.105,
                'imp_debitos': 0,
            }
        },
        'Credito DEBIN': {
            'id': 12,
            'taxes': {}
        },
        'Crédito Transf. HomeBanking': {
            'id': 12,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
                'imp_debitos': None,
            }
        },
        'Crédito por Transferencia': {
            'id': 12,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
                'imp_debitos': None,
            }
        },
        'DEB BCA ELECTR INTERBANC EXEN': {
            'id': 12,
            'taxes': {}
        },
        'DEB BCA ELECTRONICA INTERBANC': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'DEB BCA ELECTRONICA INTRABANC': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Deb. Pago de Sueldo': {
            'id': 11,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Debito Transf. HomeBanking': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Descto. Docum.- Acreditación': {
            'id': 8,
            'taxes': {
                'iibb_acred_banc': 0.018,
                'imp_debitos': 0,
            }
        },
        'Devolución Imp. Débitos': {
            'id': 5,
            'taxes': {}
        },
        'Débito Automático de Servicio': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Débito Comisión Pago a Prov.': {
            'id': 2,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'IIBB- Acreditaciones Bancarias': {
            'id': 3,
            'taxes': {}
        },
        'IMPUESTO A LOS SELLOS': {
            'id': 10,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'IVA': {
            'id': 7,
            'taxes': {}
        },
        'Impuesto Débitos y Créditos/CR': {
            'id': 4,
            'taxes': {}
        },
        'Impuesto Débitos y Créditos/DB': {
            'id': 5,
            'taxes': {}
        },
        'Intereses de Sobregiro': {
            'id': 6,
            'taxes': {
                'iva_10.5': 0.105,
                'percep_iva_1.5': 0.015,
                'percep_iibb':0.001,
                'imp_debitos': None,
            }
        },
        'Pago Automático de Préstamo': {
            'id': 8,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Pago Cheque de Cámara Recibida': {
            'id': 1,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Pago Cámara SPV 24 hs.': {
            'id': 1,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Pago de Servicios': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Percepción I.V.A. RG. 3337': {
            'id': 9,
            'taxes': {}
        },
        'Préstamos Inversion Productiva': {
            'id': 8,
            'taxes': {}
        },
        'Rech. Cheques Falla Técnica': {
            'id': 1,
            'taxes': {}
        },
        'SIPAP - Pago Cheque de Cámara': {
            'id': 1,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'SIPAP - Pago Cámara SPV 24 hs.': {
            'id': 1,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Transferencia por CBU': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Trf. Masivas Pago Proveedores': {
            'id': 12,
            'taxes': {
                'imp_debitos': 0.06,
            }
        },
        'Trf. Pago.Prov-Terceros O/Bcos': {
            'id': 1,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
                'imp_debitos': None,
            }
        },
    }
)
def _objective_parser(line, id):
    if id == 12:
        cuit = search(r"\b(\d{11})\b", line['Detalle'])
        objective = cuit.group() if cuit is not None else ""
    else:
        check_num = line['Detalle'].replace("Número De Cheque: ", '')
        if 'Falla Técnica' in line['Concepto']:
            objective = f"{check_num} // Falla Técnica"
        else:
            objective = check_num
    return objective
    
Supervielle._objective_parser = _objective_parser
