import logging
import sys

from typing import Dict, Any

import src.config.global_variables as globais

from src.utils.exceptions.exceptions import AgilusError, BoardError, \
    DaemonError, ProposalAlreadTyped, TypingWebExecutionError, \
    TypingWebSiteMessageError, UserError

from src.services.database.internal import Internal
from src.services.database.rpa import Rpa
from src.services.database.agilus import Agilus

NAME_EXCEPTION = None
EXCEPTION = None
AF_CODIGO = None
USER = None


def handle_error(exception: Any, user: Dict[str, Any]):
    global NAME_EXCEPTION  # pylint: disable=w0603
    global AF_CODIGO  # pylint: disable=w0603
    global EXCEPTION  # pylint: disable=w0603
    global USER  # pylint: disable=w0603

    NAME_EXCEPTION = type(exception).__name__
    EXCEPTION = exception
    USER = user

    if "Target page, context or browser has been closed" in str(EXCEPTION):
        logging.critical("Exception:%s::Mensagem: %s",
                         NAME_EXCEPTION, str(exception))
        sys.exit(1)

    elif NAME_EXCEPTION in ["DaemonError"]:
        # exceção que não precisa de uma af
        _daemon_error(exception)
    elif NAME_EXCEPTION in ["ProposalAlreadTyped"]:
        _proposal_alread_typed(exception)
    else:
        # coletando dados do banco de dados interno para recuperar a af a ser tratada
        af = Internal().get_af(user=USER)
        if af:
            _, _, AF_CODIGO = af

            if AF_CODIGO:

                # Tras os dados de tratamento de uma exceção
                status = Rpa().get_error_status_fase(message=EXCEPTION)

                # Registrando no banco do rpa o erro que ocorreu na digitação
                Rpa().insere_af_status(
                    af_codigo=AF_CODIGO,
                    status="error",
                    exception_name=NAME_EXCEPTION,
                    message=str(EXCEPTION),
                    reset=status["retry_errors"] if status else globais.LIMIT_COUNTER_ERROR
                )

                if status:
                    # Pesquisa o ultimo status de uma AF
                    status_af = Rpa().get_af(af_codigo=AF_CODIGO)

                    if status_af["counter_error"] >= status["retry_errors"]:
                        fase = status["af_fase_on_retry"] if status["af_fase_on_retry"] is not None else status["af_fase"]
                    else:
                        fase = status["af_fase"]
                    Rpa().clear_af_for_digitation(af_codigo=AF_CODIGO)

                    Agilus().fase_acompanhamento(
                        af_codigo=AF_CODIGO,
                        af_fase=fase,
                        message_agilus=status["replacement_message"] if status["replacement_message"] is not None else str(
                            EXCEPTION),
                    )
                    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                                  NAME_EXCEPTION, AF_CODIGO, fase, str(exception))
                    fase = None

                else:
                    # caso não seja encontrada nenhuma mensagem a ser substituida

                    if NAME_EXCEPTION in ["BoardError"]:
                        _board_error(exception)
                    elif NAME_EXCEPTION in ["AgilusError"]:
                        _agilus_error(exception)
                    elif NAME_EXCEPTION in ["TypingWebExecutionError"]:
                        _typing_web_execution_error(exception)
                    elif NAME_EXCEPTION in ["TypingWebSiteMessageError"]:
                        _typing_web_site_message_error(exception)
                    elif NAME_EXCEPTION in ["UserError"]:
                        _user_error(exception)
                    else:
                        _other_errors(exception)


def _daemon_error(exception: DaemonError):
    logging.info("Exception:%s::Mensagem: %s",
                 NAME_EXCEPTION, str(exception))

def _board_error(exception: BoardError):
    logging.info("Exception:%s::AF:%s::Mensagem: %s",
                 NAME_EXCEPTION, AF_CODIGO, str(exception))

def _proposal_alread_typed(exception: ProposalAlreadTyped):
    logging.info("Exception:%s::AF:%s::Mensagem: %s",
                 NAME_EXCEPTION, AF_CODIGO, str(exception))


def _agilus_error(exception: AgilusError):
    message_exception = str(exception)
    af_fase = 9
    Agilus().fase_acompanhamento(
        af_codigo=AF_CODIGO,
        message_agilus=str(message_exception),
        af_fase=af_fase
    )
    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                  NAME_EXCEPTION, AF_CODIGO, af_fase, str(exception))
    af_fase = None


def _typing_web_site_message_error(exception: TypingWebSiteMessageError):
    message_exception = str(exception)
    af_fase = 9
    Agilus().fase_acompanhamento(
        af_codigo=AF_CODIGO,
        message_agilus=str(message_exception),
        af_fase=af_fase
    )
    print(USER)
    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                  NAME_EXCEPTION, AF_CODIGO, af_fase, str(exception))
    af_fase = None


def _typing_web_execution_error(exception: TypingWebExecutionError):
    message_exception = str(exception)
    af_fase = 9
    Agilus().fase_acompanhamento(
        af_codigo=AF_CODIGO,
        message_agilus=str(message_exception),
        af_fase=af_fase
    )
    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                  NAME_EXCEPTION, AF_CODIGO, af_fase, str(exception))
    af_fase = None

def _user_error(exception: UserError):
    message_exception = str(exception)
    af_fase = 62
    Agilus().altera_fase(
        af_codigo=AF_CODIGO,
        af_fase=af_fase
    )
    Rpa().reset_af_digitation(af_codigo=AF_CODIGO)
    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                  NAME_EXCEPTION, AF_CODIGO, af_fase, message_exception)

def _other_errors(exception: Any):
    message_exception = str(exception)
    af_fase = 9
    Agilus().fase_acompanhamento(
        af_codigo=AF_CODIGO,
        message_agilus=str(message_exception),
        af_fase=af_fase
    )
    logging.error("Exception:%s::AF:%s::Fase:%s::Mensagem: %s",
                  NAME_EXCEPTION, AF_CODIGO, af_fase, str(exception))
    af_fase = None
