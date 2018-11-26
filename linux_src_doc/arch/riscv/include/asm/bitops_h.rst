.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/riscv/include/asm/bitops.h

.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit(int nr, volatile unsigned long *addr)

    Set a bit and return its old value

    :param nr:
        Bit to set
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`test_and_set_bit.description`:

Description
-----------

This operation may be reordered on other architectures than x86.

.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit(int nr, volatile unsigned long *addr)

    Clear a bit and return its old value

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`test_and_clear_bit.description`:

Description
-----------

This operation can be reordered on other architectures other than x86.

.. _`test_and_change_bit`:

test_and_change_bit
===================

.. c:function:: int test_and_change_bit(int nr, volatile unsigned long *addr)

    Change a bit and return its old value

    :param nr:
        Bit to change
    :type nr: int

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`test_and_change_bit.description`:

Description
-----------

This operation is atomic and cannot be reordered.
It also implies a memory barrier.

.. _`set_bit`:

set_bit
=======

.. c:function:: void set_bit(int nr, volatile unsigned long *addr)

    Atomically set a bit in memory

    :param nr:
        the bit to set
    :type nr: int

    :param addr:
        the address to start counting from
    :type addr: volatile unsigned long \*

.. _`set_bit.note`:

Note
----

there are no guarantees that this function will not be reordered
on non x86 architectures, so if you are writing portable code,
make sure not to rely on its reordering guarantees.

Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`clear_bit`:

clear_bit
=========

.. c:function:: void clear_bit(int nr, volatile unsigned long *addr)

    Clears a bit in memory

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: volatile unsigned long \*

.. _`clear_bit.note`:

Note
----

there are no guarantees that this function will not be reordered
on non x86 architectures, so if you are writing portable code,
make sure not to rely on its reordering guarantees.

.. _`change_bit`:

change_bit
==========

.. c:function:: void change_bit(int nr, volatile unsigned long *addr)

    Toggle a bit in memory

    :param nr:
        Bit to change
    :type nr: int

    :param addr:
        Address to start counting from
    :type addr: volatile unsigned long \*

.. _`change_bit.description`:

Description
-----------

\ :c:func:`change_bit`\   may be reordered on other architectures than x86.
Note that \ ``nr``\  may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.

.. _`test_and_set_bit_lock`:

test_and_set_bit_lock
=====================

.. c:function:: int test_and_set_bit_lock(unsigned long nr, volatile unsigned long *addr)

    Set a bit and return its old value, for lock

    :param nr:
        Bit to set
    :type nr: unsigned long

    :param addr:
        Address to count from
    :type addr: volatile unsigned long \*

.. _`test_and_set_bit_lock.description`:

Description
-----------

This operation is atomic and provides acquire barrier semantics.
It can be used to implement bit locks.

.. _`clear_bit_unlock`:

clear_bit_unlock
================

.. c:function:: void clear_bit_unlock(unsigned long nr, volatile unsigned long *addr)

    Clear a bit in memory, for unlock

    :param nr:
        the bit to set
    :type nr: unsigned long

    :param addr:
        the address to start counting from
    :type addr: volatile unsigned long \*

.. _`clear_bit_unlock.description`:

Description
-----------

This operation is atomic and provides release barrier semantics.

.. _`__clear_bit_unlock`:

\__clear_bit_unlock
===================

.. c:function:: void __clear_bit_unlock(unsigned long nr, volatile unsigned long *addr)

    Clear a bit in memory, for unlock

    :param nr:
        the bit to set
    :type nr: unsigned long

    :param addr:
        the address to start counting from
    :type addr: volatile unsigned long \*

.. _`__clear_bit_unlock.description`:

Description
-----------

This operation is like clear_bit_unlock, however it is not atomic.
It does provide release barrier semantics so it can be used to unlock
a bit lock, however it would only be used if no other CPU can modify
any bits in the memory until the lock is released (a good example is
if the bit lock itself protects access to the other bits in the word).

On RISC-V systems there seems to be no benefit to taking advantage of the
non-atomic property here: it's a lot more instructions and we still have to
provide release semantics anyway.

.. This file was automatic generated / don't edit.

