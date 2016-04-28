.. -*- coding: utf-8; mode: rst -*-

.. _API---media-remove-intf-links:

=========================
__media_remove_intf_links
=========================

*man __media_remove_intf_links(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
