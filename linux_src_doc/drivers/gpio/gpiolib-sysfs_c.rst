.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-sysfs.c

.. _`gpiod_export`:

gpiod_export
============

.. c:function:: int gpiod_export(struct gpio_desc *desc, bool direction_may_change)

    export a GPIO through sysfs

    :param desc:
        GPIO to make available, already requested
    :type desc: struct gpio_desc \*

    :param direction_may_change:
        true if userspace may change GPIO direction
    :type direction_may_change: bool

.. _`gpiod_export.context`:

Context
-------

arch_initcall or later

.. _`gpiod_export.description`:

Description
-----------

When drivers want to make a GPIO accessible to userspace after they
have requested it -- perhaps while debugging, or as part of their
public interface -- they may use this routine.  If the GPIO can
change direction (some can't) and the caller allows it, userspace
will see "direction" sysfs attribute which may be used to change
the gpio's direction.  A "value" attribute will always be provided.

Returns zero on success, else an error.

.. _`gpiod_export_link`:

gpiod_export_link
=================

.. c:function:: int gpiod_export_link(struct device *dev, const char *name, struct gpio_desc *desc)

    create a sysfs link to an exported GPIO node

    :param dev:
        device under which to create symlink
    :type dev: struct device \*

    :param name:
        name of the symlink
    :type name: const char \*

    :param desc:
        GPIO to create symlink to, already exported
    :type desc: struct gpio_desc \*

.. _`gpiod_export_link.description`:

Description
-----------

Set up a symlink from /sys/.../dev/name to /sys/class/gpio/gpioN
node. Caller is responsible for unlinking.

Returns zero on success, else an error.

.. _`gpiod_unexport`:

gpiod_unexport
==============

.. c:function:: void gpiod_unexport(struct gpio_desc *desc)

    reverse effect of \ :c:func:`gpiod_export`\ 

    :param desc:
        GPIO to make unavailable
    :type desc: struct gpio_desc \*

.. _`gpiod_unexport.description`:

Description
-----------

This is implicit on \ :c:func:`gpiod_free`\ .

.. This file was automatic generated / don't edit.

