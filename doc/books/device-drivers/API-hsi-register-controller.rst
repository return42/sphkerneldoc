
.. _API-hsi-register-controller:

=======================
hsi_register_controller
=======================

*man hsi_register_controller(9)*

*4.6.0-rc1*

Register an HSI controller and its ports


Synopsis
========

.. c:function:: int hsi_register_controller( struct hsi_controller * hsi )

Arguments
=========

``hsi``
    The HSI controller to register


Description
===========

Returns -errno on failure, 0 on success.
