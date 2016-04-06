
.. _API---audit-getname:

===============
__audit_getname
===============

*man __audit_getname(9)*

*4.6.0-rc1*

add a name to the list


Synopsis
========

.. c:function:: void __audit_getname( struct filename * name )

Arguments
=========

``name``
    name to add


Description
===========

Add a name to the list of audit names for this context. Called from fs/namei.c:\ ``getname``.
