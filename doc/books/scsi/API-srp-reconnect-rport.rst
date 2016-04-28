.. -*- coding: utf-8; mode: rst -*-

.. _API-srp-reconnect-rport:

===================
srp_reconnect_rport
===================

*man srp_reconnect_rport(9)*

*4.6.0-rc5*

reconnect to an SRP target port


Synopsis
========

.. c:function:: int srp_reconnect_rport( struct srp_rport * rport )

Arguments
=========

``rport``
    SRP target port.


Description
===========

Blocks SCSI command queueing before invoking ``reconnect`` such that
``queuecommand`` won't be invoked concurrently with ``reconnect`` from
outside the SCSI EH. This is important since a ``reconnect``
implementation may reallocate resources needed by ``queuecommand``.


Notes
=====

- This function neither waits until outstanding requests have finished
nor tries to abort these. It is the responsibility of the ``reconnect``
function to finish outstanding commands before reconnecting to the
target port. - It is the responsibility of the caller to ensure that the
resources reallocated by the ``reconnect`` function won't be used while
this function is in progress. One possible strategy is to invoke this
function from the context of the SCSI EH thread only. Another possible
strategy is to lock the rport mutex inside each SCSI LLD callback that
can be invoked by the SCSI EH (the scsi_host_template.eh_*()
functions and also the scsi_host_template. ``queuecommand``
function).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
