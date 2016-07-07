.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/power/bq27xxx_battery.h

.. _`bq27xxx_platform_data`:

struct bq27xxx_platform_data
============================

.. c:type:: struct bq27xxx_platform_data

    Platform data for bq27xxx devices

.. _`bq27xxx_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct bq27xxx_platform_data {
        const char *name;
        enum bq27xxx_chip chip;
        int (* read) (struct device *dev, unsigned int);
    }

.. _`bq27xxx_platform_data.members`:

Members
-------

name
    Name of the battery.

chip
    Chip class number of this device.

read
    HDQ read callback.
    This function should provide access to the HDQ bus the battery is
    connected to.
    The first parameter is a pointer to the battery device, the second the
    register to be read. The return value should either be the content of
    the passed register or an error value.

.. This file was automatic generated / don't edit.

