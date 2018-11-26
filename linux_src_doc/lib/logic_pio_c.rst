.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/logic_pio.c

.. _`logic_pio_register_range`:

logic_pio_register_range
========================

.. c:function:: int logic_pio_register_range(struct logic_pio_hwaddr *new_range)

    register logical PIO range for a host

    :param new_range:
        pointer to the IO range to be registered.
    :type new_range: struct logic_pio_hwaddr \*

.. _`logic_pio_register_range.description`:

Description
-----------

Returns 0 on success, the error code in case of failure.

Register a new IO range node in the IO range list.

.. _`find_io_range_by_fwnode`:

find_io_range_by_fwnode
=======================

.. c:function:: struct logic_pio_hwaddr *find_io_range_by_fwnode(struct fwnode_handle *fwnode)

    find logical PIO range for given FW node

    :param fwnode:
        FW node handle associated with logical PIO range
    :type fwnode: struct fwnode_handle \*

.. _`find_io_range_by_fwnode.description`:

Description
-----------

Returns pointer to node on success, NULL otherwise.

Traverse the io_range_list to find the registered node for \ ``fwnode``\ .

.. _`logic_pio_to_hwaddr`:

logic_pio_to_hwaddr
===================

.. c:function:: resource_size_t logic_pio_to_hwaddr(unsigned long pio)

    translate logical PIO to HW address

    :param pio:
        logical PIO value
    :type pio: unsigned long

.. _`logic_pio_to_hwaddr.description`:

Description
-----------

Returns HW address if valid, ~0 otherwise.

Translate the input logical PIO to the corresponding hardware address.
The input PIO should be unique in the whole logical PIO space.

.. _`logic_pio_trans_hwaddr`:

logic_pio_trans_hwaddr
======================

.. c:function:: unsigned long logic_pio_trans_hwaddr(struct fwnode_handle *fwnode, resource_size_t addr, resource_size_t size)

    translate HW address to logical PIO

    :param fwnode:
        FW node reference for the host
    :type fwnode: struct fwnode_handle \*

    :param addr:
        Host-relative HW address
    :type addr: resource_size_t

    :param size:
        size to translate
    :type size: resource_size_t

.. _`logic_pio_trans_hwaddr.description`:

Description
-----------

Returns Logical PIO value if successful, ~0UL otherwise

.. This file was automatic generated / don't edit.

