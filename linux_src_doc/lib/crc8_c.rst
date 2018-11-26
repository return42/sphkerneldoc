.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc8.c

.. _`crc8_populate_msb`:

crc8_populate_msb
=================

.. c:function:: void crc8_populate_msb(u8 table, u8 polynomial)

    fill crc table for given polynomial in reverse bit order.

    :param table:
        table to be filled.
    :type table: u8

    :param polynomial:
        polynomial for which table is to be filled.
    :type polynomial: u8

.. _`crc8_populate_lsb`:

crc8_populate_lsb
=================

.. c:function:: void crc8_populate_lsb(u8 table, u8 polynomial)

    fill crc table for given polynomial in regular bit order.

    :param table:
        table to be filled.
    :type table: u8

    :param polynomial:
        polynomial for which table is to be filled.
    :type polynomial: u8

.. _`crc8`:

crc8
====

.. c:function:: u8 crc8(const u8 table, u8 *pdata, size_t nbytes, u8 crc)

    calculate a crc8 over the given input data.

    :param table:
        crc table used for calculation.
    :type table: const u8

    :param pdata:
        pointer to data buffer.
    :type pdata: u8 \*

    :param nbytes:
        number of bytes in data buffer.
    :type nbytes: size_t

    :param crc:
        previous returned crc8 value.
    :type crc: u8

.. This file was automatic generated / don't edit.

