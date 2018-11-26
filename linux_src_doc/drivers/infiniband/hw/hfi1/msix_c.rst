.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/msix.c

.. _`msix_initialize`:

msix_initialize
===============

.. c:function:: int msix_initialize(struct hfi1_devdata *dd)

    Calculate, request and configure MSIx IRQs

    :param dd:
        valid hfi1 devdata
    :type dd: struct hfi1_devdata \*

.. _`msix_request_irq`:

msix_request_irq
================

.. c:function:: int msix_request_irq(struct hfi1_devdata *dd, void *arg, irq_handler_t handler, irq_handler_t thread, u32 idx, enum irq_type type)

    Allocate a free MSIx IRQ

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

    :param arg:
        context information for the IRQ
    :type arg: void \*

    :param handler:
        IRQ handler
    :type handler: irq_handler_t

    :param thread:
        IRQ thread handler (could be NULL)
    :type thread: irq_handler_t

    :param idx:
        zero base idx if multiple devices are needed
    :type idx: u32

    :param type:
        affinty IRQ type
    :type type: enum irq_type

.. _`msix_request_irq.description`:

Description
-----------

Allocated an MSIx vector if available, and then create the appropriate
meta data needed to keep track of the pci IRQ request.

.. _`msix_request_irq.return`:

Return
------

< 0   Error
>= 0  MSIx vector

.. _`msix_request_rcd_irq`:

msix_request_rcd_irq
====================

.. c:function:: int msix_request_rcd_irq(struct hfi1_ctxtdata *rcd)

    Helper function for RCVAVAIL IRQs

    :param rcd:
        valid rcd context
    :type rcd: struct hfi1_ctxtdata \*

.. _`msix_request_sdma_irq`:

msix_request_sdma_irq
=====================

.. c:function:: int msix_request_sdma_irq(struct sdma_engine *sde)

    Helper for getting SDMA IRQ resources

    :param sde:
        valid sdma engine
    :type sde: struct sdma_engine \*

.. _`enable_sdma_srcs`:

enable_sdma_srcs
================

.. c:function:: void enable_sdma_srcs(struct hfi1_devdata *dd, int i)

    Helper to enable SDMA IRQ srcs

    :param dd:
        valid devdata structure
    :type dd: struct hfi1_devdata \*

    :param i:
        index of SDMA engine
    :type i: int

.. _`msix_request_irqs`:

msix_request_irqs
=================

.. c:function:: int msix_request_irqs(struct hfi1_devdata *dd)

    Allocate all MSIx IRQs

    :param dd:
        valid devdata structure
    :type dd: struct hfi1_devdata \*

.. _`msix_request_irqs.description`:

Description
-----------

Helper function to request the used MSIx IRQs.

.. _`msix_free_irq`:

msix_free_irq
=============

.. c:function:: void msix_free_irq(struct hfi1_devdata *dd, u8 msix_intr)

    Free the specified MSIx resources and IRQ

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

    :param msix_intr:
        MSIx vector to free.
    :type msix_intr: u8

.. _`msix_clean_up_interrupts`:

msix_clean_up_interrupts
========================

.. c:function:: void msix_clean_up_interrupts(struct hfi1_devdata *dd)

    Free all MSIx IRQ resources

    :param dd:
        valid device data data structure
    :type dd: struct hfi1_devdata \*

.. _`msix_clean_up_interrupts.description`:

Description
-----------

Free the MSIx and associated PCI resources, if they have been allocated.

.. _`msix_vnic_synchronize_irq`:

msix_vnic_synchronize_irq
=========================

.. c:function:: void msix_vnic_synchronize_irq(struct hfi1_devdata *dd)

    Vnic IRQ synchronize

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

.. This file was automatic generated / don't edit.

