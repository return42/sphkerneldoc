
.. _API-bio-unmap-user:

==============
bio_unmap_user
==============

*man bio_unmap_user(9)*

*4.6.0-rc1*

unmap a bio


Synopsis
========

.. c:function:: void bio_unmap_user( struct bio * bio )

Arguments
=========

``bio``
    the bio being unmapped


Description
===========

Unmap a bio previously mapped by ``bio_map_user``. Must be called with a process context.

``bio_unmap_user`` may sleep.
