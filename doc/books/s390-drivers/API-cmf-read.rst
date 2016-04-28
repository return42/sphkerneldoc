.. -*- coding: utf-8; mode: rst -*-

.. _API-cmf-read:

========
cmf_read
========

*man cmf_read(9)*

*4.6.0-rc5*

read one value from the current channel measurement block


Synopsis
========

.. c:function:: u64 cmf_read( struct ccw_device * cdev, int index )

Arguments
=========

``cdev``
    the channel to be read

``index``
    the index of the value to be read


Description
===========

Returns the value read or ``0`` if the value cannot be read.


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
