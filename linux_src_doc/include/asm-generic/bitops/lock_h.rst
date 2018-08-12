.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/bitops/lock.h

.. _`test_and_set_bit_lock`:

test_and_set_bit_lock
=====================

.. c:function::  test_and_set_bit_lock( nr,  addr)

    Set a bit and return its old value, for lock

    :param  nr:
        Bit to set

    :param  addr:
        Address to count from

.. _`test_and_set_bit_lock.description`:

Description
-----------

This operation is atomic and provides acquire barrier semantics if
the returned value is 0.
It can be used to implement bit locks.

.. _`clear_bit_unlock`:

clear_bit_unlock
================

.. c:function::  clear_bit_unlock( nr,  addr)

    Clear a bit in memory, for unlock

    :param  nr:
        the bit to set

    :param  addr:
        the address to start counting from

.. _`clear_bit_unlock.description`:

Description
-----------

This operation is atomic and provides release barrier semantics.

.. _`__clear_bit_unlock`:

\__clear_bit_unlock
===================

.. c:function::  __clear_bit_unlock( nr,  addr)

    Clear a bit in memory, for unlock

    :param  nr:
        the bit to set

    :param  addr:
        the address to start counting from

.. _`__clear_bit_unlock.description`:

Description
-----------

A weaker form of \ :c:func:`clear_bit_unlock`\  as used by \__bit_lock_unlock(). If all
the bits in the word are protected by this lock some archs can use weaker
ops to safely unlock.

See for example x86's implementation.

.. This file was automatic generated / don't edit.

