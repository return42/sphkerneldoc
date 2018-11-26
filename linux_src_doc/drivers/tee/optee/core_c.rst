.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/core.c

.. _`optee_from_msg_param`:

optee_from_msg_param
====================

.. c:function:: int optee_from_msg_param(struct tee_param *params, size_t num_params, const struct optee_msg_param *msg_params)

    convert from OPTEE_MSG parameters to struct tee_param

    :param params:
        subsystem internal parameter representation
    :type params: struct tee_param \*

    :param num_params:
        number of elements in the parameter arrays
    :type num_params: size_t

    :param msg_params:
        OPTEE_MSG parameters
        Returns 0 on success or <0 on failure
    :type msg_params: const struct optee_msg_param \*

.. _`optee_to_msg_param`:

optee_to_msg_param
==================

.. c:function:: int optee_to_msg_param(struct optee_msg_param *msg_params, size_t num_params, const struct tee_param *params)

    convert from struct tee_params to OPTEE_MSG parameters

    :param msg_params:
        OPTEE_MSG parameters
    :type msg_params: struct optee_msg_param \*

    :param num_params:
        number of elements in the parameter arrays
    :type num_params: size_t

    :param params:
        subsystem itnernal parameter representation
        Returns 0 on success or <0 on failure
    :type params: const struct tee_param \*

.. This file was automatic generated / don't edit.

