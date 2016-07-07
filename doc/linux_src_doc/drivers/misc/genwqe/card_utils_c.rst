.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_utils.c

.. _`__genwqe_writeq`:

__genwqe_writeq
===============

.. c:function:: int __genwqe_writeq(struct genwqe_dev *cd, u64 byte_offs, u64 val)

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param u64 byte_offs:
        *undescribed*

    :param u64 val:
        *undescribed*

.. _`__genwqe_writeq.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`__genwqe_writeq.author`:

Author
------

Frank Haverkamp <haver\ ``linux``\ .vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt\ ``de``\ .ibm.com>

Michael Jung <mijung\ ``gmx``\ .net>

Michael Ruettger <michael\ ``ibmra``\ .de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`__genwqe_readq`:

__genwqe_readq
==============

.. c:function:: u64 __genwqe_readq(struct genwqe_dev *cd, u64 byte_offs)

    Read 64-bit register

    :param struct genwqe_dev \*cd:
        genwqe device descriptor

    :param u64 byte_offs:
        offset within BAR

.. _`__genwqe_readq.return`:

Return
------

value from register

.. _`__genwqe_writel`:

__genwqe_writel
===============

.. c:function:: int __genwqe_writel(struct genwqe_dev *cd, u64 byte_offs, u32 val)

    Write 32-bit register

    :param struct genwqe_dev \*cd:
        genwqe device descriptor

    :param u64 byte_offs:
        byte offset within BAR

    :param u32 val:
        32-bit value

.. _`__genwqe_writel.return`:

Return
------

0 if success; < 0 if error

.. _`__genwqe_readl`:

__genwqe_readl
==============

.. c:function:: u32 __genwqe_readl(struct genwqe_dev *cd, u64 byte_offs)

    Read 32-bit register

    :param struct genwqe_dev \*cd:
        genwqe device descriptor

    :param u64 byte_offs:
        offset within BAR

.. _`__genwqe_readl.return`:

Return
------

Value from register

.. _`genwqe_read_app_id`:

genwqe_read_app_id
==================

.. c:function:: int genwqe_read_app_id(struct genwqe_dev *cd, char *app_name, int len)

    Extract app_id

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param char \*app_name:
        *undescribed*

    :param int len:
        *undescribed*

.. _`genwqe_read_app_id.description`:

Description
-----------

app_unitcfg need to be filled with valid data first

.. _`crc32_polynomial`:

CRC32_POLYNOMIAL
================

.. c:function::  CRC32_POLYNOMIAL()

    Prepare a lookup table for fast crc32 calculations

.. _`crc32_polynomial.description`:

Description
-----------

Existing kernel functions seem to use a different polynom,
therefore we could not use them here.

Genwqe's Polynomial = 0x20044009

.. _`genwqe_crc32`:

genwqe_crc32
============

.. c:function:: u32 genwqe_crc32(u8 *buff, size_t len, u32 init)

    Generate 32-bit crc as required for DDCBs

    :param u8 \*buff:
        pointer to data buffer

    :param size_t len:
        length of data for calculation

    :param u32 init:
        initial crc (0xffffffff at start)

.. _`genwqe_crc32.description`:

Description
-----------

polynomial = x^32 \* + x^29 + x^18 + x^14 + x^3 + 1 (0x20044009)

.. _`genwqe_crc32.example`:

Example
-------

.. code-block:: c

    4 bytes 0x01 0x02 0x03 0x04 with init=0xffffffff should
    result in a crc32 of 0xf33cb7d3.

    The existing kernel crc functions did not cover this polynom yet.


.. _`genwqe_crc32.return`:

Return
------

crc32 checksum.

.. _`genwqe_alloc_sync_sgl`:

genwqe_alloc_sync_sgl
=====================

.. c:function:: int genwqe_alloc_sync_sgl(struct genwqe_dev *cd, struct genwqe_sgl *sgl, void __user *user_addr, size_t user_size)

    Allocate memory for sgl and overlapping pages

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param struct genwqe_sgl \*sgl:
        *undescribed*

    :param void __user \*user_addr:
        *undescribed*

    :param size_t user_size:
        *undescribed*

.. _`genwqe_alloc_sync_sgl.description`:

Description
-----------

Allocates memory for sgl and overlapping pages. Pages which might
overlap other user-space memory blocks are being cached for DMAs,
such that we do not run into syncronization issues. Data is copied
from user-space into the cached pages.

.. _`genwqe_free_sync_sgl`:

genwqe_free_sync_sgl
====================

.. c:function:: int genwqe_free_sync_sgl(struct genwqe_dev *cd, struct genwqe_sgl *sgl)

    Free memory for sgl and overlapping pages

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param struct genwqe_sgl \*sgl:
        *undescribed*

.. _`genwqe_free_sync_sgl.description`:

Description
-----------

After the DMA transfer has been completed we free the memory for
the sgl and the cached pages. Data is being transfered from cached
pages into user-space buffers.

.. _`free_user_pages`:

free_user_pages
===============

.. c:function:: int free_user_pages(struct page **page_list, unsigned int nr_pages, int dirty)

    Give pinned pages back

    :param struct page \*\*page_list:
        *undescribed*

    :param unsigned int nr_pages:
        *undescribed*

    :param int dirty:
        *undescribed*

.. _`free_user_pages.description`:

Description
-----------

Documentation of get_user_pages is in mm/memory.c:

If the page is written to, set_page_dirty (or set_page_dirty_lock,
as appropriate) must be called after the page is finished with, and
before put_page is called.

FIXME Could be of use to others and might belong in the generic
code, if others agree. E.g.
ll_free_user_pages in drivers/staging/lustre/lustre/llite/rw26.c
ceph_put_page_vector in net/ceph/pagevec.c
maybe more?

.. _`genwqe_user_vmap`:

genwqe_user_vmap
================

.. c:function:: int genwqe_user_vmap(struct genwqe_dev *cd, struct dma_mapping *m, void *uaddr, unsigned long size, struct ddcb_requ *req)

    Map user-space memory to virtual kernel memory

    :param struct genwqe_dev \*cd:
        pointer to genwqe device

    :param struct dma_mapping \*m:
        mapping params

    :param void \*uaddr:
        user virtual address

    :param unsigned long size:
        size of memory to be mapped

    :param struct ddcb_requ \*req:
        *undescribed*

.. _`genwqe_user_vmap.description`:

Description
-----------

We need to think about how we could speed this up. Of course it is
not a good idea to do this over and over again, like we are
currently doing it. Nevertheless, I am curious where on the path
the performance is spend. Most probably within the memory
allocation functions, but maybe also in the DMA mapping code.

.. _`genwqe_user_vmap.restrictions`:

Restrictions
------------

The maximum size of the possible mapping currently depends
on the amount of memory we can get using \ :c:func:`kzalloc`\  for the
page_list and pci_alloc_consistent for the sg_list.
The sg_list is currently itself not scattered, which could
be fixed with some effort. The page_list must be split into
PAGE_SIZE chunks too. All that will make the complicated
code more complicated.

.. _`genwqe_user_vmap.return`:

Return
------

0 if success

.. _`genwqe_user_vunmap`:

genwqe_user_vunmap
==================

.. c:function:: int genwqe_user_vunmap(struct genwqe_dev *cd, struct dma_mapping *m, struct ddcb_requ *req)

    Undo mapping of user-space mem to virtual kernel memory

    :param struct genwqe_dev \*cd:
        pointer to genwqe device

    :param struct dma_mapping \*m:
        mapping params

    :param struct ddcb_requ \*req:
        *undescribed*

.. _`genwqe_card_type`:

genwqe_card_type
================

.. c:function:: u8 genwqe_card_type(struct genwqe_dev *cd)

    Get chip type SLU Configuration Register

    :param struct genwqe_dev \*cd:
        pointer to the genwqe device descriptor

.. _`genwqe_card_type.return`:

Return
------

0: Altera Stratix-IV 230
1: Altera Stratix-IV 530
2: Altera Stratix-V A4
3: Altera Stratix-V A7

.. _`genwqe_card_reset`:

genwqe_card_reset
=================

.. c:function:: int genwqe_card_reset(struct genwqe_dev *cd)

    Reset the card

    :param struct genwqe_dev \*cd:
        pointer to the genwqe device descriptor

.. _`genwqe_set_interrupt_capability`:

genwqe_set_interrupt_capability
===============================

.. c:function:: int genwqe_set_interrupt_capability(struct genwqe_dev *cd, int count)

    Configure MSI capability structure

    :param struct genwqe_dev \*cd:
        pointer to the device

    :param int count:
        *undescribed*

.. _`genwqe_set_interrupt_capability.return`:

Return
------

0 if no error

.. _`genwqe_reset_interrupt_capability`:

genwqe_reset_interrupt_capability
=================================

.. c:function:: void genwqe_reset_interrupt_capability(struct genwqe_dev *cd)

    Undo \ :c:func:`genwqe_set_interrupt_capability`\ 

    :param struct genwqe_dev \*cd:
        pointer to the device

.. _`set_reg_idx`:

set_reg_idx
===========

.. c:function:: int set_reg_idx(struct genwqe_dev *cd, struct genwqe_reg *r, unsigned int *i, unsigned int m, u32 addr, u32 idx, u64 val)

    Fill array with data. Ignore illegal offsets.

    :param struct genwqe_dev \*cd:
        card device

    :param struct genwqe_reg \*r:
        debug register array

    :param unsigned int \*i:
        index to desired entry

    :param unsigned int m:
        maximum possible entries

    :param u32 addr:
        addr which is read

    :param u32 idx:
        *undescribed*

    :param u64 val:
        read value

.. _`genwqe_ffdc_buff_size`:

genwqe_ffdc_buff_size
=====================

.. c:function:: int genwqe_ffdc_buff_size(struct genwqe_dev *cd, int uid)

    Calculates the number of dump registers

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param int uid:
        *undescribed*

.. _`genwqe_ffdc_buff_read`:

genwqe_ffdc_buff_read
=====================

.. c:function:: int genwqe_ffdc_buff_read(struct genwqe_dev *cd, int uid, struct genwqe_reg *regs, unsigned int max_regs)

    Implements LogoutExtendedErrorRegisters procedure

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param int uid:
        *undescribed*

    :param struct genwqe_reg \*regs:
        *undescribed*

    :param unsigned int max_regs:
        *undescribed*

.. _`genwqe_write_vreg`:

genwqe_write_vreg
=================

.. c:function:: int genwqe_write_vreg(struct genwqe_dev *cd, u32 reg, u64 val, int func)

    Write register in virtual window

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param u32 reg:
        *undescribed*

    :param u64 val:
        *undescribed*

    :param int func:
        *undescribed*

.. _`genwqe_write_vreg.description`:

Description
-----------

Note, these registers are only accessible to the PF through the
VF-window. It is not intended for the VF to access.

.. _`genwqe_read_vreg`:

genwqe_read_vreg
================

.. c:function:: u64 genwqe_read_vreg(struct genwqe_dev *cd, u32 reg, int func)

    Read register in virtual window

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param u32 reg:
        *undescribed*

    :param int func:
        *undescribed*

.. _`genwqe_read_vreg.description`:

Description
-----------

Note, these registers are only accessible to the PF through the
VF-window. It is not intended for the VF to access.

.. _`genwqe_base_clock_frequency`:

genwqe_base_clock_frequency
===========================

.. c:function:: int genwqe_base_clock_frequency(struct genwqe_dev *cd)

    Deteremine base clock frequency of the card

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_base_clock_frequency.note`:

Note
----

From a design perspective it turned out to be a bad idea to
use codes here to specifiy the frequency/speed values. An old
driver cannot understand new codes and is therefore always a
problem. Better is to measure out the value or put the
speed/frequency directly into a register which is always a valid
value for old as well as for new software.

.. _`genwqe_base_clock_frequency.return`:

Return
------

Card clock in MHz

.. _`genwqe_stop_traps`:

genwqe_stop_traps
=================

.. c:function:: void genwqe_stop_traps(struct genwqe_dev *cd)

    Stop traps

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_stop_traps.description`:

Description
-----------

Before reading out the analysis data, we need to stop the traps.

.. _`genwqe_start_traps`:

genwqe_start_traps
==================

.. c:function:: void genwqe_start_traps(struct genwqe_dev *cd)

    Start traps

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_start_traps.description`:

Description
-----------

After having read the data, we can/must enable the traps again.

.. This file was automatic generated / don't edit.

