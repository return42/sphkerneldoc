.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/backlight.h

.. _`backlight_enable`:

backlight_enable
================

.. c:function:: int backlight_enable(struct backlight_device *bd)

    Enable backlight

    :param bd:
        the backlight device to enable
    :type bd: struct backlight_device \*

.. _`backlight_disable`:

backlight_disable
=================

.. c:function:: int backlight_disable(struct backlight_device *bd)

    Disable backlight

    :param bd:
        the backlight device to disable
    :type bd: struct backlight_device \*

.. _`backlight_put`:

backlight_put
=============

.. c:function:: void backlight_put(struct backlight_device *bd)

    Drop backlight reference

    :param bd:
        the backlight device to put
    :type bd: struct backlight_device \*

.. This file was automatic generated / don't edit.

