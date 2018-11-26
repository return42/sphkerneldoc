.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/atmel-ecc.c

.. _`atmel_ecc_checksum`:

atmel_ecc_checksum
==================

.. c:function:: void atmel_ecc_checksum(struct atmel_ecc_cmd *cmd)

    Generate 16-bit CRC as required by ATMEL ECC. CRC16 verification of the count, opcode, param1, param2 and data bytes. The checksum is saved in little-endian format in the least significant two bytes of the command. CRC polynomial is 0x8005 and the initial register value should be zero.

    :param cmd:
        structure used for communicating with the device.
    :type cmd: struct atmel_ecc_cmd \*

.. This file was automatic generated / don't edit.

