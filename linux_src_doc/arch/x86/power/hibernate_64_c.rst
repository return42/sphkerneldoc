.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/power/hibernate_64.c

.. _`get_e820_md5`:

get_e820_md5
============

.. c:function:: int get_e820_md5(struct e820_table *table, void *buf)

    calculate md5 according to given e820 table

    :param struct e820_table \*table:
        the e820 table to be calculated

    :param void \*buf:
        the md5 result to be stored to

.. _`arch_hibernation_header_save`:

arch_hibernation_header_save
============================

.. c:function:: int arch_hibernation_header_save(void *addr, unsigned int max_size)

    populate the architecture specific part of a hibernation image header

    :param void \*addr:
        address to save the data at

    :param unsigned int max_size:
        *undescribed*

.. _`arch_hibernation_header_restore`:

arch_hibernation_header_restore
===============================

.. c:function:: int arch_hibernation_header_restore(void *addr)

    read the architecture specific data from the hibernation image header

    :param void \*addr:
        address to read the data from

.. This file was automatic generated / don't edit.

