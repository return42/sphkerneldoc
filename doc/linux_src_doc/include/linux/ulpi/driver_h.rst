.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ulpi/driver.h

.. _`ulpi`:

struct ulpi
===========

.. c:type:: struct ulpi

    describes ULPI PHY device

.. _`ulpi.definition`:

Definition
----------

.. code-block:: c

    struct ulpi {
        struct ulpi_device_id id;
        struct ulpi_ops *ops;
        struct device dev;
    }

.. _`ulpi.members`:

Members
-------

id
    vendor and product ids for ULPI device

ops
    I/O access

dev
    device interface

.. _`ulpi_driver`:

struct ulpi_driver
==================

.. c:type:: struct ulpi_driver

    describes a ULPI PHY driver

.. _`ulpi_driver.definition`:

Definition
----------

.. code-block:: c

    struct ulpi_driver {
        const struct ulpi_device_id *id_table;
        int (* probe) (struct ulpi *ulpi);
        void (* remove) (struct ulpi *ulpi);
        struct device_driver driver;
    }

.. _`ulpi_driver.members`:

Members
-------

id_table
    array of device identifiers supported by this driver

probe
    binds this driver to ULPI device

remove
    unbinds this driver from ULPI device

driver
    the name and owner members must be initialized by the drivers

.. This file was automatic generated / don't edit.

