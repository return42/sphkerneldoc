.. -*- coding: utf-8; mode: rst -*-

.. _API---bio-clone-fast:

================
__bio_clone_fast
================

*man __bio_clone_fast(9)*

*4.6.0-rc5*

clone a bio that shares the original bio's biovec


Synopsis
========

.. c:function:: void __bio_clone_fast( struct bio * bio, struct bio * bio_src )

Arguments
=========

``bio``
    destination bio

``bio_src``
    bio to clone


Description
===========

Clone a ``bio``. Caller will own the returned bio, but not the actual
data it points to. Reference count of returned bio will be one.

Caller must ensure that ``bio_src`` is not freed before ``bio``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
