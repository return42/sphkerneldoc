.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-sysfs.c

.. _`hctosys_show`:

hctosys_show
============

.. c:function:: ssize_t hctosys_show(struct device *dev, struct device_attribute *attr, char *buf)

    indicate if the given RTC set the system time

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`hctosys_show.description`:

Description
-----------

Returns 1 if the system clock was set by this RTC at the last
boot or resume event.

.. This file was automatic generated / don't edit.

