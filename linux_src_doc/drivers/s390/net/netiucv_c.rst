.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/netiucv.c

.. _`iucv_dbf_setup_name`:

IUCV_DBF_SETUP_NAME
===================

.. c:function::  IUCV_DBF_SETUP_NAME()

.. _`printk_header`:

PRINTK_HEADER
=============

.. c:function::  PRINTK_HEADER()

.. _`list_head`:

LIST_HEAD
=========

.. c:function::  LIST_HEAD( iucv_connection_list)

    :param iucv_connection_list:
        *undescribed*
    :type iucv_connection_list: 

.. _`netiucv_clear_busy`:

netiucv_clear_busy
==================

.. c:function:: void netiucv_clear_busy(struct net_device *dev)

    of network devices.

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`netiucv_printname`:

netiucv_printname
=================

.. c:function:: char *netiucv_printname(char *name, int len)

    form (strip whitespace at end).

    :param name:
        *undescribed*
    :type name: char \*

    :param len:
        *undescribed*
    :type len: int

.. _`netiucv_printname.description`:

Description
-----------

\ ``param``\  An iucv userId

\ ``returns``\  The printable string (static data!!)

.. _`netiucv_action_nop`:

netiucv_action_nop
==================

.. c:function:: void netiucv_action_nop(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`netiucv_unpack_skb`:

netiucv_unpack_skb
==================

.. c:function:: void netiucv_unpack_skb(struct iucv_connection *conn, struct sk_buff *pskb)

    :param conn:
        The connection where this skb has been received.
    :type conn: struct iucv_connection \*

    :param pskb:
        The received skb.
    :type pskb: struct sk_buff \*

.. _`netiucv_unpack_skb.description`:

Description
-----------

Unpack a just received skb and hand it over to upper layers.
Helper function for conn_action_rx.

.. _`dev_action_start`:

dev_action_start
================

.. c:function:: void dev_action_start(fsm_instance *fi, int event, void *arg)

    :param fi:
        An instance of an interface statemachine.
    :type fi: fsm_instance \*

    :param event:
        The event, just happened.
    :type event: int

    :param arg:
        Generic pointer, casted from struct net_device \* upon call.
    :type arg: void \*

.. _`dev_action_start.description`:

Description
-----------

Startup connection by sending CONN_EVENT_START to it.

.. _`dev_action_stop`:

dev_action_stop
===============

.. c:function:: void dev_action_stop(fsm_instance *fi, int event, void *arg)

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_stop.description`:

Description
-----------

\ ``param``\  fi    An instance of an interface statemachine.
\ ``param``\  event The event, just happened.
\ ``param``\  arg   Generic pointer, casted from struct net_device \* upon call.

.. _`dev_action_connup`:

dev_action_connup
=================

.. c:function:: void dev_action_connup(fsm_instance *fi, int event, void *arg)

    when a connection is up and running.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_connup.description`:

Description
-----------

\ ``param``\  fi    An instance of an interface statemachine.
\ ``param``\  event The event, just happened.
\ ``param``\  arg   Generic pointer, casted from struct net_device \* upon call.

.. _`dev_action_conndown`:

dev_action_conndown
===================

.. c:function:: void dev_action_conndown(fsm_instance *fi, int event, void *arg)

    when a connection has been shutdown.

    :param fi:
        *undescribed*
    :type fi: fsm_instance \*

    :param event:
        *undescribed*
    :type event: int

    :param arg:
        *undescribed*
    :type arg: void \*

.. _`dev_action_conndown.description`:

Description
-----------

\ ``param``\  fi    An instance of an interface statemachine.
\ ``param``\  event The event, just happened.
\ ``param``\  arg   Generic pointer, casted from struct net_device \* upon call.

.. _`netiucv_transmit_skb`:

netiucv_transmit_skb
====================

.. c:function:: int netiucv_transmit_skb(struct iucv_connection *conn, struct sk_buff *skb)

    This is a helper function for \ :c:func:`netiucv_tx`\ .

    :param conn:
        *undescribed*
    :type conn: struct iucv_connection \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`netiucv_transmit_skb.description`:

Description
-----------

\ ``param``\  conn Connection to be used for sending.
\ ``param``\  skb Pointer to struct sk_buff of packet to send.
The linklevel header has already been set up
by \ :c:func:`netiucv_tx`\ .

\ ``return``\  0 on success, -ERRNO on failure. (Never fails.)

.. _`netiucv_open`:

netiucv_open
============

.. c:function:: int netiucv_open(struct net_device *dev)

    Called from generic network layer when ifconfig up is run.

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`netiucv_open.description`:

Description
-----------

\ ``param``\  dev Pointer to interface struct.

\ ``return``\  0 on success, -ERRNO on failure. (Never fails.)

.. _`netiucv_close`:

netiucv_close
=============

.. c:function:: int netiucv_close(struct net_device *dev)

    Called from generic network layer when ifconfig down is run.

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`netiucv_close.description`:

Description
-----------

\ ``param``\  dev Pointer to interface struct.

\ ``return``\  0 on success, -ERRNO on failure. (Never fails.)

.. _`netiucv_pm_freeze`:

netiucv_pm_freeze
=================

.. c:function:: int netiucv_pm_freeze(struct device *dev)

    Freeze PM callback

    :param dev:
        netiucv device
    :type dev: struct device \*

.. _`netiucv_pm_freeze.description`:

Description
-----------

close open netiucv interfaces

.. _`netiucv_pm_restore_thaw`:

netiucv_pm_restore_thaw
=======================

.. c:function:: int netiucv_pm_restore_thaw(struct device *dev)

    Thaw and restore PM callback

    :param dev:
        netiucv device
    :type dev: struct device \*

.. _`netiucv_pm_restore_thaw.description`:

Description
-----------

re-open netiucv interfaces closed during freeze

.. _`netiucv_tx`:

netiucv_tx
==========

.. c:function:: int netiucv_tx(struct sk_buff *skb, struct net_device *dev)

    Called from generic network device layer.

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`netiucv_tx.description`:

Description
-----------

\ ``param``\  skb Pointer to buffer containing the packet.
\ ``param``\  dev Pointer to interface struct.

\ ``return``\  0 if packet consumed, !0 if packet rejected.
Note: If we return !0, then the packet is free'd by
the generic network layer.

.. _`netiucv_stats`:

netiucv_stats
=============

.. c:function:: struct net_device_stats *netiucv_stats(struct net_device *dev)

    :param dev:
        Pointer to interface struct.
    :type dev: struct net_device \*

.. _`netiucv_stats.description`:

Description
-----------

Returns interface statistics of a device.

Returns pointer to stats struct of this interface.

.. _`netiucv_new_connection`:

netiucv_new_connection
======================

.. c:function:: struct iucv_connection *netiucv_new_connection(struct net_device *dev, char *username, char *userdata)

    Add it to the list of netiucv connections;

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param username:
        *undescribed*
    :type username: char \*

    :param userdata:
        *undescribed*
    :type userdata: char \*

.. _`netiucv_remove_connection`:

netiucv_remove_connection
=========================

.. c:function:: void netiucv_remove_connection(struct iucv_connection *conn)

    list of netiucv connections.

    :param conn:
        *undescribed*
    :type conn: struct iucv_connection \*

.. _`netiucv_free_netdevice`:

netiucv_free_netdevice
======================

.. c:function:: void netiucv_free_netdevice(struct net_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`netiucv_init_netdevice`:

netiucv_init_netdevice
======================

.. c:function:: struct net_device *netiucv_init_netdevice(char *username, char *userdata)

    :param username:
        *undescribed*
    :type username: char \*

    :param userdata:
        *undescribed*
    :type userdata: char \*

.. This file was automatic generated / don't edit.

