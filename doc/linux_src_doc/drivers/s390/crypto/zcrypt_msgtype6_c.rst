.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_msgtype6.c

.. _`icamex_msg_to_type6mex_msgx`:

ICAMEX_msg_to_type6MEX_msgX
===========================

.. c:function:: int ICAMEX_msg_to_type6MEX_msgX(struct zcrypt_device *zdev, struct ap_message *ap_msg, struct ica_rsa_modexpo *mex)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*ap_msg:
        pointer to AP message

    :param struct ica_rsa_modexpo \*mex:
        pointer to user input data

.. _`icamex_msg_to_type6mex_msgx.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`icacrt_msg_to_type6crt_msgx`:

ICACRT_msg_to_type6CRT_msgX
===========================

.. c:function:: int ICACRT_msg_to_type6CRT_msgX(struct zcrypt_device *zdev, struct ap_message *ap_msg, struct ica_rsa_modexpo_crt *crt)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*ap_msg:
        pointer to AP message

    :param struct ica_rsa_modexpo_crt \*crt:
        pointer to user input data

.. _`icacrt_msg_to_type6crt_msgx.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`convert_type86_xcrb`:

convert_type86_xcrb
===================

.. c:function:: int convert_type86_xcrb(struct zcrypt_device *zdev, struct ap_message *reply, struct ica_xcRB *xcRB)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*reply:
        reply AP message.

    :param struct ica_xcRB \*xcRB:
        pointer to XCRB

.. _`convert_type86_xcrb.description`:

Description
-----------

Returns 0 on success or -EINVAL, -EFAULT, -EAGAIN in case of an error.

.. _`convert_type86_ep11_xcrb`:

convert_type86_ep11_xcrb
========================

.. c:function:: int convert_type86_ep11_xcrb(struct zcrypt_device *zdev, struct ap_message *reply, struct ep11_urb *xcRB)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*reply:
        reply AP message.

    :param struct ep11_urb \*xcRB:
        pointer to EP11 user request block

.. _`convert_type86_ep11_xcrb.description`:

Description
-----------

Returns 0 on success or -EINVAL, -EFAULT, -EAGAIN in case of an error.

.. _`zcrypt_msgtype6_receive`:

zcrypt_msgtype6_receive
=======================

.. c:function:: void zcrypt_msgtype6_receive(struct ap_device *ap_dev, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param struct ap_device \*ap_dev:
        pointer to the AP device

    :param struct ap_message \*msg:
        pointer to the AP message

    :param struct ap_message \*reply:
        pointer to the AP reply message

.. _`zcrypt_msgtype6_receive_ep11`:

zcrypt_msgtype6_receive_ep11
============================

.. c:function:: void zcrypt_msgtype6_receive_ep11(struct ap_device *ap_dev, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param struct ap_device \*ap_dev:
        pointer to the AP device

    :param struct ap_message \*msg:
        pointer to the AP message

    :param struct ap_message \*reply:
        pointer to the AP reply message

.. _`zcrypt_msgtype6_modexpo`:

zcrypt_msgtype6_modexpo
=======================

.. c:function:: long zcrypt_msgtype6_modexpo(struct zcrypt_device *zdev, struct ica_rsa_modexpo *mex)

    device to handle a modexpo request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        PCIXCC/CEX2C device to the request distributor

    :param struct ica_rsa_modexpo \*mex:
        pointer to the modexpo request buffer

.. _`zcrypt_msgtype6_modexpo_crt`:

zcrypt_msgtype6_modexpo_crt
===========================

.. c:function:: long zcrypt_msgtype6_modexpo_crt(struct zcrypt_device *zdev, struct ica_rsa_modexpo_crt *crt)

    device to handle a modexpo_crt request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        PCIXCC/CEX2C device to the request distributor

    :param struct ica_rsa_modexpo_crt \*crt:
        pointer to the modexpoc_crt request buffer

.. _`zcrypt_msgtype6_send_cprb`:

zcrypt_msgtype6_send_cprb
=========================

.. c:function:: long zcrypt_msgtype6_send_cprb(struct zcrypt_device *zdev, struct ica_xcRB *xcRB)

    device to handle a send_cprb request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        PCIXCC/CEX2C device to the request distributor

    :param struct ica_xcRB \*xcRB:
        pointer to the send_cprb request buffer

.. _`zcrypt_msgtype6_send_ep11_cprb`:

zcrypt_msgtype6_send_ep11_cprb
==============================

.. c:function:: long zcrypt_msgtype6_send_ep11_cprb(struct zcrypt_device *zdev, struct ep11_urb *xcrb)

    device to handle a send_ep11_cprb request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        CEX4P device to the request distributor

    :param struct ep11_urb \*xcrb:
        *undescribed*

.. _`zcrypt_msgtype6_rng`:

zcrypt_msgtype6_rng
===================

.. c:function:: long zcrypt_msgtype6_rng(struct zcrypt_device *zdev, char *buffer)

    device to generate random data.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        PCIXCC/CEX2C device to the request distributor

    :param char \*buffer:
        pointer to a memory page to return random data

.. This file was automatic generated / don't edit.

