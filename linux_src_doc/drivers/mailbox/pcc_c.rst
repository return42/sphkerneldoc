.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mailbox/pcc.c

.. _`get_pcc_channel`:

get_pcc_channel
===============

.. c:function:: struct mbox_chan *get_pcc_channel(int id)

    Given a PCC subspace idx, get the respective mbox_channel.

    :param id:
        PCC subspace index.
    :type id: int

.. _`get_pcc_channel.return`:

Return
------

ERR_PTR(errno) if error, else pointer
to mbox channel.

.. _`pcc_map_interrupt`:

pcc_map_interrupt
=================

.. c:function:: int pcc_map_interrupt(u32 interrupt, u32 flags)

    Map a PCC subspace GSI to a linux IRQ number

    :param interrupt:
        GSI number.
    :type interrupt: u32

    :param flags:
        interrupt flags
    :type flags: u32

.. _`pcc_map_interrupt.return`:

Return
------

a valid linux IRQ number on success
0 or -EINVAL on failure

.. _`pcc_mbox_irq`:

pcc_mbox_irq
============

.. c:function:: irqreturn_t pcc_mbox_irq(int irq, void *p)

    PCC mailbox interrupt handler

    :param irq:
        *undescribed*
    :type irq: int

    :param p:
        *undescribed*
    :type p: void \*

.. _`pcc_mbox_request_channel`:

pcc_mbox_request_channel
========================

.. c:function:: struct mbox_chan *pcc_mbox_request_channel(struct mbox_client *cl, int subspace_id)

    PCC clients call this function to request a pointer to their PCC subspace, from which they can get the details of communicating with the remote.

    :param cl:
        Pointer to Mailbox client, so we know where to bind the
        Channel.
    :type cl: struct mbox_client \*

    :param subspace_id:
        The PCC Subspace index as parsed in the PCC client
        ACPI package. This is used to lookup the array of PCC
        subspaces as parsed by the PCC Mailbox controller.
    :type subspace_id: int

.. _`pcc_mbox_request_channel.return`:

Return
------

Pointer to the Mailbox Channel if successful or
ERR_PTR.

.. _`pcc_mbox_free_channel`:

pcc_mbox_free_channel
=====================

.. c:function:: void pcc_mbox_free_channel(struct mbox_chan *chan)

    Clients call this to free their Channel.

    :param chan:
        Pointer to the mailbox channel as returned by
        \ :c:func:`pcc_mbox_request_channel`\ 
    :type chan: struct mbox_chan \*

.. _`pcc_send_data`:

pcc_send_data
=============

.. c:function:: int pcc_send_data(struct mbox_chan *chan, void *data)

    Called from Mailbox Controller code. Used here only to ring the channel doorbell. The PCC client specific read/write is done in the client driver in order to maintain atomicity over PCC channel once OS has control over it. See above for flow of operations.

    :param chan:
        Pointer to Mailbox channel over which to send data.
    :type chan: struct mbox_chan \*

    :param data:
        Client specific data written over channel. Used here
        only for debug after PCC transaction completes.
    :type data: void \*

.. _`pcc_send_data.return`:

Return
------

Err if something failed else 0 for success.

.. _`parse_pcc_subspace`:

parse_pcc_subspace
==================

.. c:function:: int parse_pcc_subspace(struct acpi_subtable_header *header, const unsigned long end)

    - Count PCC subspaces defined

    :param header:
        Pointer to the ACPI subtable header under the PCCT.
    :type header: struct acpi_subtable_header \*

    :param end:
        End of subtable entry.
    :type end: const unsigned long

.. _`parse_pcc_subspace.return`:

Return
------

If we find a PCC subspace entry of a valid type, return 0.
Otherwise, return -EINVAL.

This gets called for each entry in the PCC table.

.. _`pcc_parse_subspace_irq`:

pcc_parse_subspace_irq
======================

.. c:function:: int pcc_parse_subspace_irq(int id, struct acpi_pcct_hw_reduced *pcct_ss)

    Parse the PCC IRQ and PCC ACK register There should be one entry per PCC client.

    :param id:
        PCC subspace index.
    :type id: int

    :param pcct_ss:
        Pointer to the ACPI subtable header under the PCCT.
    :type pcct_ss: struct acpi_pcct_hw_reduced \*

.. _`pcc_parse_subspace_irq.return`:

Return
------

0 for Success, else errno.

This gets called for each entry in the PCC table.

.. _`acpi_pcc_probe`:

acpi_pcc_probe
==============

.. c:function:: int acpi_pcc_probe( void)

    Parse the ACPI tree for the PCCT.

    :param void:
        no arguments
    :type void: 

.. _`acpi_pcc_probe.return`:

Return
------

0 for Success, else errno.

.. _`pcc_mbox_probe`:

pcc_mbox_probe
==============

.. c:function:: int pcc_mbox_probe(struct platform_device *pdev)

    Called when we find a match for the PCCT platform device. This is purely used to represent the PCCT as a virtual device for registering with the generic Mailbox framework.

    :param pdev:
        Pointer to platform device returned when a match
        is found.
    :type pdev: struct platform_device \*

.. _`pcc_mbox_probe.return`:

Return
------

0 for Success, else errno.

.. This file was automatic generated / don't edit.

