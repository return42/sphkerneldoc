.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/ctcm_main.c

.. _`ctcm_unpack_skb`:

ctcm_unpack_skb
===============

.. c:function:: void ctcm_unpack_skb(struct channel *ch, struct sk_buff *pskb)

    upper layers.

    :param struct channel \*ch:
        *undescribed*

    :param struct sk_buff \*pskb:
        *undescribed*

.. _`ctcm_unpack_skb.description`:

Description
-----------

ch          The channel where this skb has been received.
pskb        The received skb.

.. _`channel_free`:

channel_free
============

.. c:function:: void channel_free(struct channel *ch)

    :param struct channel \*ch:
        *undescribed*

.. _`channel_free.description`:

Description
-----------

ch          Pointer to channel struct to be released.

.. _`channel_remove`:

channel_remove
==============

.. c:function:: void channel_remove(struct channel *ch)

    :param struct channel \*ch:
        *undescribed*

.. _`channel_remove.description`:

Description
-----------

ch          Pointer to channel struct to be released.

.. _`channel_get`:

channel_get
===========

.. c:function:: struct channel *channel_get(enum ctcm_channel_types type, char *id, int direction)

    :param enum ctcm_channel_types type:
        *undescribed*

    :param char \*id:
        *undescribed*

    :param int direction:
        *undescribed*

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

    :param struct channel \*ch:
        *undescribed*

    :param __u8 sense:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

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

    :param struct channel \*ch:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

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

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

    :param int new_mtu:
        *undescribed*

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

    :param struct net_device \*dev:
        *undescribed*

.. _`ctcm_stats.description`:

Description
-----------

dev         Pointer to interface struct.

returns Pointer to stats struct of this interface.

.. _`ctcm_irq_handler`:

ctcm_irq_handler
================

.. c:function:: void ctcm_irq_handler(struct ccw_device *cdev, unsigned long intparm, struct irb *irb)

    :param struct ccw_device \*cdev:
        *undescribed*

    :param unsigned long intparm:
        *undescribed*

    :param struct irb \*irb:
        *undescribed*

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

    :param struct ccwgroup_device \*cgdev:
        *undescribed*

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

    :param struct ccw_device \*cdev:
        *undescribed*

    :param enum ctcm_channel_types type:
        *undescribed*

    :param struct ctcm_priv \*priv:
        *undescribed*

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

    :param struct ccwgroup_device \*cgdev:
        *undescribed*

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

    :param  void:
        no arguments

.. _`ctcm_init.description`:

Description
-----------

returns 0 on success, !0 on error.

.. This file was automatic generated / don't edit.

