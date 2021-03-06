.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/led-class-flash.h

.. _`led_classdev_flash_register`:

led_classdev_flash_register
===========================

.. c:function:: int led_classdev_flash_register(struct device *parent, struct led_classdev_flash *fled_cdev)

    register a new object of led_classdev class with support for flash LEDs

    :param parent:
        the flash LED to register
    :type parent: struct device \*

    :param fled_cdev:
        the led_classdev_flash structure for this device
    :type fled_cdev: struct led_classdev_flash \*

.. _`led_classdev_flash_register.return`:

Return
------

0 on success or negative error value on failure

.. _`led_classdev_flash_unregister`:

led_classdev_flash_unregister
=============================

.. c:function:: void led_classdev_flash_unregister(struct led_classdev_flash *fled_cdev)

    unregisters an object of led_classdev class with support for flash LEDs

    :param fled_cdev:
        the flash LED to unregister
    :type fled_cdev: struct led_classdev_flash \*

.. _`led_classdev_flash_unregister.description`:

Description
-----------

Unregister a previously registered via led_classdev_flash_register object

.. _`led_set_flash_strobe`:

led_set_flash_strobe
====================

.. c:function:: int led_set_flash_strobe(struct led_classdev_flash *fled_cdev, bool state)

    setup flash strobe

    :param fled_cdev:
        the flash LED to set strobe on
    :type fled_cdev: struct led_classdev_flash \*

    :param state:
        1 - strobe flash, 0 - stop flash strobe
    :type state: bool

.. _`led_set_flash_strobe.description`:

Description
-----------

Strobe the flash LED.

.. _`led_set_flash_strobe.return`:

Return
------

0 on success or negative error value on failure

.. _`led_get_flash_strobe`:

led_get_flash_strobe
====================

.. c:function:: int led_get_flash_strobe(struct led_classdev_flash *fled_cdev, bool *state)

    get flash strobe status

    :param fled_cdev:
        the flash LED to query
    :type fled_cdev: struct led_classdev_flash \*

    :param state:
        1 - flash is strobing, 0 - flash is off
    :type state: bool \*

.. _`led_get_flash_strobe.description`:

Description
-----------

Check whether the flash is strobing at the moment.

.. _`led_get_flash_strobe.return`:

Return
------

0 on success or negative error value on failure

.. _`led_set_flash_brightness`:

led_set_flash_brightness
========================

.. c:function:: int led_set_flash_brightness(struct led_classdev_flash *fled_cdev, u32 brightness)

    set flash LED brightness

    :param fled_cdev:
        the flash LED to set
    :type fled_cdev: struct led_classdev_flash \*

    :param brightness:
        the brightness to set it to
    :type brightness: u32

.. _`led_set_flash_brightness.description`:

Description
-----------

Set a flash LED's brightness.

.. _`led_set_flash_brightness.return`:

Return
------

0 on success or negative error value on failure

.. _`led_update_flash_brightness`:

led_update_flash_brightness
===========================

.. c:function:: int led_update_flash_brightness(struct led_classdev_flash *fled_cdev)

    update flash LED brightness

    :param fled_cdev:
        the flash LED to query
    :type fled_cdev: struct led_classdev_flash \*

.. _`led_update_flash_brightness.description`:

Description
-----------

Get a flash LED's current brightness and update led_flash->brightness
member with the obtained value.

.. _`led_update_flash_brightness.return`:

Return
------

0 on success or negative error value on failure

.. _`led_set_flash_timeout`:

led_set_flash_timeout
=====================

.. c:function:: int led_set_flash_timeout(struct led_classdev_flash *fled_cdev, u32 timeout)

    set flash LED timeout

    :param fled_cdev:
        the flash LED to set
    :type fled_cdev: struct led_classdev_flash \*

    :param timeout:
        the flash timeout to set it to
    :type timeout: u32

.. _`led_set_flash_timeout.description`:

Description
-----------

Set the flash strobe duration.

.. _`led_set_flash_timeout.return`:

Return
------

0 on success or negative error value on failure

.. _`led_get_flash_fault`:

led_get_flash_fault
===================

.. c:function:: int led_get_flash_fault(struct led_classdev_flash *fled_cdev, u32 *fault)

    get the flash LED fault

    :param fled_cdev:
        the flash LED to query
    :type fled_cdev: struct led_classdev_flash \*

    :param fault:
        bitmask containing flash faults
    :type fault: u32 \*

.. _`led_get_flash_fault.description`:

Description
-----------

Get the flash LED fault.

.. _`led_get_flash_fault.return`:

Return
------

0 on success or negative error value on failure

.. This file was automatic generated / don't edit.

