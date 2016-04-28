.. -*- coding: utf-8; mode: rst -*-

.. _API-sparse-keymap-free:

==================
sparse_keymap_free
==================

*man sparse_keymap_free(9)*

*4.6.0-rc5*

free memory allocated for sparse keymap


Synopsis
========

.. c:function:: void sparse_keymap_free( struct input_dev * dev )

Arguments
=========

``dev``
    Input device using sparse keymap


Description
===========

This function is used to free memory allocated by sparse keymap in an
input device that was set up by ``sparse_keymap_setup``.


NOTE
====

It is safe to cal this function while input device is still registered
(however the drivers should care not to try to use freed keymap and thus
have to shut off interrupts/polling before freeing the keymap).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
