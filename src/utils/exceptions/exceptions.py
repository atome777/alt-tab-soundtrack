from typing import Self, Dict, Any


class ExceptionBaseUnsed(Exception):
    """
    Class
        Classe base de exceção, usada para ser extendida passando um dicionario e a mensagem de erro
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
        proposal (dict): proposta coletada
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        self.__message = kwargs.get("message")
        self.__proposal = kwargs.get("proposal")
        super().__init__(self.__message)

    def to_dict(self) -> Dict[str, Any]:
        """
        Method:
        Metodo para converter a mensagem em dicionario, usado nas exceções.
        """
        return {"message": self.__message, "proposal": self.__proposal}


class ExceptionBase(Exception):
    """
    Class
        Classe base de exceção, usada para ser extendida passando um dicionario e a mensagem de erro
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        self._message = kwargs.get("message", "ExceptionBase error founded")
        super().__init__(self._message)

    def __str__(self: Self) -> str:
        return str(self._message)

    def to_str(self: Self) -> str:
        return str(self._message)


class NoArguments(Exception):
    """
    Class
        Classe de exceção usada quando o metodo não recebe um parametro
     Parameters:
        mensagem (str): mensagem a ser exibida obrigatorio
        nome_funcao (str): nome da função executada obrigatorio
        xpath (str): caminho completo do xpath obrigatorio

    """

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.mensagem = kwargs.get("mensagem", "Erro desconhecido")
        self.funcao = kwargs.get("funcao", "Erro desconhecido")
        self.xpath = kwargs.get("xpath", "Erro desconhecido")
        super().__init__(self.mensagem)

    def __str__(self):
        return f"""A função executada precisa de algum parametro:\n
            Mensagem: {self.mensagem}\n
            Nome da função: {self.funcao}\n
            Xpath: {self.xpath}\n"""


class ElementNotFound(ExceptionBase):
    """
    Class
        Classe de exceção usada quando o elemento não foi encontrado
    Parameters:
        mensagem (str): mensagem a ser exibida obrigatorio
        funcao (str): nome da função executada obrigatorio
        xpath (str): caminho completo do xpath obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.message = kwargs.get("message", "Erro desconhecido")
        self.function = kwargs.get("function", "Erro desconhecido")
        self.xpath = kwargs.get("xpath", "Erro desconhecido")
        self._message = f"""Ocorreu um erro com o elemento informado:\n
            Mensagem: {str(self.message)}\n
            Nome da função: {str(self.function)}\n
            Xpath: {str(self.xpath)}"""

        super().__init__(message=self._message)


class AgilusError(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando houver algum erro nos dados do agilus
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class ApiConsigError(ExceptionBase):
    """
    Class
        Classe de exceção usada Houver um erro no BRX
     Parameters:
        mensagem (str): mensagem a ser exibida obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class DaemonError(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando não houver af disponives no daemon
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
        proposal (dict): proposta coletada
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class UserError(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando não houver usuario
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
        proposal (dict): proposta coletada
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class TypingWebExecutionError(Exception):
    """
    Class
        Classe de exceção, quando houver algum erro em meio a digitação.
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
        proposal (dict): proposta coletada
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        self.message = kwargs.get("message", "ExceptionBase error founded")
        super().__init__(self.message)

    def __str__(self):
        return self.message


class TypingWebSiteMessageError(Exception):
    """Class
        Classe de exceção, usada para quando o site apresentar algum erro atraves de alert ou mensagem.
    Args:
        message (str): Mensagem de erro
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
    

class FormalizationWebSiteMessageError(Exception):
    """Class
        Classe de exceção, usada para quando o site apresentar algum erro atraves de alert ou mensagem.
    Args:
        message (str): Mensagem de erro
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProposalAlreadTyped(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando houver algum erro nos dados do agilus
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
        proposal (dict): proposta coletada
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class RpaError(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando houver algum erro nos dados do RPA
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)


class BoardError(ExceptionBase):
    """
    Class
        Classe de exceção, usada para quando um orgão averbador não for permitido a digitação por esse robo.
     Parameters:
        message (str): mensagem a ser exibida obrigatorio
    """

    def __init__(self, **kwargs: Dict[str, Any]):
        super().__init__(**kwargs)
