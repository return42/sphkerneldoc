.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/common/ulpi.c

.. _`ulpi_read`:

ulpi_read
=========

.. c:function:: int ulpi_read(struct ulpi *ulpi, u8 addr)

    USB ULPI PHY bus

    :param struct ulpi \*ulpi:
        *undescribed*

    :param u8 addr:
        *undescribed*

.. _`ulpi_read.description`:

Description
-----------

Copyright (C) 2015 Intel Corporation

.. _`ulpi_read.author`:

Author
------

Heikki Krogerus <heikki.krogerus@linux.intel.com>

.. _`__ulpi_register_driver`:

__ulpi_register_driver
======================

.. c:function:: int __ulpi_register_driver(struct ulpi_driver *drv, struct module *module)

    register a driver with the ULPI bus

    :param struct ulpi_driver \*drv:
        driver being registered

    :param struct module \*module:
        *undescribed*

.. _`__ulpi_register_driver.description`:

Description
-----------

Registers a driver with the ULPI bus.

.. _`ulpi_unregister_driver`:

ulpi_unregister_driver
======================

.. c:function:: void ulpi_unregister_driver(struct ulpi_driver *drv)

    unregister a driver with the ULPI bus

    :param struct ulpi_driver \*drv:
        driver to unregister

.. _`ulpi_unregister_driver.description`:

Description
-----------

Unregisters a driver with the ULPI bus.

.. _`ulpi_register_interface`:

ulpi_register_interface
=======================

.. c:function:: struct ulpi *ulpi_register_interface(struct device *dev, const struct ulpi_ops *ops)

    instantiate new ULPI device

    :param struct device \*dev:
        USB controller's device interface

    :param const struct ulpi_ops \*ops:
        ULPI register access

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

    :param struct ulpi \*ulpi:
        *undescribed*

.. _`ulpi_unregister_interface.description`:

Description
-----------

Unregisters a ULPI device and it's interface that was created with
\ :c:func:`ulpi_create_interface`\ .

.. This file was automatic generated / don't edit.

