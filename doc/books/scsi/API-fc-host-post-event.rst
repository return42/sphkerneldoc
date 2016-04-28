.. -*- coding: utf-8; mode: rst -*-

.. _API-fc-host-post-event:

==================
fc_host_post_event
==================

*man fc_host_post_event(9)*

*4.6.0-rc5*

called to post an even on an fc_host.


Synopsis
========

.. c:function:: void fc_host_post_event( struct Scsi_Host * shost, u32 event_number, enum fc_host_event_code event_code, u32 event_data )

Arguments
=========

``shost``
    host the event occurred on

``event_number``
    fc event number obtained from ``get_fc_event_number``

``event_code``
    fc_host event being posted

``event_data``
    32bits of data for the event being posted


Notes
=====

This routine assumes no locks are held on entry.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
