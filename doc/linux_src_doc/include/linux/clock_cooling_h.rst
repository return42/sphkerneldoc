.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clock_cooling.h

.. _`clock_cooling_register`:

clock_cooling_register
======================

.. c:function:: struct thermal_cooling_device *clock_cooling_register(struct device *dev, const char *clock_name)

    function to create clock cooling device.

    :param struct device \*dev:
        struct device pointer to the device used as clock cooling device.

    :param const char \*clock_name:
        string containing the clock used as cooling mechanism.

.. _`clock_cooling_unregister`:

clock_cooling_unregister
========================

.. c:function:: void clock_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove clock cooling device.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

.. This file was automatic generated / don't edit.

