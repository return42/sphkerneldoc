.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clock_cooling.h

.. _`clock_cooling_register`:

clock_cooling_register
======================

.. c:function:: struct thermal_cooling_device *clock_cooling_register(struct device *dev, const char *clock_name)

    function to create clock cooling device.

    :param dev:
        struct device pointer to the device used as clock cooling device.
    :type dev: struct device \*

    :param clock_name:
        string containing the clock used as cooling mechanism.
    :type clock_name: const char \*

.. _`clock_cooling_unregister`:

clock_cooling_unregister
========================

.. c:function:: void clock_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove clock cooling device.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

.. This file was automatic generated / don't edit.

