.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/setup-bus.c

.. _`add_to_list`:

add_to_list
===========

.. c:function:: int add_to_list(struct list_head *head, struct pci_dev *dev, struct resource *res, resource_size_t add_size, resource_size_t min_align)

    add a new resource tracker to the list

    :param head:
        Head of the list
    :type head: struct list_head \*

    :param dev:
        device corresponding to which the resource
        belongs
    :type dev: struct pci_dev \*

    :param res:
        The resource to be tracked
    :type res: struct resource \*

    :param add_size:
        additional size to be optionally added
        to the resource
    :type add_size: resource_size_t

    :param min_align:
        *undescribed*
    :type min_align: resource_size_t

.. _`reassign_resources_sorted`:

reassign_resources_sorted
=========================

.. c:function:: void reassign_resources_sorted(struct list_head *realloc_head, struct list_head *head)

    satisfy any additional resource requests

    :param realloc_head:
        head of the list tracking requests requiring additional
        resources
    :type realloc_head: struct list_head \*

    :param head:
        head of the list tracking requests with allocated
        resources
    :type head: struct list_head \*

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

    :param head:
        head of the list tracking requests for resources
    :type head: struct list_head \*

    :param fail_head:
        head of the list tracking requests that could
        not be allocated
    :type fail_head: struct list_head \*

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

    :param bus:
        the bus
    :type bus: struct pci_bus \*

    :param min_size:
        the minimum io window that must to be allocated
    :type min_size: resource_size_t

    :param add_size:
        additional optional io window
    :type add_size: resource_size_t

    :param realloc_head:
        track the additional io window on this list
    :type realloc_head: struct list_head \*

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

    :param bus:
        the bus
    :type bus: struct pci_bus \*

    :param mask:
        mask the resource flag, then compare it with type
    :type mask: unsigned long

    :param type:
        the type of free resource from bridge
    :type type: unsigned long

    :param type2:
        second match type
    :type type2: unsigned long

    :param type3:
        third match type
    :type type3: unsigned long

    :param min_size:
        the minimum memory window that must to be allocated
    :type min_size: resource_size_t

    :param add_size:
        additional optional memory window
    :type add_size: resource_size_t

    :param realloc_head:
        track the additional memory window on this list
    :type realloc_head: struct list_head \*

.. _`pbus_size_mem.description`:

Description
-----------

Calculate the size of the bus and minimal alignment which
guarantees that all child resources fit in this size.

Returns -ENOSPC if there's no available bus resource of the desired type.
Otherwise, sets the bus resource start/end to indicate the required
size, adds things to realloc_head (if supplied), and returns 0.

.. This file was automatic generated / don't edit.

