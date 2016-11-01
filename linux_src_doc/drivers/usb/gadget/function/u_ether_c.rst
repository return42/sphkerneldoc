.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/function/u_ether.c

.. _`gether_setup_name`:

gether_setup_name
=================

.. c:function:: struct eth_dev *gether_setup_name(struct usb_gadget *g, const char *dev_addr, const char *host_addr, u8 ethaddr[ETH_ALEN], unsigned qmult, const char *netname)

    initialize one ethernet-over-usb link

    :param struct usb_gadget \*g:
        gadget to associated with these links

    :param const char \*dev_addr:
        *undescribed*

    :param const char \*host_addr:
        *undescribed*

    :param u8 ethaddr:
        NULL, or a buffer in which the ethernet address of the
        host side of the link is recorded

    :param unsigned qmult:
        *undescribed*

    :param const char \*netname:
        name for network device (for example, "usb")

.. _`gether_setup_name.context`:

Context
-------

may sleep

.. _`gether_setup_name.description`:

Description
-----------

This sets up the single network link that may be exported by a
gadget driver using this framework.  The link layer addresses are
set up using module parameters.

Returns an eth_dev pointer on success, or an ERR_PTR on failure.

.. _`gether_cleanup`:

gether_cleanup
==============

.. c:function:: void gether_cleanup(struct eth_dev *dev)

    remove Ethernet-over-USB device

    :param struct eth_dev \*dev:
        *undescribed*

.. _`gether_cleanup.context`:

Context
-------

may sleep

.. _`gether_cleanup.description`:

Description
-----------

This is called to free all resources allocated by \ ``gether_setup``\ ().

.. _`gether_connect`:

gether_connect
==============

.. c:function:: struct net_device *gether_connect(struct gether *link)

    notify network layer that USB link is active

    :param struct gether \*link:
        the USB link, set up with endpoints, descriptors matching
        current device speed, and any framing wrapper(s) set up.

.. _`gether_connect.context`:

Context
-------

irqs blocked

.. _`gether_connect.description`:

Description
-----------

This is called to activate endpoints and let the network layer know
the connection is active ("carrier detect").  It may cause the I/O
queues to open and start letting network packets flow, but will in
any case activate the endpoints so that they respond properly to the
USB host.

Verify net_device pointer returned using \ :c:func:`IS_ERR`\ .  If it doesn't
indicate some error code (negative errno), ep->driver_data values
have been overwritten.

.. _`gether_disconnect`:

gether_disconnect
=================

.. c:function:: void gether_disconnect(struct gether *link)

    notify network layer that USB link is inactive

    :param struct gether \*link:
        the USB link, on which \ :c:func:`gether_connect`\  was called

.. _`gether_disconnect.context`:

Context
-------

irqs blocked

.. _`gether_disconnect.description`:

Description
-----------

This is called to deactivate endpoints and let the network layer know
the connection went inactive ("no carrier").

On return, the state is as if \ :c:func:`gether_connect`\  had never been called.
The endpoints are inactive, and accordingly without active USB I/O.
Pointers to endpoint descriptors and endpoint private data are nulled.

.. This file was automatic generated / don't edit.

