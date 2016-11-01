.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/efi.c

.. _`efi_mem_reserve`:

efi_mem_reserve
===============

.. c:function:: void efi_mem_reserve(phys_addr_t addr, u64 size)

    Reserve an EFI memory region

    :param phys_addr_t addr:
        Physical address to reserve

    :param u64 size:
        Size of reservation

.. _`efi_mem_reserve.description`:

Description
-----------

Mark a region as reserved from general kernel allocation and
prevent it being released by \ :c:func:`efi_free_boot_services`\ .

This function should be called drivers once they've parsed EFI
configuration tables to figure out where their data lives, e.g.
\ :c:func:`efi_esrt_init`\ .

.. This file was automatic generated / don't edit.

