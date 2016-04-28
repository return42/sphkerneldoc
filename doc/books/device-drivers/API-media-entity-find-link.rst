.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-find-link:

======================
media_entity_find_link
======================

*man media_entity_find_link(9)*

*4.6.0-rc5*

Find a link between two pads


Synopsis
========

.. c:function:: struct media_link * media_entity_find_link( struct media_pad * source, struct media_pad * sink )

Arguments
=========

``source``
    Source pad

``sink``
    Sink pad


Description
===========

Return a pointer to the link between the two entities. If no such link
exists, return NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
