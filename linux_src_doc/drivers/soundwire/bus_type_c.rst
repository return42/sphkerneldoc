.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/bus_type.c

.. _`sdw_get_device_id`:

sdw_get_device_id
=================

.. c:function:: const struct sdw_device_id *sdw_get_device_id(struct sdw_slave *slave, struct sdw_driver *drv)

    find the matching SoundWire device id

    :param struct sdw_slave \*slave:
        SoundWire Slave Device

    :param struct sdw_driver \*drv:
        SoundWire Slave Driver

.. _`sdw_get_device_id.description`:

Description
-----------

The match is done by comparing the mfg_id and part_id from the
struct sdw_device_id.

.. _`__sdw_register_driver`:

\__sdw_register_driver
======================

.. c:function:: int __sdw_register_driver(struct sdw_driver *drv, struct module *owner)

    register a SoundWire Slave driver

    :param struct sdw_driver \*drv:
        driver to register

    :param struct module \*owner:
        owning module/driver

.. _`__sdw_register_driver.return`:

Return
------

zero on success, else a negative error code.

.. _`sdw_unregister_driver`:

sdw_unregister_driver
=====================

.. c:function:: void sdw_unregister_driver(struct sdw_driver *drv)

    unregisters the SoundWire Slave driver

    :param struct sdw_driver \*drv:
        driver to unregister

.. This file was automatic generated / don't edit.

