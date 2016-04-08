
.. _API-superhyway-unregister-driver:

============================
superhyway_unregister_driver
============================

*man superhyway_unregister_driver(9)*

*4.6.0-rc1*

Unregister a SuperHyway driver


Synopsis
========

.. c:function:: void superhyway_unregister_driver( struct superhyway_driver * drv )

Arguments
=========

``drv``
    SuperHyway driver to unregister.


Description
===========

This cleans up after ``superhyway_register_driver``, and should be invoked in the exit path of any module drivers.
