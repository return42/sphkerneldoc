.. -*- coding: utf-8; mode: rst -*-

=====
efi.h
=====


.. _`efi_range_is_wc`:

efi_range_is_wc
===============

.. c:function:: int efi_range_is_wc (unsigned long start, unsigned long len)

    check the WC bit on an address range

    :param unsigned long start:
        starting kvirt address

    :param unsigned long len:
        length of range



.. _`efi_range_is_wc.description`:

Description
-----------

Consult the EFI memory map and make sure it's ok to set this range WC.
Returns true or false.

