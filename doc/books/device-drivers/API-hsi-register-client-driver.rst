
.. _API-hsi-register-client-driver:

==========================
hsi_register_client_driver
==========================

*man hsi_register_client_driver(9)*

*4.6.0-rc1*

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
