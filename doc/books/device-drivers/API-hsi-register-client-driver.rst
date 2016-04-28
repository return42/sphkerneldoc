.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-register-client-driver:

==========================
hsi_register_client_driver
==========================

*man hsi_register_client_driver(9)*

*4.6.0-rc5*

Register an HSI client to the HSI bus


Synopsis
========

.. c:function:: int hsi_register_client_driver( struct hsi_client_driver * drv )

Arguments
=========

``drv``
    HSI client driver to register


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
