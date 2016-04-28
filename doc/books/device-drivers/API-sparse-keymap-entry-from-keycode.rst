.. -*- coding: utf-8; mode: rst -*-

.. _API-sparse-keymap-entry-from-keycode:

================================
sparse_keymap_entry_from_keycode
================================

*man sparse_keymap_entry_from_keycode(9)*

*4.6.0-rc5*

perform sparse keymap lookup


Synopsis
========

.. c:function:: struct key_entry * sparse_keymap_entry_from_keycode( struct input_dev * dev, unsigned int keycode )

Arguments
=========

``dev``
    Input device using sparse keymap

``keycode``
    Key code


Description
===========

This function is used to perform ``struct key_entry`` lookup in an input
device using sparse keymap.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
