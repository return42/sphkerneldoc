
.. _API-rio-release-inb-mbox:

====================
rio_release_inb_mbox
====================

*man rio_release_inb_mbox(9)*

*4.6.0-rc1*

release inbound mailbox message service


Synopsis
========

.. c:function:: int rio_release_inb_mbox( struct rio_mport * mport, int mbox )

Arguments
=========

``mport``
    RIO master port from which to release the mailbox resource

``mbox``
    Mailbox number to release


Description
===========

Releases ownership of an inbound mailbox resource. Returns 0 if the request has been satisfied.
