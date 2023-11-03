class Professor:
    def _init_(self, nome):
        self.nome = nome
        self.cursos = []

    def lecionar(self, curso):
        self.cursos.append(curso)

class Curso:
    def _init_(self, nome):
        self.nome = nome
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor
        professor.lecionar(self)

professor_A = Professor("Prof. A")
professor_B = Professor("Prof. B")

matematica = Curso("Matemática")
fisica = Curso("Física")
quimica = Curso("Química")

matematica.designar_professor(professor_A)
fisica.designar_professor(professor_B)
quimica.designar_professor(professor_A)

print("Cursos do Prof. A:", professor_A.cursos)
print("Cursos do Prof. B:", professor_B.cursos)