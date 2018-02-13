.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/mmc_ops.c

.. _`__mmc_switch`:

\__mmc_switch
=============

.. c:function:: int __mmc_switch(struct mmc_card *card, u8 set, u8 index, u8 value, unsigned int timeout_ms, unsigned char timing, bool use_busy_signal, bool send_status, bool retry_crc_err)

    modify EXT_CSD register

    :param struct mmc_card \*card:
        the MMC card associated with the data transfer

    :param u8 set:
        cmd set values

    :param u8 index:
        EXT_CSD register index

    :param u8 value:
        value to program into EXT_CSD register

    :param unsigned int timeout_ms:
        timeout (ms) for operation performed by register write,
        timeout of zero implies maximum possible timeout

    :param unsigned char timing:
        new timing to change to

    :param bool use_busy_signal:
        use the busy signal as response type

    :param bool send_status:
        send status cmd to poll for busy

    :param bool retry_crc_err:
        retry when CRC errors when polling with CMD13 for busy

.. _`__mmc_switch.description`:

Description
-----------

Modifies the EXT_CSD register for selected card.

.. _`mmc_interrupt_hpi`:

mmc_interrupt_hpi
=================

.. c:function:: int mmc_interrupt_hpi(struct mmc_card *card)

    Issue for High priority Interrupt

    :param struct mmc_card \*card:
        the MMC card associated with the HPI transfer

.. _`mmc_interrupt_hpi.description`:

Description
-----------

Issued High Priority Interrupt, and check for card status
until out-of prg-state.

.. _`mmc_stop_bkops`:

mmc_stop_bkops
==============

.. c:function:: int mmc_stop_bkops(struct mmc_card *card)

    stop ongoing BKOPS

    :param struct mmc_card \*card:
        MMC card to check BKOPS

.. _`mmc_stop_bkops.description`:

Description
-----------

Send HPI command to stop ongoing background operations to
allow rapid servicing of foreground operations, e.g. read/
writes. Wait until the card comes out of the programming state
to avoid errors in servicing read/write requests.

.. _`mmc_start_bkops`:

mmc_start_bkops
===============

.. c:function:: void mmc_start_bkops(struct mmc_card *card, bool from_exception)

    start BKOPS for supported cards

    :param struct mmc_card \*card:
        MMC card to start BKOPS

    :param bool from_exception:
        A flag to indicate if this function was
        called due to an exception raised by the card

.. _`mmc_start_bkops.description`:

Description
-----------

Start background operations whenever requested.
When the urgent BKOPS bit is set in a R1 command response
then background operations should be started immediately.

.. This file was automatic generated / don't edit.

