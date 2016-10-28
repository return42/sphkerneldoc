.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rts5208/rtsx_chip.c

.. _`rtsx_stop_cmd`:

rtsx_stop_cmd
=============

.. c:function:: void rtsx_stop_cmd(struct rtsx_chip *chip, int card)

    stop command transfer and DMA transfer

    :param struct rtsx_chip \*chip:
        Realtek's card reader chip

    :param int card:
        flash card type

.. _`rtsx_stop_cmd.description`:

Description
-----------

Stop command transfer and DMA transfer.
This function is called in error handler.

.. This file was automatic generated / don't edit.

