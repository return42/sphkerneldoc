
.. _API-fc-host-post-event:

==================
fc_host_post_event
==================

*man fc_host_post_event(9)*

*4.6.0-rc1*

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
