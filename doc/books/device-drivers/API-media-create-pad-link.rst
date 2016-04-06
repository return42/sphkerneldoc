
.. _API-media-create-pad-link:

=====================
media_create_pad_link
=====================

*man media_create_pad_link(9)*

*4.6.0-rc1*

creates a link between two entities.


Synopsis
========

.. c:function:: int media_create_pad_link( struct media_entity * source, u16 source_pad, struct media_entity * sink, u16 sink_pad, u32 flags )

Arguments
=========

``source``
    pointer to ``media_entity`` of the source pad.

``source_pad``
    number of the source pad in the pads array

``sink``
    pointer to ``media_entity`` of the sink pad.

``sink_pad``
    number of the sink pad in the pads array.

``flags``
    Link flags, as defined in include/uapi/linux/media.h.


Valid values for flags
======================

A ``MEDIA_LNK_FL_ENABLED`` flag indicates that the link is enabled and can be used to transfer media data. When two or more links target a sink pad, only one of them can be enabled
at a time.

A ``MEDIA_LNK_FL_IMMUTABLE`` flag indicates that the link enabled state can't be modified at runtime. If ``MEDIA_LNK_FL_IMMUTABLE`` is set, then ``MEDIA_LNK_FL_ENABLED`` must also
be set since an immutable link is always enabled.


NOTE
====

Before calling this function, ``media_entity_pads_init`` and ``media_device_register_entity`` should be called previously for both ends.
