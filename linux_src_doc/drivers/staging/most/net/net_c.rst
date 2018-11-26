.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/net/net.c

.. _`on_netinfo`:

on_netinfo
==========

.. c:function:: void on_netinfo(struct most_interface *iface, unsigned char link_stat, unsigned char *mac_addr)

    callback for HDM to be informed about HW's MAC \ ``param``\  iface - most interface instance \ ``param``\  link_stat - link status \ ``param``\  mac_addr - MAC address

    :param iface:
        *undescribed*
    :type iface: struct most_interface \*

    :param link_stat:
        *undescribed*
    :type link_stat: unsigned char

    :param mac_addr:
        *undescribed*
    :type mac_addr: unsigned char \*

.. This file was automatic generated / don't edit.

