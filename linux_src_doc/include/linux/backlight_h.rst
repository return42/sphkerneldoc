.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/backlight.h

.. _`backlight_enable`:

backlight_enable
================

.. c:function:: int backlight_enable(struct backlight_device *bd)

    Enable backlight

    :param struct backlight_device \*bd:
        the backlight device to enable

.. _`backlight_disable`:

backlight_disable
=================

.. c:function:: int backlight_disable(struct backlight_device *bd)

    Disable backlight

    :param struct backlight_device \*bd:
        the backlight device to disable

.. _`backlight_put`:

backlight_put
=============

.. c:function:: void backlight_put(struct backlight_device *bd)

    Drop backlight reference

    :param struct backlight_device \*bd:
        the backlight device to put

.. This file was automatic generated / don't edit.

