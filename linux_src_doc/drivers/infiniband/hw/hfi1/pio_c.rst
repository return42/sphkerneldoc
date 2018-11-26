.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/pio.c

.. _`sc_wait_for_packet_egress`:

sc_wait_for_packet_egress
=========================

.. c:function:: void sc_wait_for_packet_egress(struct send_context *sc, int pause)

    :param sc:
        valid send context
    :type sc: struct send_context \*

    :param pause:
        wait for credit return
    :type pause: int

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

.. _`pio_kernel_linkup`:

pio_kernel_linkup
=================

.. c:function:: void pio_kernel_linkup(struct hfi1_devdata *dd)

    Re-enable send contexts after linkup event

    :param dd:
        valid devive data
    :type dd: struct hfi1_devdata \*

.. _`pio_kernel_linkup.description`:

Description
-----------

When the link goes down, the freeze path is taken.  However, a link down
event is different from a freeze because if the send context is re-enabled
whowever is sending data will start sending data again, which will hang
any QP that is sending data.

The freeze path now looks at the type of event that occurs and takes this
path for link down event.

.. _`sc_piobufavail`:

sc_piobufavail
==============

.. c:function:: void sc_piobufavail(struct send_context *sc)

    callback when a PIO buffer is available

    :param sc:
        the send context
    :type sc: struct send_context \*

.. _`sc_piobufavail.description`:

Description
-----------

This is called from the interrupt handler when a PIO buffer is
available after \ :c:func:`hfi1_verbs_send`\  returned an error that no buffers were
available. Disable the interrupt if there are no more QPs waiting.

.. This file was automatic generated / don't edit.

