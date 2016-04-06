
.. _API---media-remove-intf-links:

=========================
__media_remove_intf_links
=========================

*man __media_remove_intf_links(9)*

*4.6.0-rc1*

remove all links associated with an interface


Synopsis
========

.. c:function:: void __media_remove_intf_links( struct media_interface * intf )

Arguments
=========

``intf``
    pointer to ``media_interface``


Note
====

this is an unlocked version of ``media_remove_intf_links``.
