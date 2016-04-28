.. -*- coding: utf-8; mode: rst -*-

.. _API-edd-release:

===========
edd_release
===========

*man edd_release(9)*

*4.6.0-rc5*

free edd structure


Synopsis
========

.. c:function:: void edd_release( struct kobject * kobj )

Arguments
=========

``kobj``
    kobject of edd structure


Description
===========

This is called when the refcount of the edd structure reaches 0. This
should happen right after we unregister, but just in case, we use the
release callback anyway.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
