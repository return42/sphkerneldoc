.. -*- coding: utf-8; mode: rst -*-

========
bitops.h
========

.. _`set_bit`:

set_bit
=======

.. c:function:: void set_bit (long nr, volatile unsigned long *addr)

    Atomically set a bit in memory

    :param long nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from


.. _`set_bit.description`:

Description
-----------

This function is atomic and may not be reordered.  See :c:func:`__set_bit`
if you do not require the atomic guarantees.

Note: there are no guarantees that this function will not be reordered
on non x86 architectures, so if you are writing portable code,
make sure not to rely on its reordering guarantees.

Note that ``nr`` may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.


.. _`__set_bit`:

__set_bit
=========

.. c:function:: void __set_bit (long nr, volatile unsigned long *addr)

    Set a bit in memory

    :param long nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from


.. _`__set_bit.description`:

Description
-----------

Unlike :c:func:`set_bit`, this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.


.. _`clear_bit`:

clear_bit
=========

.. c:function:: void clear_bit (long nr, volatile unsigned long *addr)

    Clears a bit in memory

    :param long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to start counting from


.. _`clear_bit.description`:

Description
-----------

:c:func:`clear_bit` is atomic and may not be reordered.  However, it does
not contain a memory barrier, so if it is used for locking purposes,
you should call :c:func:`smp_mb__before_atomic` and/or :c:func:`smp_mb__after_atomic`
in order to ensure changes are visible on other processors.


.. _`__change_bit`:

__change_bit
============

.. c:function:: void __change_bit (long nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param long nr:
        the bit to change

    :param volatile unsigned long \*addr:
        the address to start counting from


.. _`__change_bit.description`:

Description
-----------

Unlike :c:func:`change_bit`, this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.


.. _`change_bit`:

change_bit
==========

.. c:function:: void change_bit (long nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to start counting from


.. _`change_bit.description`:

Description
-----------

:c:func:`change_bit` is atomic and may not be reordered.
Note that ``nr`` may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.


.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit (long nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from


.. _`test_and_set_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.


.. _`test_and_set_bit_lock`:

test_and_set_bit_lock
=====================

.. c:function:: int test_and_set_bit_lock (long nr, volatile unsigned long *addr)

    Set a bit and return its old value for lock

    :param long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from


.. _`test_and_set_bit_lock.description`:

Description
-----------

This is the same as test_and_set_bit on x86.


.. _`__test_and_set_bit`:

__test_and_set_bit
==================

.. c:function:: int __test_and_set_bit (long nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from


.. _`__test_and_set_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.


.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit (long nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to count from


.. _`test_and_clear_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.


.. _`__test_and_clear_bit`:

__test_and_clear_bit
====================

.. c:function:: int __test_and_clear_bit (long nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to count from


.. _`__test_and_clear_bit.description`:

Description
-----------

This operation is non-atomic and can be reordered.
If two examples of this operation race, one can appear to succeed
but actually fail.  You must protect multiple accesses with a lock.

Note: the operation is performed atomically with respect to
the local CPU, but not other CPUs. Portable code should not
rely on this behaviour.
KVM relies on this behaviour on x86 for modifying memory that is also
accessed from a hypervisor on the same CPU if running in a VM: don't change
this without also updating arch/x86/kernel/kvm.c


.. _`test_and_change_bit`:

test_and_change_bit
===================

.. c:function:: int test_and_change_bit (long nr, volatile unsigned long *addr)

    Change a bit and return its old value

    :param long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to count from


.. _`test_and_change_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.


.. _`test_bit`:

test_bit
========

.. c:function:: int test_bit (int nr, const volatile unsigned long *addr)

    Determine whether a bit is set

    :param int nr:
        bit number to test

    :param const volatile unsigned long \*addr:
        Address to start counting from


.. _`__ffs`:

__ffs
=====

.. c:function:: unsigned long __ffs (unsigned long word)

    find first set bit in word

    :param unsigned long word:
        The word to search


.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.


.. _`ffz`:

ffz
===

.. c:function:: unsigned long ffz (unsigned long word)

    find first zero bit in word

    :param unsigned long word:
        The word to search


.. _`ffz.description`:

Description
-----------

Undefined if no zero exists, so code should check against ~0UL first.


.. _`ffs`:

ffs
===

.. c:function:: int ffs (int x)

    find first set bit in word

    :param int x:
        the word to search


.. _`ffs.description`:

Description
-----------

This is defined the same way as the libc and compiler builtin ffs
routines, therefore differs in spirit from the other bitops.

ffs(value) returns 0 if value is 0 or the position of the first
set bit if value is nonzero. The first (least significant) bit
is at position 1.


.. _`fls`:

fls
===

.. c:function:: int fls (int x)

    find last set bit in word

    :param int x:
        the word to search


.. _`fls.description`:

Description
-----------

This is defined in a similar way as the libc and compiler builtin
ffs, but returns the position of the most significant set bit.

fls(value) returns 0 if value is 0 or the position of the last
set bit if value is nonzero. The last (most significant) bit is
at position 32.


.. _`fls64`:

fls64
=====

.. c:function:: int fls64 (__u64 x)

    find last set bit in a 64-bit word

    :param __u64 x:
        the word to search


.. _`fls64.description`:

Description
-----------

This is defined in a similar way as the libc and compiler builtin
ffsll, but returns the position of the most significant set bit.

fls64(value) returns 0 if value is 0 or the position of the last
set bit if value is nonzero. The last (most significant) bit is
at position 64.

