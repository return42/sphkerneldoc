.. -*- coding: utf-8; mode: rst -*-

=========
mmc_ops.c
=========


.. _`__mmc_switch`:

__mmc_switch
============

.. c:function:: int __mmc_switch (struct mmc_card *card, u8 set, u8 index, u8 value, unsigned int timeout_ms, bool use_busy_signal, bool send_status, bool ignore_crc)

    modify EXT_CSD register

    :param struct mmc_card \*card:
        the MMC card associated with the data transfer

    :param u8 set:
        cmd set values

    :param u8 index:
        EXT_CSD register index

    :param u8 value:
        value to program into EXT_CSD register

    :param unsigned int timeout_ms:
        timeout (ms) for operation performed by register write,
        timeout of zero implies maximum possible timeout

    :param bool use_busy_signal:
        use the busy signal as response type

    :param bool send_status:
        send status cmd to poll for busy

    :param bool ignore_crc:
        ignore CRC errors when sending status cmd to poll for busy



.. _`__mmc_switch.description`:

Description
-----------

Modifies the EXT_CSD register for selected card.

