
.. _API-sparse-keymap-report-event:

==========================
sparse_keymap_report_event
==========================

*man sparse_keymap_report_event(9)*

*4.6.0-rc1*

report event corresponding to given scancode


Synopsis
========

.. c:function:: bool sparse_keymap_report_event( struct input_dev * dev, unsigned int code, unsigned int value, bool autorelease )

Arguments
=========

``dev``
    Input device using sparse keymap

``code``
    Scan code

``value``
    Value that should be reported (ignored by ``KE_SW`` entries)

``autorelease``
    Signals whether release event should be emitted for ``KE_KEY`` entries right after reporting press event, ignored by all other entries


Description
===========

This function is used to perform lookup in an input device using sparse keymap and report corresponding event. Returns ``true`` if lookup was successful and ``false`` otherwise.
