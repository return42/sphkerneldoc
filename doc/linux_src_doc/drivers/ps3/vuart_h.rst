.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/vuart.h

.. _`ps3_vuart_port_driver`:

struct ps3_vuart_port_driver
============================

.. c:type:: struct ps3_vuart_port_driver

    a driver for a device on a vuart port

.. _`ps3_vuart_port_driver.definition`:

Definition
----------

.. code-block:: c

    struct ps3_vuart_port_driver {
        struct ps3_system_bus_driver core;
        int (*probe)(struct ps3_system_bus_device *);
        int (*remove)(struct ps3_system_bus_device *);
        void (*shutdown)(struct ps3_system_bus_device *);
        void (*work)(struct ps3_system_bus_device *);
    }

.. _`ps3_vuart_port_driver.members`:

Members
-------

core
    *undescribed*

probe
    *undescribed*

remove
    *undescribed*

shutdown
    *undescribed*

work
    *undescribed*

.. This file was automatic generated / don't edit.

