.. -*- coding: utf-8; mode: rst -*-

=====
pcc.c
=====


.. _`get_pcc_channel`:

get_pcc_channel
===============

.. c:function:: struct mbox_chan *get_pcc_channel (int id)

    Given a PCC subspace idx, get the respective mbox_channel.

    :param int id:
        PCC subspace index.



.. _`get_pcc_channel.return`:

Return
------

ERR_PTR(errno) if error, else pointer
to mbox channel.



.. _`pcc_mbox_request_channel`:

pcc_mbox_request_channel
========================

.. c:function:: struct mbox_chan *pcc_mbox_request_channel (struct mbox_client *cl, int subspace_id)

    PCC clients call this function to request a pointer to their PCC subspace, from which they can get the details of communicating with the remote.

    :param struct mbox_client \*cl:
        Pointer to Mailbox client, so we know where to bind the
        Channel.

    :param int subspace_id:
        The PCC Subspace index as parsed in the PCC client
        ACPI package. This is used to lookup the array of PCC
        subspaces as parsed by the PCC Mailbox controller.



.. _`pcc_mbox_request_channel.return`:

Return
------

Pointer to the Mailbox Channel if successful or
ERR_PTR.



.. _`pcc_mbox_free_channel`:

pcc_mbox_free_channel
=====================

.. c:function:: void pcc_mbox_free_channel (struct mbox_chan *chan)

    Clients call this to free their Channel.

    :param struct mbox_chan \*chan:
        Pointer to the mailbox channel as returned by
        :c:func:`pcc_mbox_request_channel`



.. _`pcc_send_data`:

pcc_send_data
=============

.. c:function:: int pcc_send_data (struct mbox_chan *chan, void *data)

    Called from Mailbox Controller code. Used here only to ring the channel doorbell. The PCC client specific read/write is done in the client driver in order to maintain atomicity over PCC channel once OS has control over it. See above for flow of operations.

    :param struct mbox_chan \*chan:
        Pointer to Mailbox channel over which to send data.

    :param void \*data:
        Client specific data written over channel. Used here
        only for debug after PCC transaction completes.



.. _`pcc_send_data.return`:

Return
------

Err if something failed else 0 for success.



.. _`parse_pcc_subspace`:

parse_pcc_subspace
==================

.. c:function:: int parse_pcc_subspace (struct acpi_subtable_header *header, const unsigned long end)

    Parse the PCC table and verify PCC subspace entries. There should be one entry per PCC client.

    :param struct acpi_subtable_header \*header:
        Pointer to the ACPI subtable header under the PCCT.

    :param const unsigned long end:
        End of subtable entry.



.. _`parse_pcc_subspace.return`:

Return
------

0 for Success, else errno.

This gets called for each entry in the PCC table.



.. _`acpi_pcc_probe`:

acpi_pcc_probe
==============

.. c:function:: int acpi_pcc_probe ( void)

    Parse the ACPI tree for the PCCT.

    :param void:
        no arguments



.. _`acpi_pcc_probe.return`:

Return
------

0 for Success, else errno.



.. _`pcc_mbox_probe`:

pcc_mbox_probe
==============

.. c:function:: int pcc_mbox_probe (struct platform_device *pdev)

    Called when we find a match for the PCCT platform device. This is purely used to represent the PCCT as a virtual device for registering with the generic Mailbox framework.

    :param struct platform_device \*pdev:
        Pointer to platform device returned when a match
        is found.



.. _`pcc_mbox_probe.return`:

Return
------

0 for Success, else errno.

