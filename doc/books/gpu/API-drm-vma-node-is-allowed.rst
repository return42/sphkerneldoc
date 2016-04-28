.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-node-is-allowed:

=======================
drm_vma_node_is_allowed
=======================

*man drm_vma_node_is_allowed(9)*

*4.6.0-rc5*

Check whether an open-file is granted access


Synopsis
========

.. c:function:: bool drm_vma_node_is_allowed( struct drm_vma_offset_node * node, struct file * filp )

Arguments
=========

``node``
    Node to check

``filp``
    Open-file to check for


Description
===========

Search the list in ``node`` whether ``filp`` is currently on the list of
allowed open-files (see ``drm_vma_node_allow``).

This is locked against concurrent access internally.


RETURNS
=======

true iff ``filp`` is on the list


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
