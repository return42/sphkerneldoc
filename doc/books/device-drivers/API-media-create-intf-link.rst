
.. _API-media-create-intf-link:

======================
media_create_intf_link
======================

*man media_create_intf_link(9)*

*4.6.0-rc1*

creates a link between an entity and an interface


Synopsis
========

.. c:function:: media_create_intf_link( struct media_entity * entity, struct media_interface * intf, u32 flags )

Arguments
=========

``entity``
    pointer to ``media_entity``

``intf``
    pointer to ``media_interface``

``flags``
    Link flags, as defined in include/uapi/linux/media.h.


Valid values for flags
======================

The ``MEDIA_LNK_FL_ENABLED`` flag indicates that the interface is connected to the entity hardware. That's the default value for interfaces. An interface may be disabled if the
hardware is busy due to the usage of some other interface that it is currently controlling the hardware. A typical example is an hybrid TV device that handle only one type of
stream on a given time. So, when the digital TV is streaming, the V4L2 interfaces won't be enabled, as such device is not able to also stream analog TV or radio.


Note
====

Before calling this function, ``media_devnode_create`` should be called for the interface and ``media_device_register_entity`` should be called for the interface that will be part
of the link.
