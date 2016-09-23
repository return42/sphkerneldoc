.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib.h

.. _`gpio_device`:

struct gpio_device
==================

.. c:type:: struct gpio_device

    internal state container for GPIO devices

.. _`gpio_device.definition`:

Definition
----------

.. code-block:: c

    struct gpio_device {
        int id;
        struct device dev;
        struct cdev chrdev;
        struct device *mockdev;
        struct module *owner;
        struct gpio_chip *chip;
        struct gpio_desc *descs;
        int base;
        u16 ngpio;
        char *label;
        void *data;
        struct list_head list;
    #ifdef CONFIG_PINCTRL
        struct list_head pin_ranges;
    #endif
    }

.. _`gpio_device.members`:

Members
-------

id
    numerical ID number for the GPIO chip

dev
    the GPIO device struct

chrdev
    character device for the GPIO device

mockdev
    class device used by the deprecated sysfs interface (may be
    NULL)

owner
    helps prevent removal of modules exporting active GPIOs

chip
    pointer to the corresponding gpiochip, holding static
    data for this device

descs
    array of ngpio descriptors.

base
    GPIO base in the DEPRECATED global Linux GPIO numberspace, assigned
    at device creation time.

ngpio
    the number of GPIO lines on this GPIO device, equal to the size
    of the \ ``descs``\  array.

label
    a descriptive name for the GPIO device, such as the part number
    or name of the IP component in a System on Chip.

data
    per-instance data assigned by the driver

list
    links gpio_device:s together for traversal

pin_ranges
    *undescribed*

.. _`gpio_device.description`:

Description
-----------

This state container holds most of the runtime variable data
for a GPIO device and can hold references and live on after the
GPIO chip has been removed, if it is still being used from
userspace.

.. _`acpi_gpio_info`:

struct acpi_gpio_info
=====================

.. c:type:: struct acpi_gpio_info

    ACPI GPIO specific information

.. _`acpi_gpio_info.definition`:

Definition
----------

.. code-block:: c

    struct acpi_gpio_info {
        bool gpioint;
        int polarity;
        int triggering;
    }

.. _`acpi_gpio_info.members`:

Members
-------

gpioint
    if \ ``true``\  this GPIO is of type GpioInt otherwise type is GpioIo

polarity
    *undescribed*

triggering
    *undescribed*

.. This file was automatic generated / don't edit.

