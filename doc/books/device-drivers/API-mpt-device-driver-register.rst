
.. _API-mpt-device-driver-register:

==========================
mpt_device_driver_register
==========================

*man mpt_device_driver_register(9)*

*4.6.0-rc1*

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
