.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-register-controller:

=======================
hsi_register_controller
=======================

*man hsi_register_controller(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
