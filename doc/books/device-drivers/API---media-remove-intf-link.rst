
.. _API---media-remove-intf-link:

========================
__media_remove_intf_link
========================

*man __media_remove_intf_link(9)*

*4.6.0-rc1*

remove a single interface link


Synopsis
========

.. c:function:: void __media_remove_intf_link( struct media_link * link )

Arguments
=========

``link``
    pointer to ``media_link``.


Note
====

this is an unlocked version of ``media_remove_intf_link``
