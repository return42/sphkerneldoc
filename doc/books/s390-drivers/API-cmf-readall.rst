.. -*- coding: utf-8; mode: rst -*-

.. _API-cmf-readall:

===========
cmf_readall
===========

*man cmf_readall(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
