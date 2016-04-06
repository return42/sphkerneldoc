
.. _API-devm-remove-action:

==================
devm_remove_action
==================

*man devm_remove_action(9)*

*4.6.0-rc1*

removes previously added custom action


Synopsis
========

.. c:function:: void devm_remove_action( struct device * dev, void (*action) void *, void * data )

Arguments
=========

``dev``
    Device that owns the action

``action``
    Function implementing the action

``data``
    Pointer to data passed to ``action`` implementation


Description
===========

Removes instance of ``action`` previously added by ``devm_add_action``. Both action and data should match one of the existing entries.
