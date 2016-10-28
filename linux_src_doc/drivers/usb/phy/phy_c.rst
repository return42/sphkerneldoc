.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/phy/phy.c

.. _`devm_usb_get_phy`:

devm_usb_get_phy
================

.. c:function:: struct usb_phy *devm_usb_get_phy(struct device *dev, enum usb_phy_type type)

    find the USB PHY \ ``dev``\  - device that requests this phy \ ``type``\  - the type of the phy the controller requires

    :param struct device \*dev:
        *undescribed*

    :param enum usb_phy_type type:
        *undescribed*

.. _`devm_usb_get_phy.description`:

Description
-----------

Gets the phy using \ :c:func:`usb_get_phy`\ , and associates a device with it using
devres. On driver detach, release function is invoked on the devres data,
then, devres data is freed.

For use by USB host and peripheral drivers.

.. _`usb_get_phy`:

usb_get_phy
===========

.. c:function:: struct usb_phy *usb_get_phy(enum usb_phy_type type)

    find the USB PHY \ ``type``\  - the type of the phy the controller requires

    :param enum usb_phy_type type:
        *undescribed*

.. _`usb_get_phy.description`:

Description
-----------

Returns the phy driver, after getting a refcount to it; or
-ENODEV if there is no such phy.  The caller is responsible for
calling \ :c:func:`usb_put_phy`\  to release that count.

For use by USB host and peripheral drivers.

.. _`devm_usb_get_phy_by_node`:

devm_usb_get_phy_by_node
========================

.. c:function:: struct  usb_phy *devm_usb_get_phy_by_node(struct device *dev, struct device_node *node, struct notifier_block *nb)

    find the USB PHY by device_node \ ``dev``\  - device that requests this phy \ ``node``\  - the device_node for the phy device. \ ``nb``\  - a notifier_block to register with the phy.

    :param struct device \*dev:
        *undescribed*

    :param struct device_node \*node:
        *undescribed*

    :param struct notifier_block \*nb:
        *undescribed*

.. _`devm_usb_get_phy_by_node.description`:

Description
-----------

Returns the phy driver associated with the given device_node,
after getting a refcount to it, -ENODEV if there is no such phy or
-EPROBE_DEFER if the device is not yet loaded. While at that, it
also associates the device with
the phy using devres. On driver detach, release function is invoked
on the devres data, then, devres data is freed.

For use by peripheral drivers for devices related to a phy,
such as a charger.

.. _`devm_usb_get_phy_by_phandle`:

devm_usb_get_phy_by_phandle
===========================

.. c:function:: struct usb_phy *devm_usb_get_phy_by_phandle(struct device *dev, const char *phandle, u8 index)

    find the USB PHY by phandle \ ``dev``\  - device that requests this phy \ ``phandle``\  - name of the property holding the phy phandle value \ ``index``\  - the index of the phy

    :param struct device \*dev:
        *undescribed*

    :param const char \*phandle:
        *undescribed*

    :param u8 index:
        *undescribed*

.. _`devm_usb_get_phy_by_phandle.description`:

Description
-----------

Returns the phy driver associated with the given phandle value,
after getting a refcount to it, -ENODEV if there is no such phy or
-EPROBE_DEFER if there is a phandle to the phy, but the device is
not yet loaded. While at that, it also associates the device with
the phy using devres. On driver detach, release function is invoked
on the devres data, then, devres data is freed.

For use by USB host and peripheral drivers.

.. _`usb_get_phy_dev`:

usb_get_phy_dev
===============

.. c:function:: struct usb_phy *usb_get_phy_dev(struct device *dev, u8 index)

    find the USB PHY \ ``dev``\  - device that requests this phy \ ``index``\  - the index of the phy

    :param struct device \*dev:
        *undescribed*

    :param u8 index:
        *undescribed*

.. _`usb_get_phy_dev.description`:

Description
-----------

Returns the phy driver, after getting a refcount to it; or
-ENODEV if there is no such phy.  The caller is responsible for
calling \ :c:func:`usb_put_phy`\  to release that count.

For use by USB host and peripheral drivers.

.. _`devm_usb_get_phy_dev`:

devm_usb_get_phy_dev
====================

.. c:function:: struct usb_phy *devm_usb_get_phy_dev(struct device *dev, u8 index)

    find the USB PHY using device ptr and index \ ``dev``\  - device that requests this phy \ ``index``\  - the index of the phy

    :param struct device \*dev:
        *undescribed*

    :param u8 index:
        *undescribed*

.. _`devm_usb_get_phy_dev.description`:

Description
-----------

Gets the phy using \ :c:func:`usb_get_phy_dev`\ , and associates a device with it using
devres. On driver detach, release function is invoked on the devres data,
then, devres data is freed.

For use by USB host and peripheral drivers.

.. _`devm_usb_put_phy`:

devm_usb_put_phy
================

.. c:function:: void devm_usb_put_phy(struct device *dev, struct usb_phy *phy)

    release the USB PHY \ ``dev``\  - device that wants to release this phy \ ``phy``\  - the phy returned by \ :c:func:`devm_usb_get_phy`\ 

    :param struct device \*dev:
        *undescribed*

    :param struct usb_phy \*phy:
        *undescribed*

.. _`devm_usb_put_phy.description`:

Description
-----------

destroys the devres associated with this phy and invokes usb_put_phy
to release the phy.

For use by USB host and peripheral drivers.

.. _`usb_put_phy`:

usb_put_phy
===========

.. c:function:: void usb_put_phy(struct usb_phy *x)

    release the USB PHY

    :param struct usb_phy \*x:
        the phy returned by \ :c:func:`usb_get_phy`\ 

.. _`usb_put_phy.description`:

Description
-----------

Releases a refcount the caller received from \ :c:func:`usb_get_phy`\ .

For use by USB host and peripheral drivers.

.. _`usb_add_phy`:

usb_add_phy
===========

.. c:function:: int usb_add_phy(struct usb_phy *x, enum usb_phy_type type)

    declare the USB PHY

    :param struct usb_phy \*x:
        the USB phy to be used; or NULL
        \ ``type``\  - the type of this PHY

    :param enum usb_phy_type type:
        *undescribed*

.. _`usb_add_phy.description`:

Description
-----------

This call is exclusively for use by phy drivers, which
coordinate the activities of drivers for host and peripheral
controllers, and in some cases for VBUS current regulation.

.. _`usb_add_phy_dev`:

usb_add_phy_dev
===============

.. c:function:: int usb_add_phy_dev(struct usb_phy *x)

    declare the USB PHY

    :param struct usb_phy \*x:
        the USB phy to be used; or NULL

.. _`usb_add_phy_dev.description`:

Description
-----------

This call is exclusively for use by phy drivers, which
coordinate the activities of drivers for host and peripheral
controllers, and in some cases for VBUS current regulation.

.. _`usb_remove_phy`:

usb_remove_phy
==============

.. c:function:: void usb_remove_phy(struct usb_phy *x)

    remove the OTG PHY

    :param struct usb_phy \*x:
        the USB OTG PHY to be removed;

.. _`usb_remove_phy.description`:

Description
-----------

This reverts the effects of usb_add_phy

.. _`usb_bind_phy`:

usb_bind_phy
============

.. c:function:: int usb_bind_phy(const char *dev_name, u8 index, const char *phy_dev_name)

    bind the phy and the controller that uses the phy

    :param const char \*dev_name:
        the device name of the device that will bind to the phy

    :param u8 index:
        index to specify the port number

    :param const char \*phy_dev_name:
        the device name of the phy

.. _`usb_bind_phy.description`:

Description
-----------

Fills the phy_bind structure with the dev_name and phy_dev_name. This will
be used when the phy driver registers the phy and when the controller
requests this phy.

To be used by platform specific initialization code.

.. _`usb_phy_set_event`:

usb_phy_set_event
=================

.. c:function:: void usb_phy_set_event(struct usb_phy *x, unsigned long event)

    set event to phy event

    :param struct usb_phy \*x:
        the phy returned by \ :c:func:`usb_get_phy`\ ;

    :param unsigned long event:
        *undescribed*

.. _`usb_phy_set_event.description`:

Description
-----------

This sets event to phy event

.. This file was automatic generated / don't edit.

