.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/asm-generic/bitops/find.h

.. _`find_next_bit`:

find_next_bit
=============

.. c:function:: unsigned long find_next_bit(const unsigned long *addr, unsigned long size, unsigned long offset)

    find the next set bit in a memory region

    :param const unsigned long \*addr:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long offset:
        The bitnumber to start searching at

.. _`find_next_bit.description`:

Description
-----------

Returns the bit number for the next set bit
If no bits are set, returns \ ``size``\ .

.. _`find_first_bit`:

find_first_bit
==============

.. c:function:: unsigned long find_first_bit(const unsigned long *addr, unsigned long size)

    find the first set bit in a memory region

    :param const unsigned long \*addr:
        The address to start the search at

    :param unsigned long size:
        The maximum number of bits to search

.. _`find_first_bit.description`:

Description
-----------

Returns the bit number of the first set bit.
If no bits are set, returns \ ``size``\ .

.. This file was automatic generated / don't edit.

