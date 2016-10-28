.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/init.c

.. _`init_after_reset`:

init_after_reset
================

.. c:function:: int init_after_reset(struct hfi1_devdata *dd)

    re-initialize after a reset

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

.. _`init_after_reset.description`:

Description
-----------

sanity check at least some of the values after reset, and
ensure no receive or transmit (explicitly, in case reset
failed

.. _`create_workqueues`:

create_workqueues
=================

.. c:function:: int create_workqueues(struct hfi1_devdata *dd)

    create per port workqueues

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

.. _`hfi1_init`:

hfi1_init
=========

.. c:function:: int hfi1_init(struct hfi1_devdata *dd, int reinit)

    do the actual initialization sequence on the chip

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param int reinit:
        re-initializing, so don't allocate new memory

.. _`hfi1_init.description`:

Description
-----------

Do the actual initialization sequence on the chip.  This is done
both from the init routine called from the PCI infrastructure, and
when we reset the chip, or detect that it was reset internally,
or it's administratively re-enabled.

Memory allocation here and in called routines is only done in
the first case (reinit == 0).  We have to be careful, because even
without memory allocation, we need to re-write all the chip registers
TIDs, etc. after the reset or enable has completed.

.. _`shutdown_device`:

shutdown_device
===============

.. c:function:: void shutdown_device(struct hfi1_devdata *dd)

    shut down a device

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

.. _`shutdown_device.description`:

Description
-----------

This is called to make the device quiet when we are about to
unload the driver, and also when the device is administratively
disabled.   It does not free any data structures.
Everything it does has to be setup again by hfi1_init(dd, 1)

.. _`hfi1_free_ctxtdata`:

hfi1_free_ctxtdata
==================

.. c:function:: void hfi1_free_ctxtdata(struct hfi1_devdata *dd, struct hfi1_ctxtdata *rcd)

    free a context's allocated data

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param struct hfi1_ctxtdata \*rcd:
        the ctxtdata structure

.. _`hfi1_free_ctxtdata.description`:

Description
-----------

free up any allocated data for a context
This should not touch anything that would affect a simultaneous
re-allocation of context data, because it is called after hfi1_mutex
is released (and can be called from reinit as well).
It should never change any chip state, or global driver state.

.. _`hfi1_create_rcvhdrq`:

hfi1_create_rcvhdrq
===================

.. c:function:: int hfi1_create_rcvhdrq(struct hfi1_devdata *dd, struct hfi1_ctxtdata *rcd)

    create a receive header queue

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param struct hfi1_ctxtdata \*rcd:
        the context data

.. _`hfi1_create_rcvhdrq.description`:

Description
-----------

This must be contiguous memory (from an i/o perspective), and must be
DMA'able (which means for some systems, it will go through an IOMMU,
or be forced into a low address range).

.. _`hfi1_setup_eagerbufs`:

hfi1_setup_eagerbufs
====================

.. c:function:: int hfi1_setup_eagerbufs(struct hfi1_ctxtdata *rcd)

    :param struct hfi1_ctxtdata \*rcd:
        the context we are setting up.

.. _`hfi1_setup_eagerbufs.description`:

Description
-----------

Allocate the eager TID buffers and program them into hip.
They are no longer completely contiguous, we do multiple allocation
calls.  Otherwise we get the OOM code involved, by asking for too
much per call, with disastrous results on some kernels.

.. This file was automatic generated / don't edit.

