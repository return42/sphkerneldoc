.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/host1x/bus.c

.. _`host1x_subdev_add`:

host1x_subdev_add
=================

.. c:function:: int host1x_subdev_add(struct host1x_device *device, struct host1x_driver *driver, struct device_node *np)

    add a new subdevice with an associated device node

    :param device:
        host1x device to add the subdevice to
    :type device: struct host1x_device \*

    :param driver:
        *undescribed*
    :type driver: struct host1x_driver \*

    :param np:
        device node
    :type np: struct device_node \*

.. _`host1x_subdev_del`:

host1x_subdev_del
=================

.. c:function:: void host1x_subdev_del(struct host1x_subdev *subdev)

    remove subdevice

    :param subdev:
        subdevice to remove
    :type subdev: struct host1x_subdev \*

.. _`host1x_device_parse_dt`:

host1x_device_parse_dt
======================

.. c:function:: int host1x_device_parse_dt(struct host1x_device *device, struct host1x_driver *driver)

    scan device tree and add matching subdevices

    :param device:
        host1x logical device
    :type device: struct host1x_device \*

    :param driver:
        host1x driver
    :type driver: struct host1x_driver \*

.. _`host1x_device_init`:

host1x_device_init
==================

.. c:function:: int host1x_device_init(struct host1x_device *device)

    initialize a host1x logical device

    :param device:
        host1x logical device
    :type device: struct host1x_device \*

.. _`host1x_device_init.description`:

Description
-----------

The driver for the host1x logical device can call this during execution of
its \ :c:type:`host1x_driver.probe <host1x_driver>`\  implementation to initialize each of its clients.
The client drivers access the subsystem specific driver data using the
\ :c:type:`host1x_client.parent <host1x_client>`\  field and driver data associated with it (usually by
calling \ :c:func:`dev_get_drvdata`\ ).

.. _`host1x_device_exit`:

host1x_device_exit
==================

.. c:function:: int host1x_device_exit(struct host1x_device *device)

    uninitialize host1x logical device

    :param device:
        host1x logical device
    :type device: struct host1x_device \*

.. _`host1x_device_exit.description`:

Description
-----------

When the driver for a host1x logical device is unloaded, it can call this
function to tear down each of its clients. Typically this is done after a
subsystem-specific data structure is removed and the functionality can no
longer be used.

.. _`host1x_register`:

host1x_register
===============

.. c:function:: int host1x_register(struct host1x *host1x)

    register a host1x controller

    :param host1x:
        host1x controller
    :type host1x: struct host1x \*

.. _`host1x_register.description`:

Description
-----------

The host1x controller driver uses this to register a host1x controller with
the infrastructure. Note that all Tegra SoC generations have only ever come
with a single host1x instance, so this function is somewhat academic.

.. _`host1x_unregister`:

host1x_unregister
=================

.. c:function:: int host1x_unregister(struct host1x *host1x)

    unregister a host1x controller

    :param host1x:
        host1x controller
    :type host1x: struct host1x \*

.. _`host1x_unregister.description`:

Description
-----------

The host1x controller driver uses this to remove a host1x controller from
the infrastructure.

.. _`host1x_driver_register_full`:

host1x_driver_register_full
===========================

.. c:function:: int host1x_driver_register_full(struct host1x_driver *driver, struct module *owner)

    register a host1x driver

    :param driver:
        host1x driver
    :type driver: struct host1x_driver \*

    :param owner:
        owner module
    :type owner: struct module \*

.. _`host1x_driver_register_full.description`:

Description
-----------

Drivers for host1x logical devices call this function to register a driver
with the infrastructure. Note that since these drive logical devices, the
registration of the driver actually triggers tho logical device creation.
A logical device will be created for each host1x instance.

.. _`host1x_driver_unregister`:

host1x_driver_unregister
========================

.. c:function:: void host1x_driver_unregister(struct host1x_driver *driver)

    unregister a host1x driver

    :param driver:
        host1x driver
    :type driver: struct host1x_driver \*

.. _`host1x_driver_unregister.description`:

Description
-----------

Unbinds the driver from each of the host1x logical devices that it is
bound to, effectively removing the subsystem devices that they represent.

.. _`host1x_client_register`:

host1x_client_register
======================

.. c:function:: int host1x_client_register(struct host1x_client *client)

    register a host1x client

    :param client:
        host1x client
    :type client: struct host1x_client \*

.. _`host1x_client_register.description`:

Description
-----------

Registers a host1x client with each host1x controller instance. Note that
each client will only match their parent host1x controller and will only be
associated with that instance. Once all clients have been registered with
their parent host1x controller, the infrastructure will set up the logical
device and call \ :c:func:`host1x_device_init`\ , which will in turn call each client's
\ :c:type:`host1x_client_ops.init <host1x_client_ops>`\  implementation.

.. _`host1x_client_unregister`:

host1x_client_unregister
========================

.. c:function:: int host1x_client_unregister(struct host1x_client *client)

    unregister a host1x client

    :param client:
        host1x client
    :type client: struct host1x_client \*

.. _`host1x_client_unregister.description`:

Description
-----------

Removes a host1x client from its host1x controller instance. If a logical
device has already been initialized, it will be torn down.

.. This file was automatic generated / don't edit.

