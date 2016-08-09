.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/nfc/digital.h

.. _`nfc_digital_cmd_complete_t`:

nfc_digital_cmd_complete_t
==========================

.. c:function:: void nfc_digital_cmd_complete_t(struct nfc_digital_dev *ddev, void *arg, struct sk_buff *resp)

    Definition of command result callback

    :param struct nfc_digital_dev \*ddev:
        nfc_digital_device ref

    :param void \*arg:
        user data

    :param struct sk_buff \*resp:
        response data

.. _`nfc_digital_cmd_complete_t.description`:

Description
-----------

resp pointer can be an error code and will be checked with \ :c:func:`IS_ERR`\  macro.
The callback is responsible for freeing resp sk_buff.

.. _`nfc_digital_drv_caps_in_crc`:

NFC_DIGITAL_DRV_CAPS_IN_CRC
===========================

.. c:function::  NFC_DIGITAL_DRV_CAPS_IN_CRC()

    bit mask made of the following values

.. This file was automatic generated / don't edit.

