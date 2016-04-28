.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-unmap-user:

==============
bio_unmap_user
==============

*man bio_unmap_user(9)*

*4.6.0-rc5*

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

Unmap a bio previously mapped by ``bio_map_user``. Must be called with a
process context.

``bio_unmap_user`` may sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
