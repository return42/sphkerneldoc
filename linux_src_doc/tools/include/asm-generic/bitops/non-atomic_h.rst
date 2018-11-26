.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/asm-generic/bitops/non-atomic.h

.. _`__set_bit`:

\__set_bit
==========

.. c:function:: void __set_bit(int nr, volatile unsigned long *addr)

    Set a bit in memory

    :param nr:
        the bit to set
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile unsigned long \*

.. _`__set_bit.description`:

Description
-----------

Unlike \ :c:func:`set_bit`\ , this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.

.. _`__change_bit`:

\__change_bit
=============

.. c:function:: void __change_bit(int nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param nr:
        the bit to change
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile unsigned long \*

.. _`__change_bit.description`:

Description
-----------

Unlike \ :c:func:`change_bit`\ , this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.

.. _`__test_and_set_bit`:

\__test_and_set_bit
===================

.. c:function:: int __test_and_set_bit(int nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param nr:
        Bit to set
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`__test_and_set_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.

.. _`__test_and_clear_bit`:

\__test_and_clear_bit
=====================

.. c:function:: int __test_and_clear_bit(int nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`__test_and_clear_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.

.. _`test_bit`:

test_bit
========

.. c:function:: int test_bit(int nr, const volatile unsigned long *addr)

    Determine whether a bit is set

    :param nr:
        bit number to test
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: const volatile unsigned long \*

.. This file was automatic generated / don't edit.

