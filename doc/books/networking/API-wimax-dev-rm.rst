.. -*- coding: utf-8; mode: rst -*-

.. _API-wimax-dev-rm:

============
wimax_dev_rm
============

*man wimax_dev_rm(9)*

*4.6.0-rc5*

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

Unregisters a WiMAX device previously registered for use with
``wimax_add_rm``.

IMPORTANT! Must call before calling ``unregister_netdev``.

After this function returns, you will not get any more user space
control requests (via netlink or debugfs) and thus to wimax_dev->ops.

Reentrancy control is ensured by setting the state to
``__WIMAX_ST_QUIESCING``. rfkill operations coming through
wimax_*rfkill*() will be stopped by the quiescing state; ops coming
from the rfkill subsystem will be stopped by the support being removed
by ``wimax_rfkill_rm``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
