
.. _API-rio-init-mbox-res:

=================
rio_init_mbox_res
=================

*man rio_init_mbox_res(9)*

*4.6.0-rc1*

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

This function is used to initialize the fields of a resource for use as a mailbox resource. It initializes a range of mailboxes using the start and end arguments.
