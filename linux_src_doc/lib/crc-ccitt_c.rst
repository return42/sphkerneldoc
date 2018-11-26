.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc-ccitt.c

.. _`crc_ccitt`:

crc_ccitt
=========

.. c:function:: u16 crc_ccitt(u16 crc, u8 const *buffer, size_t len)

    recompute the CRC (CRC-CCITT variant) for the data buffer

    :param crc:
        previous CRC value
    :type crc: u16

    :param buffer:
        data pointer
    :type buffer: u8 const \*

    :param len:
        number of bytes in the buffer
    :type len: size_t

.. _`crc_ccitt_false`:

crc_ccitt_false
===============

.. c:function:: u16 crc_ccitt_false(u16 crc, u8 const *buffer, size_t len)

    recompute the CRC (CRC-CCITT-FALSE variant) for the data buffer

    :param crc:
        previous CRC value
    :type crc: u16

    :param buffer:
        data pointer
    :type buffer: u8 const \*

    :param len:
        number of bytes in the buffer
    :type len: size_t

.. This file was automatic generated / don't edit.

