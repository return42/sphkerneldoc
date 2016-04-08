
.. _API-ccw-driver-unregister:

=====================
ccw_driver_unregister
=====================

*man ccw_driver_unregister(9)*

*4.6.0-rc1*

deregister a ccw driver


Synopsis
========

.. c:function:: void ccw_driver_unregister( struct ccw_driver * cdriver )

Arguments
=========

``cdriver``
    driver to be deregistered


Description
===========

This function is mainly a wrapper around ``driver_unregister``.
