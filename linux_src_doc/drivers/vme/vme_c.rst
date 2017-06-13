.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/vme/vme.c

.. _`vme_alloc_consistent`:

vme_alloc_consistent
====================

.. c:function:: void *vme_alloc_consistent(struct vme_resource *resource, size_t size, dma_addr_t *dma)

    Allocate contiguous memory.

    :param struct vme_resource \*resource:
        Pointer to VME resource.

    :param size_t size:
        Size of allocation required.

    :param dma_addr_t \*dma:
        Pointer to variable to store physical address of allocation.

.. _`vme_alloc_consistent.description`:

Description
-----------

Allocate a contiguous block of memory for use by the driver. This is used to
create the buffers for the slave windows.

.. _`vme_alloc_consistent.return`:

Return
------

Virtual address of allocation on success, NULL on failure.

.. _`vme_free_consistent`:

vme_free_consistent
===================

.. c:function:: void vme_free_consistent(struct vme_resource *resource, size_t size, void *vaddr, dma_addr_t dma)

    Free previously allocated memory.

    :param struct vme_resource \*resource:
        Pointer to VME resource.

    :param size_t size:
        Size of allocation to free.

    :param void \*vaddr:
        Virtual address of allocation.

    :param dma_addr_t dma:
        Physical address of allocation.

.. _`vme_free_consistent.description`:

Description
-----------

Free previously allocated block of contiguous memory.

.. _`vme_get_size`:

vme_get_size
============

.. c:function:: size_t vme_get_size(struct vme_resource *resource)

    Helper function returning size of a VME window

    :param struct vme_resource \*resource:
        Pointer to VME slave or master resource.

.. _`vme_get_size.description`:

Description
-----------

Determine the size of the VME window provided. This is a helper
function, wrappering the call to vme_master_get or vme_slave_get
depending on the type of window resource handed to it.

.. _`vme_get_size.return`:

Return
------

Size of the window on success, zero on failure.

.. _`vme_slave_request`:

vme_slave_request
=================

.. c:function:: struct vme_resource *vme_slave_request(struct vme_dev *vdev, u32 address, u32 cycle)

    Request a VME slave window resource.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param u32 address:
        Required VME address space.

    :param u32 cycle:
        Required VME data transfer cycle type.

.. _`vme_slave_request.description`:

Description
-----------

Request use of a VME window resource capable of being set for the requested
address space and data transfer cycle.

.. _`vme_slave_request.return`:

Return
------

Pointer to VME resource on success, NULL on failure.

.. _`vme_slave_set`:

vme_slave_set
=============

.. c:function:: int vme_slave_set(struct vme_resource *resource, int enabled, unsigned long long vme_base, unsigned long long size, dma_addr_t buf_base, u32 aspace, u32 cycle)

    Set VME slave window configuration.

    :param struct vme_resource \*resource:
        Pointer to VME slave resource.

    :param int enabled:
        State to which the window should be configured.

    :param unsigned long long vme_base:
        Base address for the window.

    :param unsigned long long size:
        Size of the VME window.

    :param dma_addr_t buf_base:
        Based address of buffer used to provide VME slave window storage.

    :param u32 aspace:
        VME address space for the VME window.

    :param u32 cycle:
        VME data transfer cycle type for the VME window.

.. _`vme_slave_set.description`:

Description
-----------

Set configuration for provided VME slave window.

.. _`vme_slave_set.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device, if an invalid resource has been provided or invalid
        attributes are provided. Hardware specific errors may also be
        returned.

.. _`vme_slave_get`:

vme_slave_get
=============

.. c:function:: int vme_slave_get(struct vme_resource *resource, int *enabled, unsigned long long *vme_base, unsigned long long *size, dma_addr_t *buf_base, u32 *aspace, u32 *cycle)

    Retrieve VME slave window configuration.

    :param struct vme_resource \*resource:
        Pointer to VME slave resource.

    :param int \*enabled:
        Pointer to variable for storing state.

    :param unsigned long long \*vme_base:
        Pointer to variable for storing window base address.

    :param unsigned long long \*size:
        Pointer to variable for storing window size.

    :param dma_addr_t \*buf_base:
        Pointer to variable for storing slave buffer base address.

    :param u32 \*aspace:
        Pointer to variable for storing VME address space.

    :param u32 \*cycle:
        Pointer to variable for storing VME data transfer cycle type.

.. _`vme_slave_get.description`:

Description
-----------

Return configuration for provided VME slave window.

.. _`vme_slave_get.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device or if an invalid resource has been provided.

.. _`vme_slave_free`:

vme_slave_free
==============

.. c:function:: void vme_slave_free(struct vme_resource *resource)

    Free VME slave window

    :param struct vme_resource \*resource:
        Pointer to VME slave resource.

.. _`vme_slave_free.description`:

Description
-----------

Free the provided slave resource so that it may be reallocated.

.. _`vme_master_request`:

vme_master_request
==================

.. c:function:: struct vme_resource *vme_master_request(struct vme_dev *vdev, u32 address, u32 cycle, u32 dwidth)

    Request a VME master window resource.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param u32 address:
        Required VME address space.

    :param u32 cycle:
        Required VME data transfer cycle type.

    :param u32 dwidth:
        Required VME data transfer width.

.. _`vme_master_request.description`:

Description
-----------

Request use of a VME window resource capable of being set for the requested
address space, data transfer cycle and width.

.. _`vme_master_request.return`:

Return
------

Pointer to VME resource on success, NULL on failure.

.. _`vme_master_set`:

vme_master_set
==============

.. c:function:: int vme_master_set(struct vme_resource *resource, int enabled, unsigned long long vme_base, unsigned long long size, u32 aspace, u32 cycle, u32 dwidth)

    Set VME master window configuration.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param int enabled:
        State to which the window should be configured.

    :param unsigned long long vme_base:
        Base address for the window.

    :param unsigned long long size:
        Size of the VME window.

    :param u32 aspace:
        VME address space for the VME window.

    :param u32 cycle:
        VME data transfer cycle type for the VME window.

    :param u32 dwidth:
        VME data transfer width for the VME window.

.. _`vme_master_set.description`:

Description
-----------

Set configuration for provided VME master window.

.. _`vme_master_set.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device, if an invalid resource has been provided or invalid
        attributes are provided. Hardware specific errors may also be
        returned.

.. _`vme_master_get`:

vme_master_get
==============

.. c:function:: int vme_master_get(struct vme_resource *resource, int *enabled, unsigned long long *vme_base, unsigned long long *size, u32 *aspace, u32 *cycle, u32 *dwidth)

    Retrieve VME master window configuration.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param int \*enabled:
        Pointer to variable for storing state.

    :param unsigned long long \*vme_base:
        Pointer to variable for storing window base address.

    :param unsigned long long \*size:
        Pointer to variable for storing window size.

    :param u32 \*aspace:
        Pointer to variable for storing VME address space.

    :param u32 \*cycle:
        Pointer to variable for storing VME data transfer cycle type.

    :param u32 \*dwidth:
        Pointer to variable for storing VME data transfer width.

.. _`vme_master_get.description`:

Description
-----------

Return configuration for provided VME master window.

.. _`vme_master_get.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device or if an invalid resource has been provided.

.. _`vme_master_read`:

vme_master_read
===============

.. c:function:: ssize_t vme_master_read(struct vme_resource *resource, void *buf, size_t count, loff_t offset)

    Read data from VME space into a buffer.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param void \*buf:
        Pointer to buffer where data should be transferred.

    :param size_t count:
        Number of bytes to transfer.

    :param loff_t offset:
        Offset into VME master window at which to start transfer.

.. _`vme_master_read.description`:

Description
-----------

Perform read of count bytes of data from location on VME bus which maps into
the VME master window at offset to buf.

.. _`vme_master_read.return`:

Return
------

Number of bytes read, -EINVAL if resource is not a VME master
        resource or read operation is not supported. -EFAULT returned if
        invalid offset is provided. Hardware specific errors may also be
        returned.

.. _`vme_master_write`:

vme_master_write
================

.. c:function:: ssize_t vme_master_write(struct vme_resource *resource, void *buf, size_t count, loff_t offset)

    Write data out to VME space from a buffer.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param void \*buf:
        Pointer to buffer holding data to transfer.

    :param size_t count:
        Number of bytes to transfer.

    :param loff_t offset:
        Offset into VME master window at which to start transfer.

.. _`vme_master_write.description`:

Description
-----------

Perform write of count bytes of data from buf to location on VME bus which
maps into the VME master window at offset.

.. _`vme_master_write.return`:

Return
------

Number of bytes written, -EINVAL if resource is not a VME master
        resource or write operation is not supported. -EFAULT returned if
        invalid offset is provided. Hardware specific errors may also be
        returned.

.. _`vme_master_rmw`:

vme_master_rmw
==============

.. c:function:: unsigned int vme_master_rmw(struct vme_resource *resource, unsigned int mask, unsigned int compare, unsigned int swap, loff_t offset)

    Perform read-modify-write cycle.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param unsigned int mask:
        Bits to be compared and swapped in operation.

    :param unsigned int compare:
        Bits to be compared with data read from offset.

    :param unsigned int swap:
        Bits to be swapped in data read from offset.

    :param loff_t offset:
        Offset into VME master window at which to perform operation.

.. _`vme_master_rmw.description`:

Description
-----------

Perform read-modify-write cycle on provided location:
- Location on VME bus is read.
- Bits selected by mask are compared with compare.
- Where a selected bit matches that in compare and are selected in swap,
the bit is swapped.
- Result written back to location on VME bus.

.. _`vme_master_rmw.return`:

Return
------

Bytes written on success, -EINVAL if resource is not a VME master
        resource or RMW operation is not supported. Hardware specific
        errors may also be returned.

.. _`vme_master_mmap`:

vme_master_mmap
===============

.. c:function:: int vme_master_mmap(struct vme_resource *resource, struct vm_area_struct *vma)

    Mmap region of VME master window.

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

    :param struct vm_area_struct \*vma:
        Pointer to definition of user mapping.

.. _`vme_master_mmap.description`:

Description
-----------

Memory map a region of the VME master window into user space.

.. _`vme_master_mmap.return`:

Return
------

Zero on success, -EINVAL if resource is not a VME master
        resource or -EFAULT if map exceeds window size. Other generic mmap
        errors may also be returned.

.. _`vme_master_free`:

vme_master_free
===============

.. c:function:: void vme_master_free(struct vme_resource *resource)

    Free VME master window

    :param struct vme_resource \*resource:
        Pointer to VME master resource.

.. _`vme_master_free.description`:

Description
-----------

Free the provided master resource so that it may be reallocated.

.. _`vme_dma_request`:

vme_dma_request
===============

.. c:function:: struct vme_resource *vme_dma_request(struct vme_dev *vdev, u32 route)

    Request a DMA controller.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param u32 route:
        Required src/destination combination.

.. _`vme_dma_request.description`:

Description
-----------

Request a VME DMA controller with capability to perform transfers bewteen
requested source/destination combination.

.. _`vme_dma_request.return`:

Return
------

Pointer to VME DMA resource on success, NULL on failure.

.. _`vme_new_dma_list`:

vme_new_dma_list
================

.. c:function:: struct vme_dma_list *vme_new_dma_list(struct vme_resource *resource)

    Create new VME DMA list.

    :param struct vme_resource \*resource:
        Pointer to VME DMA resource.

.. _`vme_new_dma_list.description`:

Description
-----------

Create a new VME DMA list. It is the responsibility of the user to free
the list once it is no longer required with \ :c:func:`vme_dma_list_free`\ .

.. _`vme_new_dma_list.return`:

Return
------

Pointer to new VME DMA list, NULL on allocation failure or invalid
        VME DMA resource.

.. _`vme_dma_pattern_attribute`:

vme_dma_pattern_attribute
=========================

.. c:function:: struct vme_dma_attr *vme_dma_pattern_attribute(u32 pattern, u32 type)

    Create "Pattern" type VME DMA list attribute.

    :param u32 pattern:
        Value to use used as pattern

    :param u32 type:
        Type of pattern to be written.

.. _`vme_dma_pattern_attribute.description`:

Description
-----------

Create VME DMA list attribute for pattern generation. It is the
responsibility of the user to free used attributes using
\ :c:func:`vme_dma_free_attribute`\ .

.. _`vme_dma_pattern_attribute.return`:

Return
------

Pointer to VME DMA attribute, NULL on failure.

.. _`vme_dma_pci_attribute`:

vme_dma_pci_attribute
=====================

.. c:function:: struct vme_dma_attr *vme_dma_pci_attribute(dma_addr_t address)

    Create "PCI" type VME DMA list attribute.

    :param dma_addr_t address:
        PCI base address for DMA transfer.

.. _`vme_dma_pci_attribute.description`:

Description
-----------

Create VME DMA list attribute pointing to a location on PCI for DMA
transfers. It is the responsibility of the user to free used attributes
using \ :c:func:`vme_dma_free_attribute`\ .

.. _`vme_dma_pci_attribute.return`:

Return
------

Pointer to VME DMA attribute, NULL on failure.

.. _`vme_dma_vme_attribute`:

vme_dma_vme_attribute
=====================

.. c:function:: struct vme_dma_attr *vme_dma_vme_attribute(unsigned long long address, u32 aspace, u32 cycle, u32 dwidth)

    Create "VME" type VME DMA list attribute.

    :param unsigned long long address:
        VME base address for DMA transfer.

    :param u32 aspace:
        VME address space to use for DMA transfer.

    :param u32 cycle:
        VME bus cycle to use for DMA transfer.

    :param u32 dwidth:
        VME data width to use for DMA transfer.

.. _`vme_dma_vme_attribute.description`:

Description
-----------

Create VME DMA list attribute pointing to a location on the VME bus for DMA
transfers. It is the responsibility of the user to free used attributes
using \ :c:func:`vme_dma_free_attribute`\ .

.. _`vme_dma_vme_attribute.return`:

Return
------

Pointer to VME DMA attribute, NULL on failure.

.. _`vme_dma_free_attribute`:

vme_dma_free_attribute
======================

.. c:function:: void vme_dma_free_attribute(struct vme_dma_attr *attributes)

    Free DMA list attribute.

    :param struct vme_dma_attr \*attributes:
        Pointer to DMA list attribute.

.. _`vme_dma_free_attribute.description`:

Description
-----------

Free VME DMA list attribute. VME DMA list attributes can be safely freed
once \ :c:func:`vme_dma_list_add`\  has returned.

.. _`vme_dma_list_add`:

vme_dma_list_add
================

.. c:function:: int vme_dma_list_add(struct vme_dma_list *list, struct vme_dma_attr *src, struct vme_dma_attr *dest, size_t count)

    Add enty to a VME DMA list.

    :param struct vme_dma_list \*list:
        Pointer to VME list.

    :param struct vme_dma_attr \*src:
        Pointer to DMA list attribute to use as source.

    :param struct vme_dma_attr \*dest:
        Pointer to DMA list attribute to use as destination.

    :param size_t count:
        Number of bytes to transfer.

.. _`vme_dma_list_add.description`:

Description
-----------

Add an entry to the provided VME DMA list. Entry requires pointers to source
and destination DMA attributes and a count.

Please note, the attributes supported as source and destinations for
transfers are hardware dependent.

.. _`vme_dma_list_add.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device or if the link list has already been submitted for execution.
        Hardware specific errors also possible.

.. _`vme_dma_list_exec`:

vme_dma_list_exec
=================

.. c:function:: int vme_dma_list_exec(struct vme_dma_list *list)

    Queue a VME DMA list for execution.

    :param struct vme_dma_list \*list:
        Pointer to VME list.

.. _`vme_dma_list_exec.description`:

Description
-----------

Queue the provided VME DMA list for execution. The call will return once the
list has been executed.

.. _`vme_dma_list_exec.return`:

Return
------

Zero on success, -EINVAL if operation is not supported on this
        device. Hardware specific errors also possible.

.. _`vme_dma_list_free`:

vme_dma_list_free
=================

.. c:function:: int vme_dma_list_free(struct vme_dma_list *list)

    Free a VME DMA list.

    :param struct vme_dma_list \*list:
        Pointer to VME list.

.. _`vme_dma_list_free.description`:

Description
-----------

Free the provided DMA list and all its entries.

.. _`vme_dma_list_free.return`:

Return
------

Zero on success, -EINVAL on invalid VME resource, -EBUSY if resource
        is still in use. Hardware specific errors also possible.

.. _`vme_dma_free`:

vme_dma_free
============

.. c:function:: int vme_dma_free(struct vme_resource *resource)

    Free a VME DMA resource.

    :param struct vme_resource \*resource:
        Pointer to VME DMA resource.

.. _`vme_dma_free.description`:

Description
-----------

Free the provided DMA resource so that it may be reallocated.

.. _`vme_dma_free.return`:

Return
------

Zero on success, -EINVAL on invalid VME resource, -EBUSY if resource
        is still active.

.. _`vme_irq_request`:

vme_irq_request
===============

.. c:function:: int vme_irq_request(struct vme_dev *vdev, int level, int statid, void (*callback)(int, int, void *), void *priv_data)

    Request a specific VME interrupt.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param int level:
        Interrupt priority being requested.

    :param int statid:
        Interrupt vector being requested.

    :param void (\*callback)(int, int, void \*):
        Pointer to callback function called when VME interrupt/vector
        received.

    :param void \*priv_data:
        Generic pointer that will be passed to the callback function.

.. _`vme_irq_request.description`:

Description
-----------

Request callback to be attached as a handler for VME interrupts with provided
level and statid.

.. _`vme_irq_request.return`:

Return
------

Zero on success, -EINVAL on invalid vme device, level or if the
        function is not supported, -EBUSY if the level/statid combination is
        already in use. Hardware specific errors also possible.

.. _`vme_irq_free`:

vme_irq_free
============

.. c:function:: void vme_irq_free(struct vme_dev *vdev, int level, int statid)

    Free a VME interrupt.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param int level:
        Interrupt priority of interrupt being freed.

    :param int statid:
        Interrupt vector of interrupt being freed.

.. _`vme_irq_free.description`:

Description
-----------

Remove previously attached callback from VME interrupt priority/vector.

.. _`vme_irq_generate`:

vme_irq_generate
================

.. c:function:: int vme_irq_generate(struct vme_dev *vdev, int level, int statid)

    Generate VME interrupt.

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

    :param int level:
        Interrupt priority at which to assert the interrupt.

    :param int statid:
        Interrupt vector to associate with the interrupt.

.. _`vme_irq_generate.description`:

Description
-----------

Generate a VME interrupt of the provided level and with the provided
statid.

.. _`vme_irq_generate.return`:

Return
------

Zero on success, -EINVAL on invalid vme device, level or if the
        function is not supported. Hardware specific errors also possible.

.. _`vme_lm_request`:

vme_lm_request
==============

.. c:function:: struct vme_resource *vme_lm_request(struct vme_dev *vdev)

    Request a VME location monitor

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

.. _`vme_lm_request.description`:

Description
-----------

Allocate a location monitor resource to the driver. A location monitor
allows the driver to monitor accesses to a contiguous number of
addresses on the VME bus.

.. _`vme_lm_request.return`:

Return
------

Pointer to a VME resource on success or NULL on failure.

.. _`vme_lm_count`:

vme_lm_count
============

.. c:function:: int vme_lm_count(struct vme_resource *resource)

    Determine number of VME Addresses monitored

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

.. _`vme_lm_count.description`:

Description
-----------

The number of contiguous addresses monitored is hardware dependent.
Return the number of contiguous addresses monitored by the
location monitor.

.. _`vme_lm_count.return`:

Return
------

Count of addresses monitored or -EINVAL when provided with an
        invalid location monitor resource.

.. _`vme_lm_set`:

vme_lm_set
==========

.. c:function:: int vme_lm_set(struct vme_resource *resource, unsigned long long lm_base, u32 aspace, u32 cycle)

    Configure location monitor

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

    :param unsigned long long lm_base:
        Base address to monitor.

    :param u32 aspace:
        VME address space to monitor.

    :param u32 cycle:
        VME bus cycle type to monitor.

.. _`vme_lm_set.description`:

Description
-----------

Set the base address, address space and cycle type of accesses to be
monitored by the location monitor.

.. _`vme_lm_set.return`:

Return
------

Zero on success, -EINVAL when provided with an invalid location
        monitor resource or function is not supported. Hardware specific
        errors may also be returned.

.. _`vme_lm_get`:

vme_lm_get
==========

.. c:function:: int vme_lm_get(struct vme_resource *resource, unsigned long long *lm_base, u32 *aspace, u32 *cycle)

    Retrieve location monitor settings

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

    :param unsigned long long \*lm_base:
        Pointer used to output the base address monitored.

    :param u32 \*aspace:
        Pointer used to output the address space monitored.

    :param u32 \*cycle:
        Pointer used to output the VME bus cycle type monitored.

.. _`vme_lm_get.description`:

Description
-----------

Retrieve the base address, address space and cycle type of accesses to
be monitored by the location monitor.

.. _`vme_lm_get.return`:

Return
------

Zero on success, -EINVAL when provided with an invalid location
        monitor resource or function is not supported. Hardware specific
        errors may also be returned.

.. _`vme_lm_attach`:

vme_lm_attach
=============

.. c:function:: int vme_lm_attach(struct vme_resource *resource, int monitor, void (*callback)(void *), void *data)

    Provide callback for location monitor address

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

    :param int monitor:
        Offset to which callback should be attached.

    :param void (\*callback)(void \*):
        Pointer to callback function called when triggered.

    :param void \*data:
        Generic pointer that will be passed to the callback function.

.. _`vme_lm_attach.description`:

Description
-----------

Attach a callback to the specificed offset into the location monitors
monitored addresses. A generic pointer is provided to allow data to be
passed to the callback when called.

.. _`vme_lm_attach.return`:

Return
------

Zero on success, -EINVAL when provided with an invalid location
        monitor resource or function is not supported. Hardware specific
        errors may also be returned.

.. _`vme_lm_detach`:

vme_lm_detach
=============

.. c:function:: int vme_lm_detach(struct vme_resource *resource, int monitor)

    Remove callback for location monitor address

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

    :param int monitor:
        Offset to which callback should be removed.

.. _`vme_lm_detach.description`:

Description
-----------

Remove the callback associated with the specificed offset into the
location monitors monitored addresses.

.. _`vme_lm_detach.return`:

Return
------

Zero on success, -EINVAL when provided with an invalid location
        monitor resource or function is not supported. Hardware specific
        errors may also be returned.

.. _`vme_lm_free`:

vme_lm_free
===========

.. c:function:: void vme_lm_free(struct vme_resource *resource)

    Free allocated VME location monitor

    :param struct vme_resource \*resource:
        Pointer to VME location monitor resource.

.. _`vme_lm_free.description`:

Description
-----------

Free allocation of a VME location monitor.

WARNING: This function currently expects that any callbacks that have
         been attached to the location monitor have been removed.

.. _`vme_lm_free.return`:

Return
------

Zero on success, -EINVAL when provided with an invalid location
        monitor resource.

.. _`vme_slot_num`:

vme_slot_num
============

.. c:function:: int vme_slot_num(struct vme_dev *vdev)

    Retrieve slot ID

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

.. _`vme_slot_num.description`:

Description
-----------

Retrieve the slot ID associated with the provided VME device.

.. _`vme_slot_num.return`:

Return
------

The slot ID on success, -EINVAL if VME bridge cannot be determined
        or the function is not supported. Hardware specific errors may also
        be returned.

.. _`vme_bus_num`:

vme_bus_num
===========

.. c:function:: int vme_bus_num(struct vme_dev *vdev)

    Retrieve bus number

    :param struct vme_dev \*vdev:
        Pointer to VME device struct vme_dev assigned to driver instance.

.. _`vme_bus_num.description`:

Description
-----------

Retrieve the bus enumeration associated with the provided VME device.

.. _`vme_bus_num.return`:

Return
------

The bus number on success, -EINVAL if VME bridge cannot be
        determined.

.. _`vme_register_driver`:

vme_register_driver
===================

.. c:function:: int vme_register_driver(struct vme_driver *drv, unsigned int ndevs)

    Register a VME driver

    :param struct vme_driver \*drv:
        Pointer to VME driver structure to register.

    :param unsigned int ndevs:
        Maximum number of devices to allow to be enumerated.

.. _`vme_register_driver.description`:

Description
-----------

Register a VME device driver with the VME subsystem.

.. _`vme_register_driver.return`:

Return
------

Zero on success, error value on registration failure.

.. _`vme_unregister_driver`:

vme_unregister_driver
=====================

.. c:function:: void vme_unregister_driver(struct vme_driver *drv)

    Unregister a VME driver

    :param struct vme_driver \*drv:
        Pointer to VME driver structure to unregister.

.. _`vme_unregister_driver.description`:

Description
-----------

Unregister a VME device driver from the VME subsystem.

.. This file was automatic generated / don't edit.

