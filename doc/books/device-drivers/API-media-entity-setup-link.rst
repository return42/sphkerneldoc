.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-setup-link:

=======================
media_entity_setup_link
=======================

*man media_entity_setup_link(9)*

*4.6.0-rc5*

changes the link flags properties in runtime


Synopsis
========

.. c:function:: int media_entity_setup_link( struct media_link * link, u32 flags )

Arguments
=========

``link``
    pointer to ``media_link``

``flags``
    the requested new link flags


Description
===========

The only configurable property is the ``MEDIA_LNK_FL_ENABLED`` link flag
flag to enable/disable a link. Links marked with the
``MEDIA_LNK_FL_IMMUTABLE`` link flag can not be enabled or disabled.

When a link is enabled or disabled, the media framework calls the
link_setup operation for the two entities at the source and sink of the
link, in that order. If the second link_setup call fails, another
link_setup call is made on the first entity to restore the original
link flags.

Media device drivers can be notified of link setup operations by setting
the


media_device
============

:link_notify pointer to a callback function. If provided, the
notification callback will be called before enabling and after disabling
links.

Entity drivers must implement the link_setup operation if any of their
links is non-immutable. The operation must either configure the hardware
or store the configuration information to be applied later.

Link configuration must not have any side effect on other links. If an
enabled link at a sink pad prevents another link at the same pad from
being enabled, the link_setup operation must return -EBUSY and can't
implicitly disable the first enabled link.


NOTE
====

the valid values of the flags for the link is the same as described on
``media_create_pad_link``, for pad to pad links or the same as described
on ``media_create_intf_link``, for interface to entity links.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
