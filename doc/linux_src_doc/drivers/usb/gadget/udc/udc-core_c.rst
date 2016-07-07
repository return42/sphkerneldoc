.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/udc/udc-core.c

.. _`usb_gadget_giveback_request`:

usb_gadget_giveback_request
===========================

.. c:function:: void usb_gadget_giveback_request(struct usb_ep *ep, struct usb_request *req)

    give the request back to the gadget layer

    :param struct usb_ep \*ep:
        *undescribed*

    :param struct usb_request \*req:
        *undescribed*

.. _`usb_gadget_giveback_request.context`:

Context
-------

\ :c:func:`in_interrupt`\ 

.. _`usb_gadget_giveback_request.description`:

Description
-----------

This is called by device controller drivers in order to return the
completed request back to the gadget layer.

.. _`gadget_find_ep_by_name`:

gadget_find_ep_by_name
======================

.. c:function:: struct usb_ep *gadget_find_ep_by_name(struct usb_gadget *g, const char *name)

    returns ep whose name is the same as sting passed in second parameter or NULL if searched endpoint not found

    :param struct usb_gadget \*g:
        controller to check for quirk

    :param const char \*name:
        name of searched endpoint

.. _`usb_udc_vbus_handler`:

usb_udc_vbus_handler
====================

.. c:function:: void usb_udc_vbus_handler(struct usb_gadget *gadget, bool status)

    updates the udc core vbus status, and try to connect or disconnect gadget

    :param struct usb_gadget \*gadget:
        The gadget which vbus change occurs

    :param bool status:
        The vbus status

.. _`usb_udc_vbus_handler.description`:

Description
-----------

The udc driver calls it when it wants to connect or disconnect gadget
according to vbus status.

.. _`usb_gadget_udc_reset`:

usb_gadget_udc_reset
====================

.. c:function:: void usb_gadget_udc_reset(struct usb_gadget *gadget, struct usb_gadget_driver *driver)

    notifies the udc core that bus reset occurs

    :param struct usb_gadget \*gadget:
        The gadget which bus reset occurs

    :param struct usb_gadget_driver \*driver:
        The gadget driver we want to notify

.. _`usb_gadget_udc_reset.description`:

Description
-----------

If the udc driver has bus reset handler, it needs to call this when the bus
reset occurs, it notifies the gadget driver that the bus reset occurs as
well as updates gadget state.

.. _`usb_gadget_udc_start`:

usb_gadget_udc_start
====================

.. c:function:: int usb_gadget_udc_start(struct usb_udc *udc)

    tells usb device controller to start up

    :param struct usb_udc \*udc:
        The UDC to be started

.. _`usb_gadget_udc_start.description`:

Description
-----------

This call is issued by the UDC Class driver when it's about
to register a gadget driver to the device controller, before
calling gadget driver's \ :c:func:`bind`\  method.

It allows the controller to be powered off until strictly
necessary to have it powered on.

Returns zero on success, else negative errno.

.. _`usb_gadget_udc_stop`:

usb_gadget_udc_stop
===================

.. c:function:: void usb_gadget_udc_stop(struct usb_udc *udc)

    tells usb device controller we don't need it anymore

    :param struct usb_udc \*udc:
        *undescribed*

.. _`usb_gadget_udc_stop.description`:

Description
-----------

This call is issued by the UDC Class driver after calling
gadget driver's \ :c:func:`unbind`\  method.

The details are implementation specific, but it can go as
far as powering off UDC completely and disable its data
line pullups.

.. _`usb_udc_release`:

usb_udc_release
===============

.. c:function:: void usb_udc_release(struct device *dev)

    release the usb_udc struct

    :param struct device \*dev:
        the dev member within usb_udc

.. _`usb_udc_release.description`:

Description
-----------

This is called by driver's core in order to free memory once the last
reference is released.

.. _`usb_add_gadget_udc_release`:

usb_add_gadget_udc_release
==========================

.. c:function:: int usb_add_gadget_udc_release(struct device *parent, struct usb_gadget *gadget, void (*) release (struct device *dev)

    adds a new gadget to the udc class driver list

    :param struct device \*parent:
        the parent device to this udc. Usually the controller driver's
        device.

    :param struct usb_gadget \*gadget:
        the gadget to be added to the list.

    :param (void (\*) release (struct device \*dev):
        a gadget release function.

.. _`usb_add_gadget_udc_release.description`:

Description
-----------

Returns zero on success, negative errno otherwise.

.. _`usb_get_gadget_udc_name`:

usb_get_gadget_udc_name
=======================

.. c:function:: char *usb_get_gadget_udc_name( void)

    get the name of the first UDC controller This functions returns the name of the first UDC controller in the system. Please note that this interface is usefull only for legacy drivers which assume that there is only one UDC controller in the system and they need to get its name before initialization. There is no guarantee that the UDC of the returned name will be still available, when gadget driver registers itself.

    :param  void:
        no arguments

.. _`usb_get_gadget_udc_name.description`:

Description
-----------

Returns pointer to string with UDC controller name on success, NULL
otherwise. Caller should \ :c:func:`kfree`\  returned string.

.. _`usb_add_gadget_udc`:

usb_add_gadget_udc
==================

.. c:function:: int usb_add_gadget_udc(struct device *parent, struct usb_gadget *gadget)

    adds a new gadget to the udc class driver list

    :param struct device \*parent:
        the parent device to this udc. Usually the controller
        driver's device.

    :param struct usb_gadget \*gadget:
        the gadget to be added to the list

.. _`usb_add_gadget_udc.description`:

Description
-----------

Returns zero on success, negative errno otherwise.

.. _`usb_del_gadget_udc`:

usb_del_gadget_udc
==================

.. c:function:: void usb_del_gadget_udc(struct usb_gadget *gadget)

    deletes \ ``udc``\  from udc_list

    :param struct usb_gadget \*gadget:
        the gadget to be removed.

.. _`usb_del_gadget_udc.description`:

Description
-----------

This, will call \ :c:func:`usb_gadget_unregister_driver`\  if
the \ ``udc``\  is still busy.

.. This file was automatic generated / don't edit.

