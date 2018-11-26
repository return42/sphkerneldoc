.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/bus_type.c

.. _`sdw_get_device_id`:

sdw_get_device_id
=================

.. c:function:: const struct sdw_device_id *sdw_get_device_id(struct sdw_slave *slave, struct sdw_driver *drv)

    find the matching SoundWire device id

    :param slave:
        SoundWire Slave Device
    :type slave: struct sdw_slave \*

    :param drv:
        SoundWire Slave Driver
    :type drv: struct sdw_driver \*

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

    :param drv:
        driver to register
    :type drv: struct sdw_driver \*

    :param owner:
        owning module/driver
    :type owner: struct module \*

.. _`__sdw_register_driver.return`:

Return
------

zero on success, else a negative error code.

.. _`sdw_unregister_driver`:

sdw_unregister_driver
=====================

.. c:function:: void sdw_unregister_driver(struct sdw_driver *drv)

    unregisters the SoundWire Slave driver

    :param drv:
        driver to unregister
    :type drv: struct sdw_driver \*

.. This file was automatic generated / don't edit.

