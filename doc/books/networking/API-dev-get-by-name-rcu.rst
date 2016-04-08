
.. _API-dev-get-by-name-rcu:

===================
dev_get_by_name_rcu
===================

*man dev_get_by_name_rcu(9)*

*4.6.0-rc1*

find a device by its name


Synopsis
========

.. c:function:: struct net_device ⋆ dev_get_by_name_rcu( struct net * net, const char * name )

Arguments
=========

``net``
    the applicable net namespace

``name``
    name to find


Description
===========

Find an interface by name. If the name is found a pointer to the device is returned. If the name is not found then ``NULL`` is returned. The reference counters are not incremented
so the caller must be careful with locks. The caller must hold RCU lock.
