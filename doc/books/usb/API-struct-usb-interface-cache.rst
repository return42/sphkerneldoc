.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-interface-cache:

==========================
struct usb_interface_cache
==========================

*man struct usb_interface_cache(9)*

*4.6.0-rc5*

long-term representation of a device interface


Synopsis
========

.. code-block:: c

    struct usb_interface_cache {
      unsigned num_altsetting;
      struct kref ref;
      struct usb_host_interface altsetting[0];
    };


Members
=======

num_altsetting
    number of altsettings defined.

ref
    reference counter.

altsetting[0]
    variable-length array of interface structures, one for each
    alternate setting that may be selected. Each one includes a set of
    endpoint configurations. They will be in no particular order.


Description
===========

These structures persist for the lifetime of a usb_device, unlike
struct usb_interface (which persists only as long as its configuration
is installed). The altsetting arrays can be accessed through these
structures at any time, permitting comparison of configurations and
providing support for the /proc/bus/usb/devices pseudo-file.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
