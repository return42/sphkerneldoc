
.. _API-w1-post-write:

=============
w1_post_write
=============

*man w1_post_write(9)*

*4.6.0-rc1*

post-write options


Synopsis
========

.. c:function:: void w1_post_write( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Description
===========

Post-write operation, currently only supporting strong pullups. If a strong pullup was requested, clear it if the hardware supports them, or execute the delay otherwise, in either
case clear the request.
