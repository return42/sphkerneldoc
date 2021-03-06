.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/lcd.c

.. _`lcd_device_register`:

lcd_device_register
===================

.. c:function:: struct lcd_device *lcd_device_register(const char *name, struct device *parent, void *devdata, struct lcd_ops *ops)

    register a new object of lcd_device class.

    :param name:
        the name of the new object(must be the same as the name of the
        respective framebuffer device).
    :type name: const char \*

    :param parent:
        *undescribed*
    :type parent: struct device \*

    :param devdata:
        an optional pointer to be stored in the device. The
        methods may retrieve it by using lcd_get_data(ld).
    :type devdata: void \*

    :param ops:
        the lcd operations structure.
    :type ops: struct lcd_ops \*

.. _`lcd_device_register.description`:

Description
-----------

Creates and registers a new lcd device. Returns either an \ :c:func:`ERR_PTR`\ 
or a pointer to the newly allocated device.

.. _`lcd_device_unregister`:

lcd_device_unregister
=====================

.. c:function:: void lcd_device_unregister(struct lcd_device *ld)

    unregisters a object of lcd_device class.

    :param ld:
        the lcd device object to be unregistered and freed.
    :type ld: struct lcd_device \*

.. _`lcd_device_unregister.description`:

Description
-----------

Unregisters a previously registered via lcd_device_register object.

.. _`devm_lcd_device_register`:

devm_lcd_device_register
========================

.. c:function:: struct lcd_device *devm_lcd_device_register(struct device *dev, const char *name, struct device *parent, void *devdata, struct lcd_ops *ops)

    resource managed \ :c:func:`lcd_device_register`\ 

    :param dev:
        the device to register
    :type dev: struct device \*

    :param name:
        the name of the device
    :type name: const char \*

    :param parent:
        a pointer to the parent device
    :type parent: struct device \*

    :param devdata:
        an optional pointer to be stored for private driver use
    :type devdata: void \*

    :param ops:
        the lcd operations structure
    :type ops: struct lcd_ops \*

.. _`devm_lcd_device_register.description`:

Description
-----------

\ ``return``\  a struct lcd on success, or an ERR_PTR on error

Managed \ :c:func:`lcd_device_register`\ . The lcd_device returned from this function
are automatically freed on driver detach. See \ :c:func:`lcd_device_register`\ 
for more information.

.. _`devm_lcd_device_unregister`:

devm_lcd_device_unregister
==========================

.. c:function:: void devm_lcd_device_unregister(struct device *dev, struct lcd_device *ld)

    resource managed \ :c:func:`lcd_device_unregister`\ 

    :param dev:
        the device to unregister
    :type dev: struct device \*

    :param ld:
        the lcd device to unregister
    :type ld: struct lcd_device \*

.. _`devm_lcd_device_unregister.description`:

Description
-----------

Deallocated a lcd allocated with \ :c:func:`devm_lcd_device_register`\ . Normally
this function will not need to be called and the resource management
code will ensure that the resource is freed.

.. This file was automatic generated / don't edit.

