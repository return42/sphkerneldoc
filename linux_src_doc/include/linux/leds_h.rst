.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/leds.h

.. _`led_blink_set`:

led_blink_set
=============

.. c:function:: void led_blink_set(struct led_classdev *led_cdev, unsigned long *delay_on, unsigned long *delay_off)

    set blinking with software fallback

    :param led_cdev:
        the LED to start blinking
    :type led_cdev: struct led_classdev \*

    :param delay_on:
        the time it should be on (in ms)
    :type delay_on: unsigned long \*

    :param delay_off:
        the time it should ble off (in ms)
    :type delay_off: unsigned long \*

.. _`led_blink_set.description`:

Description
-----------

This function makes the LED blink, attempting to use the
hardware acceleration if possible, but falling back to
software blinking if there is no hardware blinking or if
the LED refuses the passed values.

Note that if software blinking is active, simply calling
led_cdev->brightness_set() will not stop the blinking,
use \ :c:func:`led_classdev_brightness_set`\  instead.

.. _`led_blink_set_oneshot`:

led_blink_set_oneshot
=====================

.. c:function:: void led_blink_set_oneshot(struct led_classdev *led_cdev, unsigned long *delay_on, unsigned long *delay_off, int invert)

    do a oneshot software blink

    :param led_cdev:
        the LED to start blinking
    :type led_cdev: struct led_classdev \*

    :param delay_on:
        the time it should be on (in ms)
    :type delay_on: unsigned long \*

    :param delay_off:
        the time it should ble off (in ms)
    :type delay_off: unsigned long \*

    :param invert:
        blink off, then on, leaving the led on
    :type invert: int

.. _`led_blink_set_oneshot.description`:

Description
-----------

This function makes the LED blink one time for delay_on +
delay_off time, ignoring the request if another one-shot
blink is already in progress.

If invert is set, led blinks for delay_off first, then for
delay_on and leave the led on after the on-off cycle.

.. _`led_set_brightness`:

led_set_brightness
==================

.. c:function:: void led_set_brightness(struct led_classdev *led_cdev, enum led_brightness brightness)

    set LED brightness

    :param led_cdev:
        the LED to set
    :type led_cdev: struct led_classdev \*

    :param brightness:
        the brightness to set it to
    :type brightness: enum led_brightness

.. _`led_set_brightness.description`:

Description
-----------

Set an LED's brightness, and, if necessary, cancel the
software blink timer that implements blinking when the
hardware doesn't. This function is guaranteed not to sleep.

.. _`led_set_brightness_sync`:

led_set_brightness_sync
=======================

.. c:function:: int led_set_brightness_sync(struct led_classdev *led_cdev, enum led_brightness value)

    set LED brightness synchronously

    :param led_cdev:
        the LED to set
    :type led_cdev: struct led_classdev \*

    :param value:
        *undescribed*
    :type value: enum led_brightness

.. _`led_set_brightness_sync.description`:

Description
-----------

Set an LED's brightness immediately. This function will block
the caller for the time required for accessing device registers,
and it can sleep.

.. _`led_set_brightness_sync.return`:

Return
------

0 on success or negative error value on failure

.. _`led_update_brightness`:

led_update_brightness
=====================

.. c:function:: int led_update_brightness(struct led_classdev *led_cdev)

    update LED brightness

    :param led_cdev:
        the LED to query
    :type led_cdev: struct led_classdev \*

.. _`led_update_brightness.description`:

Description
-----------

Get an LED's current brightness and update led_cdev->brightness
member with the obtained value.

.. _`led_update_brightness.return`:

Return
------

0 on success or negative error value on failure

.. _`led_sysfs_disable`:

led_sysfs_disable
=================

.. c:function:: void led_sysfs_disable(struct led_classdev *led_cdev)

    disable LED sysfs interface

    :param led_cdev:
        the LED to set
    :type led_cdev: struct led_classdev \*

.. _`led_sysfs_disable.description`:

Description
-----------

Disable the led_cdev's sysfs interface.

.. _`led_sysfs_enable`:

led_sysfs_enable
================

.. c:function:: void led_sysfs_enable(struct led_classdev *led_cdev)

    enable LED sysfs interface

    :param led_cdev:
        the LED to set
    :type led_cdev: struct led_classdev \*

.. _`led_sysfs_enable.description`:

Description
-----------

Enable the led_cdev's sysfs interface.

.. _`led_sysfs_is_disabled`:

led_sysfs_is_disabled
=====================

.. c:function:: bool led_sysfs_is_disabled(struct led_classdev *led_cdev)

    check if LED sysfs interface is disabled

    :param led_cdev:
        the LED to query
    :type led_cdev: struct led_classdev \*

.. _`led_sysfs_is_disabled.return`:

Return
------

true if the led_cdev's sysfs interface is disabled.

.. _`led_trigger_rename_static`:

led_trigger_rename_static
=========================

.. c:function:: void led_trigger_rename_static(const char *name, struct led_trigger *trig)

    rename a trigger

    :param name:
        the new trigger name
    :type name: const char \*

    :param trig:
        the LED trigger to rename
    :type trig: struct led_trigger \*

.. _`led_trigger_rename_static.description`:

Description
-----------

Change a LED trigger name by copying the string passed in
name into current trigger name, which MUST be large
enough for the new string.

Note that name must NOT point to the same string used
during LED registration, as that could lead to races.

This is meant to be used on triggers with statically
allocated name.

.. _`led_pattern`:

struct led_pattern
==================

.. c:type:: struct led_pattern

    pattern interval settings

.. _`led_pattern.definition`:

Definition
----------

.. code-block:: c

    struct led_pattern {
        u32 delta_t;
        int brightness;
    }

.. _`led_pattern.members`:

Members
-------

delta_t
    pattern interval delay, in milliseconds

brightness
    pattern interval brightness

.. This file was automatic generated / don't edit.

