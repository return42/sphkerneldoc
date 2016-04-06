
.. _API-edd-get-pci-dev:

===============
edd_get_pci_dev
===============

*man edd_get_pci_dev(9)*

*4.6.0-rc1*

finds pci_dev that matches edev


Synopsis
========

.. c:function:: struct pci_dev ⋆ edd_get_pci_dev( struct edd_device * edev )

Arguments
=========

``edev``
    edd_device


Description
===========

Returns pci_dev if found, or NULL
