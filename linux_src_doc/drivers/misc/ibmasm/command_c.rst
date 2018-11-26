.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ibmasm/command.c

.. _`ibmasm_exec_command`:

ibmasm_exec_command
===================

.. c:function:: void ibmasm_exec_command(struct service_processor *sp, struct command *cmd)

    send a command to a service processor Commands are executed sequentially. One command (sp->current_command) is sent to the service processor. Once the interrupt handler gets a message of type command_response, the message is copied into the current commands buffer,

    :param sp:
        *undescribed*
    :type sp: struct service_processor \*

    :param cmd:
        *undescribed*
    :type cmd: struct command \*

.. _`ibmasm_wait_for_response`:

ibmasm_wait_for_response
========================

.. c:function:: void ibmasm_wait_for_response(struct command *cmd, int timeout)

    and the command status been updated by the interrupt handler. (see receive_response).

    :param cmd:
        *undescribed*
    :type cmd: struct command \*

    :param timeout:
        *undescribed*
    :type timeout: int

.. _`ibmasm_receive_command_response`:

ibmasm_receive_command_response
===============================

.. c:function:: void ibmasm_receive_command_response(struct service_processor *sp, void *response, size_t size)

    called by the interrupt handler when a dot command of type command_response was received.

    :param sp:
        *undescribed*
    :type sp: struct service_processor \*

    :param response:
        *undescribed*
    :type response: void \*

    :param size:
        *undescribed*
    :type size: size_t

.. This file was automatic generated / don't edit.

