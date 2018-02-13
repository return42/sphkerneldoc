.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/sync_bitops.h

.. _`sync_set_bit`:

sync_set_bit
============

.. c:function:: void sync_set_bit(long nr, volatile unsigned long *addr)

    Atomically set a bit in memory

    :param long nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from

.. _`sync_set_bit.description`:

Description
-----------

This function is atomic and may not be reordered.  See \__set_bit()
if you do not require the atomic guarantees.

Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`sync_clear_bit`:

sync_clear_bit
==============

.. c:function:: void sync_clear_bit(long nr, volatile unsigned long *addr)

    Clears a bit in memory

    :param long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`sync_clear_bit.description`:

Description
-----------

\ :c:func:`sync_clear_bit`\  is atomic and may not be reordered.  However, it does
not contain a memory barrier, so if it is used for locking purposes,
you should call \ :c:func:`smp_mb__before_atomic`\  and/or \ :c:func:`smp_mb__after_atomic`\ 
in order to ensure changes are visible on other processors.

.. _`sync_change_bit`:

sync_change_bit
===============

.. c:function:: void sync_change_bit(long nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`sync_change_bit.description`:

Description
-----------

\ :c:func:`sync_change_bit`\  is atomic and may not be reordered.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`sync_test_and_set_bit`:

sync_test_and_set_bit
=====================

.. c:function:: int sync_test_and_set_bit(long nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from

.. _`sync_test_and_set_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. _`sync_test_and_clear_bit`:

sync_test_and_clear_bit
=======================

.. c:function:: int sync_test_and_clear_bit(long nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to count from

.. _`sync_test_and_clear_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. _`sync_test_and_change_bit`:

sync_test_and_change_bit
========================

.. c:function:: int sync_test_and_change_bit(long nr, volatile unsigned long *addr)

    Change a bit and return its old value

    :param long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to count from

.. _`sync_test_and_change_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. This file was automatic generated / don't edit.

