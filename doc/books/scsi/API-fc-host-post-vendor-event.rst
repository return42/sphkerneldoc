
.. _API-fc-host-post-vendor-event:

=========================
fc_host_post_vendor_event
=========================

*man fc_host_post_vendor_event(9)*

*4.6.0-rc1*

called to post a vendor unique event on an fc_host


Synopsis
========

.. c:function:: void fc_host_post_vendor_event( struct Scsi_Host * shost, u32 event_number, u32 data_len, char * data_buf, u64 vendor_id )

Arguments
=========

``shost``
    host the event occurred on

``event_number``
    fc event number obtained from ``get_fc_event_number``

``data_len``
    amount, in bytes, of vendor unique data

``data_buf``
    pointer to vendor unique data

``vendor_id``
    Vendor id


Notes
=====

This routine assumes no locks are held on entry.
