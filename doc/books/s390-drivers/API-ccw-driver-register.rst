
.. _API-ccw-driver-register:

===================
ccw_driver_register
===================

*man ccw_driver_register(9)*

*4.6.0-rc1*

register a ccw driver


Synopsis
========

.. c:function:: int ccw_driver_register( struct ccw_driver * cdriver )

Arguments
=========

``cdriver``
    driver to be registered


Description
===========

This function is mainly a wrapper around ``driver_register``.


Returns
=======

``0`` on success and a negative error value on failure.
