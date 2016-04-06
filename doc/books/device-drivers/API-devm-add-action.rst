
.. _API-devm-add-action:

===============
devm_add_action
===============

*man devm_add_action(9)*

*4.6.0-rc1*

add a custom action to list of managed resources


Synopsis
========

.. c:function:: int devm_add_action( struct device * dev, void (*action) void *, void * data )

Arguments
=========

``dev``
    Device that owns the action

``action``
    Function that should be called

``data``
    Pointer to data passed to ``action`` implementation


Description
===========

This adds a custom action to the list of managed resources so that it gets executed as part of standard resource unwinding.
