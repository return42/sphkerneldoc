
.. _API-sparse-keymap-entry-from-scancode:

=================================
sparse_keymap_entry_from_scancode
=================================

*man sparse_keymap_entry_from_scancode(9)*

*4.6.0-rc1*

perform sparse keymap lookup


Synopsis
========

.. c:function:: struct key_entry ⋆ sparse_keymap_entry_from_scancode( struct input_dev * dev, unsigned int code )

Arguments
=========

``dev``
    Input device using sparse keymap

``code``
    Scan code


Description
===========

This function is used to perform ``struct key_entry`` lookup in an input device using sparse keymap.
