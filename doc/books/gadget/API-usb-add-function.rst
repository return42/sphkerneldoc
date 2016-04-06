
.. _API-usb-add-function:

================
usb_add_function
================

*man usb_add_function(9)*

*4.6.0-rc1*

add a function to a configuration


Synopsis
========

.. c:function:: int usb_add_function( struct usb_configuration * config, struct usb_function * function )

Arguments
=========

``config``
    the configuration

``function``
    the function being added


Context
=======

single threaded during gadget setup


Description
===========

After initialization, each configuration must have one or more functions added to it. Adding a function involves calling its ``bind``\ () method to allocate resources such as
interface and string identifiers and endpoints.

This function returns the value of the function's ``bind``, which is zero for success else a negative errno value.
