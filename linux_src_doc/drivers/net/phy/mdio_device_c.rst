.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/mdio_device.c

.. _`mdio_device_register`:

mdio_device_register
====================

.. c:function:: int mdio_device_register(struct mdio_device *mdiodev)

    Register the mdio device on the MDIO bus

    :param mdiodev:
        mdio_device structure to be added to the MDIO bus
    :type mdiodev: struct mdio_device \*

.. _`mdio_device_remove`:

mdio_device_remove
==================

.. c:function:: void mdio_device_remove(struct mdio_device *mdiodev)

    Remove a previously registered mdio device from the MDIO bus

    :param mdiodev:
        mdio_device structure to remove
    :type mdiodev: struct mdio_device \*

.. _`mdio_device_remove.description`:

Description
-----------

This doesn't free the mdio_device itself, it merely reverses the effects
of \ :c:func:`mdio_device_register`\ . Use \ :c:func:`mdio_device_free`\  to free the device
after calling this function.

.. _`mdio_probe`:

mdio_probe
==========

.. c:function:: int mdio_probe(struct device *dev)

    probe an MDIO device

    :param dev:
        device to probe
    :type dev: struct device \*

.. _`mdio_probe.description`:

Description
-----------

Take care of setting up the mdio_device structure
and calling the driver to probe the device.

.. _`mdio_driver_register`:

mdio_driver_register
====================

.. c:function:: int mdio_driver_register(struct mdio_driver *drv)

    register an mdio_driver with the MDIO layer

    :param drv:
        *undescribed*
    :type drv: struct mdio_driver \*

.. This file was automatic generated / don't edit.

