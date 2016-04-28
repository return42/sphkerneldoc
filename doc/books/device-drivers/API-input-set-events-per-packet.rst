.. -*- coding: utf-8; mode: rst -*-

.. _API-input-set-events-per-packet:

===========================
input_set_events_per_packet
===========================

*man input_set_events_per_packet(9)*

*4.6.0-rc5*

tell handlers about the driver event rate


Synopsis
========

.. c:function:: void input_set_events_per_packet( struct input_dev * dev, int n_events )

Arguments
=========

``dev``
    the input device used by the driver

``n_events``
    the average number of events between calls to ``input_sync``


Description
===========

If the event rate sent from a device is unusually large, use this
function to set the expected event rate. This will allow handlers to set
up an appropriate buffer size for the event stream, in order to minimize
information loss.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
