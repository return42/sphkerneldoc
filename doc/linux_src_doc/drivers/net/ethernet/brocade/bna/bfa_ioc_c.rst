.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/brocade/bna/bfa_ioc.c

.. _`bfa_nw_ioc_fwver_cmp`:

bfa_nw_ioc_fwver_cmp
====================

.. c:function:: bool bfa_nw_ioc_fwver_cmp(struct bfa_ioc *ioc, struct bfi_ioc_image_hdr *fwhdr)

    :param struct bfa_ioc \*ioc:
        *undescribed*

    :param struct bfi_ioc_image_hdr \*fwhdr:
        *undescribed*

.. _`bfa_nw_ioc_smem_read`:

bfa_nw_ioc_smem_read
====================

.. c:function:: int bfa_nw_ioc_smem_read(struct bfa_ioc *ioc, void *tbuf, u32 soff, u32 sz)

    Read data from SMEM to host through PCI memmap

    :param struct bfa_ioc \*ioc:
        memory for IOC

    :param void \*tbuf:
        app memory to store data from smem

    :param u32 soff:
        smem offset

    :param u32 sz:
        size of smem in bytes

.. _`bfa_nw_ioc_attach`:

bfa_nw_ioc_attach
=================

.. c:function:: void bfa_nw_ioc_attach(struct bfa_ioc *ioc, void *bfa, struct bfa_ioc_cbfn *cbfn)

    IOC attach time initialization and setup.

    :param struct bfa_ioc \*ioc:
        memory for IOC

    :param void \*bfa:
        driver instance structure

    :param struct bfa_ioc_cbfn \*cbfn:
        *undescribed*

.. _`bfa_nw_ioc_pci_init`:

bfa_nw_ioc_pci_init
===================

.. c:function:: void bfa_nw_ioc_pci_init(struct bfa_ioc *ioc, struct bfa_pcidev *pcidev, enum bfi_pcifn_class clscode)

    Setup IOC PCI properties.

    :param struct bfa_ioc \*ioc:
        *undescribed*

    :param struct bfa_pcidev \*pcidev:
        PCI device information for this IOC

    :param enum bfi_pcifn_class clscode:
        *undescribed*

.. _`bfa_nw_ioc_mem_claim`:

bfa_nw_ioc_mem_claim
====================

.. c:function:: void bfa_nw_ioc_mem_claim(struct bfa_ioc *ioc, u8 *dm_kva, u64 dm_pa)

    Initialize IOC dma memory

    :param struct bfa_ioc \*ioc:
        *undescribed*

    :param u8 \*dm_kva:
        kernel virtual address of IOC dma memory

    :param u64 dm_pa:
        physical address of IOC dma memory

.. _`bfa_nw_ioc_mbox_queue`:

bfa_nw_ioc_mbox_queue
=====================

.. c:function:: bool bfa_nw_ioc_mbox_queue(struct bfa_ioc *ioc, struct bfa_mbox_cmd *cmd, bfa_mbox_cmd_cbfn_t cbfn, void *cbarg)

    Queue a mailbox command request to firmware.

    :param struct bfa_ioc \*ioc:
        IOC instance

    :param struct bfa_mbox_cmd \*cmd:
        Mailbox command

    :param bfa_mbox_cmd_cbfn_t cbfn:
        *undescribed*

    :param void \*cbarg:
        *undescribed*

.. _`bfa_nw_ioc_mbox_queue.description`:

Description
-----------

Waits if mailbox is busy. Responsibility of caller to serialize

.. _`bfa_flash_read_send`:

bfa_flash_read_send
===================

.. c:function:: void bfa_flash_read_send(void *cbarg)

    Send flash read request.

    :param void \*cbarg:
        callback argument

.. _`bfa_flash_intr`:

bfa_flash_intr
==============

.. c:function:: void bfa_flash_intr(void *flasharg, struct bfi_mbmsg *msg)

    Process flash response messages upon receiving interrupts.

    :param void \*flasharg:
        flash structure

    :param struct bfi_mbmsg \*msg:
        message structure

.. _`bfa_nw_flash_attach`:

bfa_nw_flash_attach
===================

.. c:function:: void bfa_nw_flash_attach(struct bfa_flash *flash, struct bfa_ioc *ioc, void *dev)

    Flash attach API.

    :param struct bfa_flash \*flash:
        flash structure

    :param struct bfa_ioc \*ioc:
        ioc structure

    :param void \*dev:
        device structure

.. _`bfa_nw_flash_memclaim`:

bfa_nw_flash_memclaim
=====================

.. c:function:: void bfa_nw_flash_memclaim(struct bfa_flash *flash, u8 *dm_kva, u64 dm_pa)

    Claim memory for flash

    :param struct bfa_flash \*flash:
        flash structure

    :param u8 \*dm_kva:
        pointer to virtual memory address

    :param u64 dm_pa:
        physical memory address

.. _`bfa_nw_flash_get_attr`:

bfa_nw_flash_get_attr
=====================

.. c:function:: enum bfa_status bfa_nw_flash_get_attr(struct bfa_flash *flash, struct bfa_flash_attr *attr, bfa_cb_flash cbfn, void *cbarg)

    Get flash attribute.

    :param struct bfa_flash \*flash:
        flash structure

    :param struct bfa_flash_attr \*attr:
        flash attribute structure

    :param bfa_cb_flash cbfn:
        callback function

    :param void \*cbarg:
        callback argument

.. _`bfa_nw_flash_get_attr.description`:

Description
-----------

Return status.

.. _`bfa_nw_flash_update_part`:

bfa_nw_flash_update_part
========================

.. c:function:: enum bfa_status bfa_nw_flash_update_part(struct bfa_flash *flash, u32 type, u8 instance, void *buf, u32 len, u32 offset, bfa_cb_flash cbfn, void *cbarg)

    Update flash partition.

    :param struct bfa_flash \*flash:
        flash structure

    :param u32 type:
        flash partition type

    :param u8 instance:
        flash partition instance

    :param void \*buf:
        update data buffer

    :param u32 len:
        data buffer length

    :param u32 offset:
        offset relative to the partition starting address

    :param bfa_cb_flash cbfn:
        callback function

    :param void \*cbarg:
        callback argument

.. _`bfa_nw_flash_update_part.description`:

Description
-----------

Return status.

.. _`bfa_nw_flash_read_part`:

bfa_nw_flash_read_part
======================

.. c:function:: enum bfa_status bfa_nw_flash_read_part(struct bfa_flash *flash, u32 type, u8 instance, void *buf, u32 len, u32 offset, bfa_cb_flash cbfn, void *cbarg)

    Read flash partition.

    :param struct bfa_flash \*flash:
        flash structure

    :param u32 type:
        flash partition type

    :param u8 instance:
        flash partition instance

    :param void \*buf:
        read data buffer

    :param u32 len:
        data buffer length

    :param u32 offset:
        offset relative to the partition starting address

    :param bfa_cb_flash cbfn:
        callback function

    :param void \*cbarg:
        callback argument

.. _`bfa_nw_flash_read_part.description`:

Description
-----------

Return status.

.. This file was automatic generated / don't edit.

