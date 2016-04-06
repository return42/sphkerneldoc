
.. _API-input-scancode-to-scalar:

========================
input_scancode_to_scalar
========================

*man input_scancode_to_scalar(9)*

*4.6.0-rc1*

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

This function is used to convert scancode stored in ``struct keymap_entry`` into scalar form understood by legacy keymap handling methods. These methods expect scancodes to be
represented as 'unsigned int'.
