from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

class Operacion:
    def __init__(self, numero_destino, valor):
        self.numero_destino = numero_destino
        self.fecha = datetime.now()
        self.valor = valor

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos = []):
        self.numero = numero
        self.saldo = saldo
        self.nombre = nombre
        self.contactos = contactos
        self.operaciones = []

    def agregar_contacto(self, nombre, numero):
        self.contactos.append({'nombre': nombre, 'numero': numero})

    def eliminar_contacto(self, numero):
        self.contactos = [contacto for contacto in self.contactos if contacto != numero]

    def listar_contactos(self):
        return [f'{BD[contacto].numero} : {BD[contacto].nombre}' for contacto in self.contactos]

    def pagar(self, numero_destino, valor):
        if numero_destino in self.contactos and self.saldo >= valor:
            self.saldo -= valor
            self.operaciones.append(Operacion(numero_destino, f'-{valor}'))
            BD[numero_destino].saldo += valor
            BD[numero_destino].operaciones.append(Operacion(self.numero,f'+{valor}'))
            return True
        return False

    def historial(self):
        return self.saldo, [(operacion.numero_destino, operacion.fecha, operacion.valor) for operacion in self.operaciones]
 
BD = {}
BD[21345] = Cuenta(21345, 'Arnaldo', 200, [123, 456])  
BD[123] = Cuenta(123, 'Luisa', 400, [456])
BD[456] = Cuenta(456, 'Andrea', 300, [21345])


@app.route('/billetera/contactos', methods=['GET'])
def contactos():
    minumero = request.args.get('minumero')
    cuenta = BD[int(minumero)]
    if cuenta:
        return jsonify(cuenta.listar_contactos())
    return jsonify({'error': 'Cuenta no encontrada'}), 404

@app.route('/billetera/pagar', methods=['POST', 'GET'])
def pagar():
    minumero = request.args.get('minumero')
    numerodestino = request.args.get('numerodestino')
    valor = request.args.get('valor')
    cuenta = BD[int(minumero)]
    if cuenta and cuenta.pagar(int(numerodestino), int(valor)):
        return jsonify({'success': f'{datetime.now()}'})
    return jsonify({'error': 'Pago no realizado'}), 400

@app.route('/billetera/historial', methods=['GET'])
def historial():
    minumero = request.args.get('minumero')
    cuenta = BD[int(minumero)]
    if cuenta:
        return jsonify(cuenta.historial())
    return jsonify({'error': 'Cuenta no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
