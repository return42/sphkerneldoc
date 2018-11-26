.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_dev.c

.. _`genwqe_open_files`:

genwqe_open_files
=================

.. c:function:: int genwqe_open_files(struct genwqe_dev *cd)

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_open_files.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`genwqe_open_files.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`genwqe_search_pin`:

genwqe_search_pin
=================

.. c:function:: struct dma_mapping *genwqe_search_pin(struct genwqe_file *cfile, unsigned long u_addr, unsigned int size, void **virt_addr)

    Search for the mapping for a userspace address

    :param cfile:
        Descriptor of opened file
    :type cfile: struct genwqe_file \*

    :param u_addr:
        User virtual address
    :type u_addr: unsigned long

    :param size:
        Size of buffer
    :type size: unsigned int

    :param virt_addr:
        *undescribed*
    :type virt_addr: void \*\*

.. _`genwqe_search_pin.return`:

Return
------

Pointer to the corresponding mapping NULL if not found

.. _`__genwqe_search_mapping`:

\__genwqe_search_mapping
========================

.. c:function:: struct dma_mapping *__genwqe_search_mapping(struct genwqe_file *cfile, unsigned long u_addr, unsigned int size, dma_addr_t *dma_addr, void **virt_addr)

    Search for the mapping for a userspace address

    :param cfile:
        descriptor of opened file
    :type cfile: struct genwqe_file \*

    :param u_addr:
        user virtual address
    :type u_addr: unsigned long

    :param size:
        size of buffer
    :type size: unsigned int

    :param dma_addr:
        DMA address to be updated
    :type dma_addr: dma_addr_t \*

    :param virt_addr:
        *undescribed*
    :type virt_addr: void \*\*

.. _`__genwqe_search_mapping.return`:

Return
------

Pointer to the corresponding mapping NULL if not found

.. _`genwqe_kill_fasync`:

genwqe_kill_fasync
==================

.. c:function:: int genwqe_kill_fasync(struct genwqe_dev *cd, int sig)

    Send signal to all processes with open GenWQE files

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

    :param sig:
        *undescribed*
    :type sig: int

.. _`genwqe_kill_fasync.description`:

Description
-----------

E.g. genwqe_send_signal(cd, SIGIO);

.. _`genwqe_open`:

genwqe_open
===========

.. c:function:: int genwqe_open(struct inode *inode, struct file *filp)

    file open

    :param inode:
        file system information
    :type inode: struct inode \*

    :param filp:
        file handle
    :type filp: struct file \*

.. _`genwqe_open.description`:

Description
-----------

This function is executed whenever an application calls
open("/dev/genwqe",..).

.. _`genwqe_open.return`:

Return
------

0 if successful or <0 if errors

.. _`genwqe_fasync`:

genwqe_fasync
=============

.. c:function:: int genwqe_fasync(int fd, struct file *filp, int mode)

    Setup process to receive SIGIO.

    :param fd:
        file descriptor
    :type fd: int

    :param filp:
        file handle
    :type filp: struct file \*

    :param mode:
        file mode
    :type mode: int

.. _`genwqe_fasync.sending-a-signal-is-working-as-following`:

Sending a signal is working as following
----------------------------------------


if (cdev->async_queue)
kill_fasync(&cdev->async_queue, SIGIO, POLL_IN);

Some devices also implement asynchronous notification to indicate
when the device can be written; in this case, of course,
kill_fasync must be called with a mode of POLL_OUT.

.. _`genwqe_release`:

genwqe_release
==============

.. c:function:: int genwqe_release(struct inode *inode, struct file *filp)

    file close

    :param inode:
        file system information
    :type inode: struct inode \*

    :param filp:
        file handle
    :type filp: struct file \*

.. _`genwqe_release.description`:

Description
-----------

This function is executed whenever an application calls 'close(fd_genwqe)'

.. _`genwqe_release.return`:

Return
------

always 0

.. _`genwqe_vma_close`:

genwqe_vma_close
================

.. c:function:: void genwqe_vma_close(struct vm_area_struct *vma)

    Called each time when vma is unmapped

    :param vma:
        *undescribed*
    :type vma: struct vm_area_struct \*

.. _`genwqe_vma_close.description`:

Description
-----------

Free memory which got allocated by GenWQE \ :c:func:`mmap`\ .

.. _`genwqe_mmap`:

genwqe_mmap
===========

.. c:function:: int genwqe_mmap(struct file *filp, struct vm_area_struct *vma)

    Provide contignous buffers to userspace

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param vma:
        *undescribed*
    :type vma: struct vm_area_struct \*

.. _`genwqe_mmap.description`:

Description
-----------

We use \ :c:func:`mmap`\  to allocate contignous buffers used for DMA
transfers. After the buffer is allocated we remap it to user-space
and remember a reference to our dma_mapping data structure, where
we store the associated DMA address and allocated size.

When we receive a DDCB execution request with the ATS bits set to
plain buffer, we lookup our dma_mapping list to find the
corresponding DMA address for the associated user-space address.

.. _`flash_block`:

FLASH_BLOCK
===========

.. c:function::  FLASH_BLOCK()

    Excute flash update (write image or CVPD)

.. _`flash_block.return`:

Return
------

0 if successful

.. _`ddcb_cmd_cleanup`:

ddcb_cmd_cleanup
================

.. c:function:: int ddcb_cmd_cleanup(struct genwqe_file *cfile, struct ddcb_requ *req)

    Remove dynamically created fixup entries

    :param cfile:
        *undescribed*
    :type cfile: struct genwqe_file \*

    :param req:
        *undescribed*
    :type req: struct ddcb_requ \*

.. _`ddcb_cmd_cleanup.description`:

Description
-----------

Only if there are any. Pinnings are not removed.

.. _`ddcb_cmd_fixups`:

ddcb_cmd_fixups
===============

.. c:function:: int ddcb_cmd_fixups(struct genwqe_file *cfile, struct ddcb_requ *req)

    Establish DMA fixups/sglists for user memory references

    :param cfile:
        *undescribed*
    :type cfile: struct genwqe_file \*

    :param req:
        *undescribed*
    :type req: struct ddcb_requ \*

.. _`ddcb_cmd_fixups.description`:

Description
-----------

Before the DDCB gets executed we need to handle the fixups. We
replace the user-space addresses with DMA addresses or do
additional setup work e.g. generating a scatter-gather list which
is used to describe the memory referred to in the fixup.

.. _`genwqe_execute_ddcb`:

genwqe_execute_ddcb
===================

.. c:function:: int genwqe_execute_ddcb(struct genwqe_file *cfile, struct genwqe_ddcb_cmd *cmd)

    Execute DDCB using userspace address fixups

    :param cfile:
        *undescribed*
    :type cfile: struct genwqe_file \*

    :param cmd:
        *undescribed*
    :type cmd: struct genwqe_ddcb_cmd \*

.. _`genwqe_execute_ddcb.description`:

Description
-----------

The code will build up the translation tables or lookup the
contignous memory allocation table to find the right translations
and DMA addresses.

.. _`genwqe_ioctl`:

genwqe_ioctl
============

.. c:function:: long genwqe_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    IO control

    :param filp:
        file handle
    :type filp: struct file \*

    :param cmd:
        command identifier (passed from user)
    :type cmd: unsigned int

    :param arg:
        argument (passed from user)
    :type arg: unsigned long

.. _`genwqe_ioctl.return`:

Return
------

0 success

.. _`genwqe_compat_ioctl`:

genwqe_compat_ioctl
===================

.. c:function:: long genwqe_compat_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    Compatibility ioctl

    :param filp:
        file pointer.
    :type filp: struct file \*

    :param cmd:
        command.
    :type cmd: unsigned int

    :param arg:
        user argument.
    :type arg: unsigned long

.. _`genwqe_compat_ioctl.description`:

Description
-----------

Called whenever a 32-bit process running under a 64-bit kernel
performs an ioctl on /dev/genwqe<n>_card.

.. _`genwqe_compat_ioctl.return`:

Return
------

zero on success or negative number on failure.

.. _`genwqe_device_create`:

genwqe_device_create
====================

.. c:function:: int genwqe_device_create(struct genwqe_dev *cd)

    Create and configure genwqe char device

    :param cd:
        genwqe device descriptor
    :type cd: struct genwqe_dev \*

.. _`genwqe_device_create.description`:

Description
-----------

This function must be called before we create any more genwqe
character devices, because it is allocating the major and minor
number which are supposed to be used by the client drivers.

.. _`genwqe_device_remove`:

genwqe_device_remove
====================

.. c:function:: int genwqe_device_remove(struct genwqe_dev *cd)

    Remove genwqe's char device

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_device_remove.description`:

Description
-----------

This function must be called after the client devices are removed
because it will free the major/minor number range for the genwqe
drivers.

This function must be robust enough to be called twice.

.. This file was automatic generated / don't edit.

