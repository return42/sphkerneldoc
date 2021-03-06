.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/function/u_ether.h

.. _`gether_set_gadget`:

gether_set_gadget
=================

.. c:function:: void gether_set_gadget(struct net_device *net, struct usb_gadget *g)

    initialize one ethernet-over-usb link with a gadget

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param g:
        the gadget to initialize with
    :type g: struct usb_gadget \*

.. _`gether_set_gadget.description`:

Description
-----------

This associates one ethernet-over-usb link with a gadget.

.. _`gether_set_dev_addr`:

gether_set_dev_addr
===================

.. c:function:: int gether_set_dev_addr(struct net_device *net, const char *dev_addr)

    initialize an ethernet-over-usb link with eth address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param dev_addr:
        eth address of this device
    :type dev_addr: const char \*

.. _`gether_set_dev_addr.description`:

Description
-----------

This sets the device-side Ethernet address of this ethernet-over-usb link
if dev_addr is correct.
Returns negative errno if the new address is incorrect.

.. _`gether_get_dev_addr`:

gether_get_dev_addr
===================

.. c:function:: int gether_get_dev_addr(struct net_device *net, char *dev_addr, int len)

    get an ethernet-over-usb link eth address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param dev_addr:
        place to store device's eth address
    :type dev_addr: char \*

    :param len:
        length of the \ ``dev_addr``\  buffer
    :type len: int

.. _`gether_get_dev_addr.description`:

Description
-----------

This gets the device-side Ethernet address of this ethernet-over-usb link.
Returns zero on success, else negative errno.

.. _`gether_set_host_addr`:

gether_set_host_addr
====================

.. c:function:: int gether_set_host_addr(struct net_device *net, const char *host_addr)

    initialize an ethernet-over-usb link with host address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param host_addr:
        eth address of the host
    :type host_addr: const char \*

.. _`gether_set_host_addr.description`:

Description
-----------

This sets the host-side Ethernet address of this ethernet-over-usb link
if host_addr is correct.
Returns negative errno if the new address is incorrect.

.. _`gether_get_host_addr`:

gether_get_host_addr
====================

.. c:function:: int gether_get_host_addr(struct net_device *net, char *host_addr, int len)

    get an ethernet-over-usb link host address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param host_addr:
        place to store eth address of the host
    :type host_addr: char \*

    :param len:
        length of the \ ``host_addr``\  buffer
    :type len: int

.. _`gether_get_host_addr.description`:

Description
-----------

This gets the host-side Ethernet address of this ethernet-over-usb link.
Returns zero on success, else negative errno.

.. _`gether_get_host_addr_cdc`:

gether_get_host_addr_cdc
========================

.. c:function:: int gether_get_host_addr_cdc(struct net_device *net, char *host_addr, int len)

    get an ethernet-over-usb link host address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param host_addr:
        place to store eth address of the host
    :type host_addr: char \*

    :param len:
        length of the \ ``host_addr``\  buffer
    :type len: int

.. _`gether_get_host_addr_cdc.description`:

Description
-----------

This gets the CDC formatted host-side Ethernet address of this
ethernet-over-usb link.
Returns zero on success, else negative errno.

.. _`gether_get_host_addr_u8`:

gether_get_host_addr_u8
=======================

.. c:function:: void gether_get_host_addr_u8(struct net_device *net, u8 host_mac)

    get an ethernet-over-usb link host address

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param host_mac:
        place to store the eth address of the host
    :type host_mac: u8

.. _`gether_get_host_addr_u8.description`:

Description
-----------

This gets the binary formatted host-side Ethernet address of this
ethernet-over-usb link.

.. _`gether_set_qmult`:

gether_set_qmult
================

.. c:function:: void gether_set_qmult(struct net_device *net, unsigned qmult)

    initialize an ethernet-over-usb link with a multiplier

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param qmult:
        queue multiplier
    :type qmult: unsigned

.. _`gether_set_qmult.description`:

Description
-----------

This sets the queue length multiplier of this ethernet-over-usb link.
For higher speeds use longer queues.

.. _`gether_get_qmult`:

gether_get_qmult
================

.. c:function:: unsigned gether_get_qmult(struct net_device *net)

    get an ethernet-over-usb link multiplier

    :param net:
        device representing this link
    :type net: struct net_device \*

.. _`gether_get_qmult.description`:

Description
-----------

This gets the queue length multiplier of this ethernet-over-usb link.

.. _`gether_get_ifname`:

gether_get_ifname
=================

.. c:function:: int gether_get_ifname(struct net_device *net, char *name, int len)

    get an ethernet-over-usb link interface name

    :param net:
        device representing this link
    :type net: struct net_device \*

    :param name:
        place to store the interface name
    :type name: char \*

    :param len:
        length of the \ ``name``\  buffer
    :type len: int

.. _`gether_get_ifname.description`:

Description
-----------

This gets the interface name of this ethernet-over-usb link.
Returns zero on success, else negative errno.

.. This file was automatic generated / don't edit.

