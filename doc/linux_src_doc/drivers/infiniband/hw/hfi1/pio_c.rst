.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/pio.c

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

