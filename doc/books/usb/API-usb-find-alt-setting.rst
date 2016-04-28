.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-find-alt-setting:

====================
usb_find_alt_setting
====================

*man usb_find_alt_setting(9)*

*4.6.0-rc5*

Given a configuration, find the alternate setting for the given
interface.


Synopsis
========

.. c:function:: struct usb_host_interface * usb_find_alt_setting( struct usb_host_config * config, unsigned int iface_num, unsigned int alt_num )

Arguments
=========

``config``
    the configuration to search (not necessarily the current config).

``iface_num``
    interface number to search in

``alt_num``
    alternate interface setting number to search for.


Description
===========

Search the configuration's interface cache for the given alt setting.


Return
======

The alternate setting, if found. ``NULL`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
