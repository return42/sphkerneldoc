.. -*- coding: utf-8; mode: rst -*-

.. _API-superhyway-unregister-driver:

============================
superhyway_unregister_driver
============================

*man superhyway_unregister_driver(9)*

*4.6.0-rc5*

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

This cleans up after ``superhyway_register_driver``, and should be
invoked in the exit path of any module drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
