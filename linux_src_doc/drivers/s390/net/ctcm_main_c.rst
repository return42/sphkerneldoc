.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/ctcm_main.c

.. _`ctcm_unpack_skb`:

ctcm_unpack_skb
===============

.. c:function:: void ctcm_unpack_skb(struct channel *ch, struct sk_buff *pskb)

    upper layers.

    :param ch:
        *undescribed*
    :type ch: struct channel \*

    :param pskb:
        *undescribed*
    :type pskb: struct sk_buff \*

.. _`ctcm_unpack_skb.description`:

Description
-----------

ch          The channel where this skb has been received.
pskb        The received skb.

.. _`channel_free`:

channel_free
============

.. c:function:: void channel_free(struct channel *ch)

    :param ch:
        *undescribed*
    :type ch: struct channel \*

.. _`channel_free.description`:

Description
-----------

ch          Pointer to channel struct to be released.

.. _`channel_remove`:

channel_remove
==============

.. c:function:: void channel_remove(struct channel *ch)

    :param ch:
        *undescribed*
    :type ch: struct channel \*

.. _`channel_remove.description`:

Description
-----------

ch          Pointer to channel struct to be released.

.. _`channel_get`:

channel_get
===========

.. c:function:: struct channel *channel_get(enum ctcm_channel_types type, char *id, int direction)

    :param type:
        *undescribed*
    :type type: enum ctcm_channel_types

    :param id:
        *undescribed*
    :type id: char \*

    :param direction:
        *undescribed*
    :type direction: int

.. _`channel_get.description`:

Description
-----------

type        Type of channel we are interested in.
id          Id of channel we are interested in.
direction   Direction we want to use this channel for.

returns Pointer to a channel or NULL if no matching channel available.

.. _`ccw_unit_check`:

ccw_unit_check
==============

.. c:function:: void ccw_unit_check(struct channel *ch, __u8 sense)

    :param ch:
        *undescribed*
    :type ch: struct channel \*

    :param sense:
        *undescribed*
    :type sense: __u8

.. _`ccw_unit_check.description`:

Description
-----------

ch          The channel, the sense code belongs to.
sense       The sense code to inspect.

.. _`ctcm_open`:

ctcm_open
=========

.. c:function:: int ctcm_open(struct net_device *dev)

    Called from generic network layer when ifconfig up is run.

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`ctcm_open.description`:

Description
-----------

dev         Pointer to interface struct.

returns 0 on success, -ERRNO on failure. (Never fails.)

.. _`ctcm_close`:

ctcm_close
==========

.. c:function:: int ctcm_close(struct net_device *dev)

    Called from generic network layer when ifconfig down is run.

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`ctcm_close.description`:

Description
-----------

dev         Pointer to interface struct.

returns 0 on success, -ERRNO on failure. (Never fails.)

.. _`ctcm_transmit_skb`:

ctcm_transmit_skb
=================

.. c:function:: int ctcm_transmit_skb(struct channel *ch, struct sk_buff *skb)

    This is a helper function for \ :c:func:`ctcm_tx`\ .

    :param ch:
        *undescribed*
    :type ch: struct channel \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`ctcm_transmit_skb.description`:

Description
-----------

ch          Channel to be used for sending.
skb         Pointer to struct sk_buff of packet to send.
The linklevel header has already been set up
by \ :c:func:`ctcm_tx`\ .

returns 0 on success, -ERRNO on failure. (Never fails.)

.. _`ctcm_tx`:

ctcm_tx
=======

.. c:function:: int ctcm_tx(struct sk_buff *skb, struct net_device *dev)

    Called from generic network device layer.

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`ctcm_tx.description`:

Description
-----------

skb         Pointer to buffer containing the packet.
dev         Pointer to interface struct.

returns 0 if packet consumed, !0 if packet rejected.
Note: If we return !0, then the packet is free'd by
the generic network layer.

.. _`ctcm_change_mtu`:

ctcm_change_mtu
===============

.. c:function:: int ctcm_change_mtu(struct net_device *dev, int new_mtu)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param new_mtu:
        *undescribed*
    :type new_mtu: int

.. _`ctcm_change_mtu.description`:

Description
-----------

dev         Pointer to interface struct.
new_mtu     The new MTU to use for this interface.

returns 0 on success, -EINVAL if MTU is out of valid range.
(valid range is 576 .. 65527). If VM is on the
remote side, maximum MTU is 32760, however this is
not checked here.

.. _`ctcm_stats`:

ctcm_stats
==========

.. c:function:: struct net_device_stats *ctcm_stats(struct net_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`ctcm_stats.description`:

Description
-----------

dev         Pointer to interface struct.

returns Pointer to stats struct of this interface.

.. _`ctcm_irq_handler`:

ctcm_irq_handler
================

.. c:function:: void ctcm_irq_handler(struct ccw_device *cdev, unsigned long intparm, struct irb *irb)

    :param cdev:
        *undescribed*
    :type cdev: struct ccw_device \*

    :param intparm:
        *undescribed*
    :type intparm: unsigned long

    :param irb:
        *undescribed*
    :type irb: struct irb \*

.. _`ctcm_irq_handler.description`:

Description
-----------

cdev        The ccw_device the interrupt is for.
intparm     interruption parameter.
irb         interruption response block.

.. _`ctcm_probe_device`:

ctcm_probe_device
=================

.. c:function:: int ctcm_probe_device(struct ccwgroup_device *cgdev)

    Add ctcm private data.

    :param cgdev:
        *undescribed*
    :type cgdev: struct ccwgroup_device \*

.. _`ctcm_probe_device.description`:

Description
-----------

cgdev       pointer to ccwgroup_device just added

returns 0 on success, !0 on failure.

.. _`add_channel`:

add_channel
===========

.. c:function:: int add_channel(struct ccw_device *cdev, enum ctcm_channel_types type, struct ctcm_priv *priv)

    Keeps the channel list sorted.

    :param cdev:
        *undescribed*
    :type cdev: struct ccw_device \*

    :param type:
        *undescribed*
    :type type: enum ctcm_channel_types

    :param priv:
        *undescribed*
    :type priv: struct ctcm_priv \*

.. _`add_channel.description`:

Description
-----------

cdev        The ccw_device to be added.
type        The type class of the new channel.
priv        Points to the private data of the ccwgroup_device.

returns 0 on success, !0 on error.

.. _`ctcm_shutdown_device`:

ctcm_shutdown_device
====================

.. c:function:: int ctcm_shutdown_device(struct ccwgroup_device *cgdev)

    :param cgdev:
        *undescribed*
    :type cgdev: struct ccwgroup_device \*

.. _`ctcm_shutdown_device.description`:

Description
-----------

cgdev       Device to be shut down.

returns 0 on success, !0 on failure.

.. _`ctcm_init`:

ctcm_init
=========

.. c:function:: int ctcm_init( void)

    This is called just after the module is loaded.

    :param void:
        no arguments
    :type void: 

.. _`ctcm_init.description`:

Description
-----------

returns 0 on success, !0 on error.

.. This file was automatic generated / don't edit.

