
.. _API-edd-release:

===========
edd_release
===========

*man edd_release(9)*

*4.6.0-rc1*

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

This is called when the refcount of the edd structure reaches 0. This should happen right after we unregister, but just in case, we use the release callback anyway.
