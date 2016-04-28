.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-init-mbox-res:

=================
rio_init_mbox_res
=================

*man rio_init_mbox_res(9)*

*4.6.0-rc5*

Initialize a RIO mailbox resource


Synopsis
========

.. c:function:: void rio_init_mbox_res( struct resource * res, int start, int end )

Arguments
=========

``res``
    resource struct

``start``
    start of mailbox range

``end``
    end of mailbox range


Description
===========

This function is used to initialize the fields of a resource for use as
a mailbox resource. It initializes a range of mailboxes using the start
and end arguments.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
