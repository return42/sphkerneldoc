.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib-sysfs.c

.. _`gpiod_export`:

gpiod_export
============

.. c:function:: int gpiod_export(struct gpio_desc *desc, bool direction_may_change)

    export a GPIO through sysfs

    :param struct gpio_desc \*desc:
        *undescribed*

    :param bool direction_may_change:
        true if userspace may change gpio direction

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

    :param struct device \*dev:
        device under which to create symlink

    :param const char \*name:
        name of the symlink

    :param struct gpio_desc \*desc:
        *undescribed*

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

    reverse effect of \ :c:func:`gpio_export`\ 

    :param struct gpio_desc \*desc:
        *undescribed*

.. _`gpiod_unexport.description`:

Description
-----------

This is implicit on \ :c:func:`gpio_free`\ .

.. This file was automatic generated / don't edit.

