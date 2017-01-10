.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/remoteproc_core.c

.. _`rproc_da_to_va`:

rproc_da_to_va
==============

.. c:function:: void *rproc_da_to_va(struct rproc *rproc, u64 da, int len)

    lookup the kernel virtual address for a remoteproc address

    :param struct rproc \*rproc:
        handle of a remote processor

    :param u64 da:
        remoteproc device address to translate

    :param int len:
        length of the memory region \ ``da``\  is pointing to

.. _`rproc_da_to_va.description`:

Description
-----------

Some remote processors will ask us to allocate them physically contiguous
memory regions (which we call "carveouts"), and map them to specific
device addresses (which are hardcoded in the firmware). They may also have
dedicated memory regions internal to the processors, and use them either
exclusively or alongside carveouts.

They may then ask us to copy objects into specific device addresses (e.g.
code/data sections) or expose us certain symbols in other device address
(e.g. their trace buffer).

This function is a helper function with which we can go over the allocated
carveouts and translate specific device addresses to kernel virtual addresses
so we can access the referenced memory. This function also allows to perform
translations on the internal remoteproc memory regions through a platform
implementation specific da_to_va ops, if present.

The function returns a valid kernel address on success or NULL on failure.

.. _`rproc_da_to_va.note`:

Note
----

phys_to_virt(iommu_iova_to_phys(rproc->domain, da)) will work too,
but only on kernel direct mapped RAM memory. Instead, we're just using
here the output of the DMA API for the carveouts, which should be more
correct.

.. _`rproc_handle_vdev`:

rproc_handle_vdev
=================

.. c:function:: int rproc_handle_vdev(struct rproc *rproc, struct fw_rsc_vdev *rsc, int offset, int avail)

    handle a vdev fw resource

    :param struct rproc \*rproc:
        the remote processor

    :param struct fw_rsc_vdev \*rsc:
        the vring resource descriptor

    :param int offset:
        *undescribed*

    :param int avail:
        size of available data (for sanity checking the image)

.. _`rproc_handle_vdev.description`:

Description
-----------

This resource entry requests the host to statically register a virtio
device (vdev), and setup everything needed to support it. It contains

.. _`rproc_handle_vdev.everything-needed-to-make-it-possible`:

everything needed to make it possible
-------------------------------------

the virtio device id, virtio
device features, vrings information, virtio config space, etc...

Before registering the vdev, the vrings are allocated from non-cacheable
physically contiguous memory. Currently we only support two vrings per
remote processor (temporary limitation). We might also want to consider
doing the vring allocation only later when ->find_vqs() is invoked, and
then release them upon ->del_vqs().

.. _`rproc_handle_vdev.note`:

Note
----

@da is currently not really handled correctly: we dynamically
allocate it using the DMA API, ignoring requested hard coded addresses,
and we don't take care of any required IOMMU programming. This is all
going to be taken care of when the generic iommu-based DMA API will be
merged. Meanwhile, statically-addressed iommu-based firmware images should
use RSC_DEVMEM resource entries to map their required \ ``da``\  to the physical
address of their base CMA region (ouch, hacky!).

Returns 0 on success, or an appropriate error code otherwise

.. _`rproc_handle_trace`:

rproc_handle_trace
==================

.. c:function:: int rproc_handle_trace(struct rproc *rproc, struct fw_rsc_trace *rsc, int offset, int avail)

    handle a shared trace buffer resource

    :param struct rproc \*rproc:
        the remote processor

    :param struct fw_rsc_trace \*rsc:
        the trace resource descriptor

    :param int offset:
        *undescribed*

    :param int avail:
        size of available data (for sanity checking the image)

.. _`rproc_handle_trace.description`:

Description
-----------

In case the remote processor dumps trace logs into memory,
export it via debugfs.

Currently, the 'da' member of \ ``rsc``\  should contain the device address
where the remote processor is dumping the traces. Later we could also
support dynamically allocating this address using the generic
DMA API (but currently there isn't a use case for that).

Returns 0 on success, or an appropriate error code otherwise

.. _`rproc_handle_devmem`:

rproc_handle_devmem
===================

.. c:function:: int rproc_handle_devmem(struct rproc *rproc, struct fw_rsc_devmem *rsc, int offset, int avail)

    handle devmem resource entry

    :param struct rproc \*rproc:
        remote processor handle

    :param struct fw_rsc_devmem \*rsc:
        the devmem resource entry

    :param int offset:
        *undescribed*

    :param int avail:
        size of available data (for sanity checking the image)

.. _`rproc_handle_devmem.description`:

Description
-----------

Remote processors commonly need to access certain on-chip peripherals.

Some of these remote processors access memory via an iommu device,
and might require us to configure their iommu before they can access
the on-chip peripherals they need.

This resource entry is a request to map such a peripheral device.

These devmem entries will contain the physical address of the device in
the 'pa' member. If a specific device address is expected, then 'da' will
contain it (currently this is the only use case supported). 'len' will
contain the size of the physical region we need to map.

Currently we just "trust" those devmem entries to contain valid physical
addresses, but this is going to change: we want the implementations to
tell us ranges of physical addresses the firmware is allowed to request,
and not allow firmwares to request access to physical addresses that
are outside those ranges.

.. _`rproc_handle_carveout`:

rproc_handle_carveout
=====================

.. c:function:: int rproc_handle_carveout(struct rproc *rproc, struct fw_rsc_carveout *rsc, int offset, int avail)

    handle phys contig memory allocation requests

    :param struct rproc \*rproc:
        rproc handle

    :param struct fw_rsc_carveout \*rsc:
        the resource entry

    :param int offset:
        *undescribed*

    :param int avail:
        size of available data (for image validation)

.. _`rproc_handle_carveout.description`:

Description
-----------

This function will handle firmware requests for allocation of physically
contiguous memory regions.

These request entries should come first in the firmware's resource table,
as other firmware entries might request placing other data objects inside
these memory regions (e.g. data/code segments, trace resource entries, ...).

Allocating memory this way helps utilizing the reserved physical memory
(e.g. CMA) more efficiently, and also minimizes the number of TLB entries
needed to map it (in case \ ``rproc``\  is using an IOMMU). Reducing the TLB
pressure is important; it may have a substantial impact on performance.

.. _`rproc_resource_cleanup`:

rproc_resource_cleanup
======================

.. c:function:: void rproc_resource_cleanup(struct rproc *rproc)

    clean up and free all acquired resources

    :param struct rproc \*rproc:
        rproc handle

.. _`rproc_resource_cleanup.description`:

Description
-----------

This function will free all resources acquired for \ ``rproc``\ , and it
is called whenever \ ``rproc``\  either shuts down or fails to boot.

.. _`rproc_trigger_recovery`:

rproc_trigger_recovery
======================

.. c:function:: int rproc_trigger_recovery(struct rproc *rproc)

    recover a remoteproc

    :param struct rproc \*rproc:
        the remote processor

.. _`rproc_trigger_recovery.description`:

Description
-----------

The recovery is done by resetting all the virtio devices, that way all the
rpmsg drivers will be reseted along with the remote processor making the
remoteproc functional again.

This function can sleep, so it cannot be called from atomic context.

.. _`rproc_crash_handler_work`:

rproc_crash_handler_work
========================

.. c:function:: void rproc_crash_handler_work(struct work_struct *work)

    handle a crash

    :param struct work_struct \*work:
        *undescribed*

.. _`rproc_crash_handler_work.description`:

Description
-----------

This function needs to handle everything related to a crash, like cpu
registers and stack dump, information to help to debug the fatal error, etc.

.. _`__rproc_boot`:

__rproc_boot
============

.. c:function:: int __rproc_boot(struct rproc *rproc)

    boot a remote processor

    :param struct rproc \*rproc:
        handle of a remote processor

.. _`__rproc_boot.description`:

Description
-----------

Boot a remote processor (i.e. load its firmware, power it on, ...).

If the remote processor is already powered on, this function immediately
returns (successfully).

Returns 0 on success, and an appropriate error value otherwise.

.. _`rproc_boot`:

rproc_boot
==========

.. c:function:: int rproc_boot(struct rproc *rproc)

    boot a remote processor

    :param struct rproc \*rproc:
        handle of a remote processor

.. _`rproc_shutdown`:

rproc_shutdown
==============

.. c:function:: void rproc_shutdown(struct rproc *rproc)

    power off the remote processor

    :param struct rproc \*rproc:
        the remote processor

.. _`rproc_shutdown.description`:

Description
-----------

Power off a remote processor (previously booted with \ :c:func:`rproc_boot`\ ).

In case \ ``rproc``\  is still being used by an additional user(s), then
this function will just decrement the power refcount and exit,
without really powering off the device.

Every call to \ :c:func:`rproc_boot`\  must (eventually) be accompanied by a call
to \ :c:func:`rproc_shutdown`\ . Calling \ :c:func:`rproc_shutdown`\  redundantly is a bug.

.. _`rproc_shutdown.notes`:

Notes
-----

- we're not decrementing the rproc's refcount, only the power refcount.
which means that the \ ``rproc``\  handle stays valid even after \ :c:func:`rproc_shutdown`\ 
returns, and users can still use it with a subsequent \ :c:func:`rproc_boot`\ , if
needed.

.. _`rproc_get_by_phandle`:

rproc_get_by_phandle
====================

.. c:function:: struct rproc *rproc_get_by_phandle(phandle phandle)

    find a remote processor by phandle

    :param phandle phandle:
        phandle to the rproc

.. _`rproc_get_by_phandle.description`:

Description
-----------

Finds an rproc handle using the remote processor's phandle, and then
return a handle to the rproc.

This function increments the remote processor's refcount, so always
use \ :c:func:`rproc_put`\  to decrement it back once rproc isn't needed anymore.

Returns the rproc handle on success, and NULL on failure.

.. _`rproc_add`:

rproc_add
=========

.. c:function:: int rproc_add(struct rproc *rproc)

    register a remote processor

    :param struct rproc \*rproc:
        the remote processor handle to register

.. _`rproc_add.description`:

Description
-----------

Registers \ ``rproc``\  with the remoteproc framework, after it has been
allocated with \ :c:func:`rproc_alloc`\ .

This is called by the platform-specific rproc implementation, whenever
a new remote processor device is probed.

Returns 0 on success and an appropriate error code otherwise.

.. _`rproc_add.note`:

Note
----

this function initiates an asynchronous firmware loading
context, which will look for virtio devices supported by the rproc's
firmware.

If found, those virtio devices will be created and added, so as a result
of registering this remote processor, additional virtio drivers might be
probed.

.. _`rproc_type_release`:

rproc_type_release
==================

.. c:function:: void rproc_type_release(struct device *dev)

    release a remote processor instance

    :param struct device \*dev:
        the rproc's device

.. _`rproc_type_release.description`:

Description
-----------

This function should \_never\_ be called directly.

It will be called by the driver core when no one holds a valid pointer
to \ ``dev``\  anymore.

.. _`rproc_alloc`:

rproc_alloc
===========

.. c:function:: struct rproc *rproc_alloc(struct device *dev, const char *name, const struct rproc_ops *ops, const char *firmware, int len)

    allocate a remote processor handle

    :param struct device \*dev:
        the underlying device

    :param const char \*name:
        name of this remote processor

    :param const struct rproc_ops \*ops:
        platform-specific handlers (mainly start/stop)

    :param const char \*firmware:
        name of firmware file to load, can be NULL

    :param int len:
        length of private data needed by the rproc driver (in bytes)

.. _`rproc_alloc.description`:

Description
-----------

Allocates a new remote processor handle, but does not register
it yet. if \ ``firmware``\  is NULL, a default name is used.

This function should be used by rproc implementations during initialization
of the remote processor.

After creating an rproc handle using this function, and when ready,
implementations should then call \ :c:func:`rproc_add`\  to complete
the registration of the remote processor.

On success the new rproc is returned, and on failure, NULL.

.. _`rproc_alloc.note`:

Note
----

_never\_ directly deallocate \ ``rproc``\ , even if it was not registered
yet. Instead, when you need to unroll \ :c:func:`rproc_alloc`\ , use \ :c:func:`rproc_free`\ .

.. _`rproc_free`:

rproc_free
==========

.. c:function:: void rproc_free(struct rproc *rproc)

    unroll \ :c:func:`rproc_alloc`\ 

    :param struct rproc \*rproc:
        the remote processor handle

.. _`rproc_free.description`:

Description
-----------

This function decrements the rproc dev refcount.

If no one holds any reference to rproc anymore, then its refcount would
now drop to zero, and it would be freed.

.. _`rproc_put`:

rproc_put
=========

.. c:function:: void rproc_put(struct rproc *rproc)

    release rproc reference

    :param struct rproc \*rproc:
        the remote processor handle

.. _`rproc_put.description`:

Description
-----------

This function decrements the rproc dev refcount.

If no one holds any reference to rproc anymore, then its refcount would
now drop to zero, and it would be freed.

.. _`rproc_del`:

rproc_del
=========

.. c:function:: int rproc_del(struct rproc *rproc)

    unregister a remote processor

    :param struct rproc \*rproc:
        rproc handle to unregister

.. _`rproc_del.description`:

Description
-----------

This function should be called when the platform specific rproc
implementation decides to remove the rproc device. it should
\_only\_ be called if a previous invocation of \ :c:func:`rproc_add`\ 
has completed successfully.

After \ :c:func:`rproc_del`\  returns, \ ``rproc``\  isn't freed yet, because
of the outstanding reference created by rproc_alloc. To decrement that
one last refcount, one still needs to call \ :c:func:`rproc_free`\ .

Returns 0 on success and -EINVAL if \ ``rproc``\  isn't valid.

.. _`rproc_add_subdev`:

rproc_add_subdev
================

.. c:function:: void rproc_add_subdev(struct rproc *rproc, struct rproc_subdev *subdev, int (*probe)(struct rproc_subdev *subdev), void (*remove)(struct rproc_subdev *subdev))

    add a subdevice to a remoteproc

    :param struct rproc \*rproc:
        rproc handle to add the subdevice to

    :param struct rproc_subdev \*subdev:
        subdev handle to register

    :param int (\*probe)(struct rproc_subdev \*subdev):
        function to call when the rproc boots

    :param void (\*remove)(struct rproc_subdev \*subdev):
        function to call when the rproc shuts down

.. _`rproc_remove_subdev`:

rproc_remove_subdev
===================

.. c:function:: void rproc_remove_subdev(struct rproc *rproc, struct rproc_subdev *subdev)

    remove a subdevice from a remoteproc

    :param struct rproc \*rproc:
        rproc handle to remove the subdevice from

    :param struct rproc_subdev \*subdev:
        subdev handle, previously registered with \ :c:func:`rproc_add_subdev`\ 

.. _`rproc_report_crash`:

rproc_report_crash
==================

.. c:function:: void rproc_report_crash(struct rproc *rproc, enum rproc_crash_type type)

    rproc crash reporter function

    :param struct rproc \*rproc:
        remote processor

    :param enum rproc_crash_type type:
        crash type

.. _`rproc_report_crash.description`:

Description
-----------

This function must be called every time a crash is detected by the low-level
drivers implementing a specific remoteproc. This should not be called from a
non-remoteproc driver.

This function can be called from atomic/interrupt context.

.. This file was automatic generated / don't edit.

