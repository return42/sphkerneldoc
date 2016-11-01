.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/brocade/bna/bfa_cee.c

.. _`bfa_cee_attr_meminfo`:

bfa_cee_attr_meminfo
====================

.. c:function:: u32 bfa_cee_attr_meminfo( void)

    Returns the size of the DMA memory needed by CEE attributes

    :param  void:
        no arguments

.. _`bfa_cee_stats_meminfo`:

bfa_cee_stats_meminfo
=====================

.. c:function:: u32 bfa_cee_stats_meminfo( void)

    Returns the size of the DMA memory needed by CEE stats

    :param  void:
        no arguments

.. _`bfa_cee_get_attr_isr`:

bfa_cee_get_attr_isr
====================

.. c:function:: void bfa_cee_get_attr_isr(struct bfa_cee *cee, enum bfa_status status)

    CEE ISR for get-attributes responses from f/w

    :param struct bfa_cee \*cee:
        Pointer to the CEE module

    :param enum bfa_status status:
        Return status from the f/w

.. _`bfa_cee_get_stats_isr`:

bfa_cee_get_stats_isr
=====================

.. c:function:: void bfa_cee_get_stats_isr(struct bfa_cee *cee, enum bfa_status status)

    CEE ISR for get-stats responses from f/w

    :param struct bfa_cee \*cee:
        Pointer to the CEE module

    :param enum bfa_status status:
        Return status from the f/w

.. _`bfa_cee_reset_stats_isr`:

bfa_cee_reset_stats_isr
=======================

.. c:function:: void bfa_cee_reset_stats_isr(struct bfa_cee *cee, enum bfa_status status)

    :param struct bfa_cee \*cee:
        *undescribed*

    :param enum bfa_status status:
        *undescribed*

.. _`bfa_cee_reset_stats_isr.description`:

Description
-----------

@brief CEE ISR for reset-stats responses from f/w

\ ``param``\ [in] cee - Pointer to the CEE module
status - Return status from the f/w

\ ``return``\  void

.. _`bfa_nw_cee_meminfo`:

bfa_nw_cee_meminfo
==================

.. c:function:: u32 bfa_nw_cee_meminfo( void)

    Returns the size of the DMA memory needed by CEE module

    :param  void:
        no arguments

.. _`bfa_nw_cee_mem_claim`:

bfa_nw_cee_mem_claim
====================

.. c:function:: void bfa_nw_cee_mem_claim(struct bfa_cee *cee, u8 *dma_kva, u64 dma_pa)

    Initialized CEE DMA Memory

    :param struct bfa_cee \*cee:
        CEE module pointer

    :param u8 \*dma_kva:
        Kernel Virtual Address of CEE DMA Memory

    :param u64 dma_pa:
        Physical Address of CEE DMA Memory

.. _`bfa_nw_cee_get_attr`:

bfa_nw_cee_get_attr
===================

.. c:function:: enum bfa_status bfa_nw_cee_get_attr(struct bfa_cee *cee, struct bfa_cee_attr *attr, bfa_cee_get_attr_cbfn_t cbfn, void *cbarg)

    Send the request to the f/w to fetch CEE attributes.

    :param struct bfa_cee \*cee:
        Pointer to the CEE module data structure.

    :param struct bfa_cee_attr \*attr:
        *undescribed*

    :param bfa_cee_get_attr_cbfn_t cbfn:
        *undescribed*

    :param void \*cbarg:
        *undescribed*

.. _`bfa_nw_cee_get_attr.return`:

Return
------

status

.. _`bfa_cee_isr`:

bfa_cee_isr
===========

.. c:function:: void bfa_cee_isr(void *cbarg, struct bfi_mbmsg *m)

    Handles Mail-box interrupts for CEE module.

    :param void \*cbarg:
        *undescribed*

    :param struct bfi_mbmsg \*m:
        *undescribed*

.. _`bfa_cee_notify`:

bfa_cee_notify
==============

.. c:function:: void bfa_cee_notify(void *arg, enum bfa_ioc_event event)

    CEE module heart-beat failure handler.

    :param void \*arg:
        *undescribed*

    :param enum bfa_ioc_event event:
        IOC event type

.. _`bfa_nw_cee_attach`:

bfa_nw_cee_attach
=================

.. c:function:: void bfa_nw_cee_attach(struct bfa_cee *cee, struct bfa_ioc *ioc, void *dev)

    CEE module-attach API

    :param struct bfa_cee \*cee:
        Pointer to the CEE module data structure

    :param struct bfa_ioc \*ioc:
        Pointer to the ioc module data structure

    :param void \*dev:
        Pointer to the device driver module data structure.
        The device driver specific mbox ISR functions have
        this pointer as one of the parameters.

.. This file was automatic generated / don't edit.

