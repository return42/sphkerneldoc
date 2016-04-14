.. -*- coding: utf-8; mode: rst -*-

=============
genwqe_card.h
=============

.. _`genwqe_devname`:

GENWQE_DEVNAME
==============

.. c:function:: GENWQE_DEVNAME ()


.. _`genwqe_devname.description`:

Description
-----------


(C) Copyright IBM Corp. 2013

Author: Frank Haverkamp <haver\ ``linux``\ .vnet.ibm.com>
Author: Joerg-Stephan Vogt <jsvogt\ ``de``\ .ibm.com>
Author: Michael Jung <mijung\ ``gmx``\ .net>
Author: Michael Ruettger <michael\ ``ibmra``\ .de>

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



Definition
----------

.. code-block:: c

  struct genwqe_ddcb_cmd {
    union {unnamed_union};
  };



Members
-------

:``{unnamed_union}``:
    anonymous



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



Definition
----------

.. code-block:: c

  struct genwqe_mem {
    __u64 addr;
    __u64 size;
  };



Members
-------

:``addr``:
    virtual user space address

:``size``:
    size of the area pin/dma-map/unmap
    direction:      0: read/1: read and write



Description
-----------

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

