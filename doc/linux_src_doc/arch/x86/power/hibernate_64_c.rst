.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/power/hibernate_64.c

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

