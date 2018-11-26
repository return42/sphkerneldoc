.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_msgtype6.c

.. _`icamex_msg_to_type6mex_msgx`:

ICAMEX_msg_to_type6MEX_msgX
===========================

.. c:function:: int ICAMEX_msg_to_type6MEX_msgX(struct zcrypt_queue *zq, struct ap_message *ap_msg, struct ica_rsa_modexpo *mex)

    :param zq:
        crypto device pointer
    :type zq: struct zcrypt_queue \*

    :param ap_msg:
        pointer to AP message
    :type ap_msg: struct ap_message \*

    :param mex:
        pointer to user input data
    :type mex: struct ica_rsa_modexpo \*

.. _`icamex_msg_to_type6mex_msgx.description`:

Description
-----------

Returns 0 on success or negative errno value.

.. _`icacrt_msg_to_type6crt_msgx`:

ICACRT_msg_to_type6CRT_msgX
===========================

.. c:function:: int ICACRT_msg_to_type6CRT_msgX(struct zcrypt_queue *zq, struct ap_message *ap_msg, struct ica_rsa_modexpo_crt *crt)

    :param zq:
        crypto device pointer
    :type zq: struct zcrypt_queue \*

    :param ap_msg:
        pointer to AP message
    :type ap_msg: struct ap_message \*

    :param crt:
        pointer to user input data
    :type crt: struct ica_rsa_modexpo_crt \*

.. _`icacrt_msg_to_type6crt_msgx.description`:

Description
-----------

Returns 0 on success or negative errno value.

.. _`convert_type86_xcrb`:

convert_type86_xcrb
===================

.. c:function:: int convert_type86_xcrb(struct zcrypt_queue *zq, struct ap_message *reply, struct ica_xcRB *xcRB)

    :param zq:
        crypto device pointer
    :type zq: struct zcrypt_queue \*

    :param reply:
        reply AP message.
    :type reply: struct ap_message \*

    :param xcRB:
        pointer to XCRB
    :type xcRB: struct ica_xcRB \*

.. _`convert_type86_xcrb.description`:

Description
-----------

Returns 0 on success or -EINVAL, -EFAULT, -EAGAIN in case of an error.

.. _`convert_type86_ep11_xcrb`:

convert_type86_ep11_xcrb
========================

.. c:function:: int convert_type86_ep11_xcrb(struct zcrypt_queue *zq, struct ap_message *reply, struct ep11_urb *xcRB)

    :param zq:
        crypto device pointer
    :type zq: struct zcrypt_queue \*

    :param reply:
        reply AP message.
    :type reply: struct ap_message \*

    :param xcRB:
        pointer to EP11 user request block
    :type xcRB: struct ep11_urb \*

.. _`convert_type86_ep11_xcrb.description`:

Description
-----------

Returns 0 on success or -EINVAL, -EFAULT, -EAGAIN in case of an error.

.. _`zcrypt_msgtype6_receive`:

zcrypt_msgtype6_receive
=======================

.. c:function:: void zcrypt_msgtype6_receive(struct ap_queue *aq, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

    :param msg:
        pointer to the AP message
    :type msg: struct ap_message \*

    :param reply:
        pointer to the AP reply message
    :type reply: struct ap_message \*

.. _`zcrypt_msgtype6_receive_ep11`:

zcrypt_msgtype6_receive_ep11
============================

.. c:function:: void zcrypt_msgtype6_receive_ep11(struct ap_queue *aq, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param aq:
        pointer to the AP queue
    :type aq: struct ap_queue \*

    :param msg:
        pointer to the AP message
    :type msg: struct ap_message \*

    :param reply:
        pointer to the AP reply message
    :type reply: struct ap_message \*

.. _`zcrypt_msgtype6_modexpo`:

zcrypt_msgtype6_modexpo
=======================

.. c:function:: long zcrypt_msgtype6_modexpo(struct zcrypt_queue *zq, struct ica_rsa_modexpo *mex)

    device to handle a modexpo request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxC device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param mex:
        pointer to the modexpo request buffer
    :type mex: struct ica_rsa_modexpo \*

.. _`zcrypt_msgtype6_modexpo_crt`:

zcrypt_msgtype6_modexpo_crt
===========================

.. c:function:: long zcrypt_msgtype6_modexpo_crt(struct zcrypt_queue *zq, struct ica_rsa_modexpo_crt *crt)

    device to handle a modexpo_crt request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxC device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param crt:
        pointer to the modexpoc_crt request buffer
    :type crt: struct ica_rsa_modexpo_crt \*

.. _`get_cprb_fc`:

get_cprb_fc
===========

.. c:function:: unsigned int get_cprb_fc(struct ica_xcRB *xcRB, struct ap_message *ap_msg, unsigned int *func_code, unsigned short **dom)

    Extracting the fc requires to copy the cprb from userspace. So this function allocates memory and needs an ap_msg prepared by the caller with \ :c:func:`ap_init_message`\ . Also the caller has to make sure \ :c:func:`ap_release_message`\  is always called even on failure.

    :param xcRB:
        *undescribed*
    :type xcRB: struct ica_xcRB \*

    :param ap_msg:
        *undescribed*
    :type ap_msg: struct ap_message \*

    :param func_code:
        *undescribed*
    :type func_code: unsigned int \*

    :param dom:
        *undescribed*
    :type dom: unsigned short \*\*

.. _`zcrypt_msgtype6_send_cprb`:

zcrypt_msgtype6_send_cprb
=========================

.. c:function:: long zcrypt_msgtype6_send_cprb(struct zcrypt_queue *zq, struct ica_xcRB *xcRB, struct ap_message *ap_msg)

    device to handle a send_cprb request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxC device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param xcRB:
        pointer to the send_cprb request buffer
    :type xcRB: struct ica_xcRB \*

    :param ap_msg:
        *undescribed*
    :type ap_msg: struct ap_message \*

.. _`get_ep11cprb_fc`:

get_ep11cprb_fc
===============

.. c:function:: unsigned int get_ep11cprb_fc(struct ep11_urb *xcrb, struct ap_message *ap_msg, unsigned int *func_code)

    Extracting the fc requires to copy the ep11 cprb from userspace. So this function allocates memory and needs an ap_msg prepared by the caller with \ :c:func:`ap_init_message`\ . Also the caller has to make sure \ :c:func:`ap_release_message`\  is always called even on failure.

    :param xcrb:
        *undescribed*
    :type xcrb: struct ep11_urb \*

    :param ap_msg:
        *undescribed*
    :type ap_msg: struct ap_message \*

    :param func_code:
        *undescribed*
    :type func_code: unsigned int \*

.. _`zcrypt_msgtype6_send_ep11_cprb`:

zcrypt_msgtype6_send_ep11_cprb
==============================

.. c:function:: long zcrypt_msgtype6_send_ep11_cprb(struct zcrypt_queue *zq, struct ep11_urb *xcrb, struct ap_message *ap_msg)

    device to handle a send_ep11_cprb request.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEX4P device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param xcrb:
        *undescribed*
    :type xcrb: struct ep11_urb \*

    :param ap_msg:
        *undescribed*
    :type ap_msg: struct ap_message \*

.. _`zcrypt_msgtype6_rng`:

zcrypt_msgtype6_rng
===================

.. c:function:: long zcrypt_msgtype6_rng(struct zcrypt_queue *zq, char *buffer, struct ap_message *ap_msg)

    device to generate random data.

    :param zq:
        pointer to zcrypt_queue structure that identifies the
        CEXxC device to the request distributor
    :type zq: struct zcrypt_queue \*

    :param buffer:
        pointer to a memory page to return random data
    :type buffer: char \*

    :param ap_msg:
        *undescribed*
    :type ap_msg: struct ap_message \*

.. This file was automatic generated / don't edit.

