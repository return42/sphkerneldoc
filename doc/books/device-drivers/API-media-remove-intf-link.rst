.. -*- coding: utf-8; mode: rst -*-

.. _API-media-remove-intf-link:

======================
media_remove_intf_link
======================

*man media_remove_intf_link(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
