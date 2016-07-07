.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/dev_addr_lists.c

.. _`__hw_addr_sync_dev`:

__hw_addr_sync_dev
==================

.. c:function:: int __hw_addr_sync_dev(struct netdev_hw_addr_list *list, struct net_device *dev, int (*) sync (struct net_device *, const unsigned char *, int (*) unsync (struct net_device *, const unsigned char *)

    Synchonize device's multicast list

    :param struct netdev_hw_addr_list \*list:
        address list to syncronize

    :param struct net_device \*dev:
        device to sync

    :param (int (\*) sync (struct net_device \*, const unsigned char \*):
        function to call if address should be added

    :param (int (\*) unsync (struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__hw_addr_sync_dev.description`:

Description
-----------

This funciton is intended to be called from the ndo_set_rx_mode
function of devices that require explicit address add/remove
notifications.  The unsync function may be NULL in which case
the addresses requiring removal will simply be removed without
any notification to the device.

.. _`__hw_addr_unsync_dev`:

__hw_addr_unsync_dev
====================

.. c:function:: void __hw_addr_unsync_dev(struct netdev_hw_addr_list *list, struct net_device *dev, int (*) unsync (struct net_device *, const unsigned char *)

    Remove synchronized addresses from device

    :param struct netdev_hw_addr_list \*list:
        address list to remove synchronized addresses from

    :param struct net_device \*dev:
        device to sync

    :param (int (\*) unsync (struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__hw_addr_unsync_dev.description`:

Description
-----------

Remove all addresses that were added to the device by \\ :c:func:`__hw_addr_sync_dev`\ .
This function is intended to be called from the ndo_stop or ndo_open
functions on devices that require explicit address add/remove
notifications.  If the unsync function pointer is NULL then this function
can be used to just reset the sync_cnt for the addresses in the list.

.. _`dev_addr_flush`:

dev_addr_flush
==============

.. c:function:: void dev_addr_flush(struct net_device *dev)

    Flush device address list

    :param struct net_device \*dev:
        device

.. _`dev_addr_flush.description`:

Description
-----------

Flush device address list and reset ->dev_addr.

The caller must hold the rtnl_mutex.

.. _`dev_addr_init`:

dev_addr_init
=============

.. c:function:: int dev_addr_init(struct net_device *dev)

    Init device address list

    :param struct net_device \*dev:
        device

.. _`dev_addr_init.description`:

Description
-----------

Init device address list and create the first element,
used by ->dev_addr.

The caller must hold the rtnl_mutex.

.. _`dev_addr_add`:

dev_addr_add
============

.. c:function:: int dev_addr_add(struct net_device *dev, const unsigned char *addr, unsigned char addr_type)

    Add a device address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

    :param unsigned char addr_type:
        address type

.. _`dev_addr_add.description`:

Description
-----------

Add a device address to the device or increase the reference count if
it already exists.

The caller must hold the rtnl_mutex.

.. _`dev_addr_del`:

dev_addr_del
============

.. c:function:: int dev_addr_del(struct net_device *dev, const unsigned char *addr, unsigned char addr_type)

    Release a device address.

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to delete

    :param unsigned char addr_type:
        address type

.. _`dev_addr_del.description`:

Description
-----------

Release reference to a device address and remove it from the device
if the reference count drops to zero.

The caller must hold the rtnl_mutex.

.. _`dev_uc_add_excl`:

dev_uc_add_excl
===============

.. c:function:: int dev_uc_add_excl(struct net_device *dev, const unsigned char *addr)

    Add a global secondary unicast address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

.. _`dev_uc_add`:

dev_uc_add
==========

.. c:function:: int dev_uc_add(struct net_device *dev, const unsigned char *addr)

    Add a secondary unicast address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

.. _`dev_uc_add.description`:

Description
-----------

Add a secondary unicast address to the device or increase
the reference count if it already exists.

.. _`dev_uc_del`:

dev_uc_del
==========

.. c:function:: int dev_uc_del(struct net_device *dev, const unsigned char *addr)

    Release secondary unicast address.

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to delete

.. _`dev_uc_del.description`:

Description
-----------

Release reference to a secondary unicast address and remove it
from the device if the reference count drops to zero.

.. _`dev_uc_sync`:

dev_uc_sync
===========

.. c:function:: int dev_uc_sync(struct net_device *to, struct net_device *from)

    Synchronize device's unicast list to another device

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_uc_sync.description`:

Description
-----------

Add newly added addresses to the destination device and release
addresses that have no users left. The source device must be
locked by netif_addr_lock_bh.

This function is intended to be called from the dev->set_rx_mode
function of layered software devices.  This function assumes that
addresses will only ever be synced to the \ ``to``\  devices and no other.

.. _`dev_uc_sync_multiple`:

dev_uc_sync_multiple
====================

.. c:function:: int dev_uc_sync_multiple(struct net_device *to, struct net_device *from)

    Synchronize device's unicast list to another device, but allow for multiple calls to sync to multiple devices.

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_uc_sync_multiple.description`:

Description
-----------

Add newly added addresses to the destination device and release
addresses that have been deleted from the source. The source device
must be locked by netif_addr_lock_bh.

This function is intended to be called from the dev->set_rx_mode
function of layered software devices.  It allows for a single source
device to be synced to multiple destination devices.

.. _`dev_uc_unsync`:

dev_uc_unsync
=============

.. c:function:: void dev_uc_unsync(struct net_device *to, struct net_device *from)

    Remove synchronized addresses from the destination device

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_uc_unsync.description`:

Description
-----------

Remove all addresses that were added to the destination device by
\ :c:func:`dev_uc_sync`\ . This function is intended to be called from the
dev->stop function of layered software devices.

.. _`dev_uc_flush`:

dev_uc_flush
============

.. c:function:: void dev_uc_flush(struct net_device *dev)

    Flush unicast addresses

    :param struct net_device \*dev:
        device

.. _`dev_uc_flush.description`:

Description
-----------

Flush unicast addresses.

.. _`dev_uc_init`:

dev_uc_init
===========

.. c:function:: void dev_uc_init(struct net_device *dev)

    Init unicast address list

    :param struct net_device \*dev:
        device

.. _`dev_uc_init.description`:

Description
-----------

Init unicast address list.

.. _`dev_mc_add_excl`:

dev_mc_add_excl
===============

.. c:function:: int dev_mc_add_excl(struct net_device *dev, const unsigned char *addr)

    Add a global secondary multicast address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

.. _`dev_mc_add`:

dev_mc_add
==========

.. c:function:: int dev_mc_add(struct net_device *dev, const unsigned char *addr)

    Add a multicast address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

.. _`dev_mc_add.description`:

Description
-----------

Add a multicast address to the device or increase
the reference count if it already exists.

.. _`dev_mc_add_global`:

dev_mc_add_global
=================

.. c:function:: int dev_mc_add_global(struct net_device *dev, const unsigned char *addr)

    Add a global multicast address

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to add

.. _`dev_mc_add_global.description`:

Description
-----------

Add a global multicast address to the device.

.. _`dev_mc_del`:

dev_mc_del
==========

.. c:function:: int dev_mc_del(struct net_device *dev, const unsigned char *addr)

    Delete a multicast address.

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to delete

.. _`dev_mc_del.description`:

Description
-----------

Release reference to a multicast address and remove it
from the device if the reference count drops to zero.

.. _`dev_mc_del_global`:

dev_mc_del_global
=================

.. c:function:: int dev_mc_del_global(struct net_device *dev, const unsigned char *addr)

    Delete a global multicast address.

    :param struct net_device \*dev:
        device

    :param const unsigned char \*addr:
        address to delete

.. _`dev_mc_del_global.description`:

Description
-----------

Release reference to a multicast address and remove it
from the device if the reference count drops to zero.

.. _`dev_mc_sync`:

dev_mc_sync
===========

.. c:function:: int dev_mc_sync(struct net_device *to, struct net_device *from)

    Synchronize device's multicast list to another device

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_mc_sync.description`:

Description
-----------

Add newly added addresses to the destination device and release
addresses that have no users left. The source device must be
locked by netif_addr_lock_bh.

This function is intended to be called from the ndo_set_rx_mode
function of layered software devices.

.. _`dev_mc_sync_multiple`:

dev_mc_sync_multiple
====================

.. c:function:: int dev_mc_sync_multiple(struct net_device *to, struct net_device *from)

    Synchronize device's multicast list to another device, but allow for multiple calls to sync to multiple devices.

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_mc_sync_multiple.description`:

Description
-----------

Add newly added addresses to the destination device and release
addresses that have no users left. The source device must be
locked by netif_addr_lock_bh.

This function is intended to be called from the ndo_set_rx_mode
function of layered software devices.  It allows for a single
source device to be synced to multiple destination devices.

.. _`dev_mc_unsync`:

dev_mc_unsync
=============

.. c:function:: void dev_mc_unsync(struct net_device *to, struct net_device *from)

    Remove synchronized addresses from the destination device

    :param struct net_device \*to:
        destination device

    :param struct net_device \*from:
        source device

.. _`dev_mc_unsync.description`:

Description
-----------

Remove all addresses that were added to the destination device by
\ :c:func:`dev_mc_sync`\ . This function is intended to be called from the
dev->stop function of layered software devices.

.. _`dev_mc_flush`:

dev_mc_flush
============

.. c:function:: void dev_mc_flush(struct net_device *dev)

    Flush multicast addresses

    :param struct net_device \*dev:
        device

.. _`dev_mc_flush.description`:

Description
-----------

Flush multicast addresses.

.. _`dev_mc_init`:

dev_mc_init
===========

.. c:function:: void dev_mc_init(struct net_device *dev)

    Init multicast address list

    :param struct net_device \*dev:
        device

.. _`dev_mc_init.description`:

Description
-----------

Init multicast address list.

.. This file was automatic generated / don't edit.

