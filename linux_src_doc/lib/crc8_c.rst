.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/crc8.c

.. _`crc8_populate_msb`:

crc8_populate_msb
=================

.. c:function:: void crc8_populate_msb(u8 table, u8 polynomial)

    fill crc table for given polynomial in reverse bit order.

    :param u8 table:
        table to be filled.

    :param u8 polynomial:
        polynomial for which table is to be filled.

.. _`crc8_populate_lsb`:

crc8_populate_lsb
=================

.. c:function:: void crc8_populate_lsb(u8 table, u8 polynomial)

    fill crc table for given polynomial in regular bit order.

    :param u8 table:
        table to be filled.

    :param u8 polynomial:
        polynomial for which table is to be filled.

.. _`crc8`:

crc8
====

.. c:function:: u8 crc8(const u8 table, u8 *pdata, size_t nbytes, u8 crc)

    calculate a crc8 over the given input data.

    :param const u8 table:
        crc table used for calculation.

    :param u8 \*pdata:
        pointer to data buffer.

    :param size_t nbytes:
        number of bytes in data buffer.

    :param u8 crc:
        previous returned crc8 value.

.. This file was automatic generated / don't edit.

