.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/led-class.c

.. _`led_classdev_suspend`:

led_classdev_suspend
====================

.. c:function:: void led_classdev_suspend(struct led_classdev *led_cdev)

    suspend an led_classdev.

    :param led_cdev:
        the led_classdev to suspend.
    :type led_cdev: struct led_classdev \*

.. _`led_classdev_resume`:

led_classdev_resume
===================

.. c:function:: void led_classdev_resume(struct led_classdev *led_cdev)

    resume an led_classdev.

    :param led_cdev:
        the led_classdev to resume.
    :type led_cdev: struct led_classdev \*

.. _`of_led_classdev_register`:

of_led_classdev_register
========================

.. c:function:: int of_led_classdev_register(struct device *parent, struct device_node *np, struct led_classdev *led_cdev)

    register a new object of led_classdev class.

    :param parent:
        parent of LED device
    :type parent: struct device \*

    :param np:
        DT node describing this LED
    :type np: struct device_node \*

    :param led_cdev:
        the led_classdev structure for this device.
    :type led_cdev: struct led_classdev \*

.. _`led_classdev_unregister`:

led_classdev_unregister
=======================

.. c:function:: void led_classdev_unregister(struct led_classdev *led_cdev)

    unregisters a object of led_properties class.

    :param led_cdev:
        the led device to unregister
    :type led_cdev: struct led_classdev \*

.. _`led_classdev_unregister.description`:

Description
-----------

Unregisters a previously registered via led_classdev_register object.

.. _`devm_of_led_classdev_register`:

devm_of_led_classdev_register
=============================

.. c:function:: int devm_of_led_classdev_register(struct device *parent, struct device_node *np, struct led_classdev *led_cdev)

    resource managed \ :c:func:`led_classdev_register`\ 

    :param parent:
        parent of LED device
    :type parent: struct device \*

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param led_cdev:
        the led_classdev structure for this device.
    :type led_cdev: struct led_classdev \*

.. _`devm_led_classdev_unregister`:

devm_led_classdev_unregister
============================

.. c:function:: void devm_led_classdev_unregister(struct device *dev, struct led_classdev *led_cdev)

    resource managed \ :c:func:`led_classdev_unregister`\ 

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param led_cdev:
        the led_classdev structure for this device.
    :type led_cdev: struct led_classdev \*

.. This file was automatic generated / don't edit.

