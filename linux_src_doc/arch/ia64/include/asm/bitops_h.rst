.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/include/asm/bitops.h

.. _`set_bit`:

set_bit
=======

.. c:function:: void set_bit(int nr, volatile void *addr)

    Atomically set a bit in memory

    :param nr:
        the bit to set
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile void \*

.. _`set_bit.description`:

Description
-----------

This function is atomic and may not be reordered.  See \__set_bit()
if you do not require the atomic guarantees.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

The address must be (at least) "long" aligned.
Note that there are driver (e.g., eepro100) which use these operations to
operate on hw-defined data-structures, so we can't easily change these
operations to force a bigger alignment.

bit 0 is the LSB of addr; bit 32 is the LSB of (addr+1).

.. _`__set_bit`:

\__set_bit
==========

.. c:function:: void __set_bit(int nr, volatile void *addr)

    Set a bit in memory

    :param nr:
        the bit to set
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile void \*

.. _`__set_bit.description`:

Description
-----------

Unlike \ :c:func:`set_bit`\ , this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.

.. _`clear_bit`:

clear_bit
=========

.. c:function:: void clear_bit(int nr, volatile void *addr)

    Clears a bit in memory

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: volatile void \*

.. _`clear_bit.description`:

Description
-----------

\ :c:func:`clear_bit`\  is atomic and may not be reordered.  However, it does
not contain a memory barrier, so if it is used for locking purposes,
you should call \ :c:func:`smp_mb__before_atomic`\  and/or \ :c:func:`smp_mb__after_atomic`\ 
in order to ensure changes are visible on other processors.

.. _`clear_bit_unlock`:

clear_bit_unlock
================

.. c:function:: void clear_bit_unlock(int nr, volatile void *addr)

    Clears a bit in memory with release

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: volatile void \*

.. _`clear_bit_unlock.description`:

Description
-----------

\ :c:func:`clear_bit_unlock`\  is atomic and may not be reordered.  It does
contain a memory barrier suitable for unlock type operations.

.. _`__clear_bit_unlock`:

\__clear_bit_unlock
===================

.. c:function:: void __clear_bit_unlock(int nr, void *addr)

    Non-atomically clears a bit in memory with release

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: void \*

.. _`__clear_bit_unlock.description`:

Description
-----------

Similarly to clear_bit_unlock, the implementation uses a store
with release semantics. See also \ :c:func:`arch_spin_unlock`\ .

.. _`__clear_bit`:

\__clear_bit
============

.. c:function:: void __clear_bit(int nr, volatile void *addr)

    Clears a bit in memory (non-atomic version)

    :param nr:
        the bit to clear
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile void \*

.. _`__clear_bit.description`:

Description
-----------

Unlike \ :c:func:`clear_bit`\ , this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.

.. _`change_bit`:

change_bit
==========

.. c:function:: void change_bit(int nr, volatile void *addr)

    Toggle a bit in memory

    :param nr:
        Bit to toggle
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: volatile void \*

.. _`change_bit.description`:

Description
-----------

\ :c:func:`change_bit`\  is atomic and may not be reordered.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`__change_bit`:

\__change_bit
=============

.. c:function:: void __change_bit(int nr, volatile void *addr)

    Toggle a bit in memory

    :param nr:
        the bit to toggle
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile void \*

.. _`__change_bit.description`:

Description
-----------

Unlike \ :c:func:`change_bit`\ , this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.

.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit(int nr, volatile void *addr)

    Set a bit and return its old value

    :param nr:
        Bit to set
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile void \*

.. _`test_and_set_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies the acquisition side of the memory barrier.

.. _`test_and_set_bit_lock`:

test_and_set_bit_lock
=====================

.. c:function::  test_and_set_bit_lock()

    Set a bit and return its old value for lock

.. _`test_and_set_bit_lock.description`:

Description
-----------

This is the same as test_and_set_bit on ia64

.. _`__test_and_set_bit`:

\__test_and_set_bit
===================

.. c:function:: int __test_and_set_bit(int nr, volatile void *addr)

    Set a bit and return its old value

    :param nr:
        Bit to set
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile void \*

.. _`__test_and_set_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.

.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit(int nr, volatile void *addr)

    Clear a bit and return its old value

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile void \*

.. _`test_and_clear_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies the acquisition side of the memory barrier.

.. _`__test_and_clear_bit`:

\__test_and_clear_bit
=====================

.. c:function:: int __test_and_clear_bit(int nr, volatile void *addr)

    Clear a bit and return its old value

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile void \*

.. _`__test_and_clear_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.

.. _`test_and_change_bit`:

test_and_change_bit
===================

.. c:function:: int test_and_change_bit(int nr, volatile void *addr)

    Change a bit and return its old value

    :param nr:
        Bit to change
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile void \*

.. _`test_and_change_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies the acquisition side of the memory barrier.

.. _`__test_and_change_bit`:

\__test_and_change_bit
======================

.. c:function:: int __test_and_change_bit(int nr, void *addr)

    Change a bit and return its old value

    :param nr:
        Bit to change
    :type nr: int

    :param addr:
        Address to count from
    :type addr: void \*

.. _`__test_and_change_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.

.. _`ffz`:

ffz
===

.. c:function:: unsigned long ffz(unsigned long x)

    find the first zero bit in a long word

    :param x:
        The long word to find the bit in
    :type x: unsigned long

.. _`ffz.description`:

Description
-----------

Returns the bit-number (0..63) of the first (least significant) zero bit.
Undefined if no zero exists, so code should check against ~0UL first...

.. _`__ffs`:

\__ffs
======

.. c:function:: unsigned long __ffs(unsigned long x)

    find first bit in word.

    :param x:
        The word to search
    :type x: unsigned long

.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.

.. This file was automatic generated / don't edit.

