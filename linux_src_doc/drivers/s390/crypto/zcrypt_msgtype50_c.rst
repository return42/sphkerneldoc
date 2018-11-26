.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_msgtype50.c

.. _`type80_rsp_code`:

TYPE80_RSP_CODE
===============

.. c:function::  TYPE80_RSP_CODE()

.. _`type80_rsp_code.description`:

Description
-----------

Note that all unsigned char arrays are right-justified and left-padded
with zeroes.

Note that all reserved fields must be zeroes.

.. _`icamex_msg_to_type50mex_msg`:

ICAMEX_msg_to_type50MEX_msg
===========================

.. c:function:: int ICAMEX_msg_to_type50MEX_msg(struct zcrypt_queue *zq, struct ap_message *ap_msg, struct ica_rsa_modexpo *mex)

    :param zq:
        crypto queue pointer
    :type zq: struct zcrypt_queue \*

    :param ap_msg:
        crypto request pointer
    :type ap_msg: struct ap_message \*

    :param mex:
        pointer to user input data
    :type mex: struct ica_rsa_modexpo \*

.. _`icamex_msg_to_type50mex_msg.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`icacrt_msg_to_type50crt_msg`:

ICACRT_msg_to_type50CRT_msg
===========================

.. c:function:: int ICACRT_msg_to_type50CRT_msg(struct zcrypt_queue *zq, struct ap_message *ap_msg, struct ica_rsa_modexpo_crt *crt)

    :param zq:
        crypto queue pointer
    :type zq: struct zcrypt_queue \*

    :param ap_msg:
        crypto request pointer
    :type ap_msg: struct ap_message \*

    :param crt:
        pointer to user input data
    :type crt: struct ica_rsa_modexpo_crt \*

.. _`icacrt_msg_to_type50crt_msg.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`convert_type80`:

convert_type80
==============

.. c:function:: int convert_type80(struct zcrypt_queue *zq, struct ap_message *reply, char __user *outputdata, unsigned int outputdatalength)

    :param zq:
        crypto device pointer
    :type zq: struct zcrypt_queue \*

    :param reply:
        reply AP message.
    :type reply: struct ap_message \*

    :param outputdata:
        *undescribed*
    :type outputdata: char __user \*

    :param outputdatalength:
        *undescribed*
    :type outputdatalength: unsigned int

.. _`convert_type80.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`zcrypt_cex2a_receive`:

zcrypt_cex2a_receive
====================

.. c:function:: void zcrypt_cex2a_receive(struct ap_queue *aq, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param aq:
        pointer to the AP device
    :type aq: struct ap_queue \*

    :param msg:
        pointer to the AP message
    :type msg: struct ap_message \*

    :param reply:
        pointer to the AP reply message
    :type reply: struct ap_message \*

.. _`zcrypt_cex2a_modexpo`:

zcrypt_cex2a_modexpo
====================

.. c:function:: long zcrypt_cex2a_modexpo(struct zcrypt_queue *zq, struct ica_rsa_modexpo *mex)

    device to handle a modexpo request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxA device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param mex:
        pointer to the modexpo request buffer
    :type mex: struct ica_rsa_modexpo \*

.. _`zcrypt_cex2a_modexpo_crt`:

zcrypt_cex2a_modexpo_crt
========================

.. c:function:: long zcrypt_cex2a_modexpo_crt(struct zcrypt_queue *zq, struct ica_rsa_modexpo_crt *crt)

    device to handle a modexpo_crt request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxA device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param crt:
        pointer to the modexpoc_crt request buffer
    :type crt: struct ica_rsa_modexpo_crt \*

.. This file was automatic generated / don't edit.

