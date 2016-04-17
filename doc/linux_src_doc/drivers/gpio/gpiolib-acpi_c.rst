.. -*- coding: utf-8; mode: rst -*-

==============
gpiolib-acpi.c
==============


.. _`acpi_gpiochip_pin_to_gpio_offset`:

acpi_gpiochip_pin_to_gpio_offset
================================

.. c:function:: int acpi_gpiochip_pin_to_gpio_offset (struct gpio_device *gdev, int pin)

    translates ACPI GPIO to Linux GPIO

    :param struct gpio_device \*gdev:

        *undescribed*

    :param int pin:
        ACPI GPIO pin number from GpioIo/GpioInt resource



.. _`acpi_gpiochip_pin_to_gpio_offset.description`:

Description
-----------

Function takes ACPI GpioIo/GpioInt pin number as a parameter and
translates it to a corresponding offset suitable to be passed to a
GPIO controller driver.

Typically the returned offset is same as ``pin``\ , but if the GPIO
controller uses pin controller and the mapping is not contiguous the
offset might be different.



.. _`acpi_get_gpiod`:

acpi_get_gpiod
==============

.. c:function:: struct gpio_desc *acpi_get_gpiod (char *path, int pin)

    Translate ACPI GPIO pin to GPIO descriptor usable with GPIO API

    :param char \*path:
        ACPI GPIO controller full path name, (e.g. "\\_SB.GPO1")

    :param int pin:
        ACPI GPIO pin number (0-based, controller-relative)



.. _`acpi_get_gpiod.return`:

Return
------

GPIO descriptor to use with Linux generic GPIO API, or ERR_PTR
error value. Specifically returns ``-EPROBE_DEFER`` if the referenced GPIO
controller does not have gpiochip registered at the moment. This is to
support probe deferral.



.. _`acpi_gpiochip_request_interrupts`:

acpi_gpiochip_request_interrupts
================================

.. c:function:: void acpi_gpiochip_request_interrupts (struct gpio_chip *chip)

    Register isr for gpio chip ACPI events

    :param struct gpio_chip \*chip:
        GPIO chip



.. _`acpi_gpiochip_request_interrupts.description`:

Description
-----------

ACPI5 platforms can use GPIO signaled ACPI events. These GPIO interrupts are
handled by ACPI event methods which need to be called from the GPIO
chip's interrupt handler. acpi_gpiochip_request_interrupts finds out which
gpio pins have acpi event methods and assigns interrupt handlers that calls
the acpi event methods for those pins.



.. _`acpi_gpiochip_free_interrupts`:

acpi_gpiochip_free_interrupts
=============================

.. c:function:: void acpi_gpiochip_free_interrupts (struct gpio_chip *chip)

    Free GPIO ACPI event interrupts.

    :param struct gpio_chip \*chip:
        GPIO chip



.. _`acpi_gpiochip_free_interrupts.description`:

Description
-----------

Free interrupts associated with GPIO ACPI event method for the given
GPIO chip.



.. _`acpi_get_gpiod_by_index`:

acpi_get_gpiod_by_index
=======================

.. c:function:: struct gpio_desc *acpi_get_gpiod_by_index (struct acpi_device *adev, const char *propname, int index, struct acpi_gpio_info *info)

    get a GPIO descriptor from device resources

    :param struct acpi_device \*adev:
        pointer to a ACPI device to get GPIO from

    :param const char \*propname:
        Property name of the GPIO (optional)

    :param int index:
        index of GpioIo/GpioInt resource (starting from ``0``\ )

    :param struct acpi_gpio_info \*info:
        info pointer to fill in (optional)



.. _`acpi_get_gpiod_by_index.description`:

Description
-----------

Function goes through ACPI resources for ``adev`` and based on ``index`` looks
up a GpioIo/GpioInt resource, translates it to the Linux GPIO descriptor,
and returns it. ``index`` matches GpioIo/GpioInt resources only so if there
are total ``3`` GPIO resources, the index goes from ``0`` to ``2``\ .

If ``propname`` is specified the GPIO is looked using device property. In
that case ``index`` is used to select the GPIO entry in the property value
(in case of multiple).

If the GPIO cannot be translated or there is an error an ERR_PTR is
returned.



.. _`acpi_get_gpiod_by_index.note`:

Note
----

if the GPIO resource has multiple entries in the pin list, this
function only returns the first.



.. _`acpi_node_get_gpiod`:

acpi_node_get_gpiod
===================

.. c:function:: struct gpio_desc *acpi_node_get_gpiod (struct fwnode_handle *fwnode, const char *propname, int index, struct acpi_gpio_info *info)

    get a GPIO descriptor from ACPI resources

    :param struct fwnode_handle \*fwnode:
        pointer to an ACPI firmware node to get the GPIO information from

    :param const char \*propname:
        Property name of the GPIO

    :param int index:
        index of GpioIo/GpioInt resource (starting from ``0``\ )

    :param struct acpi_gpio_info \*info:
        info pointer to fill in (optional)



.. _`acpi_node_get_gpiod.description`:

Description
-----------

If ``fwnode`` is an ACPI device object, call ``acpi_get_gpiod_by_index``\ () for it.
Otherwise (ie. it is a data-only non-device object), use the property-based
GPIO lookup to get to the GPIO resource with the relevant information and use
that to obtain the GPIO descriptor to return.



.. _`acpi_dev_gpio_irq_get`:

acpi_dev_gpio_irq_get
=====================

.. c:function:: int acpi_dev_gpio_irq_get (struct acpi_device *adev, int index)

    Find GpioInt and translate it to Linux IRQ number

    :param struct acpi_device \*adev:
        pointer to a ACPI device to get IRQ from

    :param int index:
        index of GpioInt resource (starting from ``0``\ )



.. _`acpi_dev_gpio_irq_get.description`:

Description
-----------

If the device has one or more GpioInt resources, this function can be
used to translate from the GPIO offset in the resource to the Linux IRQ
number.



.. _`acpi_dev_gpio_irq_get.return`:

Return
------

Linux IRQ number (>\ ``0``\ ) on success, negative errno on failure.



.. _`acpi_gpio_count`:

acpi_gpio_count
===============

.. c:function:: int acpi_gpio_count (struct device *dev, const char *con_id)

    return the number of GPIOs associated with a device / function or -ENOENT if no GPIO has been assigned to the requested function.

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

