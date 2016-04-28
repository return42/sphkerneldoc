.. -*- coding: utf-8; mode: rst -*-

.. _API-priv-to-wiphy:

=============
priv_to_wiphy
=============

*man priv_to_wiphy(9)*

*4.6.0-rc5*

return the wiphy containing the priv


Synopsis
========

.. c:function:: struct wiphy * priv_to_wiphy( void * priv )

Arguments
=========

``priv``
    a pointer previously returned by wiphy_priv


Return
======

The wiphy of ``priv``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
