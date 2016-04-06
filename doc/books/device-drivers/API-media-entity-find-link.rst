
.. _API-media-entity-find-link:

======================
media_entity_find_link
======================

*man media_entity_find_link(9)*

*4.6.0-rc1*

Find a link between two pads


Synopsis
========

.. c:function:: struct media_link ⋆ media_entity_find_link( struct media_pad * source, struct media_pad * sink )

Arguments
=========

``source``
    Source pad

``sink``
    Sink pad


Description
===========

Return a pointer to the link between the two entities. If no such link exists, return NULL.
