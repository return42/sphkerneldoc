.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/hdm-i2c/hdm_i2c.c

.. _`list_first_mbo`:

list_first_mbo
==============

.. c:function::  list_first_mbo( ptr)

    get the first mbo from a list

    :param  ptr:
        the list head to take the mbo from.

.. _`configure_channel`:

configure_channel
=================

.. c:function:: int configure_channel(struct most_interface *most_iface, int ch_idx, struct most_channel_config *channel_config)

    called from MOST core to configure a channel

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

    :param struct most_channel_config \*channel_config:
        structure that holds the configuration information

.. _`configure_channel.description`:

Description
-----------

Return 0 on success, negative on failure.

Receives configuration information from MOST core and initialize the
corresponding channel.

.. _`enqueue`:

enqueue
=======

.. c:function:: int enqueue(struct most_interface *most_iface, int ch_idx, struct mbo *mbo)

    called from MOST core to enqueue a buffer for data transfer

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

    :param struct mbo \*mbo:
        pointer to the buffer object

.. _`enqueue.description`:

Description
-----------

Return 0 on success, negative on failure.

Transmit the data over I2C if it is a "write" request or push the buffer into
list if it is an "read" request

.. _`poison_channel`:

poison_channel
==============

.. c:function:: int poison_channel(struct most_interface *most_iface, int ch_idx)

    called from MOST core to poison buffers of a channel

    :param struct most_interface \*most_iface:
        *undescribed*

    :param int ch_idx:
        *undescribed*

.. _`poison_channel.description`:

Description
-----------

Return 0 on success, negative on failure.

If channel direction is RX, complete the buffers in list with
status MBO_E_CLOSE

.. _`pending_rx_work`:

pending_rx_work
===============

.. c:function:: void pending_rx_work(struct work_struct *work)

    Read pending messages through I2C

    :param struct work_struct \*work:
        definition of this work item

.. _`pending_rx_work.description`:

Description
-----------

Invoked by the Interrupt Service Routine, \ :c:func:`most_irq_handler`\ 

.. This file was automatic generated / don't edit.

