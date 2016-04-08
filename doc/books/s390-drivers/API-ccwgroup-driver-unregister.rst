
.. _API-ccwgroup-driver-unregister:

==========================
ccwgroup_driver_unregister
==========================

*man ccwgroup_driver_unregister(9)*

*4.6.0-rc1*

deregister a ccw group driver


Synopsis
========

.. c:function:: void ccwgroup_driver_unregister( struct ccwgroup_driver * cdriver )

Arguments
=========

``cdriver``
    driver to be deregistered


Description
===========

This function is mainly a wrapper around ``driver_unregister``.
