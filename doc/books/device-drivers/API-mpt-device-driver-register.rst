.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-device-driver-register:

==========================
mpt_device_driver_register
==========================

*man mpt_device_driver_register(9)*

*4.6.0-rc5*

Register device driver hooks


Synopsis
========

.. c:function:: int mpt_device_driver_register( struct mpt_pci_driver * dd_cbfunc, u8 cb_idx )

Arguments
=========

``dd_cbfunc``
    driver callbacks struct

``cb_idx``
    MPT protocol driver index


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
