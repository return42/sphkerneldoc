.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/8390/axnet_cs.c

.. _`ax_open`:

ax_open
=======

.. c:function:: int ax_open(struct net_device *dev)

    Open/initialize the board.

    :param struct net_device \*dev:
        network device to initialize

.. _`ax_open.description`:

Description
-----------

This routine goes all-out, setting everything
up anew at each open, even though many of these registers should only
need to be set once at boot.

.. _`ax_close`:

ax_close
========

.. c:function:: int ax_close(struct net_device *dev)

    shut down network device

    :param struct net_device \*dev:
        network device to close

.. _`ax_close.description`:

Description
-----------

Opposite of \ :c:func:`ax_open`\ . Only used when "ifconfig <devname> down" is done.

.. _`axnet_tx_timeout`:

axnet_tx_timeout
================

.. c:function:: void axnet_tx_timeout(struct net_device *dev)

    handle transmit time out condition

    :param struct net_device \*dev:
        network device which has apparently fallen asleep

.. _`axnet_tx_timeout.description`:

Description
-----------

Called by kernel when device never acknowledges a transmit has
completed (or failed) - i.e. never posted a Tx related interrupt.

.. _`axnet_start_xmit`:

axnet_start_xmit
================

.. c:function:: netdev_tx_t axnet_start_xmit(struct sk_buff *skb, struct net_device *dev)

    begin packet transmission

    :param struct sk_buff \*skb:
        packet to be sent

    :param struct net_device \*dev:
        network device to which packet is sent

.. _`axnet_start_xmit.description`:

Description
-----------

Sends a packet to an 8390 network device.

.. _`ax_interrupt`:

ax_interrupt
============

.. c:function:: irqreturn_t ax_interrupt(int irq, void *dev_id)

    handle the interrupts from an 8390

    :param int irq:
        interrupt number

    :param void \*dev_id:
        a pointer to the net_device

.. _`ax_interrupt.description`:

Description
-----------

Handle the ether interface interrupts. We pull packets from
the 8390 via the card specific functions and fire them at the networking
stack. We also handle transmit completions and wake the transmit path if
necessary. We also update the counters and do other housekeeping as
needed.

.. _`ei_tx_err`:

ei_tx_err
=========

.. c:function:: void ei_tx_err(struct net_device *dev)

    handle transmitter error

    :param struct net_device \*dev:
        network device which threw the exception

.. _`ei_tx_err.description`:

Description
-----------

A transmitter error has happened. Most likely excess collisions (which
is a fairly normal condition). If the error is one where the Tx will
have been aborted, we try and send another one right away, instead of
letting the failed packet sit and collect dust in the Tx buffer. This
is a much better solution as it avoids kernel based Tx timeouts, and
an unnecessary card reset.

Called with lock held.

.. _`ei_tx_intr`:

ei_tx_intr
==========

.. c:function:: void ei_tx_intr(struct net_device *dev)

    transmit interrupt handler

    :param struct net_device \*dev:
        network device for which tx intr is handled

.. _`ei_tx_intr.we-have-finished-a-transmit`:

We have finished a transmit
---------------------------

check for errors and then trigger the next
packet to be sent. Called with lock held.

.. _`ei_receive`:

ei_receive
==========

.. c:function:: void ei_receive(struct net_device *dev)

    receive some packets

    :param struct net_device \*dev:
        network device with which receive will be run

.. _`ei_receive.description`:

Description
-----------

We have a good packet(s), get it/them out of the buffers.
Called with lock held.

.. _`ei_rx_overrun`:

ei_rx_overrun
=============

.. c:function:: void ei_rx_overrun(struct net_device *dev)

    handle receiver overrun

    :param struct net_device \*dev:
        network device which threw exception

.. _`ei_rx_overrun.we-have-a-receiver-overrun`:

We have a receiver overrun
--------------------------

we have to kick the 8390 to get it started
again. Problem is that you have to kick it exactly as NS prescribes in
the updated datasheets, or "the NIC may act in an unpredictable manner."
This includes causing "the NIC to defer indefinitely when it is stopped
on a busy network."  Ugh.
Called with lock held. Don't call this with the interrupts off or your
computer will hate you - it takes 10ms or so.

.. _`do_set_multicast_list`:

do_set_multicast_list
=====================

.. c:function:: void do_set_multicast_list(struct net_device *dev)

    set/clear multicast filter

    :param struct net_device \*dev:
        net device for which multicast filter is adjusted

.. _`do_set_multicast_list.description`:

Description
-----------

Set or clear the multicast filter for this adaptor.
Must be called with lock held.

.. _`ax88190_init`:

AX88190_init
============

.. c:function:: void AX88190_init(struct net_device *dev, int startp)

    initialize 8390 hardware

    :param struct net_device \*dev:
        network device to initialize

    :param int startp:
        boolean.  non-zero value to initiate chip processing

.. _`ax88190_init.description`:

Description
-----------

Must be called with lock held.

.. This file was automatic generated / don't edit.

