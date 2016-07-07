.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/adc/ad7606_ring.c

.. _`ad7606_trigger_handler_th_bh`:

ad7606_trigger_handler_th_bh
============================

.. c:function:: irqreturn_t ad7606_trigger_handler_th_bh(int irq, void *p)

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

.. _`ad7606_poll_bh_to_ring`:

ad7606_poll_bh_to_ring
======================

.. c:function:: void ad7606_poll_bh_to_ring(struct work_struct *work_s)

    :param struct work_struct \*work_s:
        the work struct through which this was scheduled

.. _`ad7606_poll_bh_to_ring.description`:

Description
-----------

Currently there is no option in this driver to disable the saving of
timestamps within the ring.
I think the one copy of this at a time was to avoid problems if the
trigger was set far too high and the reads then locked up the computer.

.. This file was automatic generated / don't edit.

