.. -*- coding: utf-8; mode: rst -*-

.. _API-sparse-keymap-report-entry:

==========================
sparse_keymap_report_entry
==========================

*man sparse_keymap_report_entry(9)*

*4.6.0-rc5*

report event corresponding to given key entry


Synopsis
========

.. c:function:: void sparse_keymap_report_entry( struct input_dev * dev, const struct key_entry * ke, unsigned int value, bool autorelease )

Arguments
=========

``dev``
    Input device for which event should be reported

``ke``
    key entry describing event

``value``
    Value that should be reported (ignored by ``KE_SW`` entries)

``autorelease``
    Signals whether release event should be emitted for ``KE_KEY``
    entries right after reporting press event, ignored by all other
    entries


Description
===========

This function is used to report input event described by given
``struct key_entry``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
