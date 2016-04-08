
.. _API-wimax-dev-rm:

============
wimax_dev_rm
============

*man wimax_dev_rm(9)*

*4.6.0-rc1*

Unregister an existing WiMAX device


Synopsis
========

.. c:function:: void wimax_dev_rm( struct wimax_dev * wimax_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor


Description
===========

Unregisters a WiMAX device previously registered for use with ``wimax_add_rm``.

IMPORTANT! Must call before calling ``unregister_netdev``.

After this function returns, you will not get any more user space control requests (via netlink or debugfs) and thus to wimax_dev->ops.

Reentrancy control is ensured by setting the state to ``__WIMAX_ST_QUIESCING``. rfkill operations coming through wimax_⋆rfkill⋆() will be stopped by the quiescing state; ops
coming from the rfkill subsystem will be stopped by the support being removed by ``wimax_rfkill_rm``.
