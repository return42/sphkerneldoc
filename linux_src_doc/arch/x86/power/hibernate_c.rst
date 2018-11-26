.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/power/hibernate.c

.. _`pfn_is_nosave`:

pfn_is_nosave
=============

.. c:function:: int pfn_is_nosave(unsigned long pfn)

    check if given pfn is in the 'nosave' section

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

.. _`get_e820_md5`:

get_e820_md5
============

.. c:function:: int get_e820_md5(struct e820_table *table, void *buf)

    calculate md5 according to given e820 table

    :param table:
        the e820 table to be calculated
    :type table: struct e820_table \*

    :param buf:
        the md5 result to be stored to
    :type buf: void \*

.. _`arch_hibernation_header_save`:

arch_hibernation_header_save
============================

.. c:function:: int arch_hibernation_header_save(void *addr, unsigned int max_size)

    populate the architecture specific part of a hibernation image header

    :param addr:
        address to save the data at
    :type addr: void \*

    :param max_size:
        *undescribed*
    :type max_size: unsigned int

.. _`arch_hibernation_header_restore`:

arch_hibernation_header_restore
===============================

.. c:function:: int arch_hibernation_header_restore(void *addr)

    read the architecture specific data from the hibernation image header

    :param addr:
        address to read the data from
    :type addr: void \*

.. This file was automatic generated / don't edit.

