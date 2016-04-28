.. -*- coding: utf-8; mode: rst -*-

.. _API-edd-get-pci-dev:

===============
edd_get_pci_dev
===============

*man edd_get_pci_dev(9)*

*4.6.0-rc5*

finds pci_dev that matches edev


Synopsis
========

.. c:function:: struct pci_dev * edd_get_pci_dev( struct edd_device * edev )

Arguments
=========

``edev``
    edd_device


Description
===========

Returns pci_dev if found, or NULL


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
