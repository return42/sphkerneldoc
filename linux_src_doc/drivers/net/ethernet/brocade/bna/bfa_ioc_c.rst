.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/brocade/bna/bfa_ioc.c

.. _`bfa_nw_ioc_fwver_cmp`:

bfa_nw_ioc_fwver_cmp
====================

.. c:function:: bool bfa_nw_ioc_fwver_cmp(struct bfa_ioc *ioc, struct bfi_ioc_image_hdr *fwhdr)

    :param ioc:
        *undescribed*
    :type ioc: struct bfa_ioc \*

    :param fwhdr:
        *undescribed*
    :type fwhdr: struct bfi_ioc_image_hdr \*

.. _`bfa_nw_ioc_smem_read`:

bfa_nw_ioc_smem_read
====================

.. c:function:: int bfa_nw_ioc_smem_read(struct bfa_ioc *ioc, void *tbuf, u32 soff, u32 sz)

    Read data from SMEM to host through PCI memmap

    :param ioc:
        memory for IOC
    :type ioc: struct bfa_ioc \*

    :param tbuf:
        app memory to store data from smem
    :type tbuf: void \*

    :param soff:
        smem offset
    :type soff: u32

    :param sz:
        size of smem in bytes
    :type sz: u32

.. _`bfa_nw_ioc_attach`:

bfa_nw_ioc_attach
=================

.. c:function:: void bfa_nw_ioc_attach(struct bfa_ioc *ioc, void *bfa, struct bfa_ioc_cbfn *cbfn)

    IOC attach time initialization and setup.

    :param ioc:
        memory for IOC
    :type ioc: struct bfa_ioc \*

    :param bfa:
        driver instance structure
    :type bfa: void \*

    :param cbfn:
        *undescribed*
    :type cbfn: struct bfa_ioc_cbfn \*

.. _`bfa_nw_ioc_pci_init`:

bfa_nw_ioc_pci_init
===================

.. c:function:: void bfa_nw_ioc_pci_init(struct bfa_ioc *ioc, struct bfa_pcidev *pcidev, enum bfi_pcifn_class clscode)

    Setup IOC PCI properties.

    :param ioc:
        *undescribed*
    :type ioc: struct bfa_ioc \*

    :param pcidev:
        PCI device information for this IOC
    :type pcidev: struct bfa_pcidev \*

    :param clscode:
        *undescribed*
    :type clscode: enum bfi_pcifn_class

.. _`bfa_nw_ioc_mem_claim`:

bfa_nw_ioc_mem_claim
====================

.. c:function:: void bfa_nw_ioc_mem_claim(struct bfa_ioc *ioc, u8 *dm_kva, u64 dm_pa)

    Initialize IOC dma memory

    :param ioc:
        *undescribed*
    :type ioc: struct bfa_ioc \*

    :param dm_kva:
        kernel virtual address of IOC dma memory
    :type dm_kva: u8 \*

    :param dm_pa:
        physical address of IOC dma memory
    :type dm_pa: u64

.. _`bfa_nw_ioc_mbox_queue`:

bfa_nw_ioc_mbox_queue
=====================

.. c:function:: bool bfa_nw_ioc_mbox_queue(struct bfa_ioc *ioc, struct bfa_mbox_cmd *cmd, bfa_mbox_cmd_cbfn_t cbfn, void *cbarg)

    Queue a mailbox command request to firmware.

    :param ioc:
        IOC instance
    :type ioc: struct bfa_ioc \*

    :param cmd:
        Mailbox command
    :type cmd: struct bfa_mbox_cmd \*

    :param cbfn:
        *undescribed*
    :type cbfn: bfa_mbox_cmd_cbfn_t

    :param cbarg:
        *undescribed*
    :type cbarg: void \*

.. _`bfa_nw_ioc_mbox_queue.description`:

Description
-----------

Waits if mailbox is busy. Responsibility of caller to serialize

.. _`bfa_flash_read_send`:

bfa_flash_read_send
===================

.. c:function:: void bfa_flash_read_send(void *cbarg)

    Send flash read request.

    :param cbarg:
        callback argument
    :type cbarg: void \*

.. _`bfa_flash_intr`:

bfa_flash_intr
==============

.. c:function:: void bfa_flash_intr(void *flasharg, struct bfi_mbmsg *msg)

    Process flash response messages upon receiving interrupts.

    :param flasharg:
        flash structure
    :type flasharg: void \*

    :param msg:
        message structure
    :type msg: struct bfi_mbmsg \*

.. _`bfa_nw_flash_attach`:

bfa_nw_flash_attach
===================

.. c:function:: void bfa_nw_flash_attach(struct bfa_flash *flash, struct bfa_ioc *ioc, void *dev)

    Flash attach API.

    :param flash:
        flash structure
    :type flash: struct bfa_flash \*

    :param ioc:
        ioc structure
    :type ioc: struct bfa_ioc \*

    :param dev:
        device structure
    :type dev: void \*

.. _`bfa_nw_flash_memclaim`:

bfa_nw_flash_memclaim
=====================

.. c:function:: void bfa_nw_flash_memclaim(struct bfa_flash *flash, u8 *dm_kva, u64 dm_pa)

    Claim memory for flash

    :param flash:
        flash structure
    :type flash: struct bfa_flash \*

    :param dm_kva:
        pointer to virtual memory address
    :type dm_kva: u8 \*

    :param dm_pa:
        physical memory address
    :type dm_pa: u64

.. _`bfa_nw_flash_get_attr`:

bfa_nw_flash_get_attr
=====================

.. c:function:: enum bfa_status bfa_nw_flash_get_attr(struct bfa_flash *flash, struct bfa_flash_attr *attr, bfa_cb_flash cbfn, void *cbarg)

    Get flash attribute.

    :param flash:
        flash structure
    :type flash: struct bfa_flash \*

    :param attr:
        flash attribute structure
    :type attr: struct bfa_flash_attr \*

    :param cbfn:
        callback function
    :type cbfn: bfa_cb_flash

    :param cbarg:
        callback argument
    :type cbarg: void \*

.. _`bfa_nw_flash_get_attr.description`:

Description
-----------

Return status.

.. _`bfa_nw_flash_update_part`:

bfa_nw_flash_update_part
========================

.. c:function:: enum bfa_status bfa_nw_flash_update_part(struct bfa_flash *flash, u32 type, u8 instance, void *buf, u32 len, u32 offset, bfa_cb_flash cbfn, void *cbarg)

    Update flash partition.

    :param flash:
        flash structure
    :type flash: struct bfa_flash \*

    :param type:
        flash partition type
    :type type: u32

    :param instance:
        flash partition instance
    :type instance: u8

    :param buf:
        update data buffer
    :type buf: void \*

    :param len:
        data buffer length
    :type len: u32

    :param offset:
        offset relative to the partition starting address
    :type offset: u32

    :param cbfn:
        callback function
    :type cbfn: bfa_cb_flash

    :param cbarg:
        callback argument
    :type cbarg: void \*

.. _`bfa_nw_flash_update_part.description`:

Description
-----------

Return status.

.. _`bfa_nw_flash_read_part`:

bfa_nw_flash_read_part
======================

.. c:function:: enum bfa_status bfa_nw_flash_read_part(struct bfa_flash *flash, u32 type, u8 instance, void *buf, u32 len, u32 offset, bfa_cb_flash cbfn, void *cbarg)

    Read flash partition.

    :param flash:
        flash structure
    :type flash: struct bfa_flash \*

    :param type:
        flash partition type
    :type type: u32

    :param instance:
        flash partition instance
    :type instance: u8

    :param buf:
        read data buffer
    :type buf: void \*

    :param len:
        data buffer length
    :type len: u32

    :param offset:
        offset relative to the partition starting address
    :type offset: u32

    :param cbfn:
        callback function
    :type cbfn: bfa_cb_flash

    :param cbarg:
        callback argument
    :type cbarg: void \*

.. _`bfa_nw_flash_read_part.description`:

Description
-----------

Return status.

.. This file was automatic generated / don't edit.

