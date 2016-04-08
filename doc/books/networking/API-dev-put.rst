
.. _API-dev-put:

=======
dev_put
=======

*man dev_put(9)*

*4.6.0-rc1*

release reference to device


Synopsis
========

.. c:function:: void dev_put( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Release reference to device to allow it to be freed.
