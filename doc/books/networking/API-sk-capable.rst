
.. _API-sk-capable:

==========
sk_capable
==========

*man sk_capable(9)*

*4.6.0-rc1*

Socket global capability test


Synopsis
========

.. c:function:: bool sk_capable( const struct sock * sk, int cap )

Arguments
=========

``sk``
    Socket to use a capability on or through

``cap``
    The global capability to use


Description
===========

Test to see if the opener of the socket had when the socket was created and the current process has the capability ``cap`` in all user namespaces.
