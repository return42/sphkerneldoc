.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/epautoconf.c

.. _`usb_ep_autoconfig_ss`:

usb_ep_autoconfig_ss
====================

.. c:function:: struct usb_ep *usb_ep_autoconfig_ss(struct usb_gadget *gadget, struct usb_endpoint_descriptor *desc, struct usb_ss_ep_comp_descriptor *ep_comp)

    choose an endpoint matching the ep descriptor and ep companion descriptor

    :param gadget:
        The device to which the endpoint must belong.
    :type gadget: struct usb_gadget \*

    :param desc:
        Endpoint descriptor, with endpoint direction and transfer mode
        initialized.  For periodic transfers, the maximum packet
        size must also be initialized.  This is modified on
        success.
    :type desc: struct usb_endpoint_descriptor \*

    :param ep_comp:
        Endpoint companion descriptor, with the required
        number of streams. Will be modified when the chosen EP
        supports a different number of streams.
    :type ep_comp: struct usb_ss_ep_comp_descriptor \*

.. _`usb_ep_autoconfig_ss.description`:

Description
-----------

This routine replaces the usb_ep_autoconfig when needed
superspeed enhancments. If such enhancemnets are required,
the FD should call usb_ep_autoconfig_ss directly and provide
the additional ep_comp parameter.

By choosing an endpoint to use with the specified descriptor,
this routine simplifies writing gadget drivers that work with
multiple USB device controllers.  The endpoint would be
passed later to \ :c:func:`usb_ep_enable`\ , along with some descriptor.

That second descriptor won't always be the same as the first one.
For example, isochronous endpoints can be autoconfigured for high
bandwidth, and then used in several lower bandwidth altsettings.
Also, high and full speed descriptors will be different.

Be sure to examine and test the results of autoconfiguration
on your hardware.  This code may not make the best choices
about how to use the USB controller, and it can't know all
the restrictions that may apply. Some combinations of driver
and hardware won't be able to autoconfigure.

On success, this returns an claimed usb_ep, and modifies the endpoint
descriptor bEndpointAddress.  For bulk endpoints, the wMaxPacket value
is initialized as if the endpoint were used at full speed and
the bmAttribute field in the ep companion descriptor is
updated with the assigned number of streams if it is
different from the original value. To prevent the endpoint
from being returned by a later autoconfig call, claims it by
assigning ep->claimed to true.

On failure, this returns a null endpoint descriptor.

.. _`usb_ep_autoconfig`:

usb_ep_autoconfig
=================

.. c:function:: struct usb_ep *usb_ep_autoconfig(struct usb_gadget *gadget, struct usb_endpoint_descriptor *desc)

    choose an endpoint matching the descriptor

    :param gadget:
        The device to which the endpoint must belong.
    :type gadget: struct usb_gadget \*

    :param desc:
        Endpoint descriptor, with endpoint direction and transfer mode
        initialized.  For periodic transfers, the maximum packet
        size must also be initialized.  This is modified on success.
    :type desc: struct usb_endpoint_descriptor \*

.. _`usb_ep_autoconfig.description`:

Description
-----------

By choosing an endpoint to use with the specified descriptor, this
routine simplifies writing gadget drivers that work with multiple
USB device controllers.  The endpoint would be passed later to
\ :c:func:`usb_ep_enable`\ , along with some descriptor.

That second descriptor won't always be the same as the first one.
For example, isochronous endpoints can be autoconfigured for high
bandwidth, and then used in several lower bandwidth altsettings.
Also, high and full speed descriptors will be different.

Be sure to examine and test the results of autoconfiguration on your
hardware.  This code may not make the best choices about how to use the
USB controller, and it can't know all the restrictions that may apply.
Some combinations of driver and hardware won't be able to autoconfigure.

On success, this returns an claimed usb_ep, and modifies the endpoint
descriptor bEndpointAddress.  For bulk endpoints, the wMaxPacket value
is initialized as if the endpoint were used at full speed.  To prevent
the endpoint from being returned by a later autoconfig call, claims it
by assigning ep->claimed to true.

On failure, this returns a null endpoint descriptor.

.. _`usb_ep_autoconfig_release`:

usb_ep_autoconfig_release
=========================

.. c:function:: void usb_ep_autoconfig_release(struct usb_ep *ep)

    releases endpoint and set it to initial state

    :param ep:
        endpoint which should be released
    :type ep: struct usb_ep \*

.. _`usb_ep_autoconfig_release.description`:

Description
-----------

This function can be used during function bind for endpoints obtained
from \ :c:func:`usb_ep_autoconfig`\ . It unclaims endpoint claimed by
\ :c:func:`usb_ep_autoconfig`\  to make it available for other functions. Endpoint
which was released is no longer invalid and shouldn't be used in
context of function which released it.

.. _`usb_ep_autoconfig_reset`:

usb_ep_autoconfig_reset
=======================

.. c:function:: void usb_ep_autoconfig_reset(struct usb_gadget *gadget)

    reset endpoint autoconfig state

    :param gadget:
        device for which autoconfig state will be reset
    :type gadget: struct usb_gadget \*

.. _`usb_ep_autoconfig_reset.description`:

Description
-----------

Use this for devices where one configuration may need to assign
endpoint resources very differently from the next one.  It clears
state such as ep->claimed and the record of assigned endpoints
used by \ :c:func:`usb_ep_autoconfig`\ .

.. This file was automatic generated / don't edit.

