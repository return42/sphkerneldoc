.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-get-inb-message:

===================
rio_get_inb_message
===================

*man rio_get_inb_message(9)*

*4.6.0-rc5*

Get A RIO message from an inbound mailbox queue


Synopsis
========

.. c:function:: void * rio_get_inb_message( struct rio_mport * mport, int mbox )

Arguments
=========

``mport``
    Master port containing the inbound mailbox

``mbox``
    The inbound mailbox number


Description
===========

Get a RIO message from an inbound mailbox queue. Returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
