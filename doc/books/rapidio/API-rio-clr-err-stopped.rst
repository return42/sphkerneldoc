
.. _API-rio-clr-err-stopped:

===================
rio_clr_err_stopped
===================

*man rio_clr_err_stopped(9)*

*4.6.0-rc1*

Clears port Error-stopped states.


Synopsis
========

.. c:function:: int rio_clr_err_stopped( struct rio_dev * rdev, u32 pnum, u32 err_status )

Arguments
=========

``rdev``
    Pointer to RIO device control structure

``pnum``
    Switch port number to clear errors

``err_status``
    port error status (if 0 reads register from device)
