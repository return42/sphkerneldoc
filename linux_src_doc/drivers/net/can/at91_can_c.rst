.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/can/at91_can.c

.. _`at91_activate_rx_low`:

at91_activate_rx_low
====================

.. c:function:: void at91_activate_rx_low(const struct at91_priv *priv)

    activate lower rx mailboxes

    :param const struct at91_priv \*priv:
        a91 context

.. _`at91_activate_rx_low.description`:

Description
-----------

Reenables the lower mailboxes for reception of new CAN messages

.. _`at91_activate_rx_mb`:

at91_activate_rx_mb
===================

.. c:function:: void at91_activate_rx_mb(const struct at91_priv *priv, unsigned int mb)

    reactive single rx mailbox

    :param const struct at91_priv \*priv:
        a91 context

    :param unsigned int mb:
        mailbox to reactivate

.. _`at91_activate_rx_mb.description`:

Description
-----------

Reenables given mailbox for reception of new CAN messages

.. _`at91_rx_overflow_err`:

at91_rx_overflow_err
====================

.. c:function:: void at91_rx_overflow_err(struct net_device *dev)

    send error frame due to rx overflow

    :param struct net_device \*dev:
        net device

.. _`at91_read_mb`:

at91_read_mb
============

.. c:function:: void at91_read_mb(struct net_device *dev, unsigned int mb, struct can_frame *cf)

    read CAN msg from mailbox (lowlevel impl)

    :param struct net_device \*dev:
        net device

    :param unsigned int mb:
        mailbox number to read from

    :param struct can_frame \*cf:
        can frame where to store message

.. _`at91_read_mb.description`:

Description
-----------

Reads a CAN message from the given mailbox and stores data into
given can frame. "mb" and "cf" must be valid.

.. _`at91_read_msg`:

at91_read_msg
=============

.. c:function:: void at91_read_msg(struct net_device *dev, unsigned int mb)

    read CAN message from mailbox

    :param struct net_device \*dev:
        net device

    :param unsigned int mb:
        mail box to read from

.. _`at91_read_msg.description`:

Description
-----------

Reads a CAN message from given mailbox, and put into linux network
RX queue, does all housekeeping chores (stats, ...)

.. _`at91_poll_rx`:

at91_poll_rx
============

.. c:function:: int at91_poll_rx(struct net_device *dev, int quota)

    read multiple CAN messages from mailboxes

    :param struct net_device \*dev:
        net device

    :param int quota:
        max number of pkgs we're allowed to receive

.. _`at91_poll_rx.theory-of-operation`:

Theory of Operation
-------------------


About 3/4 of the mailboxes (get_mb_rx_first()...get_mb_rx_last())
on the chip are reserved for RX. We split them into 2 groups. The
lower group ranges from \ :c:func:`get_mb_rx_first`\  to \ :c:func:`get_mb_rx_low_last`\ .

Like it or not, but the chip always saves a received CAN message
into the first free mailbox it finds (starting with the
lowest). This makes it very difficult to read the messages in the
right order from the chip. This is how we work around that problem:

The first message goes into mb nr. 1 and issues an interrupt. All
rx ints are disabled in the interrupt handler and a napi poll is
scheduled. We read the mailbox, but do \_not\_ reenable the mb (to
receive another message).

lower mbxs      upper
\____^_____\_    \__^__
/           \  /     \
+-+-+-+-+-+-+-+-++-+-+-+-+
\| \|x\|x\|x\|x\|x\|x\|x\|\| \| \| \| \|
+-+-+-+-+-+-+-+-++-+-+-+-+
0 0 0 0 0 0  0 0 0 0 1 1  \ mail
0 1 2 3 4 5  6 7 8 9 0 1  / box
^
\|
\
unused, due to chip bug

The variable priv->rx_next points to the next mailbox to read a
message from. As long we're in the lower mailboxes we just read the
mailbox but not reenable it.

With completion of the last of the lower mailboxes, we reenable the
whole first group, but continue to look for filled mailboxes in the
upper mailboxes. Imagine the second group like overflow mailboxes,
which takes CAN messages if the lower goup is full. While in the
upper group we reenable the mailbox right after reading it. Giving
the chip more room to store messages.

After finishing we look again in the lower group if we've still
quota.

.. This file was automatic generated / don't edit.

