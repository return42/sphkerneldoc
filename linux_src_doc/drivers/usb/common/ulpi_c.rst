.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/common/ulpi.c

.. _`ulpi_read`:

ulpi_read
=========

.. c:function:: int ulpi_read(struct ulpi *ulpi, u8 addr)

    USB ULPI PHY bus

    :param ulpi:
        *undescribed*
    :type ulpi: struct ulpi \*

    :param addr:
        *undescribed*
    :type addr: u8

.. _`ulpi_read.description`:

Description
-----------

Copyright (C) 2015 Intel Corporation

.. _`ulpi_read.author`:

Author
------

Heikki Krogerus <heikki.krogerus@linux.intel.com>

.. _`__ulpi_register_driver`:

\__ulpi_register_driver
=======================

.. c:function:: int __ulpi_register_driver(struct ulpi_driver *drv, struct module *module)

    register a driver with the ULPI bus

    :param drv:
        driver being registered
    :type drv: struct ulpi_driver \*

    :param module:
        *undescribed*
    :type module: struct module \*

.. _`__ulpi_register_driver.description`:

Description
-----------

Registers a driver with the ULPI bus.

.. _`ulpi_unregister_driver`:

ulpi_unregister_driver
======================

.. c:function:: void ulpi_unregister_driver(struct ulpi_driver *drv)

    unregister a driver with the ULPI bus

    :param drv:
        driver to unregister
    :type drv: struct ulpi_driver \*

.. _`ulpi_unregister_driver.description`:

Description
-----------

Unregisters a driver with the ULPI bus.

.. _`ulpi_register_interface`:

ulpi_register_interface
=======================

.. c:function:: struct ulpi *ulpi_register_interface(struct device *dev, const struct ulpi_ops *ops)

    instantiate new ULPI device

    :param dev:
        USB controller's device interface
    :type dev: struct device \*

    :param ops:
        ULPI register access
    :type ops: const struct ulpi_ops \*

.. _`ulpi_register_interface.description`:

Description
-----------

Allocates and registers a ULPI device and an interface for it. Called from
the USB controller that provides the ULPI interface.

.. _`ulpi_unregister_interface`:

ulpi_unregister_interface
=========================

.. c:function:: void ulpi_unregister_interface(struct ulpi *ulpi)

    unregister ULPI interface

    :param ulpi:
        *undescribed*
    :type ulpi: struct ulpi \*

.. _`ulpi_unregister_interface.description`:

Description
-----------

Unregisters a ULPI device and it's interface that was created with
\ :c:func:`ulpi_create_interface`\ .

.. This file was automatic generated / don't edit.

