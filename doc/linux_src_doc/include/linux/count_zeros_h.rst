.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/count_zeros.h

.. _`count_leading_zeros`:

count_leading_zeros
===================

.. c:function:: int count_leading_zeros(unsigned long x)

    Count the number of zeros from the MSB back

    :param unsigned long x:
        The value

.. _`count_leading_zeros.description`:

Description
-----------

Count the number of leading zeros from the MSB going towards the LSB in \ ``x``\ .

If the MSB of \ ``x``\  is set, the result is 0.
If only the LSB of \ ``x``\  is set, then the result is BITS_PER_LONG-1.
If \ ``x``\  is 0 then the result is COUNT_LEADING_ZEROS_0.

.. _`count_trailing_zeros`:

count_trailing_zeros
====================

.. c:function:: int count_trailing_zeros(unsigned long x)

    Count the number of zeros from the LSB forwards

    :param unsigned long x:
        The value

.. _`count_trailing_zeros.description`:

Description
-----------

Count the number of trailing zeros from the LSB going towards the MSB in \ ``x``\ .

If the LSB of \ ``x``\  is set, the result is 0.
If only the MSB of \ ``x``\  is set, then the result is BITS_PER_LONG-1.
If \ ``x``\  is 0 then the result is COUNT_TRAILING_ZEROS_0.

.. This file was automatic generated / don't edit.

