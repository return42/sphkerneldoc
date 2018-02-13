.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_device.h

.. _`omap_device`:

struct omap_device
==================

.. c:type:: struct omap_device

    omap_device wrapper for platform_devices

.. _`omap_device.definition`:

Definition
----------

.. code-block:: c

    struct omap_device {
        struct platform_device *pdev;
        struct omap_hwmod **hwmods;
        unsigned long _driver_status;
        u8 hwmods_cnt;
        u8 _state;
        u8 flags;
    }

.. _`omap_device.members`:

Members
-------

pdev
    platform_device

hwmods
    (one .. many per omap_device)

\_driver_status
    one of BUS_NOTIFY\_\*\_DRIVER from <linux/device.h>

hwmods_cnt
    \ :c:func:`ARRAY_SIZE`\  of \ ``hwmods``\ 

\_state
    one of OMAP_DEVICE_STATE\_\* (see above)

flags
    device flags

.. _`omap_device.description`:

Description
-----------

Integrates omap_hwmod data into Linux platform_device.

Field names beginning with underscores are for the internal use of
the omap_device code.

.. This file was automatic generated / don't edit.

