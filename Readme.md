### Conta Bancária em POO 
![imagem-exemplo](https://user-images.githubusercontent.com/71408872/129200259-3fc842af-7e93-438b-bfba-b704f1d3947c.jpg)


# 📚 Conteúdo
* [Introdução](#introdução)
* [Classes](#classes)
* [Objetos](#objetos)
* [Atributos e Métodos](#atributos-e-metodos)
* [Constructor](#constructor)
* [No código](#no-codigo)

## Introdução
Em paradigmas de programação, a POO (programação orientada a objetos) resolve problemas encontrados no paradigma procedural tentando aproximar as estruturas desenvolvidas no código de estruturas que existem no mundo real, e para isso essas estruturas precisam possuir as seguintes características inerentes: 
* Classe
* Objeto
* Atributos e Métodos 
Como a ideia desse projeto é criar uma conta bancária podemos destrinchar os termos acima com os aspectos de uma conta real. 

## Classes
Primeiro é necessário entender que toda conta no banco, apesar das suas diferenças (nome de titular, quantos saques pode fazer, limite de crédito etc) herdam propriedades de uma categoria no nosso universo chamada Conta Bancária. Essa categoria é a nossa ***Classe***.

## Objetos 
Embora todas as contas do banco estejam incluídas no nosso conceito de "Conta Bancária", é fácil de perceber que a conta0001 é diferente da conta0002 e portanto, cada uma delas deve ser tratada como um ***Objeto*** diferente do outro. Mesmo ainda pertencentes a mesma ***Classe***. A sua conta no banco é um objeto instanciado da classe *ContasEmBancos*

## Atributos e Métodos
Com essa linha de raciocínio podemos nos aprofundar dentro de uma conta e dividir suas propriedades em dois tipos.

* Aquelas que tangem o estado da conta, como o valor encontrado no saldo ou o número de saques que o usuário pode realizar são chamadas de ***Atributos***. Os atributos são as "características" de um objeto.

* Já as propriedades que remetem a uma ação, como a mudança do titular da conta, ou visualizar seu extrato, são os ***Métodos***. Eles interagem como os atributos e são tratados como o "comportamento" do objeto. 

>É possível existir um tipo de conta PlatinumMaster2000 que tem mais métodos disponíveis e valores diferentes em comparação a uma conta comum mas ainda sim, podemos afirmar que ela terá todos os métodos e atributos de uma ContaBancaria e isso é o que chamamos de **Herança**

## Constructor 
Geralmente gostamos de instanciar um objeto com características preestabelecidas. Para isso, precisamos de uma função que realiza tarefas assim que o objeto for instanciado, independente de ser chamada ou não. O nome dessa função é ***constructor***, e no python temos o método `__init__()` encarregado desse posto.

Existem dois tipos de construtores:
* Default Constructor
```py
class Carro:
    #constructor sem argumentos
    def __init__(self):
        self.quantidade_de_rodas = 4
    def quantas_rodas(self):
        print(self.quantidade_de_rodas)

carro1 = Carro()
carro1.quantas_rodas() 
# Output: 4
```

* Parameterized constructor
```py
class Carro:
    #constructor com argumentos 
    def __init__(self, qtd_rodas):
        self.quantidade_de_rodas = qtd_rodas 
    def quantas_rodas(self):
        print(self.quantidade_de_rodas)

carro1 = Carro(66)
carro1.quantas_rodas()
# Output: 66
```

Em resumo, o  ***Default constructor** não aceita parâmetros na hora de sua criação e pode instanciar objetos com atributos predefinidos sem o usuário escrever argumentos na hora de chamar a classe. 
No caso do ***Parameterized constructor, é necessário que o usuário passe argumentos na hora de instanciar um novo objeto. Somente assim o constructor terá as informações a serem assinaladas nos atributos iniciais.