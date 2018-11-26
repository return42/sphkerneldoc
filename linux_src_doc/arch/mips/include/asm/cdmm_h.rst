.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/cdmm.h

.. _`mips_cdmm_device`:

struct mips_cdmm_device
=======================

.. c:type:: struct mips_cdmm_device

    Represents a single device on a CDMM bus.

.. _`mips_cdmm_device.definition`:

Definition
----------

.. code-block:: c

    struct mips_cdmm_device {
        struct device dev;
        unsigned int cpu;
        struct resource res;
        unsigned int type;
        unsigned int rev;
    }

.. _`mips_cdmm_device.members`:

Members
-------

dev
    Driver model device object.

cpu
    CPU which can access this device.

res
    MMIO resource.

type
    Device type identifier.

rev
    Device revision number.

.. _`mips_cdmm_driver`:

struct mips_cdmm_driver
=======================

.. c:type:: struct mips_cdmm_driver

    Represents a driver for a CDMM device.

.. _`mips_cdmm_driver.definition`:

Definition
----------

.. code-block:: c

    struct mips_cdmm_driver {
        struct device_driver drv;
        int (*probe)(struct mips_cdmm_device *);
        int (*remove)(struct mips_cdmm_device *);
        void (*shutdown)(struct mips_cdmm_device *);
        int (*cpu_down)(struct mips_cdmm_device *);
        int (*cpu_up)(struct mips_cdmm_device *);
        const struct mips_cdmm_device_id *id_table;
    }

.. _`mips_cdmm_driver.members`:

Members
-------

drv
    Driver model driver object.
    \ ``probe``\        Callback for probing newly discovered devices.

probe
    *undescribed*

remove
    Callback to remove the device.

shutdown
    Callback on system shutdown.

cpu_down
    Callback when the parent CPU is going down.
    Any CPU pinned threads/timers should be disabled.

cpu_up
    Callback when the parent CPU is coming back up again.
    CPU pinned threads/timers can be restarted.

id_table
    Table for CDMM IDs to match against.

.. _`mips_cdmm_phys_base`:

mips_cdmm_phys_base
===================

.. c:function:: phys_addr_t mips_cdmm_phys_base( void)

    Choose a physical base address for CDMM region.

    :param void:
        no arguments
    :type void: 

.. _`mips_cdmm_phys_base.description`:

Description
-----------

Picking a suitable physical address at which to map the CDMM region is
platform specific, so this function can be defined by platform code to
pick a suitable value if none is configured by the bootloader.

This address must be 32kB aligned, and the region occupies a maximum of 32kB
of physical address space which must not be used for anything else.

.. _`mips_cdmm_phys_base.return`:

Return
------

Physical base address for CDMM region, or 0 on failure.

.. This file was automatic generated / don't edit.

