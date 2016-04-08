
.. _API-ata-std-postreset:

=================
ata_std_postreset
=================

*man ata_std_postreset(9)*

*4.6.0-rc1*

standard postreset callback


Synopsis
========

.. c:function:: void ata_std_postreset( struct ata_link * link, unsigned int * classes )

Arguments
=========

``link``
    the target ata_link

``classes``
    classes of attached devices


Description
===========

This function is invoked after a successful reset. Note that the device might have been reset more than once using different reset methods before postreset is invoked.


LOCKING
=======

Kernel thread context (may sleep)
