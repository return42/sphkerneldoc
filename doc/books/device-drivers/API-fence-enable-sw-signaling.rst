.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-enable-sw-signaling:

=========================
fence_enable_sw_signaling
=========================

*man fence_enable_sw_signaling(9)*

*4.6.0-rc5*

enable signaling on fence


Synopsis
========

.. c:function:: void fence_enable_sw_signaling( struct fence * fence )

Arguments
=========

``fence``
    [in] the fence to enable


Description
===========

this will request for sw signaling to be enabled, to make the fence
complete as soon as possible


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
