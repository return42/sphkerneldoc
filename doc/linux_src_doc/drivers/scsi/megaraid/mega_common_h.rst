.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/mega_common.h

.. _`mraid_get_device_map`:

MRAID_GET_DEVICE_MAP
====================

.. c:function::  MRAID_GET_DEVICE_MAP( adp,  scp,  p_chan,  target,  islogical)

    device ids

    :param  adp:
        adapter's soft state

    :param  scp:
        mid-layer scsi command pointer

    :param  p_chan:
        physical channel on the controller

    :param  target:
        target id of the device or logical drive number

    :param  islogical:
        set if the command is for the logical drive

.. _`mraid_get_device_map.description`:

Description
-----------

Macro to retrieve information about device class, logical or physical and
the corresponding physical channel and target or logical drive number

.. _`mraid_pci_blk`:

struct mraid_pci_blk
====================

.. c:type:: struct mraid_pci_blk

    structure holds DMA memory block info

.. _`mraid_pci_blk.definition`:

Definition
----------

.. code-block:: c

    struct mraid_pci_blk {
        caddr_t vaddr;
        dma_addr_t dma_addr;
    }

.. _`mraid_pci_blk.members`:

Members
-------

vaddr
    virtual address to a memory block

dma_addr
    DMA handle to a memory block

.. _`mraid_pci_blk.description`:

Description
-----------

This structure is filled up for the caller. It is the responsibilty of the
caller to allocate this array big enough to store addresses for all
requested elements

.. This file was automatic generated / don't edit.

