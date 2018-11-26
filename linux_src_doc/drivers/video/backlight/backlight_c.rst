.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/backlight.c

.. _`backlight_force_update`:

backlight_force_update
======================

.. c:function:: void backlight_force_update(struct backlight_device *bd, enum backlight_update_reason reason)

    tell the backlight subsystem that hardware state has changed

    :param bd:
        the backlight device to update
    :type bd: struct backlight_device \*

    :param reason:
        *undescribed*
    :type reason: enum backlight_update_reason

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

    :param name:
        the name of the new object(must be the same as the name of the
        respective framebuffer device).
    :type name: const char \*

    :param parent:
        a pointer to the parent device
    :type parent: struct device \*

    :param devdata:
        an optional pointer to be stored for private driver use. The
        methods may retrieve it by using bl_get_data(bd).
    :type devdata: void \*

    :param ops:
        the backlight operations structure.
    :type ops: const struct backlight_ops \*

    :param props:
        *undescribed*
    :type props: const struct backlight_properties \*

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

    :param bd:
        the backlight device object to be unregistered and freed.
    :type bd: struct backlight_device \*

.. _`backlight_device_unregister.description`:

Description
-----------

Unregisters a previously registered via backlight_device_register object.

.. _`backlight_register_notifier`:

backlight_register_notifier
===========================

.. c:function:: int backlight_register_notifier(struct notifier_block *nb)

    get notified of backlight (un)registration

    :param nb:
        notifier block with the notifier to call on backlight (un)registration
    :type nb: struct notifier_block \*

.. _`backlight_register_notifier.description`:

Description
-----------

\ ``return``\  0 on success, otherwise a negative error code

Register a notifier to get notified when backlight devices get registered
or unregistered.

.. _`backlight_unregister_notifier`:

backlight_unregister_notifier
=============================

.. c:function:: int backlight_unregister_notifier(struct notifier_block *nb)

    unregister a backlight notifier

    :param nb:
        notifier block to unregister
    :type nb: struct notifier_block \*

.. _`backlight_unregister_notifier.description`:

Description
-----------

\ ``return``\  0 on success, otherwise a negative error code

Register a notifier to get notified when backlight devices get registered
or unregistered.

.. _`devm_backlight_device_register`:

devm_backlight_device_register
==============================

.. c:function:: struct backlight_device *devm_backlight_device_register(struct device *dev, const char *name, struct device *parent, void *devdata, const struct backlight_ops *ops, const struct backlight_properties *props)

    resource managed \ :c:func:`backlight_device_register`\ 

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
        the backlight operations structure
    :type ops: const struct backlight_ops \*

    :param props:
        the backlight properties
    :type props: const struct backlight_properties \*

.. _`devm_backlight_device_register.description`:

Description
-----------

\ ``return``\  a struct backlight on success, or an ERR_PTR on error

Managed \ :c:func:`backlight_device_register`\ . The backlight_device returned
from this function are automatically freed on driver detach.
See \ :c:func:`backlight_device_register`\  for more information.

.. _`devm_backlight_device_unregister`:

devm_backlight_device_unregister
================================

.. c:function:: void devm_backlight_device_unregister(struct device *dev, struct backlight_device *bd)

    resource managed \ :c:func:`backlight_device_unregister`\ 

    :param dev:
        the device to unregister
    :type dev: struct device \*

    :param bd:
        the backlight device to unregister
    :type bd: struct backlight_device \*

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

    :param node:
        device-tree node of the backlight device
    :type node: struct device_node \*

.. _`of_find_backlight_by_node.description`:

Description
-----------

Returns a pointer to the backlight device corresponding to the given DT
node or NULL if no such backlight device exists or if the device hasn't
been probed yet.

This function obtains a reference on the backlight device and it is the
caller's responsibility to drop the reference by calling \ :c:func:`put_device`\  on
the backlight device's .dev field.

.. _`of_find_backlight`:

of_find_backlight
=================

.. c:function:: struct backlight_device *of_find_backlight(struct device *dev)

    Get backlight device

    :param dev:
        Device
    :type dev: struct device \*

.. _`of_find_backlight.description`:

Description
-----------

This function looks for a property named 'backlight' on the DT node
connected to \ ``dev``\  and looks up the backlight device.

Call \ :c:func:`backlight_put`\  to drop the reference on the backlight device.

.. _`of_find_backlight.return`:

Return
------

A pointer to the backlight device if found.
Error pointer -EPROBE_DEFER if the DT property is set, but no backlight
device is found.
NULL if there's no backlight property.

.. _`devm_of_find_backlight`:

devm_of_find_backlight
======================

.. c:function:: struct backlight_device *devm_of_find_backlight(struct device *dev)

    Resource-managed \ :c:func:`of_find_backlight`\ 

    :param dev:
        Device
    :type dev: struct device \*

.. _`devm_of_find_backlight.description`:

Description
-----------

Device managed version of \ :c:func:`of_find_backlight`\ .
The reference on the backlight device is automatically
dropped on driver detach.

.. This file was automatic generated / don't edit.

