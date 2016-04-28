.. -*- coding: utf-8; mode: rst -*-

.. _API-sparse-keymap-setup:

===================
sparse_keymap_setup
===================

*man sparse_keymap_setup(9)*

*4.6.0-rc5*

set up sparse keymap for an input device


Synopsis
========

.. c:function:: int sparse_keymap_setup( struct input_dev * dev, const struct key_entry * keymap, int (*setup) struct input_dev *, struct key_entry * )

Arguments
=========

``dev``
    Input device

``keymap``
    Keymap in form of array of ``key_entry`` structures ending with
    ``KE_END`` type entry

``setup``
    Function that can be used to adjust keymap entries depending on
    device's deeds, may be ``NULL``


Description
===========

The function calculates size and allocates copy of the original keymap
after which sets up input device event bits appropriately. Before
destroying input device allocated keymap should be freed with a call to
``sparse_keymap_free``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
