.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/include/asm/bitops.h

.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit(int nr, volatile void *addr)

    clear a bit and return its old value

    :param nr:
        bit number to clear
    :type nr: int

    :param addr:
        pointer to memory
    :type addr: volatile void \*

.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit(int nr, volatile void *addr)

    set a bit and return its old value

    :param nr:
        bit number to set
    :type nr: int

    :param addr:
        pointer to memory
    :type addr: volatile void \*

.. _`test_and_change_bit`:

test_and_change_bit
===================

.. c:function:: int test_and_change_bit(int nr, volatile void *addr)

    toggle a bit and return its old value

    :param nr:
        bit number to set
    :type nr: int

    :param addr:
        pointer to memory
    :type addr: volatile void \*

.. This file was automatic generated / don't edit.

