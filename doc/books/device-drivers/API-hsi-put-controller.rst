
.. _API-hsi-put-controller:

==================
hsi_put_controller
==================

*man hsi_put_controller(9)*

*4.6.0-rc1*

Free an HSI controller


Synopsis
========

.. c:function:: void hsi_put_controller( struct hsi_controller * hsi )

Arguments
=========

``hsi``
    Pointer to the HSI controller to freed


Description
===========

HSI controller drivers should only use this function if they need to free their allocated hsi_controller structures before a successful call to hsi_register_controller. Other
use is not allowed.
