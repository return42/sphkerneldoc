.. -*- coding: utf-8; mode: rst -*-

.. _API-input-scancode-to-scalar:

========================
input_scancode_to_scalar
========================

*man input_scancode_to_scalar(9)*

*4.6.0-rc5*

converts scancode in ``struct input_keymap_entry``


Synopsis
========

.. c:function:: int input_scancode_to_scalar( const struct input_keymap_entry * ke, unsigned int * scancode )

Arguments
=========

``ke``
    keymap entry containing scancode to be converted.

``scancode``
    pointer to the location where converted scancode should be stored.


Description
===========

This function is used to convert scancode stored in
``struct keymap_entry`` into scalar form understood by legacy keymap
handling methods. These methods expect scancodes to be represented as
'unsigned int'.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
