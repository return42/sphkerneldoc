.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-dev-init:

==============
wimax_dev_init
==============

*man wimax_dev_init(9)*

*4.6.0-rc5*

initialize a newly allocated instance


Synopsis
========

.. c:function:: void wimax_dev_init( struct wimax_dev * wimax_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor to initialize.


Description
===========

Initializes fields of a freshly allocated ``wimax_dev`` instance. This
function assumes that after allocation, the memory occupied by
``wimax_dev`` was zeroed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
