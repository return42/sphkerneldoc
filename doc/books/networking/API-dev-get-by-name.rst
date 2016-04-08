
.. _API-dev-get-by-name:

===============
dev_get_by_name
===============

*man dev_get_by_name(9)*

*4.6.0-rc1*

find a device by its name


Synopsis
========

.. c:function:: struct net_device ⋆ dev_get_by_name( struct net * net, const char * name )

Arguments
=========

``net``
    the applicable net namespace

``name``
    name to find


Description
===========

Find an interface by name. This can be called from any context and does its own locking. The returned handle has the usage count incremented and the caller must use ``dev_put`` to
release it when it is no longer needed. ``NULL`` is returned if no matching device is found.
