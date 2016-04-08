
.. _API-ccwgroup-driver-register:

========================
ccwgroup_driver_register
========================

*man ccwgroup_driver_register(9)*

*4.6.0-rc1*

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
