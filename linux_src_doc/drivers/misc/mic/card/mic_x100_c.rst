.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/card/mic_x100.c

.. _`mic_read_spad`:

mic_read_spad
=============

.. c:function:: u32 mic_read_spad(struct mic_device *mdev, unsigned int idx)

    read from the scratchpad register

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        index to scratchpad register, 0 based
    :type idx: unsigned int

.. _`mic_read_spad.description`:

Description
-----------

This function allows reading of the 32bit scratchpad register.

.. _`mic_read_spad.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_send_intr`:

mic_send_intr
=============

.. c:function:: void mic_send_intr(struct mic_device *mdev, int doorbell)

    Send interrupt to Host.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param doorbell:
        Doorbell number.
    :type doorbell: int

.. _`mic_ack_interrupt`:

mic_ack_interrupt
=================

.. c:function:: u32 mic_ack_interrupt(struct mic_device *mdev)

    Device specific interrupt handling.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_ack_interrupt.return`:

Return
------

bitmask of doorbell events triggered.

.. _`mic_hw_intr_init`:

mic_hw_intr_init
================

.. c:function:: void mic_hw_intr_init(struct mic_driver *mdrv)

    Initialize h/w specific interrupt information.

    :param mdrv:
        pointer to mic_driver
    :type mdrv: struct mic_driver \*

.. _`mic_db_to_irq`:

mic_db_to_irq
=============

.. c:function:: int mic_db_to_irq(struct mic_driver *mdrv, int db)

    Retrieve irq number corresponding to a doorbell.

    :param mdrv:
        pointer to mic_driver
    :type mdrv: struct mic_driver \*

    :param db:
        The doorbell obtained for which the irq is needed. Doorbell
        may correspond to an sbox doorbell or an rdmasr index.
    :type db: int

.. _`mic_db_to_irq.description`:

Description
-----------

Returns the irq corresponding to the doorbell.

.. This file was automatic generated / don't edit.

