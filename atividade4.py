class Cabeça:
    def _init_(self):
        self.esta_intacta = True

class Boneco:
    def _init_(self):
        self.cabeça = Cabeça()

    def destruir(self):
        self.cabeça.esta_intacta = False

boneco1 = Boneco()
print("O boneco 1 tem cabeça intacta:", boneco1.cabeça.esta_intacta)

boneco1.destruir()
print("O boneco 1 tem cabeça intacta:", boneco1.cabeça.esta_intacta)

boneco2 = Boneco()
print("O boneco 2 tem cabeça intacta:", boneco2.cabeça.esta_intacta)