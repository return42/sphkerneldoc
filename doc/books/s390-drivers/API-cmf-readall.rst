
.. _API-cmf-readall:

===========
cmf_readall
===========

*man cmf_readall(9)*

*4.6.0-rc1*

read the current channel measurement block


Synopsis
========

.. c:function:: int cmf_readall( struct ccw_device * cdev, struct cmbdata * data )

Arguments
=========

``cdev``
    the channel to be read

``data``
    a pointer to a data block that will be filled


Description
===========

Returns ``0`` on success, a negative error value otherwise.


Context
=======

any
