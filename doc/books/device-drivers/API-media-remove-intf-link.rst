
.. _API-media-remove-intf-link:

======================
media_remove_intf_link
======================

*man media_remove_intf_link(9)*

*4.6.0-rc1*

remove a single interface link


Synopsis
========

.. c:function:: void media_remove_intf_link( struct media_link * link )

Arguments
=========

``link``
    pointer to ``media_link``.


Note
====

prefer to use this one, instead of ``__media_remove_intf_link``
