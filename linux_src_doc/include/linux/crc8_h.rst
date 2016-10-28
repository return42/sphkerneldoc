.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/crc8.h

.. _`crc8_populate_lsb`:

crc8_populate_lsb
=================

.. c:function:: void crc8_populate_lsb(u8 table[CRC8_TABLE_SIZE], u8 polynomial)

    fill crc table for given polynomial in regular bit order.

    :param u8 table:
        table to be filled.

    :param u8 polynomial:
        polynomial for which table is to be filled.

.. _`crc8_populate_lsb.description`:

Description
-----------

This function fills the provided table according the polynomial provided for
regular bit order (lsb first). Polynomials in CRC algorithms are typically
represented as shown below.

poly = x^8 + x^7 + x^6 + x^4 + x^2 + 1

For lsb first direction x^7 maps to the lsb. So the polynomial is as below.

- lsb first: poly = 10101011(1) = 0xAB

.. _`crc8_populate_msb`:

crc8_populate_msb
=================

.. c:function:: void crc8_populate_msb(u8 table[CRC8_TABLE_SIZE], u8 polynomial)

    fill crc table for given polynomial in reverse bit order.

    :param u8 table:
        table to be filled.

    :param u8 polynomial:
        polynomial for which table is to be filled.

.. _`crc8_populate_msb.description`:

Description
-----------

This function fills the provided table according the polynomial provided for
reverse bit order (msb first). Polynomials in CRC algorithms are typically
represented as shown below.

poly = x^8 + x^7 + x^6 + x^4 + x^2 + 1

For msb first direction x^7 maps to the msb. So the polynomial is as below.

- msb first: poly = (1)11010101 = 0xD5

.. _`crc8`:

crc8
====

.. c:function:: u8 crc8(const u8 table[CRC8_TABLE_SIZE], u8 *pdata, size_t nbytes, u8 crc)

    calculate a crc8 over the given input data.

    :param const u8 table:
        crc table used for calculation.

    :param u8 \*pdata:
        pointer to data buffer.

    :param size_t nbytes:
        number of bytes in data buffer.

    :param u8 crc:
        previous returned crc8 value.

.. _`crc8.description`:

Description
-----------

The CRC8 is calculated using the polynomial given in \ :c:func:`crc8_populate_msb`\ 
or \ :c:func:`crc8_populate_lsb`\ .

The caller provides the initial value (either \ ``CRC8_INIT_VALUE``\ 
or the previous returned value) to allow for processing of
discontiguous blocks of data.  When generating the CRC the
caller is responsible for complementing the final return value
and inserting it into the byte stream.  When validating a byte
stream (including CRC8), a final return value of \ ``CRC8_GOOD_VALUE``\ 
indicates the byte stream data can be considered valid.

.. _`crc8.reference`:

Reference
---------

"A Painless Guide to CRC Error Detection Algorithms", ver 3, Aug 1993
Williams, Ross N., ross<at>ross.net
(see URL http://www.ross.net/crc/download/crc_v3.txt).

.. This file was automatic generated / don't edit.

