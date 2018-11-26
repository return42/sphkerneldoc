.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/brocade/bna/bfa_cee.c

.. _`bfa_cee_attr_meminfo`:

bfa_cee_attr_meminfo
====================

.. c:function:: u32 bfa_cee_attr_meminfo( void)

    Returns the size of the DMA memory needed by CEE attributes

    :param void:
        no arguments
    :type void: 

.. _`bfa_cee_stats_meminfo`:

bfa_cee_stats_meminfo
=====================

.. c:function:: u32 bfa_cee_stats_meminfo( void)

    Returns the size of the DMA memory needed by CEE stats

    :param void:
        no arguments
    :type void: 

.. _`bfa_cee_get_attr_isr`:

bfa_cee_get_attr_isr
====================

.. c:function:: void bfa_cee_get_attr_isr(struct bfa_cee *cee, enum bfa_status status)

    CEE ISR for get-attributes responses from f/w

    :param cee:
        Pointer to the CEE module
    :type cee: struct bfa_cee \*

    :param status:
        Return status from the f/w
    :type status: enum bfa_status

.. _`bfa_cee_get_stats_isr`:

bfa_cee_get_stats_isr
=====================

.. c:function:: void bfa_cee_get_stats_isr(struct bfa_cee *cee, enum bfa_status status)

    CEE ISR for get-stats responses from f/w

    :param cee:
        Pointer to the CEE module
    :type cee: struct bfa_cee \*

    :param status:
        Return status from the f/w
    :type status: enum bfa_status

.. _`bfa_cee_reset_stats_isr`:

bfa_cee_reset_stats_isr
=======================

.. c:function:: void bfa_cee_reset_stats_isr(struct bfa_cee *cee, enum bfa_status status)

    :param cee:
        *undescribed*
    :type cee: struct bfa_cee \*

    :param status:
        *undescribed*
    :type status: enum bfa_status

.. _`bfa_cee_reset_stats_isr.description`:

Description
-----------

\ ``brief``\  CEE ISR for reset-stats responses from f/w

\ ``param``\ [in] cee - Pointer to the CEE module
status - Return status from the f/w

\ ``return``\  void

.. _`bfa_nw_cee_meminfo`:

bfa_nw_cee_meminfo
==================

.. c:function:: u32 bfa_nw_cee_meminfo( void)

    Returns the size of the DMA memory needed by CEE module

    :param void:
        no arguments
    :type void: 

.. _`bfa_nw_cee_mem_claim`:

bfa_nw_cee_mem_claim
====================

.. c:function:: void bfa_nw_cee_mem_claim(struct bfa_cee *cee, u8 *dma_kva, u64 dma_pa)

    Initialized CEE DMA Memory

    :param cee:
        CEE module pointer
    :type cee: struct bfa_cee \*

    :param dma_kva:
        Kernel Virtual Address of CEE DMA Memory
    :type dma_kva: u8 \*

    :param dma_pa:
        Physical Address of CEE DMA Memory
    :type dma_pa: u64

.. _`bfa_nw_cee_get_attr`:

bfa_nw_cee_get_attr
===================

.. c:function:: enum bfa_status bfa_nw_cee_get_attr(struct bfa_cee *cee, struct bfa_cee_attr *attr, bfa_cee_get_attr_cbfn_t cbfn, void *cbarg)

    Send the request to the f/w to fetch CEE attributes.

    :param cee:
        Pointer to the CEE module data structure.
    :type cee: struct bfa_cee \*

    :param attr:
        *undescribed*
    :type attr: struct bfa_cee_attr \*

    :param cbfn:
        *undescribed*
    :type cbfn: bfa_cee_get_attr_cbfn_t

    :param cbarg:
        *undescribed*
    :type cbarg: void \*

.. _`bfa_nw_cee_get_attr.return`:

Return
------

status

.. _`bfa_cee_isr`:

bfa_cee_isr
===========

.. c:function:: void bfa_cee_isr(void *cbarg, struct bfi_mbmsg *m)

    Handles Mail-box interrupts for CEE module.

    :param cbarg:
        *undescribed*
    :type cbarg: void \*

    :param m:
        *undescribed*
    :type m: struct bfi_mbmsg \*

.. _`bfa_cee_notify`:

bfa_cee_notify
==============

.. c:function:: void bfa_cee_notify(void *arg, enum bfa_ioc_event event)

    CEE module heart-beat failure handler.

    :param arg:
        *undescribed*
    :type arg: void \*

    :param event:
        IOC event type
    :type event: enum bfa_ioc_event

.. _`bfa_nw_cee_attach`:

bfa_nw_cee_attach
=================

.. c:function:: void bfa_nw_cee_attach(struct bfa_cee *cee, struct bfa_ioc *ioc, void *dev)

    CEE module-attach API

    :param cee:
        Pointer to the CEE module data structure
    :type cee: struct bfa_cee \*

    :param ioc:
        Pointer to the ioc module data structure
    :type ioc: struct bfa_ioc \*

    :param dev:
        Pointer to the device driver module data structure.
        The device driver specific mbox ISR functions have
        this pointer as one of the parameters.
    :type dev: void \*

.. This file was automatic generated / don't edit.

