
.. _API-sk-ns-capable:

=============
sk_ns_capable
=============

*man sk_ns_capable(9)*

*4.6.0-rc1*

General socket capability test


Synopsis
========

.. c:function:: bool sk_ns_capable( const struct sock * sk, struct user_namespace * user_ns, int cap )

Arguments
=========

``sk``
    Socket to use a capability on or through

``user_ns``
    The user namespace of the capability to use

``cap``
    The capability to use


Description
===========

Test to see if the opener of the socket had when the socket was created and the current process has the capability ``cap`` in the user namespace ``user_ns``.
