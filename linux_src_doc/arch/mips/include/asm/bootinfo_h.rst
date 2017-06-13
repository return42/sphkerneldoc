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

.. _`plat_fdt_relocated`:

plat_fdt_relocated
==================

.. c:function:: void plat_fdt_relocated(void *new_location)

    Update platform's information about relocated dtb

    :param void \*new_location:
        *undescribed*

.. _`plat_fdt_relocated.description`:

Description
-----------

This function provides a platform-independent API to set platform's
information about relocated DTB if it needs to be moved due to kernel
relocation occurring at boot.

.. This file was automatic generated / don't edit.

