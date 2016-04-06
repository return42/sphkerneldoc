
.. _API-input-set-keycode:

=================
input_set_keycode
=================

*man input_set_keycode(9)*

*4.6.0-rc1*

attribute a keycode to a given scancode


Synopsis
========

.. c:function:: int input_set_keycode( struct input_dev * dev, const struct input_keymap_entry * ke )

Arguments
=========

``dev``
    input device which keymap is being updated

``ke``
    new keymap entry


Description
===========

This function should be called by anyone needing to update current keymap. Presently keyboard and evdev handlers use it.
