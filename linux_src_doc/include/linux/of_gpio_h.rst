.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/of_gpio.h

.. _`of_gpio_named_count`:

of_gpio_named_count
===================

.. c:function:: int of_gpio_named_count(struct device_node *np, const char* propname)

    Count GPIOs for a device

    :param np:
        device node to count GPIOs for
    :type np: struct device_node \*

    :param propname:
        property name containing gpio specifier(s)
    :type propname: const char\*

.. _`of_gpio_named_count.description`:

Description
-----------

The function returns the count of GPIOs specified for a node.
Note that the empty GPIO specifiers count too. Returns either
Number of gpios defined in property,
-EINVAL for an incorrectly formed gpios property, or
-ENOENT for a missing gpios property

.. _`of_gpio_named_count.example`:

Example
-------

.. code-block:: c

    gpios = <0
             &gpio1 1 2
             0
             &gpio2 3 4>;

    The above example defines four GPIOs, two of which are not specified.
    This function will return '4'


.. _`of_gpio_count`:

of_gpio_count
=============

.. c:function:: int of_gpio_count(struct device_node *np)

    Count GPIOs for a device

    :param np:
        device node to count GPIOs for
    :type np: struct device_node \*

.. _`of_gpio_count.description`:

Description
-----------

Same as of_gpio_named_count, but hard coded to use the 'gpios' property

.. _`of_get_named_gpio`:

of_get_named_gpio
=================

.. c:function:: int of_get_named_gpio(struct device_node *np, const char *propname, int index)

    Get a GPIO number to use with GPIO API

    :param np:
        device node to get GPIO from
    :type np: struct device_node \*

    :param propname:
        Name of property containing gpio specifier(s)
    :type propname: const char \*

    :param index:
        index of the GPIO
    :type index: int

.. _`of_get_named_gpio.description`:

Description
-----------

Returns GPIO number to use with Linux generic GPIO API, or one of the errno
value on the error condition.

.. _`of_get_gpio`:

of_get_gpio
===========

.. c:function:: int of_get_gpio(struct device_node *np, int index)

    Get a GPIO number to use with GPIO API

    :param np:
        device node to get GPIO from
    :type np: struct device_node \*

    :param index:
        index of the GPIO
    :type index: int

.. _`of_get_gpio.description`:

Description
-----------

Returns GPIO number to use with Linux generic GPIO API, or one of the errno
value on the error condition.

.. This file was automatic generated / don't edit.

