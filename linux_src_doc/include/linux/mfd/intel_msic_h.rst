.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/intel_msic.h

.. _`intel_msic_gpio_pdata`:

struct intel_msic_gpio_pdata
============================

.. c:type:: struct intel_msic_gpio_pdata

    platform data for the MSIC GPIO driver

.. _`intel_msic_gpio_pdata.definition`:

Definition
----------

.. code-block:: c

    struct intel_msic_gpio_pdata {
        unsigned gpio_base;
    }

.. _`intel_msic_gpio_pdata.members`:

Members
-------

gpio_base
    base number for the GPIOs

.. _`intel_msic_ocd_pdata`:

struct intel_msic_ocd_pdata
===========================

.. c:type:: struct intel_msic_ocd_pdata

    platform data for the MSIC OCD driver

.. _`intel_msic_ocd_pdata.definition`:

Definition
----------

.. code-block:: c

    struct intel_msic_ocd_pdata {
        unsigned gpio;
    }

.. _`intel_msic_ocd_pdata.members`:

Members
-------

gpio
    GPIO number used for OCD interrupts

.. _`intel_msic_ocd_pdata.description`:

Description
-----------

The MSIC MFD driver converts \ ``gpio``\  into an IRQ number and passes it to
the OCD driver as \ ``IORESOURCE_IRQ``\ .

.. _`intel_msic_platform_data`:

struct intel_msic_platform_data
===============================

.. c:type:: struct intel_msic_platform_data

    platform data for the MSIC driver

.. _`intel_msic_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct intel_msic_platform_data {
        int irq;
        struct intel_msic_gpio_pdata *gpio;
        struct intel_msic_ocd_pdata *ocd;
    }

.. _`intel_msic_platform_data.members`:

Members
-------

irq
    array of interrupt numbers, one per device. If \ ``irq``\  is set to \ ``0``\ 
    for a given block, the corresponding platform device is not
    created. For devices which don't have an interrupt, use \ ``0xff``\ 
    (this is same as in SFI spec).

gpio
    platform data for the MSIC GPIO driver

ocd
    platform data for the MSIC OCD driver

.. _`intel_msic_platform_data.description`:

Description
-----------

Once the MSIC driver is initialized, the register interface is ready to
use. All the platform devices for subdevices are created after the
register interface is ready so that we can guarantee its availability to
the subdevice drivers.

Interrupt numbers are passed to the subdevices via \ ``IORESOURCE_IRQ``\ 
resources of the created platform device.

.. This file was automatic generated / don't edit.

