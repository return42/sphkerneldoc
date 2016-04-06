
.. _API-mpt-diag-reset:

==============
mpt_diag_reset
==============

*man mpt_diag_reset(9)*

*4.6.0-rc1*

Perform hard reset of the adapter.


Synopsis
========

.. c:function:: int mpt_diag_reset( MPT_ADAPTER * ioc, int ignore, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``ignore``
    Set if to honor and clear to ignore the reset history bit

``sleepFlag``
    CAN_SLEEP if called in a non-interrupt thread, else set to NO_SLEEP (use mdelay instead)


Description
===========

This routine places the adapter in diagnostic mode via the WriteSequence register and then performs a hard reset of adapter via the Diagnostic register. Adapter should be in ready
state upon successful completion.


Returns
=======

1 hard reset successful 0 no reset performed because reset history bit set -2 enabling diagnostic mode failed -3 diagnostic reset failed
