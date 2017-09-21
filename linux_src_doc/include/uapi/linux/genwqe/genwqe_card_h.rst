.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/genwqe/genwqe_card.h

.. _`genwqe_devname`:

GENWQE_DEVNAME
==============

.. c:function::  GENWQE_DEVNAME()

.. _`genwqe_devname.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`genwqe_devname.author`:

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

.. _`genwqe_ddcb_cmd`:

struct genwqe_ddcb_cmd
======================

.. c:type:: struct genwqe_ddcb_cmd

    User parameter for generic DDCB commands

.. _`genwqe_ddcb_cmd.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_ddcb_cmd {
        __u64 next_addr;
        __u64 flags;
        __u8 acfunc;
        __u8 cmd;
        __u8 asiv_length;
        __u8 asv_length;
        __u16 cmdopts;
        __u16 retc;
        __u16 attn;
        __u16 vcrc;
        __u32 progress;
        __u64 deque_ts;
        __u64 cmplt_ts;
        __u64 disp_ts;
        __u64 ddata_addr;
        __u8 asv;
        union {unnamed_union};
        __u8 __asiv;
         };
    }

.. _`genwqe_ddcb_cmd.members`:

Members
-------

next_addr
    *undescribed*

flags
    *undescribed*

acfunc
    *undescribed*

cmd
    *undescribed*

asiv_length
    *undescribed*

asv_length
    *undescribed*

cmdopts
    *undescribed*

retc
    *undescribed*

attn
    *undescribed*

vcrc
    *undescribed*

progress
    *undescribed*

deque_ts
    *undescribed*

cmplt_ts
    *undescribed*

disp_ts
    *undescribed*

ddata_addr
    *undescribed*

asv
    *undescribed*

{unnamed_union}
    anonymous


__asiv
    *undescribed*

}
    *undescribed*

.. _`genwqe_ddcb_cmd.description`:

Description
-----------

On the way into the kernel the driver will read the whole data
structure. On the way out the driver will not copy the ASIV data
back to user-space.

.. _`genwqe_mem`:

struct genwqe_mem
=================

.. c:type:: struct genwqe_mem

    Memory pinning/unpinning information

.. _`genwqe_mem.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_mem {
        __u64 addr;
        __u64 size;
        __u64 direction;
        __u64 flags;
    }

.. _`genwqe_mem.members`:

Members
-------

addr
    virtual user space address

size
    size of the area pin/dma-map/unmap

direction
    *undescribed*

flags
    *undescribed*

.. _`genwqe_mem.direction`:

direction
---------

0: read/1: read and write

Avoid pinning and unpinning of memory pages dynamically. Instead
the idea is to pin the whole buffer space required for DDCB
opertionas in advance. The driver will reuse this pinning and the
memory associated with it to setup the sglists for the DDCB
requests without the need to allocate and free memory or map and
unmap to get the DMA addresses.

The inverse operation needs to be called after the pinning is not
needed anymore. The pinnings else the pinnings will get removed
after the device is closed. Note that pinnings will required
memory.

.. This file was automatic generated / don't edit.

