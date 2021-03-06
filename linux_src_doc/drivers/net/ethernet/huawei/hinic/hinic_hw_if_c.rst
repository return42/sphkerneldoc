.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_if.c

.. _`hinic_msix_attr_set`:

hinic_msix_attr_set
===================

.. c:function:: int hinic_msix_attr_set(struct hinic_hwif *hwif, u16 msix_index, u8 pending_limit, u8 coalesc_timer, u8 lli_timer, u8 lli_credit_limit, u8 resend_timer)

    set message attribute for msix entry

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param msix_index:
        msix_index
    :type msix_index: u16

    :param pending_limit:
        the maximum pending interrupt events (unit 8)
    :type pending_limit: u8

    :param coalesc_timer:
        coalesc period for interrupt (unit 8 us)
    :type coalesc_timer: u8

    :param lli_timer:
        replenishing period for low latency credit (unit 8 us)
    :type lli_timer: u8

    :param lli_credit_limit:
        maximum credits for low latency msix messages (unit 8)
    :type lli_credit_limit: u8

    :param resend_timer:
        maximum wait for resending msix (unit coalesc period)
    :type resend_timer: u8

.. _`hinic_msix_attr_set.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_msix_attr_get`:

hinic_msix_attr_get
===================

.. c:function:: int hinic_msix_attr_get(struct hinic_hwif *hwif, u16 msix_index, u8 *pending_limit, u8 *coalesc_timer, u8 *lli_timer, u8 *lli_credit_limit, u8 *resend_timer)

    get message attribute of msix entry

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param msix_index:
        msix_index
    :type msix_index: u16

    :param pending_limit:
        the maximum pending interrupt events (unit 8)
    :type pending_limit: u8 \*

    :param coalesc_timer:
        coalesc period for interrupt (unit 8 us)
    :type coalesc_timer: u8 \*

    :param lli_timer:
        replenishing period for low latency credit (unit 8 us)
    :type lli_timer: u8 \*

    :param lli_credit_limit:
        maximum credits for low latency msix messages (unit 8)
    :type lli_credit_limit: u8 \*

    :param resend_timer:
        maximum wait for resending msix (unit coalesc period)
    :type resend_timer: u8 \*

.. _`hinic_msix_attr_get.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_msix_attr_cnt_clear`:

hinic_msix_attr_cnt_clear
=========================

.. c:function:: int hinic_msix_attr_cnt_clear(struct hinic_hwif *hwif, u16 msix_index)

    clear message attribute counters for msix entry

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param msix_index:
        msix_index
    :type msix_index: u16

.. _`hinic_msix_attr_cnt_clear.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_set_pf_action`:

hinic_set_pf_action
===================

.. c:function:: void hinic_set_pf_action(struct hinic_hwif *hwif, enum hinic_pf_action action)

    set action on pf channel

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param action:
        action on pf channel
    :type action: enum hinic_pf_action

.. _`hinic_set_pf_action.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hwif_ready`:

hwif_ready
==========

.. c:function:: int hwif_ready(struct hinic_hwif *hwif)

    test if the HW is ready for use

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. _`hwif_ready.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`set_hwif_attr`:

set_hwif_attr
=============

.. c:function:: void set_hwif_attr(struct hinic_hwif *hwif, u32 attr0, u32 attr1)

    set the attributes in the relevant members in hwif

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param attr0:
        the first attribute that was read from the hw
    :type attr0: u32

    :param attr1:
        the second attribute that was read from the hw
    :type attr1: u32

.. _`read_hwif_attr`:

read_hwif_attr
==============

.. c:function:: void read_hwif_attr(struct hinic_hwif *hwif)

    read the attributes and set members in hwif

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. _`set_ppf`:

set_ppf
=======

.. c:function:: void set_ppf(struct hinic_hwif *hwif)

    try to set hwif as ppf and set the type of hwif in this case

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. _`set_dma_attr`:

set_dma_attr
============

.. c:function:: void set_dma_attr(struct hinic_hwif *hwif, u32 entry_idx, u8 st, u8 at, u8 ph, enum hinic_pcie_nosnoop no_snooping, enum hinic_pcie_tph tph_en)

    set the dma attributes in the HW

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param entry_idx:
        the entry index in the dma table
    :type entry_idx: u32

    :param st:
        PCIE TLP steering tag
    :type st: u8

    :param at:
        PCIE TLP AT field
    :type at: u8

    :param ph:
        PCIE TLP Processing Hint field
    :type ph: u8

    :param no_snooping:
        PCIE TLP No snooping
    :type no_snooping: enum hinic_pcie_nosnoop

    :param tph_en:
        PCIE TLP Processing Hint Enable
    :type tph_en: enum hinic_pcie_tph

.. _`dma_attr_init`:

dma_attr_init
=============

.. c:function:: void dma_attr_init(struct hinic_hwif *hwif)

    initialize the the default dma attributes

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. _`hinic_init_hwif`:

hinic_init_hwif
===============

.. c:function:: int hinic_init_hwif(struct hinic_hwif *hwif, struct pci_dev *pdev)

    initialize the hw interface

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

    :param pdev:
        the pci device for acessing PCI resources
    :type pdev: struct pci_dev \*

.. _`hinic_init_hwif.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_free_hwif`:

hinic_free_hwif
===============

.. c:function:: void hinic_free_hwif(struct hinic_hwif *hwif)

    free the HW interface

    :param hwif:
        the HW interface of a pci function device
    :type hwif: struct hinic_hwif \*

.. This file was automatic generated / don't edit.

