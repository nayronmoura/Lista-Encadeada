from node import Node


class NodeList:
    """
    Classe que representa um nó de uma lista encadeada
    """

    def __init__(self):
        self.__begin = None
        self.__ending = None
        self.__lenth = 0

    def __str__(self):
        """
            Retorna uma representação em string da lista
            Fluxo:
                1. Verificar se a lista está vazia
                2. Se estiver vazia, retorna uma string vazia
                3. Se não estiver vazia, retorna uma string com todos os valores da lista
                :return: String
        """
        list = ''
        aux = self.__begin
        if aux is None:
            return '[]'
        while aux.next:
            list += f'{aux.value}, '
            aux = aux.next
        else:
            list += f'{aux.value}'
        return f'[{list}]'

    def length(self):
        """
        Retorna o tamanho da lista
        :return: Int
        """
        return self.__lenth

    def append(self, value):
        """
            Adiciona um novo ‘item’ ao final da lista
            Fluxo:
                1. Criar um nó
                2. Verificar se a lista está vazia
                3. Se estiver vazia, o novo nó será o primeiro ‘item’ da lista
                4. Se não estiver vazia, o novo nó será o último ‘item’ da lista
            :param value: Any
            :return: void
        """
        node = Node(value)

        if self.__begin is None:
            self.__begin = node
            self.__ending = node

        else:

            self.__ending.next = node
            self.__ending = self.__ending.next

            # caso eu não tenha o ending...
            # esse método é ineficiente
            # aux = self.__begin
            # while aux.next is not None:
            #     aux = aux.next
            #
            # aux.next = node

        self.__lenth += 1

    def get(self, index):
        """
            Retorna o valor de um ‘item’ da lista
            Fluxo:
                1. Verificar se o índice é válido
                2. Se for válido, percorrer a lista até o índice desejado
                3. Retornar o valor do nó
        :param index:
        :return:
        """
        if index > self.__lenth:
            raise IndexError('Index out of range')
        if index == 0:
            return self.__begin.value

        if index == self.__lenth - 1:
            return self.__ending.value

        aux = self.__begin
        for c in range(index):
            aux = aux.next

        return aux.value

    def insert(self, index, value):
        """
            Insere um novo ‘item’ em uma posição específica da lista
        :param index:
        :param value:
        :return: void
        """
        if index > self.__lenth:
            raise IndexError('Index out of range')

        if index == 0:
            node = Node(value)
            node.next = self.__begin
            self.__begin = node
            self.__lenth += 1
            return

        if index == self.__lenth:
            self.append(value)
            return

        node = Node(value)
        aux = self.__begin
        for c in range(index - 1):
            aux = aux.next

        node.next = aux.next
        aux.next = node

        self.__lenth += 1
