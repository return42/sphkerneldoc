.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/init.c

.. _`hfi1_rcd_free`:

hfi1_rcd_free
=============

.. c:function:: void hfi1_rcd_free(struct kref *kref)

    When reference is zero clean up.

    :param struct kref \*kref:
        pointer to an initialized rcd data structure

.. _`hfi1_rcd_put`:

hfi1_rcd_put
============

.. c:function:: int hfi1_rcd_put(struct hfi1_ctxtdata *rcd)

    decrement reference for rcd

    :param struct hfi1_ctxtdata \*rcd:
        pointer to an initialized rcd data structure

.. _`hfi1_rcd_put.description`:

Description
-----------

Use this to put a reference after the init.

.. _`hfi1_rcd_get`:

hfi1_rcd_get
============

.. c:function:: void hfi1_rcd_get(struct hfi1_ctxtdata *rcd)

    increment reference for rcd

    :param struct hfi1_ctxtdata \*rcd:
        pointer to an initialized rcd data structure

.. _`hfi1_rcd_get.description`:

Description
-----------

Use this to get a reference after the init.

.. _`allocate_rcd_index`:

allocate_rcd_index
==================

.. c:function:: int allocate_rcd_index(struct hfi1_devdata *dd, struct hfi1_ctxtdata *rcd, u16 *index)

    allocate an rcd index from the rcd array

    :param struct hfi1_devdata \*dd:
        pointer to a valid devdata structure

    :param struct hfi1_ctxtdata \*rcd:
        rcd data structure to assign

    :param u16 \*index:
        pointer to index that is allocated

.. _`allocate_rcd_index.description`:

Description
-----------

Find an empty index in the rcd array, and assign the given rcd to it.
If the array is full, we are EBUSY.

.. _`hfi1_rcd_get_by_index_safe`:

hfi1_rcd_get_by_index_safe
==========================

.. c:function:: struct hfi1_ctxtdata *hfi1_rcd_get_by_index_safe(struct hfi1_devdata *dd, u16 ctxt)

    validate the ctxt index before accessing the array

    :param struct hfi1_devdata \*dd:
        pointer to a valid devdata structure

    :param u16 ctxt:
        the index of an possilbe rcd

.. _`hfi1_rcd_get_by_index_safe.description`:

Description
-----------

This is a wrapper for \ :c:func:`hfi1_rcd_get_by_index`\  to validate that the given
ctxt index is valid.

The caller is responsible for making the \_put().

.. _`hfi1_rcd_get_by_index`:

hfi1_rcd_get_by_index
=====================

.. c:function:: struct hfi1_ctxtdata *hfi1_rcd_get_by_index(struct hfi1_devdata *dd, u16 ctxt)

    :param struct hfi1_devdata \*dd:
        pointer to a valid devdata structure

    :param u16 ctxt:
        the index of an possilbe rcd

.. _`hfi1_rcd_get_by_index.description`:

Description
-----------

We need to protect access to the rcd array.  If access is needed to
one or more index, get the protecting spinlock and then increment the
kref.

The caller is responsible for making the \_put().

.. _`hfi1_free_ctxt`:

hfi1_free_ctxt
==============

.. c:function:: void hfi1_free_ctxt(struct hfi1_ctxtdata *rcd)

    :param struct hfi1_ctxtdata \*rcd:
        pointer to an initialized rcd data structure

.. _`hfi1_free_ctxt.description`:

Description
-----------

This wrapper is the free function that matches \ :c:func:`hfi1_create_ctxtdata`\ .
When a context is done being used (kernel or user), this function is called
for the "final" put to match the kref init from \ :c:func:`hf1i_create_ctxtdata`\ .
Other users of the context do a get/put sequence to make sure that the
structure isn't removed while in use.

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

