.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/led-class.c

.. _`led_classdev_suspend`:

led_classdev_suspend
====================

.. c:function:: void led_classdev_suspend(struct led_classdev *led_cdev)

    suspend an led_classdev.

    :param struct led_classdev \*led_cdev:
        the led_classdev to suspend.

.. _`led_classdev_resume`:

led_classdev_resume
===================

.. c:function:: void led_classdev_resume(struct led_classdev *led_cdev)

    resume an led_classdev.

    :param struct led_classdev \*led_cdev:
        the led_classdev to resume.

.. _`led_classdev_register`:

led_classdev_register
=====================

.. c:function:: int led_classdev_register(struct device *parent, struct led_classdev *led_cdev)

    register a new object of led_classdev class.

    :param struct device \*parent:
        The device to register.

    :param struct led_classdev \*led_cdev:
        the led_classdev structure for this device.

.. _`led_classdev_unregister`:

led_classdev_unregister
=======================

.. c:function:: void led_classdev_unregister(struct led_classdev *led_cdev)

    unregisters a object of led_properties class.

    :param struct led_classdev \*led_cdev:
        the led device to unregister

.. _`led_classdev_unregister.description`:

Description
-----------

Unregisters a previously registered via led_classdev_register object.

.. _`devm_led_classdev_register`:

devm_led_classdev_register
==========================

.. c:function:: int devm_led_classdev_register(struct device *parent, struct led_classdev *led_cdev)

    resource managed \ :c:func:`led_classdev_register`\ 

    :param struct device \*parent:
        The device to register.

    :param struct led_classdev \*led_cdev:
        the led_classdev structure for this device.

.. _`devm_led_classdev_unregister`:

devm_led_classdev_unregister
============================

.. c:function:: void devm_led_classdev_unregister(struct device *dev, struct led_classdev *led_cdev)

    resource managed \ :c:func:`led_classdev_unregister`\ 

    :param struct device \*dev:
        *undescribed*

    :param struct led_classdev \*led_cdev:
        the led_classdev structure for this device.

.. This file was automatic generated / don't edit.

