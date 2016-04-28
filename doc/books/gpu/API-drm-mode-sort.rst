.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-sort:

=============
drm_mode_sort
=============

*man drm_mode_sort(9)*

*4.6.0-rc5*

sort mode list


Synopsis
========

.. c:function:: void drm_mode_sort( struct list_head * mode_list )

Arguments
=========

``mode_list``
    list of drm_display_mode structures to sort


Description
===========

Sort ``mode_list`` by favorability, moving good modes to the head of the
list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
