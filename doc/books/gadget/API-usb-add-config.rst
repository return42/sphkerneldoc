.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-add-config:

==============
usb_add_config
==============

*man usb_add_config(9)*

*4.6.0-rc5*

add a configuration to a device.


Synopsis
========

.. c:function:: int usb_add_config( struct usb_composite_dev * cdev, struct usb_configuration * config, int (*bind) struct usb_configuration * )

Arguments
=========

``cdev``
    wraps the USB gadget

``config``
    the configuration, with bConfigurationValue assigned

``bind``
    the configuration's bind function


Context
=======

single threaded during gadget setup


Description
===========

One of the main tasks of a composite ``bind``\ () routine is to add each
of the configurations it supports, using this routine.

This function returns the value of the configuration's ``bind``\ (),
which is zero for success else a negative errno value. Binding
configurations assigns global resources including string IDs, and
per-configuration resources such as interface IDs and endpoints.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
