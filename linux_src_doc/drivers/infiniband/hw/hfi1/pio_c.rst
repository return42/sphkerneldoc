.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/pio.c

.. _`sc_wait_for_packet_egress`:

sc_wait_for_packet_egress
=========================

.. c:function:: void sc_wait_for_packet_egress(struct send_context *sc, int pause)

    :param struct send_context \*sc:
        valid send context

    :param int pause:
        wait for credit return

.. _`sc_wait_for_packet_egress.description`:

Description
-----------

Wait for packet egress, optionally pause for credit return

Egress halt and Context halt are not necessarily the same thing, so
check for both.

.. _`sc_wait_for_packet_egress.note`:

NOTE
----

The context halt bit may not be set immediately.  Because of this,
it is necessary to check the SW SFC_HALTED bit (set in the IRQ) and the HW
context bit to determine if the context is halted.

.. _`sc_piobufavail`:

sc_piobufavail
==============

.. c:function:: void sc_piobufavail(struct send_context *sc)

    callback when a PIO buffer is available

    :param struct send_context \*sc:
        the send context

.. _`sc_piobufavail.description`:

Description
-----------

This is called from the interrupt handler when a PIO buffer is
available after \ :c:func:`hfi1_verbs_send`\  returned an error that no buffers were
available. Disable the interrupt if there are no more QPs waiting.

.. This file was automatic generated / don't edit.

