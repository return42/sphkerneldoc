.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/bitops/lock.h

.. _`test_and_set_bit_lock`:

test_and_set_bit_lock
=====================

.. c:function:: int test_and_set_bit_lock(unsigned int nr, volatile unsigned long *p)

    Set a bit and return its old value, for lock

    :param nr:
        Bit to set
    :type nr: unsigned int

    :param p:
        *undescribed*
    :type p: volatile unsigned long \*

.. _`test_and_set_bit_lock.description`:

Description
-----------

This operation is atomic and provides acquire barrier semantics if
the returned value is 0.
It can be used to implement bit locks.

.. _`clear_bit_unlock`:

clear_bit_unlock
================

.. c:function:: void clear_bit_unlock(unsigned int nr, volatile unsigned long *p)

    Clear a bit in memory, for unlock

    :param nr:
        the bit to set
    :type nr: unsigned int

    :param p:
        *undescribed*
    :type p: volatile unsigned long \*

.. _`clear_bit_unlock.description`:

Description
-----------

This operation is atomic and provides release barrier semantics.

.. _`__clear_bit_unlock`:

\__clear_bit_unlock
===================

.. c:function:: void __clear_bit_unlock(unsigned int nr, volatile unsigned long *p)

    Clear a bit in memory, for unlock

    :param nr:
        the bit to set
    :type nr: unsigned int

    :param p:
        *undescribed*
    :type p: volatile unsigned long \*

.. _`__clear_bit_unlock.description`:

Description
-----------

A weaker form of \ :c:func:`clear_bit_unlock`\  as used by \__bit_lock_unlock(). If all
the bits in the word are protected by this lock some archs can use weaker
ops to safely unlock.

See for example x86's implementation.

.. _`clear_bit_unlock_is_negative_byte`:

clear_bit_unlock_is_negative_byte
=================================

.. c:function:: bool clear_bit_unlock_is_negative_byte(unsigned int nr, volatile unsigned long *p)

    Clear a bit in memory and test if bottom byte is negative, for unlock.

    :param nr:
        the bit to clear
    :type nr: unsigned int

    :param p:
        *undescribed*
    :type p: volatile unsigned long \*

.. _`clear_bit_unlock_is_negative_byte.description`:

Description
-----------

This is a bit of a one-trick-pony for the filemap code, which clears
PG_locked and tests PG_waiters,

.. This file was automatic generated / don't edit.

