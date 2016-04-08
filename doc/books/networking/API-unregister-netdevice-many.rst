
.. _API-unregister-netdevice-many:

=========================
unregister_netdevice_many
=========================

*man unregister_netdevice_many(9)*

*4.6.0-rc1*

unregister many devices


Synopsis
========

.. c:function:: void unregister_netdevice_many( struct list_head * head )

Arguments
=========

``head``
    list of devices


Note
====

As most callers use a stack allocated list_head, we force a ``list_del`` to make sure stack wont be corrupted later.
