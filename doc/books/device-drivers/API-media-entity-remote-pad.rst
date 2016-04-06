
.. _API-media-entity-remote-pad:

=======================
media_entity_remote_pad
=======================

*man media_entity_remote_pad(9)*

*4.6.0-rc1*

Find the pad at the remote end of a link


Synopsis
========

.. c:function:: struct media_pad ⋆ media_entity_remote_pad( struct media_pad * pad )

Arguments
=========

``pad``
    Pad at the local end of the link


Description
===========

Search for a remote pad connected to the given pad by iterating over all links originating or terminating at that pad until an enabled link is found.

Return a pointer to the pad at the remote end of the first found enabled link, or NULL if no enabled link has been found.
