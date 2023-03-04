from re import search

from src.bank import Bank


Supervielle = Bank(
    name='supervielle',
    key='Concepto',
    concepts_map = {
        'Acreditación Cheque Dep.48 Hs.': 1,
        'COMIS.TRANSFERENCIAS': 2,
        'COMISIONES DATANET': 2,
        'CRED BCA ELECTR INTERBANC EXEN':12,
        'CRED BCA ELECTRONICA INTERBANC':12,
        'Cobro Percepción IIBB': 3,
        'Comisión Consulta Cámara': 2,
        'Comisión Mantenimiento Cuenta': 2,
        'Comisión Riesgo Contigente': 2,
        'Contras.Ints.Sobreg.': 6,
        'Credito DEBIN':12,
        'Crédito Transf. HomeBanking':12,
        'Crédito por Transferencia':12,
        'DEB BCA ELECTR INTERBANC EXEN':12,
        'DEB BCA ELECTRONICA INTERBANC':12,
        'DEB BCA ELECTRONICA INTRABANC':12,
        'Deb. Pago de Sueldo':11,
        'Debito Transf. HomeBanking':12,
        'Descto. Docum.- Acreditación': 8,
        'Devolución Imp. Débitos': 5,
        'Débito Automático de Servicio':12,
        'Débito Comisión Pago a Prov.': 2,
        'IIBB- Acreditaciones Bancarias': 3,
        'IMPUESTO A LOS SELLOS':10,
        'IVA': 7,
        'Impuesto Débitos y Créditos/CR': 4,
        'Impuesto Débitos y Créditos/DB': 5,
        'Intereses de Sobregiro': 6,
        'Pago Automático de Préstamo': 8,
        'Pago Cheque de Cámara Recibida': 1,
        'Pago Cámara SPV 24 hs.': 1,
        'Pago de Servicios':12,
        'Percepción I.V.A. RG. 3337': 9,
        'Préstamos Inversion Productiva': 8,
        'Rech. Cheques Falla Técnica': 1,
        'SIPAP - Pago Cheque de Cámara': 1,
        'SIPAP - Pago Cámara SPV 24 hs.': 1,
        'Transferencia por CBU': 12,
        'Trf. Masivas Pago Proveedores':12,
        'Trf. Pago.Prov-Terceros O/Bcos': 1
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
