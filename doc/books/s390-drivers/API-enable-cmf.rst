
.. _API-enable-cmf:

==========
enable_cmf
==========

*man enable_cmf(9)*

*4.6.0-rc1*

switch on the channel measurement for a specific device


Synopsis
========

.. c:function:: int enable_cmf( struct ccw_device * cdev )

Arguments
=========

``cdev``
    The ccw device to be enabled


Description
===========

Returns ``0`` for success or a negative error value.


Context
=======

non-atomic
