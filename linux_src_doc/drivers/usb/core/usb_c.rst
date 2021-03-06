.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/usb.c

.. _`usb_find_common_endpoints`:

usb_find_common_endpoints
=========================

.. c:function:: int usb_find_common_endpoints(struct usb_host_interface *alt, struct usb_endpoint_descriptor **bulk_in, struct usb_endpoint_descriptor **bulk_out, struct usb_endpoint_descriptor **int_in, struct usb_endpoint_descriptor **int_out)

    - look up common endpoint descriptors

    :param alt:
        alternate setting to search
    :type alt: struct usb_host_interface \*

    :param bulk_in:
        pointer to descriptor pointer, or NULL
    :type bulk_in: struct usb_endpoint_descriptor \*\*

    :param bulk_out:
        pointer to descriptor pointer, or NULL
    :type bulk_out: struct usb_endpoint_descriptor \*\*

    :param int_in:
        pointer to descriptor pointer, or NULL
    :type int_in: struct usb_endpoint_descriptor \*\*

    :param int_out:
        pointer to descriptor pointer, or NULL
    :type int_out: struct usb_endpoint_descriptor \*\*

.. _`usb_find_common_endpoints.description`:

Description
-----------

Search the alternate setting's endpoint descriptors for the first bulk-in,
bulk-out, interrupt-in and interrupt-out endpoints and return them in the
provided pointers (unless they are NULL).

If a requested endpoint is not found, the corresponding pointer is set to
NULL.

.. _`usb_find_common_endpoints.return`:

Return
------

Zero if all requested descriptors were found, or -ENXIO otherwise.

.. _`usb_find_common_endpoints_reverse`:

usb_find_common_endpoints_reverse
=================================

.. c:function:: int usb_find_common_endpoints_reverse(struct usb_host_interface *alt, struct usb_endpoint_descriptor **bulk_in, struct usb_endpoint_descriptor **bulk_out, struct usb_endpoint_descriptor **int_in, struct usb_endpoint_descriptor **int_out)

    - look up common endpoint descriptors

    :param alt:
        alternate setting to search
    :type alt: struct usb_host_interface \*

    :param bulk_in:
        pointer to descriptor pointer, or NULL
    :type bulk_in: struct usb_endpoint_descriptor \*\*

    :param bulk_out:
        pointer to descriptor pointer, or NULL
    :type bulk_out: struct usb_endpoint_descriptor \*\*

    :param int_in:
        pointer to descriptor pointer, or NULL
    :type int_in: struct usb_endpoint_descriptor \*\*

    :param int_out:
        pointer to descriptor pointer, or NULL
    :type int_out: struct usb_endpoint_descriptor \*\*

.. _`usb_find_common_endpoints_reverse.description`:

Description
-----------

Search the alternate setting's endpoint descriptors for the last bulk-in,
bulk-out, interrupt-in and interrupt-out endpoints and return them in the
provided pointers (unless they are NULL).

If a requested endpoint is not found, the corresponding pointer is set to
NULL.

.. _`usb_find_common_endpoints_reverse.return`:

Return
------

Zero if all requested descriptors were found, or -ENXIO otherwise.

.. _`usb_find_alt_setting`:

usb_find_alt_setting
====================

.. c:function:: struct usb_host_interface *usb_find_alt_setting(struct usb_host_config *config, unsigned int iface_num, unsigned int alt_num)

    Given a configuration, find the alternate setting for the given interface.

    :param config:
        the configuration to search (not necessarily the current config).
    :type config: struct usb_host_config \*

    :param iface_num:
        interface number to search in
    :type iface_num: unsigned int

    :param alt_num:
        alternate interface setting number to search for.
    :type alt_num: unsigned int

.. _`usb_find_alt_setting.description`:

Description
-----------

Search the configuration's interface cache for the given alt setting.

.. _`usb_find_alt_setting.return`:

Return
------

The alternate setting, if found. \ ``NULL``\  otherwise.

.. _`usb_ifnum_to_if`:

usb_ifnum_to_if
===============

.. c:function:: struct usb_interface *usb_ifnum_to_if(const struct usb_device *dev, unsigned ifnum)

    get the interface object with a given interface number

    :param dev:
        the device whose current configuration is considered
    :type dev: const struct usb_device \*

    :param ifnum:
        the desired interface
    :type ifnum: unsigned

.. _`usb_ifnum_to_if.description`:

Description
-----------

This walks the device descriptor for the currently active configuration
to find the interface object with the particular interface number.

Note that configuration descriptors are not required to assign interface
numbers sequentially, so that it would be incorrect to assume that
the first interface in that descriptor corresponds to interface zero.
This routine helps device drivers avoid such mistakes.
However, you should make sure that you do the right thing with any
alternate settings available for this interfaces.

Don't call this function unless you are bound to one of the interfaces
on this device or you have locked the device!

.. _`usb_ifnum_to_if.return`:

Return
------

A pointer to the interface that has \ ``ifnum``\  as interface number,
if found. \ ``NULL``\  otherwise.

.. _`usb_altnum_to_altsetting`:

usb_altnum_to_altsetting
========================

.. c:function:: struct usb_host_interface *usb_altnum_to_altsetting(const struct usb_interface *intf, unsigned int altnum)

    get the altsetting structure with a given alternate setting number.

    :param intf:
        the interface containing the altsetting in question
    :type intf: const struct usb_interface \*

    :param altnum:
        the desired alternate setting number
    :type altnum: unsigned int

.. _`usb_altnum_to_altsetting.description`:

Description
-----------

This searches the altsetting array of the specified interface for
an entry with the correct bAlternateSetting value.

Note that altsettings need not be stored sequentially by number, so
it would be incorrect to assume that the first altsetting entry in
the array corresponds to altsetting zero.  This routine helps device
drivers avoid such mistakes.

Don't call this function unless you are bound to the intf interface
or you have locked the device!

.. _`usb_altnum_to_altsetting.return`:

Return
------

A pointer to the entry of the altsetting array of \ ``intf``\  that
has \ ``altnum``\  as the alternate setting number. \ ``NULL``\  if not found.

.. _`usb_find_interface`:

usb_find_interface
==================

.. c:function:: struct usb_interface *usb_find_interface(struct usb_driver *drv, int minor)

    find usb_interface pointer for driver and device

    :param drv:
        the driver whose current configuration is considered
    :type drv: struct usb_driver \*

    :param minor:
        the minor number of the desired device
    :type minor: int

.. _`usb_find_interface.description`:

Description
-----------

This walks the bus device list and returns a pointer to the interface
with the matching minor and driver.  Note, this only works for devices
that share the USB major number.

.. _`usb_find_interface.return`:

Return
------

A pointer to the interface with the matching major and \ ``minor``\ .

.. _`usb_for_each_dev`:

usb_for_each_dev
================

.. c:function:: int usb_for_each_dev(void *data, int (*fn)(struct usb_device *, void *))

    iterate over all USB devices in the system

    :param data:
        data pointer that will be handed to the callback function
    :type data: void \*

    :param int (\*fn)(struct usb_device \*, void \*):
        callback function to be called for each USB device

.. _`usb_for_each_dev.description`:

Description
-----------

Iterate over all USB devices and call \ ``fn``\  for each, passing it \ ``data``\ . If it
returns anything other than 0, we break the iteration prematurely and return
that value.

.. _`usb_release_dev`:

usb_release_dev
===============

.. c:function:: void usb_release_dev(struct device *dev)

    free a usb device structure when all users of it are finished.

    :param dev:
        device that's been disconnected
    :type dev: struct device \*

.. _`usb_release_dev.description`:

Description
-----------

Will be called only by the device core when all users of this usb device are
done.

.. _`usb_alloc_dev`:

usb_alloc_dev
=============

.. c:function:: struct usb_device *usb_alloc_dev(struct usb_device *parent, struct usb_bus *bus, unsigned port1)

    usb device constructor (usbcore-internal)

    :param parent:
        hub to which device is connected; null to allocate a root hub
    :type parent: struct usb_device \*

    :param bus:
        bus used to access the device
    :type bus: struct usb_bus \*

    :param port1:
        one-based index of port; ignored for root hubs
    :type port1: unsigned

.. _`usb_alloc_dev.context`:

Context
-------

!in_interrupt()

.. _`usb_alloc_dev.description`:

Description
-----------

Only hub drivers (including virtual root hub drivers for host
controllers) should ever call this.

This call may not be used in a non-sleeping context.

.. _`usb_alloc_dev.return`:

Return
------

On success, a pointer to the allocated usb device. \ ``NULL``\  on
failure.

.. _`usb_get_dev`:

usb_get_dev
===========

.. c:function:: struct usb_device *usb_get_dev(struct usb_device *dev)

    increments the reference count of the usb device structure

    :param dev:
        the device being referenced
    :type dev: struct usb_device \*

.. _`usb_get_dev.description`:

Description
-----------

Each live reference to a device should be refcounted.

Drivers for USB interfaces should normally record such references in
their \ :c:func:`probe`\  methods, when they bind to an interface, and release
them by calling \ :c:func:`usb_put_dev`\ , in their \ :c:func:`disconnect`\  methods.

.. _`usb_get_dev.return`:

Return
------

A pointer to the device with the incremented reference counter.

.. _`usb_put_dev`:

usb_put_dev
===========

.. c:function:: void usb_put_dev(struct usb_device *dev)

    release a use of the usb device structure

    :param dev:
        device that's been disconnected
    :type dev: struct usb_device \*

.. _`usb_put_dev.description`:

Description
-----------

Must be called when a user of a device is finished with it.  When the last
user of the device calls this function, the memory of the device is freed.

.. _`usb_get_intf`:

usb_get_intf
============

.. c:function:: struct usb_interface *usb_get_intf(struct usb_interface *intf)

    increments the reference count of the usb interface structure

    :param intf:
        the interface being referenced
    :type intf: struct usb_interface \*

.. _`usb_get_intf.description`:

Description
-----------

Each live reference to a interface must be refcounted.

Drivers for USB interfaces should normally record such references in
their \ :c:func:`probe`\  methods, when they bind to an interface, and release
them by calling \ :c:func:`usb_put_intf`\ , in their \ :c:func:`disconnect`\  methods.

.. _`usb_get_intf.return`:

Return
------

A pointer to the interface with the incremented reference counter.

.. _`usb_put_intf`:

usb_put_intf
============

.. c:function:: void usb_put_intf(struct usb_interface *intf)

    release a use of the usb interface structure

    :param intf:
        interface that's been decremented
    :type intf: struct usb_interface \*

.. _`usb_put_intf.description`:

Description
-----------

Must be called when a user of an interface is finished with it.  When the
last user of the interface calls this function, the memory of the interface
is freed.

.. _`usb_lock_device_for_reset`:

usb_lock_device_for_reset
=========================

.. c:function:: int usb_lock_device_for_reset(struct usb_device *udev, const struct usb_interface *iface)

    cautiously acquire the lock for a usb device structure

    :param udev:
        device that's being locked
    :type udev: struct usb_device \*

    :param iface:
        interface bound to the driver making the request (optional)
    :type iface: const struct usb_interface \*

.. _`usb_lock_device_for_reset.description`:

Description
-----------

Attempts to acquire the device lock, but fails if the device is
NOTATTACHED or SUSPENDED, or if iface is specified and the interface
is neither BINDING nor BOUND.  Rather than sleeping to wait for the
lock, the routine polls repeatedly.  This is to prevent deadlock with
disconnect; in some drivers (such as usb-storage) the \ :c:func:`disconnect`\ 
or \ :c:func:`suspend`\  method will block waiting for a device reset to complete.

.. _`usb_lock_device_for_reset.return`:

Return
------

A negative error code for failure, otherwise 0.

.. _`usb_get_current_frame_number`:

usb_get_current_frame_number
============================

.. c:function:: int usb_get_current_frame_number(struct usb_device *dev)

    return current bus frame number

    :param dev:
        the device whose bus is being queried
    :type dev: struct usb_device \*

.. _`usb_get_current_frame_number.return`:

Return
------

The current frame number for the USB host controller used
with the given USB device. This can be used when scheduling
isochronous requests.

.. _`usb_get_current_frame_number.note`:

Note
----

Different kinds of host controller have different "scheduling
horizons". While one type might support scheduling only 32 frames
into the future, others could support scheduling up to 1024 frames
into the future.

.. _`usb_alloc_coherent`:

usb_alloc_coherent
==================

.. c:function:: void *usb_alloc_coherent(struct usb_device *dev, size_t size, gfp_t mem_flags, dma_addr_t *dma)

    allocate dma-consistent buffer for URB_NO_xxx_DMA_MAP

    :param dev:
        device the buffer will be used with
    :type dev: struct usb_device \*

    :param size:
        requested buffer size
    :type size: size_t

    :param mem_flags:
        affect whether allocation may block
    :type mem_flags: gfp_t

    :param dma:
        used to return DMA address of buffer
    :type dma: dma_addr_t \*

.. _`usb_alloc_coherent.return`:

Return
------

Either null (indicating no buffer could be allocated), or the
cpu-space pointer to a buffer that may be used to perform DMA to the
specified device.  Such cpu-space buffers are returned along with the DMA
address (through the pointer provided).

.. _`usb_alloc_coherent.note`:

Note
----

These buffers are used with URB_NO_xxx_DMA_MAP set in urb->transfer_flags
to avoid behaviors like using "DMA bounce buffers", or thrashing IOMMU
hardware during URB completion/resubmit.  The implementation varies between
platforms, depending on details of how DMA will work to this device.
Using these buffers also eliminates cacheline sharing problems on
architectures where CPU caches are not DMA-coherent.  On systems without
bus-snooping caches, these buffers are uncached.

When the buffer is no longer used, free it with \ :c:func:`usb_free_coherent`\ .

.. _`usb_free_coherent`:

usb_free_coherent
=================

.. c:function:: void usb_free_coherent(struct usb_device *dev, size_t size, void *addr, dma_addr_t dma)

    free memory allocated with \ :c:func:`usb_alloc_coherent`\ 

    :param dev:
        device the buffer was used with
    :type dev: struct usb_device \*

    :param size:
        requested buffer size
    :type size: size_t

    :param addr:
        CPU address of buffer
    :type addr: void \*

    :param dma:
        DMA address of buffer
    :type dma: dma_addr_t

.. _`usb_free_coherent.description`:

Description
-----------

This reclaims an I/O buffer, letting it be reused.  The memory must have
been allocated using \ :c:func:`usb_alloc_coherent`\ , and the parameters must match
those provided in that allocation request.

.. _`usb_buffer_map`:

usb_buffer_map
==============

.. c:function:: struct urb *usb_buffer_map(struct urb *urb)

    create DMA mapping(s) for an urb

    :param urb:
        urb whose transfer_buffer/setup_packet will be mapped
    :type urb: struct urb \*

.. _`usb_buffer_map.description`:

Description
-----------

URB_NO_TRANSFER_DMA_MAP is added to urb->transfer_flags if the operation
succeeds. If the device is connected to this system through a non-DMA
controller, this operation always succeeds.

This call would normally be used for an urb which is reused, perhaps
as the target of a large periodic transfer, with \ :c:func:`usb_buffer_dmasync`\ 
calls to synchronize memory and dma state.

Reverse the effect of this call with \ :c:func:`usb_buffer_unmap`\ .

.. _`usb_buffer_map.return`:

Return
------

Either \ ``NULL``\  (indicating no buffer could be mapped), or \ ``urb``\ .

.. _`usb_buffer_dmasync`:

usb_buffer_dmasync
==================

.. c:function:: void usb_buffer_dmasync(struct urb *urb)

    synchronize DMA and CPU view of buffer(s)

    :param urb:
        urb whose transfer_buffer/setup_packet will be synchronized
    :type urb: struct urb \*

.. _`usb_buffer_unmap`:

usb_buffer_unmap
================

.. c:function:: void usb_buffer_unmap(struct urb *urb)

    free DMA mapping(s) for an urb

    :param urb:
        urb whose transfer_buffer will be unmapped
    :type urb: struct urb \*

.. _`usb_buffer_unmap.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_buffer_map`\ .

.. _`usb_buffer_map_sg`:

usb_buffer_map_sg
=================

.. c:function:: int usb_buffer_map_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int nents)

    create scatterlist DMA mapping(s) for an endpoint

    :param dev:
        device to which the scatterlist will be mapped
    :type dev: const struct usb_device \*

    :param is_in:
        mapping transfer direction
    :type is_in: int

    :param sg:
        the scatterlist to map
    :type sg: struct scatterlist \*

    :param nents:
        the number of entries in the scatterlist
    :type nents: int

.. _`usb_buffer_map_sg.return`:

Return
------

Either < 0 (indicating no buffers could be mapped), or the
number of DMA mapping array entries in the scatterlist.

.. _`usb_buffer_map_sg.note`:

Note
----

The caller is responsible for placing the resulting DMA addresses from
the scatterlist into URB transfer buffer pointers, and for setting the
URB_NO_TRANSFER_DMA_MAP transfer flag in each of those URBs.

Top I/O rates come from queuing URBs, instead of waiting for each one
to complete before starting the next I/O.   This is particularly easy
to do with scatterlists.  Just allocate and submit one URB for each DMA
mapping entry returned, stopping on the first error or when all succeed.
Better yet, use the usb_sg_*() calls, which do that (and more) for you.

This call would normally be used when translating scatterlist requests,
rather than \ :c:func:`usb_buffer_map`\ , since on some hardware (with IOMMUs) it
may be able to coalesce mappings for improved I/O efficiency.

Reverse the effect of this call with \ :c:func:`usb_buffer_unmap_sg`\ .

.. _`usb_buffer_dmasync_sg`:

usb_buffer_dmasync_sg
=====================

.. c:function:: void usb_buffer_dmasync_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int n_hw_ents)

    synchronize DMA and CPU view of scatterlist buffer(s)

    :param dev:
        device to which the scatterlist will be mapped
    :type dev: const struct usb_device \*

    :param is_in:
        mapping transfer direction
    :type is_in: int

    :param sg:
        the scatterlist to synchronize
    :type sg: struct scatterlist \*

    :param n_hw_ents:
        the positive return value from usb_buffer_map_sg
    :type n_hw_ents: int

.. _`usb_buffer_dmasync_sg.description`:

Description
-----------

Use this when you are re-using a scatterlist's data buffers for
another USB request.

.. _`usb_buffer_unmap_sg`:

usb_buffer_unmap_sg
===================

.. c:function:: void usb_buffer_unmap_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int n_hw_ents)

    free DMA mapping(s) for a scatterlist

    :param dev:
        device to which the scatterlist will be mapped
    :type dev: const struct usb_device \*

    :param is_in:
        mapping transfer direction
    :type is_in: int

    :param sg:
        the scatterlist to unmap
    :type sg: struct scatterlist \*

    :param n_hw_ents:
        the positive return value from usb_buffer_map_sg
    :type n_hw_ents: int

.. _`usb_buffer_unmap_sg.description`:

Description
-----------

Reverses the effect of \ :c:func:`usb_buffer_map_sg`\ .

.. This file was automatic generated / don't edit.

