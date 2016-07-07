.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/nfc/digital.h

.. _`void`:

void
====

.. c:function:: typedef void(*nfc_digital_cmd_complete_t)

    Definition of command result callback

    :param \*nfc_digital_cmd_complete_t:
        *undescribed*

.. _`void.description`:

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

