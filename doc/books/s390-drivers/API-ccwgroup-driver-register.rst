.. -*- coding: utf-8; mode: rst -*-

.. _API-ccwgroup-driver-register:

========================
ccwgroup_driver_register
========================

*man ccwgroup_driver_register(9)*

*4.6.0-rc5*

register a ccw group driver


Synopsis
========

.. c:function:: int ccwgroup_driver_register( struct ccwgroup_driver * cdriver )

Arguments
=========

``cdriver``
    driver to be registered


Description
===========

This function is mainly a wrapper around ``driver_register``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
