
.. _API-media-create-pad-links:

======================
media_create_pad_links
======================

*man media_create_pad_links(9)*

*4.6.0-rc1*

creates a link between two entities.


Synopsis
========

.. c:function:: int media_create_pad_links( const struct media_device * mdev, const u32 source_function, struct media_entity * source, const u16 source_pad, const u32 sink_function, struct media_entity * sink, const u16 sink_pad, u32 flags, const bool allow_both_undefined )

Arguments
=========

``mdev``
    Pointer to the media_device that contains the object

``source_function``
    Function of the source entities. Used only if ``source`` is NULL.

``source``
    pointer to ``media_entity`` of the source pad. If NULL, it will use all entities that matches the ``sink_function``.

``source_pad``
    number of the source pad in the pads array

``sink_function``
    Function of the sink entities. Used only if ``sink`` is NULL.

``sink``
    pointer to ``media_entity`` of the sink pad. If NULL, it will use all entities that matches the ``sink_function``.

``sink_pad``
    number of the sink pad in the pads array.

``flags``
    Link flags, as defined in include/uapi/linux/media.h.

``allow_both_undefined``
    if true, then both ``source`` and ``sink`` can be NULL. In such case, it will create a crossbar between all entities that matches ``source_function`` to all entities that
    matches ``sink_function``. If false, it will return 0 and won't create any link if both ``source`` and ``sink`` are NULL.


Valid values for flags
======================

A ``MEDIA_LNK_FL_ENABLED`` flag indicates that the link is enabled and can be used to transfer media data. If multiple links are created and this flag is passed as an argument,
only the first created link will have this flag.

A ``MEDIA_LNK_FL_IMMUTABLE`` flag indicates that the link enabled state can't be modified at runtime. If ``MEDIA_LNK_FL_IMMUTABLE`` is set, then ``MEDIA_LNK_FL_ENABLED`` must also
be set since an immutable link is always enabled.

It is common for some devices to have multiple source and/or sink entities of the same type that should be linked. While ``media_create_pad_link`` creates link by link, this
function is meant to allow 1:n, n:1 and even cross-bar (n:n) links.


NOTE
====

Before calling this function, ``media_entity_pads_init`` and ``media_device_register_entity`` should be called previously for the entities to be linked.
