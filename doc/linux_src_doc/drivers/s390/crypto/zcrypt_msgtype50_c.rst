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

.. c:function:: int ICAMEX_msg_to_type50MEX_msg(struct zcrypt_device *zdev, struct ap_message *ap_msg, struct ica_rsa_modexpo *mex)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*ap_msg:
        *undescribed*

    :param struct ica_rsa_modexpo \*mex:
        pointer to user input data

.. _`icamex_msg_to_type50mex_msg.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`icacrt_msg_to_type50crt_msg`:

ICACRT_msg_to_type50CRT_msg
===========================

.. c:function:: int ICACRT_msg_to_type50CRT_msg(struct zcrypt_device *zdev, struct ap_message *ap_msg, struct ica_rsa_modexpo_crt *crt)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*ap_msg:
        *undescribed*

    :param struct ica_rsa_modexpo_crt \*crt:
        pointer to user input data

.. _`icacrt_msg_to_type50crt_msg.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`convert_type80`:

convert_type80
==============

.. c:function:: int convert_type80(struct zcrypt_device *zdev, struct ap_message *reply, char __user *outputdata, unsigned int outputdatalength)

    :param struct zcrypt_device \*zdev:
        crypto device pointer

    :param struct ap_message \*reply:
        reply AP message.

    :param char __user \*outputdata:
        *undescribed*

    :param unsigned int outputdatalength:
        *undescribed*

.. _`convert_type80.description`:

Description
-----------

Returns 0 on success or -EFAULT.

.. _`zcrypt_cex2a_receive`:

zcrypt_cex2a_receive
====================

.. c:function:: void zcrypt_cex2a_receive(struct ap_device *ap_dev, struct ap_message *msg, struct ap_message *reply)

    "msg" has finished with the reply message "reply". It is called from tasklet context.

    :param struct ap_device \*ap_dev:
        pointer to the AP device

    :param struct ap_message \*msg:
        pointer to the AP message

    :param struct ap_message \*reply:
        pointer to the AP reply message

.. _`zcrypt_cex2a_modexpo`:

zcrypt_cex2a_modexpo
====================

.. c:function:: long zcrypt_cex2a_modexpo(struct zcrypt_device *zdev, struct ica_rsa_modexpo *mex)

    device to handle a modexpo request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        CEX2A device to the request distributor

    :param struct ica_rsa_modexpo \*mex:
        pointer to the modexpo request buffer

.. _`zcrypt_cex2a_modexpo_crt`:

zcrypt_cex2a_modexpo_crt
========================

.. c:function:: long zcrypt_cex2a_modexpo_crt(struct zcrypt_device *zdev, struct ica_rsa_modexpo_crt *crt)

    device to handle a modexpo_crt request.

    :param struct zcrypt_device \*zdev:
        pointer to zcrypt_device structure that identifies the
        CEX2A device to the request distributor

    :param struct ica_rsa_modexpo_crt \*crt:
        pointer to the modexpoc_crt request buffer

.. This file was automatic generated / don't edit.

