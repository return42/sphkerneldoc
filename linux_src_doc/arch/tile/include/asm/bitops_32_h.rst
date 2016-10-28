.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/bitops_32.h

.. _`set_bit`:

set_bit
=======

.. c:function:: void set_bit(unsigned nr, volatile unsigned long *addr)

    Atomically set a bit in memory

    :param unsigned nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from

.. _`set_bit.description`:

Description
-----------

This function is atomic and may not be reordered.
See \\ :c:func:`__set_bit`\  if you do not require the atomic guarantees.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`clear_bit`:

clear_bit
=========

.. c:function:: void clear_bit(unsigned nr, volatile unsigned long *addr)

    Clears a bit in memory

    :param unsigned nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`clear_bit.description`:

Description
-----------

\ :c:func:`clear_bit`\  is atomic and may not be reordered.
See \\ :c:func:`__clear_bit`\  if you do not require the atomic guarantees.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

\ :c:func:`clear_bit`\  may not contain a memory barrier, so if it is used for
locking purposes, you should call \ :c:func:`smp_mb__before_atomic`\  and/or
\ :c:func:`smp_mb__after_atomic`\  to ensure changes are visible on other cpus.

.. _`change_bit`:

change_bit
==========

.. c:function:: void change_bit(unsigned nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param unsigned nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`change_bit.description`:

Description
-----------

\ :c:func:`change_bit`\  is atomic and may not be reordered.
See \\ :c:func:`__change_bit`\  if you do not require the atomic guarantees.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit(unsigned nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param unsigned nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from

.. _`test_and_set_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit(unsigned nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param unsigned nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to count from

.. _`test_and_clear_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. _`test_and_change_bit`:

test_and_change_bit
===================

.. c:function:: int test_and_change_bit(unsigned nr, volatile unsigned long *addr)

    Change a bit and return its old value

    :param unsigned nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to count from

.. _`test_and_change_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. This file was automatic generated / don't edit.

