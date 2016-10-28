.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/lib/bitops.c

.. _`__mips_set_bit`:

__mips_set_bit
==============

.. c:function:: void __mips_set_bit(unsigned long nr, volatile unsigned long *addr)

    Atomically set a bit in memory.  This is called by \ :c:func:`set_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        the bit to set

    :param volatile unsigned long \*addr:
        the address to start counting from

.. _`__mips_clear_bit`:

__mips_clear_bit
================

.. c:function:: void __mips_clear_bit(unsigned long nr, volatile unsigned long *addr)

    Clears a bit in memory.  This is called by \ :c:func:`clear_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`__mips_change_bit`:

__mips_change_bit
=================

.. c:function:: void __mips_change_bit(unsigned long nr, volatile unsigned long *addr)

    Toggle a bit in memory.  This is called by \ :c:func:`change_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to start counting from

.. _`__mips_test_and_set_bit`:

__mips_test_and_set_bit
=======================

.. c:function:: int __mips_test_and_set_bit(unsigned long nr, volatile unsigned long *addr)

    Set a bit and return its old value.  This is called by \ :c:func:`test_and_set_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from

.. _`__mips_test_and_set_bit_lock`:

__mips_test_and_set_bit_lock
============================

.. c:function:: int __mips_test_and_set_bit_lock(unsigned long nr, volatile unsigned long *addr)

    Set a bit and return its old value.  This is called by \ :c:func:`test_and_set_bit_lock`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to set

    :param volatile unsigned long \*addr:
        Address to count from

.. _`__mips_test_and_clear_bit`:

__mips_test_and_clear_bit
=========================

.. c:function:: int __mips_test_and_clear_bit(unsigned long nr, volatile unsigned long *addr)

    Clear a bit and return its old value.  This is called by \ :c:func:`test_and_clear_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to clear

    :param volatile unsigned long \*addr:
        Address to count from

.. _`__mips_test_and_change_bit`:

__mips_test_and_change_bit
==========================

.. c:function:: int __mips_test_and_change_bit(unsigned long nr, volatile unsigned long *addr)

    Change a bit and return its old value.  This is called by \ :c:func:`test_and_change_bit`\  if it cannot find a faster solution.

    :param unsigned long nr:
        Bit to change

    :param volatile unsigned long \*addr:
        Address to count from

.. This file was automatic generated / don't edit.

