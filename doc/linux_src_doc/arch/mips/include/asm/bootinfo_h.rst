.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/bootinfo.h

.. _`plat_get_fdt`:

plat_get_fdt
============

.. c:function:: void *plat_get_fdt( void)

    Return a pointer to the platform's device tree blob

    :param  void:
        no arguments

.. _`plat_get_fdt.description`:

Description
-----------

This function provides a platform independent API to get a pointer to the
flattened device tree blob. The interface between bootloader and kernel
is not consistent across platforms so it is necessary to provide this
API such that common startup code can locate the FDT.

This is used by the KASLR code to get command line arguments and random
seed from the device tree. Any platform wishing to use KASLR should
provide this API and select SYS_SUPPORTS_RELOCATABLE.

.. _`plat_get_fdt.return`:

Return
------

Pointer to the flattened device tree blob.

.. This file was automatic generated / don't edit.

