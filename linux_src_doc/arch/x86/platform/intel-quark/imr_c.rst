.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/platform/intel-quark/imr.c

.. _`pr_fmt`:

pr_fmt
======

.. c:function::  pr_fmt( fmt)

    - Intel Isolated Memory Region driver

    :param  fmt:
        *undescribed*

.. _`pr_fmt.description`:

Description
-----------

Copyright(c) 2013 Intel Corporation.
Copyright(c) 2015 Bryan O'Donoghue <pure.logic@nexus-software.ie>

IMR registers define an isolated region of memory that can
be masked to prohibit certain system agents from accessing memory.
When a device behind a masked port performs an access - snooped or
not, an IMR may optionally prevent that transaction from changing
the state of memory or from getting correct data in response to the
operation.

Write data will be dropped and reads will return 0xFFFFFFFF, the
system will reset and system BIOS will print out an error message to
inform the user that an IMR has been violated.

This code is based on the Linux MTRR code and reference code from
Intel's Quark BSP EFI, Linux and grub code.

See quark-x1000-datasheet.pdf for register definitions.
http://www.intel.com/content/dam/www/public/us/en/documents/datasheets/quark-x1000-datasheet.pdf

.. _`imr_is_enabled`:

imr_is_enabled
==============

.. c:function:: int imr_is_enabled(struct imr_regs *imr)

    true if an IMR is enabled false otherwise.

    :param struct imr_regs \*imr:
        pointer to IMR descriptor.

.. _`imr_is_enabled.description`:

Description
-----------

Determines if an IMR is enabled based on address range and read/write
mask. An IMR set with an address range set to zero and a read/write
access mask set to all is considered to be disabled. An IMR in any
other state - for example set to zero but without read/write access
all is considered to be enabled. This definition of disabled is how
firmware switches off an IMR and is maintained in kernel for
consistency.

.. _`imr_read`:

imr_read
========

.. c:function:: int imr_read(struct imr_device *idev, u32 imr_id, struct imr_regs *imr)

    read an IMR at a given index.

    :param struct imr_device \*idev:
        pointer to imr_device structure.

    :param u32 imr_id:
        IMR entry to read.

    :param struct imr_regs \*imr:
        IMR structure representing address and access masks.

.. _`imr_read.description`:

Description
-----------

Requires caller to hold imr mutex.

.. _`imr_write`:

imr_write
=========

.. c:function:: int imr_write(struct imr_device *idev, u32 imr_id, struct imr_regs *imr)

    write an IMR at a given index.

    :param struct imr_device \*idev:
        pointer to imr_device structure.

    :param u32 imr_id:
        IMR entry to write.

    :param struct imr_regs \*imr:
        IMR structure representing address and access masks.

.. _`imr_write.description`:

Description
-----------

Requires caller to hold imr mutex.
Note lock bits need to be written independently of address bits.

.. _`imr_dbgfs_state_show`:

imr_dbgfs_state_show
====================

.. c:function:: int imr_dbgfs_state_show(struct seq_file *s, void *unused)

    print state of IMR registers.

    :param struct seq_file \*s:
        pointer to seq_file for output.

    :param void \*unused:
        unused parameter.

.. _`imr_debugfs_register`:

imr_debugfs_register
====================

.. c:function:: int imr_debugfs_register(struct imr_device *idev)

    register debugfs hooks.

    :param struct imr_device \*idev:
        pointer to imr_device structure.

.. _`imr_check_params`:

imr_check_params
================

.. c:function:: int imr_check_params(phys_addr_t base, size_t size)

    check passed address range IMR alignment and non-zero size

    :param phys_addr_t base:
        base address of intended IMR.

    :param size_t size:
        size of intended IMR.

.. _`imr_raw_size`:

imr_raw_size
============

.. c:function:: size_t imr_raw_size(size_t size)

    account for the IMR_ALIGN bytes that addr_hi appends.

    :param size_t size:
        input size bytes.

.. _`imr_raw_size.description`:

Description
-----------

IMR addr_hi has a built in offset of plus IMR_ALIGN (0x400) bytes from the
value in the register. We need to subtract IMR_ALIGN bytes from input sizes
as a result.

.. _`imr_address_overlap`:

imr_address_overlap
===================

.. c:function:: int imr_address_overlap(phys_addr_t addr, struct imr_regs *imr)

    detects an address overlap.

    :param phys_addr_t addr:
        address to check against an existing IMR.

    :param struct imr_regs \*imr:
        imr being checked.

.. _`imr_add_range`:

imr_add_range
=============

.. c:function:: int imr_add_range(phys_addr_t base, size_t size, unsigned int rmask, unsigned int wmask)

    add an Isolated Memory Region.

    :param phys_addr_t base:
        physical base address of region aligned to 1KiB.

    :param size_t size:
        physical size of region in bytes must be aligned to 1KiB.

    :param unsigned int rmask:
        *undescribed*

    :param unsigned int wmask:
        *undescribed*

.. _`__imr_remove_range`:

\__imr_remove_range
===================

.. c:function:: int __imr_remove_range(int reg, phys_addr_t base, size_t size)

    delete an Isolated Memory Region.

    :param int reg:
        imr index to remove.

    :param phys_addr_t base:
        physical base address of region aligned to 1 KiB.

    :param size_t size:
        physical size of region in bytes aligned to 1 KiB.

.. _`__imr_remove_range.description`:

Description
-----------

This function allows you to delete an IMR by its index specified by reg or
by address range specified by base and size respectively. If you specify an
index on its own the base and size parameters are ignored.
imr_remove_range(0, base, size); delete IMR at index 0 base/size ignored.
imr_remove_range(-1, base, size); delete IMR from base to base+size.

.. _`imr_remove_range`:

imr_remove_range
================

.. c:function:: int imr_remove_range(phys_addr_t base, size_t size)

    delete an Isolated Memory Region by address

    :param phys_addr_t base:
        physical base address of region aligned to 1 KiB.

    :param size_t size:
        physical size of region in bytes aligned to 1 KiB.

.. _`imr_remove_range.description`:

Description
-----------

This function allows you to delete an IMR by an address range specified
by base and size respectively.
imr_remove_range(base, size); delete IMR from base to base+size.

.. _`imr_clear`:

imr_clear
=========

.. c:function:: int imr_clear(int reg)

    delete an Isolated Memory Region by index

    :param int reg:
        imr index to remove.

.. _`imr_clear.description`:

Description
-----------

This function allows you to delete an IMR by an address range specified
by the index of the IMR. Useful for initial sanitization of the IMR
address map.
imr_ge(base, size); delete IMR from base to base+size.

.. _`imr_fixup_memmap`:

imr_fixup_memmap
================

.. c:function:: void imr_fixup_memmap(struct imr_device *idev)

    Tear down IMRs used during bootup.

    :param struct imr_device \*idev:
        pointer to imr_device structure.

.. _`imr_fixup_memmap.description`:

Description
-----------

BIOS and Grub both setup IMRs around compressed kernel, initrd memory
that need to be removed before the kernel hands out one of the IMR
encased addresses to a downstream DMA agent such as the SD or Ethernet.
IMRs on Galileo are setup to immediately reset the system on violation.
As a result if you're running a root filesystem from SD - you'll need
the boot-time IMRs torn down or you'll find seemingly random resets when
using your filesystem.

.. _`imr_init`:

imr_init
========

.. c:function:: int imr_init( void)

    entry point for IMR driver.

    :param  void:
        no arguments

.. _`imr_init.return`:

Return
------

-ENODEV for no IMR support 0 if good to go.

.. This file was automatic generated / don't edit.

