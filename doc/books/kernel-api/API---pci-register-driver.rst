.. -*- coding: utf-8; mode: rst -*-

.. _API---pci-register-driver:

=====================
__pci_register_driver
=====================

*man __pci_register_driver(9)*

*4.6.0-rc5*

register a new pci driver


Synopsis
========

.. c:function:: int __pci_register_driver( struct pci_driver * drv, struct module * owner, const char * mod_name )

Arguments
=========

``drv``
    the driver structure to register

``owner``
    owner module of drv

``mod_name``
    module name string


Description
===========

Adds the driver structure to the list of registered drivers. Returns a
negative value on error, otherwise 0. If no error occurred, the driver
remains registered even if no device was claimed during registration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
