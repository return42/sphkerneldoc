.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_init.c

.. _`init_shadow_tids`:

init_shadow_tids
================

.. c:function:: void init_shadow_tids(struct qib_devdata *dd)

    allocate the shadow TID array

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`init_shadow_tids.description`:

Description
-----------

allocate the shadow TID array, so we can qib_munlock previous
entries.  It may make more sense to move the pageshadow to the
ctxt data structure, so we only allocate memory for ctxts actually
in use, since we at 8k per ctxt, now.
We don't want failures here to prevent use of the driver/chip,
so no return value.

.. _`init_after_reset`:

init_after_reset
================

.. c:function:: int init_after_reset(struct qib_devdata *dd)

    re-initialize after a reset

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`init_after_reset.description`:

Description
-----------

sanity check at least some of the values after reset, and
ensure no receive or transmit (explicitly, in case reset
failed

.. _`qib_create_workqueues`:

qib_create_workqueues
=====================

.. c:function:: int qib_create_workqueues(struct qib_devdata *dd)

    create per port workqueues

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`qib_init`:

qib_init
========

.. c:function:: int qib_init(struct qib_devdata *dd, int reinit)

    do the actual initialization sequence on the chip

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param reinit:
        reinitializing, so don't allocate new memory
    :type reinit: int

.. _`qib_init.description`:

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

.. _`qib_shutdown_device`:

qib_shutdown_device
===================

.. c:function:: void qib_shutdown_device(struct qib_devdata *dd)

    shut down a device

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`qib_shutdown_device.description`:

Description
-----------

This is called to make the device quiet when we are about to
unload the driver, and also when the device is administratively
disabled.   It does not free any data structures.
Everything it does has to be setup again by qib_init(dd, 1)

.. _`qib_free_ctxtdata`:

qib_free_ctxtdata
=================

.. c:function:: void qib_free_ctxtdata(struct qib_devdata *dd, struct qib_ctxtdata *rcd)

    free a context's allocated data

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param rcd:
        the ctxtdata structure
    :type rcd: struct qib_ctxtdata \*

.. _`qib_free_ctxtdata.description`:

Description
-----------

free up any allocated data for a context
This should not touch anything that would affect a simultaneous
re-allocation of context data, because it is called after qib_mutex
is released (and can be called from reinit as well).
It should never change any chip state, or global driver state.

.. _`qib_create_rcvhdrq`:

qib_create_rcvhdrq
==================

.. c:function:: int qib_create_rcvhdrq(struct qib_devdata *dd, struct qib_ctxtdata *rcd)

    create a receive header queue

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param rcd:
        the context data
    :type rcd: struct qib_ctxtdata \*

.. _`qib_create_rcvhdrq.description`:

Description
-----------

This must be contiguous memory (from an i/o perspective), and must be
DMA'able (which means for some systems, it will go through an IOMMU,
or be forced into a low address range).

.. _`qib_setup_eagerbufs`:

qib_setup_eagerbufs
===================

.. c:function:: int qib_setup_eagerbufs(struct qib_ctxtdata *rcd)

    :param rcd:
        the context we are setting up.
    :type rcd: struct qib_ctxtdata \*

.. _`qib_setup_eagerbufs.description`:

Description
-----------

Allocate the eager TID buffers and program them into hip.
They are no longer completely contiguous, we do multiple allocation
calls.  Otherwise we get the OOM code involved, by asking for too
much per call, with disastrous results on some kernels.

.. This file was automatic generated / don't edit.

