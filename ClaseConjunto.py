class conjunto:
    __lista=[]
    def __init__(self):
        self.__lista=[]

    def agregarElemento(self,v1):
        self.__lista.append(v1)

    def getLista(self):
        return(self.__lista)

    def __add__(self, other):
        if type(other)==type(self):
            unaLista=self.__lista
            unaLista+=other.__lista
            tempelimi=int
            intercambios = True
            numPasada = len(unaLista)-1
            i=0
            while numPasada > 0 and intercambios:
                numPasada2 = len(unaLista)-1
                intercambios = False
                while i < numPasada2:
                    if unaLista[i]>unaLista[i+1]:
                        intercambios = True
                        temp = unaLista[i]
                        unaLista[i] = unaLista[i+1]
                        unaLista[i+1] = temp
                    elif unaLista[i]==unaLista[i+1]:
                        intercambios = True
                        unaLista.pop(i)
                        numPasada2-=1
                    i+=1
                numPasada = numPasada-1
                i=0
            return unaLista
        else:
            print("no son conjuntos")    
    
    def __sub__(self,other):
        if type(other)==type(self):
            unaLista=self.__lista
            unaLista2=other.__lista
            numPasada = len(unaLista)-1
            numPasada2 = len(unaLista2)-1
            i=0
            while i < numPasada:
                j=0
                while j < numPasada2:
                    if unaLista[i]==unaLista2[j]:
                        unaLista.pop(i)
                        numPasada-=1
                    j+=1
                i+=1
            return unaLista
        else:
            print("no son conjuntos")  

    def __eq__(self,other):
        if type(other)==type(self):

            unaLista=self.__lista
            unaLista2=other.__lista
            numPasada = len(unaLista)-1
            numPasada2 = len(unaLista2)-1
            iguales=True
            i=0
            if numPasada2==numPasada:
                while i < numPasada:
                    if unaLista[i]!=unaLista2[i]:
                        iguales=False
                    i+=1
            return iguales
        else:
            print("no son conjuntos") 