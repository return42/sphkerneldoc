
.. _API-media-devnode-register:

======================
media_devnode_register
======================

*man media_devnode_register(9)*

*4.6.0-rc1*

register a media device node


Synopsis
========

.. c:function:: int media_devnode_register( struct media_devnode * mdev, struct module * owner )

Arguments
=========

``mdev``
    media device node structure we want to register

``owner``
    should be filled with ``THIS_MODULE``


Description
===========

The registration code assigns minor numbers and registers the new device node with the kernel. An error is returned if no free minor number can be found, or if the registration of
the device node fails.

Zero is returned on success.

Note that if the media_devnode_register call fails, the ``release`` callback of the media_devnode structure is ⋆not⋆ called, so the caller is responsible for freeing any data.
