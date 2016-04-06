
.. _API-input-get-keycode:

=================
input_get_keycode
=================

*man input_get_keycode(9)*

*4.6.0-rc1*

retrieve keycode currently mapped to a given scancode


Synopsis
========

.. c:function:: int input_get_keycode( struct input_dev * dev, struct input_keymap_entry * ke )

Arguments
=========

``dev``
    input device which keymap is being queried

``ke``
    keymap entry


Description
===========

This function should be called by anyone interested in retrieving current keymap. Presently evdev handlers use it.
