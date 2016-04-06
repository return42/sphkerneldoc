
.. _API-srp-tmo-valid:

=============
srp_tmo_valid
=============

*man srp_tmo_valid(9)*

*4.6.0-rc1*

check timeout combination validity


Synopsis
========

.. c:function:: int srp_tmo_valid( int reconnect_delay, int fast_io_fail_tmo, int dev_loss_tmo )

Arguments
=========

``reconnect_delay``
    Reconnect delay in seconds.

``fast_io_fail_tmo``
    Fast I/O fail timeout in seconds.

``dev_loss_tmo``
    Device loss timeout in seconds.


Description
===========

The combination of the timeout parameters must be such that SCSI commands are finished in a reasonable time. Hence do not allow the fast I/O fail timeout to exceed
SCSI_DEVICE_BLOCK_MAX_TIMEOUT nor allow dev_loss_tmo to exceed that limit if failing I/O fast has been disabled. Furthermore, these parameters must be such that multipath can
detect failed paths timely. Hence do not allow all three parameters to be disabled simultaneously.
