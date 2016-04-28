.. -*- coding: utf-8; mode: rst -*-

.. _API-module-usb-driver:

=================
module_usb_driver
=================

*man module_usb_driver(9)*

*4.6.0-rc5*

Helper macro for registering a USB driver


Synopsis
========

.. c:function:: module_usb_driver( __usb_driver )

Arguments
=========

``__usb_driver``
    usb_driver struct


Description
===========

Helper macro for USB drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces ``module_init`` and
``module_exit``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
