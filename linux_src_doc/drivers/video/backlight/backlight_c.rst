.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/backlight.c

.. _`backlight_force_update`:

backlight_force_update
======================

.. c:function:: void backlight_force_update(struct backlight_device *bd, enum backlight_update_reason reason)

    tell the backlight subsystem that hardware state has changed

    :param struct backlight_device \*bd:
        the backlight device to update

    :param enum backlight_update_reason reason:
        *undescribed*

.. _`backlight_force_update.description`:

Description
-----------

Updates the internal state of the backlight in response to a hardware event,
and generate a uevent to notify userspace

.. _`backlight_device_register`:

backlight_device_register
=========================

.. c:function:: struct backlight_device *backlight_device_register(const char *name, struct device *parent, void *devdata, const struct backlight_ops *ops, const struct backlight_properties *props)

    create and register a new object of backlight_device class.

    :param const char \*name:
        the name of the new object(must be the same as the name of the
        respective framebuffer device).

    :param struct device \*parent:
        a pointer to the parent device

    :param void \*devdata:
        an optional pointer to be stored for private driver use. The
        methods may retrieve it by using bl_get_data(bd).

    :param const struct backlight_ops \*ops:
        the backlight operations structure.

    :param const struct backlight_properties \*props:
        *undescribed*

.. _`backlight_device_register.description`:

Description
-----------

Creates and registers new backlight device. Returns either an
\ :c:func:`ERR_PTR`\  or a pointer to the newly allocated device.

.. _`backlight_device_unregister`:

backlight_device_unregister
===========================

.. c:function:: void backlight_device_unregister(struct backlight_device *bd)

    unregisters a backlight device object.

    :param struct backlight_device \*bd:
        the backlight device object to be unregistered and freed.

.. _`backlight_device_unregister.description`:

Description
-----------

Unregisters a previously registered via backlight_device_register object.

.. _`backlight_register_notifier`:

backlight_register_notifier
===========================

.. c:function:: int backlight_register_notifier(struct notifier_block *nb)

    get notified of backlight (un)registration

    :param struct notifier_block \*nb:
        notifier block with the notifier to call on backlight (un)registration

.. _`backlight_register_notifier.description`:

Description
-----------

@return 0 on success, otherwise a negative error code

Register a notifier to get notified when backlight devices get registered
or unregistered.

.. _`backlight_unregister_notifier`:

backlight_unregister_notifier
=============================

.. c:function:: int backlight_unregister_notifier(struct notifier_block *nb)

    unregister a backlight notifier

    :param struct notifier_block \*nb:
        notifier block to unregister

.. _`backlight_unregister_notifier.description`:

Description
-----------

@return 0 on success, otherwise a negative error code

Register a notifier to get notified when backlight devices get registered
or unregistered.

.. _`devm_backlight_device_register`:

devm_backlight_device_register
==============================

.. c:function:: struct backlight_device *devm_backlight_device_register(struct device *dev, const char *name, struct device *parent, void *devdata, const struct backlight_ops *ops, const struct backlight_properties *props)

    resource managed \ :c:func:`backlight_device_register`\ 

    :param struct device \*dev:
        the device to register

    :param const char \*name:
        the name of the device

    :param struct device \*parent:
        a pointer to the parent device

    :param void \*devdata:
        an optional pointer to be stored for private driver use

    :param const struct backlight_ops \*ops:
        the backlight operations structure

    :param const struct backlight_properties \*props:
        the backlight properties

.. _`devm_backlight_device_register.description`:

Description
-----------

@return a struct backlight on success, or an ERR_PTR on error

Managed \ :c:func:`backlight_device_register`\ . The backlight_device returned
from this function are automatically freed on driver detach.
See \ :c:func:`backlight_device_register`\  for more information.

.. _`devm_backlight_device_unregister`:

devm_backlight_device_unregister
================================

.. c:function:: void devm_backlight_device_unregister(struct device *dev, struct backlight_device *bd)

    resource managed \ :c:func:`backlight_device_unregister`\ 

    :param struct device \*dev:
        the device to unregister

    :param struct backlight_device \*bd:
        the backlight device to unregister

.. _`devm_backlight_device_unregister.description`:

Description
-----------

Deallocated a backlight allocated with \ :c:func:`devm_backlight_device_register`\ .
Normally this function will not need to be called and the resource management
code will ensure that the resource is freed.

.. _`of_find_backlight_by_node`:

of_find_backlight_by_node
=========================

.. c:function:: struct backlight_device *of_find_backlight_by_node(struct device_node *node)

    find backlight device by device-tree node

    :param struct device_node \*node:
        device-tree node of the backlight device

.. _`of_find_backlight_by_node.description`:

Description
-----------

Returns a pointer to the backlight device corresponding to the given DT
node or NULL if no such backlight device exists or if the device hasn't
been probed yet.

This function obtains a reference on the backlight device and it is the
caller's responsibility to drop the reference by calling \ :c:func:`put_device`\  on
the backlight device's .dev field.

.. This file was automatic generated / don't edit.

