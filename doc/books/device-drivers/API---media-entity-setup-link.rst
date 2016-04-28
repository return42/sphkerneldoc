.. -*- coding: utf-8; mode: rst -*-

.. _API---media-entity-setup-link:

=========================
__media_entity_setup_link
=========================

*man __media_entity_setup_link(9)*

*4.6.0-rc5*

Configure a media link without locking


Synopsis
========

.. c:function:: int __media_entity_setup_link( struct media_link * link, u32 flags )

Arguments
=========

``link``
    The link being configured

``flags``
    Link configuration flags


Description
===========

The bulk of link setup is handled by the two entities connected through
the link. This function notifies both entities of the link configuration
change.

If the link is immutable or if the current and new configuration are
identical, return immediately.

The user is expected to hold link->source->parent->mutex. If not,
``media_entity_setup_link`` should be used instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
