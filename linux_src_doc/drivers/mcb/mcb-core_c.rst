.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mcb/mcb-core.c

.. _`__mcb_register_driver`:

__mcb_register_driver
=====================

.. c:function:: int __mcb_register_driver(struct mcb_driver *drv, struct module *owner, const char *mod_name)

    Register a \ ``mcb_driver``\  at the system

    :param struct mcb_driver \*drv:
        The \ ``mcb_driver``\ 

    :param struct module \*owner:
        The \ ``mcb_driver``\ 's module

    :param const char \*mod_name:
        The name of the \ ``mcb_driver``\ 's module

.. _`__mcb_register_driver.description`:

Description
-----------

Register a \ ``mcb_driver``\  at the system. Perform some sanity checks, if
the .probe and .remove methods are provided by the driver.

.. _`mcb_unregister_driver`:

mcb_unregister_driver
=====================

.. c:function:: void mcb_unregister_driver(struct mcb_driver *drv)

    Unregister a \ ``mcb_driver``\  from the system

    :param struct mcb_driver \*drv:
        The \ ``mcb_driver``\ 

.. _`mcb_unregister_driver.description`:

Description
-----------

Unregister a \ ``mcb_driver``\  from the system.

.. _`mcb_device_register`:

mcb_device_register
===================

.. c:function:: int mcb_device_register(struct mcb_bus *bus, struct mcb_device *dev)

    Register a mcb_device

    :param struct mcb_bus \*bus:
        The \ ``mcb_bus``\  of the device

    :param struct mcb_device \*dev:
        The \ ``mcb_device``\ 

.. _`mcb_device_register.description`:

Description
-----------

Register a specific \ ``mcb_device``\  at a \ ``mcb_bus``\  and the system itself.

.. _`mcb_alloc_bus`:

mcb_alloc_bus
=============

.. c:function:: struct mcb_bus *mcb_alloc_bus(struct device *carrier)

    Allocate a new \ ``mcb_bus``\ 

    :param struct device \*carrier:
        *undescribed*

.. _`mcb_alloc_bus.description`:

Description
-----------

Allocate a new \ ``mcb_bus``\ .

.. _`mcb_release_bus`:

mcb_release_bus
===============

.. c:function:: void mcb_release_bus(struct mcb_bus *bus)

    Free a \ ``mcb_bus``\ 

    :param struct mcb_bus \*bus:
        The \ ``mcb_bus``\  to release

.. _`mcb_release_bus.description`:

Description
-----------

Release an allocated \ ``mcb_bus``\  from the system.

.. _`mcb_bus_get`:

mcb_bus_get
===========

.. c:function:: struct mcb_bus *mcb_bus_get(struct mcb_bus *bus)

    Increment refcnt

    :param struct mcb_bus \*bus:
        The \ ``mcb_bus``\ 

.. _`mcb_bus_get.description`:

Description
-----------

Get a \ ``mcb_bus``\ ' ref

.. _`mcb_bus_put`:

mcb_bus_put
===========

.. c:function:: void mcb_bus_put(struct mcb_bus *bus)

    Decrement refcnt

    :param struct mcb_bus \*bus:
        The \ ``mcb_bus``\ 

.. _`mcb_bus_put.description`:

Description
-----------

Release a \ ``mcb_bus``\ ' ref

.. _`mcb_alloc_dev`:

mcb_alloc_dev
=============

.. c:function:: struct mcb_device *mcb_alloc_dev(struct mcb_bus *bus)

    Allocate a device

    :param struct mcb_bus \*bus:
        The \ ``mcb_bus``\  the device is part of

.. _`mcb_alloc_dev.description`:

Description
-----------

Allocate a \ ``mcb_device``\  and add bus.

.. _`mcb_free_dev`:

mcb_free_dev
============

.. c:function:: void mcb_free_dev(struct mcb_device *dev)

    Free \ ``mcb_device``\ 

    :param struct mcb_device \*dev:
        The device to free

.. _`mcb_free_dev.description`:

Description
-----------

Free a \ ``mcb_device``\ 

.. _`mcb_bus_add_devices`:

mcb_bus_add_devices
===================

.. c:function:: void mcb_bus_add_devices(const struct mcb_bus *bus)

    Add devices in the bus' internal device list

    :param const struct mcb_bus \*bus:
        The \ ``mcb_bus``\  we add the devices

.. _`mcb_bus_add_devices.description`:

Description
-----------

Add devices in the bus' internal device list to the system.

.. _`mcb_get_resource`:

mcb_get_resource
================

.. c:function:: struct resource *mcb_get_resource(struct mcb_device *dev, unsigned int type)

    get a resource for a mcb device

    :param struct mcb_device \*dev:
        the mcb device

    :param unsigned int type:
        the type of resource

.. _`mcb_request_mem`:

mcb_request_mem
===============

.. c:function:: struct resource *mcb_request_mem(struct mcb_device *dev, const char *name)

    Request memory

    :param struct mcb_device \*dev:
        The \ ``mcb_device``\  the memory is for

    :param const char \*name:
        The name for the memory reference.

.. _`mcb_request_mem.description`:

Description
-----------

Request memory for a \ ``mcb_device``\ . If \ ``name``\  is NULL the driver name will
be used.

.. _`mcb_release_mem`:

mcb_release_mem
===============

.. c:function:: void mcb_release_mem(struct resource *mem)

    Release memory requested by device

    :param struct resource \*mem:
        *undescribed*

.. _`mcb_release_mem.description`:

Description
-----------

Release memory that was prior requested via \ ``mcb_request_mem``\ ().

.. _`mcb_get_irq`:

mcb_get_irq
===========

.. c:function:: int mcb_get_irq(struct mcb_device *dev)

    Get device's IRQ number

    :param struct mcb_device \*dev:
        The \ ``mcb_device``\  the IRQ is for

.. _`mcb_get_irq.description`:

Description
-----------

Get the IRQ number of a given \ ``mcb_device``\ .

.. This file was automatic generated / don't edit.

