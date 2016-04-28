.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-put:

=======
bio_put
=======

*man bio_put(9)*

*4.6.0-rc5*

release a reference to a bio


Synopsis
========

.. c:function:: void bio_put( struct bio * bio )

Arguments
=========

``bio``
    bio to release reference to


Description
===========

Put a reference to a ``struct bio``, either one you have gotten with
bio_alloc, bio_get or bio_clone. The last put of a bio will free it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
