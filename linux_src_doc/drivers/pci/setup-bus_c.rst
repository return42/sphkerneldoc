.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/setup-bus.c

.. _`add_to_list`:

add_to_list
===========

.. c:function:: int add_to_list(struct list_head *head, struct pci_dev *dev, struct resource *res, resource_size_t add_size, resource_size_t min_align)

    add a new resource tracker to the list

    :param struct list_head \*head:
        Head of the list

    :param struct pci_dev \*dev:
        device corresponding to which the resource
        belongs

    :param struct resource \*res:
        The resource to be tracked

    :param resource_size_t add_size:
        additional size to be optionally added
        to the resource

    :param resource_size_t min_align:
        *undescribed*

.. _`reassign_resources_sorted`:

reassign_resources_sorted
=========================

.. c:function:: void reassign_resources_sorted(struct list_head *realloc_head, struct list_head *head)

    satisfy any additional resource requests

    :param struct list_head \*realloc_head:
        head of the list tracking requests requiring additional
        resources

    :param struct list_head \*head:
        head of the list tracking requests with allocated
        resources

.. _`reassign_resources_sorted.description`:

Description
-----------

Walk through each element of the realloc_head and try to procure
additional resources for the element, provided the element
is in the head list.

.. _`assign_requested_resources_sorted`:

assign_requested_resources_sorted
=================================

.. c:function:: void assign_requested_resources_sorted(struct list_head *head, struct list_head *fail_head)

    satisfy resource requests

    :param struct list_head \*head:
        head of the list tracking requests for resources

    :param struct list_head \*fail_head:
        head of the list tracking requests that could
        not be allocated

.. _`assign_requested_resources_sorted.description`:

Description
-----------

Satisfy resource requests of each element in the list. Add
requests that could not satisfied to the failed_list.

.. _`pbus_size_io`:

pbus_size_io
============

.. c:function:: void pbus_size_io(struct pci_bus *bus, resource_size_t min_size, resource_size_t add_size, struct list_head *realloc_head)

    size the io window of a given bus

    :param struct pci_bus \*bus:
        the bus

    :param resource_size_t min_size:
        the minimum io window that must to be allocated

    :param resource_size_t add_size:
        additional optional io window

    :param struct list_head \*realloc_head:
        track the additional io window on this list

.. _`pbus_size_io.description`:

Description
-----------

Sizing the IO windows of the PCI-PCI bridge is trivial,
since these windows have 1K or 4K granularity and the IO ranges
of non-bridge PCI devices are limited to 256 bytes.
We must be careful with the ISA aliasing though.

.. _`pbus_size_mem`:

pbus_size_mem
=============

.. c:function:: int pbus_size_mem(struct pci_bus *bus, unsigned long mask, unsigned long type, unsigned long type2, unsigned long type3, resource_size_t min_size, resource_size_t add_size, struct list_head *realloc_head)

    size the memory window of a given bus

    :param struct pci_bus \*bus:
        the bus

    :param unsigned long mask:
        mask the resource flag, then compare it with type

    :param unsigned long type:
        the type of free resource from bridge

    :param unsigned long type2:
        second match type

    :param unsigned long type3:
        third match type

    :param resource_size_t min_size:
        the minimum memory window that must to be allocated

    :param resource_size_t add_size:
        additional optional memory window

    :param struct list_head \*realloc_head:
        track the additional memory window on this list

.. _`pbus_size_mem.description`:

Description
-----------

Calculate the size of the bus and minimal alignment which
guarantees that all child resources fit in this size.

Returns -ENOSPC if there's no available bus resource of the desired type.
Otherwise, sets the bus resource start/end to indicate the required
size, adds things to realloc_head (if supplied), and returns 0.

.. This file was automatic generated / don't edit.

