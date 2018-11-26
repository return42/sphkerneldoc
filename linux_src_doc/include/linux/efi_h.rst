.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/efi.h

.. _`for_each_efi_memory_desc`:

for_each_efi_memory_desc
========================

.. c:function::  for_each_efi_memory_desc( md)

    iterate over descriptors in efi.memmap

    :param md:
        the efi_memory_desc_t \* iterator
    :type md: 

.. _`for_each_efi_memory_desc.description`:

Description
-----------

Once the loop finishes \ ``md``\  must not be accessed.

.. _`efi_range_is_wc`:

efi_range_is_wc
===============

.. c:function:: int efi_range_is_wc(unsigned long start, unsigned long len)

    check the WC bit on an address range

    :param start:
        starting kvirt address
    :type start: unsigned long

    :param len:
        length of range
    :type len: unsigned long

.. _`efi_range_is_wc.description`:

Description
-----------

Consult the EFI memory map and make sure it's ok to set this range WC.
Returns true or false.

.. This file was automatic generated / don't edit.

