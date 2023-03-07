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
            }
        },
        'COMIS.TRANSFERENCIAS': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'percep_iibb':0.001,
            }
        },
        'COMISIONES DATANET': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
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
            }
        },
        'Comisión Mantenimiento Cuenta': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
                'percep_iva_3': 0.03,
                'percep_iibb':0.001,
            }
        },
        'Comisión Riesgo Contigente': {
            'id': 2,
            'taxes': {
                'iva_21': 0.21,
            }
        },
        'Contras.Ints.Sobreg.': {
            'id': 6,
            'taxes': {
                'iva_10.5': 0.105,
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
            }
        },
        'Crédito por Transferencia': {
            'id': 12,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
            }
        },
        'DEB BCA ELECTR INTERBANC EXEN': {
            'id': 12,
            'taxes': {}
        },
        'DEB BCA ELECTRONICA INTERBANC': {
            'id': 12,
            'taxes': {}
        },
        'DEB BCA ELECTRONICA INTRABANC': {
            'id': 12,
            'taxes': {}
        },
        'Deb. Pago de Sueldo': {
            'id': 11,
            'taxes': {}
        },
        'Debito Transf. HomeBanking': {
            'id': 12,
            'taxes': {}
        },
        'Descto. Docum.- Acreditación': {
            'id': 8,
            'taxes': {
                'iibb_acred_banc': 0.018,
            }
        },
        'Devolución Imp. Débitos': {
            'id': 5,
            'taxes': {}
        },
        'Débito Automático de Servicio': {
            'id': 12,
            'taxes': {}
        },
        'Débito Comisión Pago a Prov.': {
            'id': 2,
            'taxes': {}
        },
        'IIBB- Acreditaciones Bancarias': {
            'id': 3,
            'taxes': {}
        },
        'IMPUESTO A LOS SELLOS': {
            'id': 10,
            'taxes': {}
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
            }
        },
        'Pago Automático de Préstamo': {
            'id': 8,
            'taxes': {}
        },
        'Pago Cheque de Cámara Recibida': {
            'id': 1,
            'taxes': {}
        },
        'Pago Cámara SPV 24 hs.': {
            'id': 1,
            'taxes': {}
        },
        'Pago de Servicios': {
            'id': 12,
            'taxes': {}
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
            'taxes': {}
        },
        'SIPAP - Pago Cámara SPV 24 hs.': {
            'id': 1,
            'taxes': {}
        },
        'Transferencia por CBU': {
            'id': 12,
            'taxes': {}
        },
        'Trf. Masivas Pago Proveedores': {
            'id': 12,
            'taxes': {}
        },
        'Trf. Pago.Prov-Terceros O/Bcos': {
            'id': 1,
            'taxes': {
                'imp_creditos': 0.006,
                'iibb_acred_banc': 0.018,
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
