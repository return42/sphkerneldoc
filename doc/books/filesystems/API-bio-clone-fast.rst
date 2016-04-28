.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-clone-fast:

==============
bio_clone_fast
==============

*man bio_clone_fast(9)*

*4.6.0-rc5*

clone a bio that shares the original bio's biovec


Synopsis
========

.. c:function:: struct bio * bio_clone_fast( struct bio * bio, gfp_t gfp_mask, struct bio_set * bs )

Arguments
=========

``bio``
    bio to clone

``gfp_mask``
    allocation priority

``bs``
    bio_set to allocate from


Description
===========

Like __bio_clone_fast, only also allocates the returned bio


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
