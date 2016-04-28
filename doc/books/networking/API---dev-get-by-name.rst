.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-get-by-name:

=================
__dev_get_by_name
=================

*man __dev_get_by_name(9)*

*4.6.0-rc5*

find a device by its name


Synopsis
========

.. c:function:: struct net_device * __dev_get_by_name( struct net * net, const char * name )

Arguments
=========

``net``
    the applicable net namespace

``name``
    name to find


Description
===========

Find an interface by name. Must be called under RTNL semaphore or
``dev_base_lock``. If the name is found a pointer to the device is
returned. If the name is not found then ``NULL`` is returned. The
reference counters are not incremented so the caller must be careful
with locks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
