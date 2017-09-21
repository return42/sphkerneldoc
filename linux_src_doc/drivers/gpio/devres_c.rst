.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/devres.c

.. _`devm_gpiod_get`:

devm_gpiod_get
==============

.. c:function:: struct gpio_desc *devm_gpiod_get(struct device *dev, const char *con_id, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get.description`:

Description
-----------

Managed \ :c:func:`gpiod_get`\ . GPIO descriptors returned from this function are
automatically disposed on driver detach. See \ :c:func:`gpiod_get`\  for detailed
information about behavior and return values.

.. _`devm_gpiod_get_optional`:

devm_gpiod_get_optional
=======================

.. c:function:: struct gpio_desc *devm_gpiod_get_optional(struct device *dev, const char *con_id, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get_optional`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get_optional.description`:

Description
-----------

Managed \ :c:func:`gpiod_get_optional`\ . GPIO descriptors returned from this function
are automatically disposed on driver detach. See \ :c:func:`gpiod_get_optional`\  for
detailed information about behavior and return values.

.. _`devm_gpiod_get_index`:

devm_gpiod_get_index
====================

.. c:function:: struct gpio_desc *devm_gpiod_get_index(struct device *dev, const char *con_id, unsigned int idx, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get_index`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int idx:
        index of the GPIO to obtain in the consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get_index.description`:

Description
-----------

Managed \ :c:func:`gpiod_get_index`\ . GPIO descriptors returned from this function are
automatically disposed on driver detach. See \ :c:func:`gpiod_get_index`\  for detailed
information about behavior and return values.

.. _`devm_fwnode_get_index_gpiod_from_child`:

devm_fwnode_get_index_gpiod_from_child
======================================

.. c:function:: struct gpio_desc *devm_fwnode_get_index_gpiod_from_child(struct device *dev, const char *con_id, int index, struct fwnode_handle *child, enum gpiod_flags flags, const char *label)

    get a GPIO descriptor from a device's child node

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param int index:
        index of the GPIO to obtain in the consumer

    :param struct fwnode_handle \*child:
        firmware node (child of \ ``dev``\ )

    :param enum gpiod_flags flags:
        GPIO initialization flags

    :param const char \*label:
        label to attach to the requested GPIO

.. _`devm_fwnode_get_index_gpiod_from_child.description`:

Description
-----------

GPIO descriptors returned from this function are automatically disposed on
driver detach.

On successful request the GPIO pin is configured in accordance with
provided \ ``flags``\ .

.. _`devm_gpiod_get_index_optional`:

devm_gpiod_get_index_optional
=============================

.. c:function:: struct gpio_desc *devm_gpiod_get_index_optional(struct device *dev, const char *con_id, unsigned int index, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get_index_optional`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int index:
        index of the GPIO to obtain in the consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get_index_optional.description`:

Description
-----------

Managed \ :c:func:`gpiod_get_index_optional`\ . GPIO descriptors returned from this
function are automatically disposed on driver detach. See
\ :c:func:`gpiod_get_index_optional`\  for detailed information about behavior and
return values.

.. _`devm_gpiod_get_array`:

devm_gpiod_get_array
====================

.. c:function:: struct gpio_descs *devm_gpiod_get_array(struct device *dev, const char *con_id, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get_array`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get_array.description`:

Description
-----------

Managed \ :c:func:`gpiod_get_array`\ . GPIO descriptors returned from this function are
automatically disposed on driver detach. See \ :c:func:`gpiod_get_array`\  for detailed
information about behavior and return values.

.. _`devm_gpiod_get_array_optional`:

devm_gpiod_get_array_optional
=============================

.. c:function:: struct gpio_descs *devm_gpiod_get_array_optional(struct device *dev, const char *con_id, enum gpiod_flags flags)

    Resource-managed \ :c:func:`gpiod_get_array_optional`\ 

    :param struct device \*dev:
        GPIO consumer

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`devm_gpiod_get_array_optional.description`:

Description
-----------

Managed \ :c:func:`gpiod_get_array_optional`\ . GPIO descriptors returned from this
function are automatically disposed on driver detach.
See \ :c:func:`gpiod_get_array_optional`\  for detailed information about behavior and
return values.

.. _`devm_gpiod_put`:

devm_gpiod_put
==============

.. c:function:: void devm_gpiod_put(struct device *dev, struct gpio_desc *desc)

    Resource-managed \ :c:func:`gpiod_put`\ 

    :param struct device \*dev:
        GPIO consumer

    :param struct gpio_desc \*desc:
        GPIO descriptor to dispose of

.. _`devm_gpiod_put.description`:

Description
-----------

Dispose of a GPIO descriptor obtained with \ :c:func:`devm_gpiod_get`\  or
\ :c:func:`devm_gpiod_get_index`\ . Normally this function will not be called as the GPIO
will be disposed of by the resource management code.

.. _`devm_gpiod_put_array`:

devm_gpiod_put_array
====================

.. c:function:: void devm_gpiod_put_array(struct device *dev, struct gpio_descs *descs)

    Resource-managed \ :c:func:`gpiod_put_array`\ 

    :param struct device \*dev:
        GPIO consumer

    :param struct gpio_descs \*descs:
        GPIO descriptor array to dispose of

.. _`devm_gpiod_put_array.description`:

Description
-----------

Dispose of an array of GPIO descriptors obtained with \ :c:func:`devm_gpiod_get_array`\ .
Normally this function will not be called as the GPIOs will be disposed of
by the resource management code.

.. _`devm_gpio_request`:

devm_gpio_request
=================

.. c:function:: int devm_gpio_request(struct device *dev, unsigned gpio, const char *label)

    request a GPIO for a managed device

    :param struct device \*dev:
        device to request the GPIO for

    :param unsigned gpio:
        GPIO to allocate

    :param const char \*label:
        the name of the requested GPIO

.. _`devm_gpio_request.description`:

Description
-----------

     Except for the extra \ ``dev``\  argument, this function takes the
     same arguments and performs the same function as
     \ :c:func:`gpio_request`\ .  GPIOs requested with this function will be
     automatically freed on driver detach.

     If an GPIO allocated with this function needs to be freed
     separately, \ :c:func:`devm_gpio_free`\  must be used.

.. _`devm_gpio_request_one`:

devm_gpio_request_one
=====================

.. c:function:: int devm_gpio_request_one(struct device *dev, unsigned gpio, unsigned long flags, const char *label)

    request a single GPIO with initial setup

    :param struct device \*dev:
        device to request for

    :param unsigned gpio:
        the GPIO number

    :param unsigned long flags:
        GPIO configuration as specified by GPIOF_*

    :param const char \*label:
        a literal description string of this GPIO

.. _`devm_gpio_free`:

devm_gpio_free
==============

.. c:function:: void devm_gpio_free(struct device *dev, unsigned int gpio)

    free a GPIO

    :param struct device \*dev:
        device to free GPIO for

    :param unsigned int gpio:
        GPIO to free

.. _`devm_gpio_free.description`:

Description
-----------

     Except for the extra \ ``dev``\  argument, this function takes the
     same arguments and performs the same function as \ :c:func:`gpio_free`\ .
     This function instead of \ :c:func:`gpio_free`\  should be used to manually
     free GPIOs allocated with \ :c:func:`devm_gpio_request`\ .

.. This file was automatic generated / don't edit.

