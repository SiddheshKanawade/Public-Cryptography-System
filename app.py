from flask import Flask, redirect, url_for, request, render_template

import newtonRaphson
import helper
import encryption
import decryption

newtonRaphsonObj = newtonRaphson.newtonRaphsonClass
helperObj = helper.Helper
encryptionObj = encryption.Encryption
decryptionObj = decryption.Decryption

class main:

    def __init__(self, cipher, list, string):
        self.cipher = cipher
        self.list = list
        self.string = string


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return "Encreypted array: %s" % name
#    return render_template("output.html", name = name)



@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        inputText = request.form['full-name']

        main.list=[]
        for i in range(len(inputText)):
            main.list.append(ord(inputText[i]))

        # print(main.list)
        # print("\n")

        print("\nProgram output: \n")
        # encryption
        main.cipher = encryptionObj.encrption(main.list)
        print("Encrption output: \n")
        print(main.cipher)


        # decryption
        decryptionOutput = decryptionObj.decryption(main.cipher)
        main.string = decryptionOutput[0]
        asciiList = decryptionOutput[1]
        print("\nDecrypted message:\n" + main.string)
        print("\n")
        
        outputString = main.cipher

        listfinal = []

        for i in range(len(outputString)):
            listfinal.append([inputText[i], outputString[i], asciiList[i]])

        print(listfinal)
        # return redirect(url_for('success',name = dict))
        return render_template("output.html", name = listfinal)
  
if __name__ == '__main__':
   app.run(debug = True)