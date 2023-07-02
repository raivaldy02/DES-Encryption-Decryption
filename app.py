from flask import *
from Crypto.Cipher import DES
import binascii

app = Flask(__name__)

def pad(s) : 
    while len(s) % 8 != 0 : 
        s += " "
    
    return s

@app.route("/",methods = ['POST', 'GET'])
def main():
    if request.method == 'POST' : 
        param = {
            'Key' : request.form['Key'],
            'Text' : request.form['Text'],
            'action' : request.form['action']
        }

        if param['action'] == 'enc' : 
            #Encryption Stage
            DEScrypt = DES.new(param['Key'].encode('utf-8'), DES.MODE_ECB)
            encResult = DEScrypt.encrypt(pad(param['Text']).encode('utf-8'))

            return render_template('index.html',result_enc = binascii.hexlify(encResult).decode())
        if param['action'] == 'dec' : 
            #DecryptionStage
            DEScrypt = DES.new(param['Key'].encode('utf-8'), DES.MODE_ECB)
            decResult = DEScrypt.decrypt(binascii.unhexlify(param['Text']))

            return render_template('index.html',result_dec = decResult.decode())

    return render_template('index.html')

if __name__ == '__main__':  
    app.run(debug=True)