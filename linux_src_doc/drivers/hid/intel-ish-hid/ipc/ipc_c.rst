.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ipc/ipc.c

.. _`ish_reg_read`:

ish_reg_read
============

.. c:function:: uint32_t ish_reg_read(const struct ishtp_device *dev, unsigned long offset)

    Read register

    :param dev:
        ISHTP device pointer
    :type dev: const struct ishtp_device \*

    :param offset:
        Register offset
    :type offset: unsigned long

.. _`ish_reg_read.description`:

Description
-----------

Read 32 bit register at a given offset

.. _`ish_reg_read.return`:

Return
------

Read register value

.. _`ish_reg_write`:

ish_reg_write
=============

.. c:function:: void ish_reg_write(struct ishtp_device *dev, unsigned long offset, uint32_t value)

    Write register

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

    :param offset:
        Register offset
    :type offset: unsigned long

    :param value:
        Value to write
    :type value: uint32_t

.. _`ish_reg_write.description`:

Description
-----------

Writes 32 bit register at a give offset

.. _`_ish_read_fw_sts_reg`:

\_ish_read_fw_sts_reg
=====================

.. c:function:: uint32_t _ish_read_fw_sts_reg(struct ishtp_device *dev)

    Read FW status register

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`_ish_read_fw_sts_reg.description`:

Description
-----------

Read FW status register

.. _`_ish_read_fw_sts_reg.return`:

Return
------

Read register value

.. _`check_generated_interrupt`:

check_generated_interrupt
=========================

.. c:function:: bool check_generated_interrupt(struct ishtp_device *dev)

    Check if ISH interrupt

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`check_generated_interrupt.description`:

Description
-----------

Check if an interrupt was generated for ISH

.. _`check_generated_interrupt.return`:

Return
------

Read true or false

.. _`ish_is_input_ready`:

ish_is_input_ready
==================

.. c:function:: bool ish_is_input_ready(struct ishtp_device *dev)

    Check if FW ready for RX

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`ish_is_input_ready.description`:

Description
-----------

Check if ISH FW is ready for receiving data

.. _`ish_is_input_ready.return`:

Return
------

Read true or false

.. _`set_host_ready`:

set_host_ready
==============

.. c:function:: void set_host_ready(struct ishtp_device *dev)

    Indicate host ready

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`set_host_ready.description`:

Description
-----------

Set host ready indication to FW

.. _`ishtp_fw_is_ready`:

ishtp_fw_is_ready
=================

.. c:function:: bool ishtp_fw_is_ready(struct ishtp_device *dev)

    Check if FW ready

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`ishtp_fw_is_ready.description`:

Description
-----------

Check if ISH FW is ready

.. _`ishtp_fw_is_ready.return`:

Return
------

Read true or false

.. _`ish_set_host_rdy`:

ish_set_host_rdy
================

.. c:function:: void ish_set_host_rdy(struct ishtp_device *dev)

    Indicate host ready

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`ish_set_host_rdy.description`:

Description
-----------

Set host ready indication to FW

.. _`ish_clr_host_rdy`:

ish_clr_host_rdy
================

.. c:function:: void ish_clr_host_rdy(struct ishtp_device *dev)

    Indicate host not ready

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`ish_clr_host_rdy.description`:

Description
-----------

Send host not ready indication to FW

.. _`_ishtp_read_hdr`:

\_ishtp_read_hdr
================

.. c:function:: uint32_t _ishtp_read_hdr(const struct ishtp_device *dev)

    Read message header

    :param dev:
        ISHTP device pointer
    :type dev: const struct ishtp_device \*

.. _`_ishtp_read_hdr.description`:

Description
-----------

Read header of 32bit length

.. _`_ishtp_read_hdr.return`:

Return
------

Read register value

.. _`_ishtp_read`:

\_ishtp_read
============

.. c:function:: int _ishtp_read(struct ishtp_device *dev, unsigned char *buffer, unsigned long buffer_length)

    Read message

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

    :param buffer:
        message buffer
    :type buffer: unsigned char \*

    :param buffer_length:
        length of message buffer
    :type buffer_length: unsigned long

.. _`_ishtp_read.description`:

Description
-----------

Read message from FW

.. _`_ishtp_read.return`:

Return
------

Always 0

.. _`write_ipc_from_queue`:

write_ipc_from_queue
====================

.. c:function:: int write_ipc_from_queue(struct ishtp_device *dev)

    try to write ipc msg from Tx queue to device

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`write_ipc_from_queue.description`:

Description
-----------

Check if DRBL is cleared. if it is - write the first IPC msg,  then call
the callback function (unless it's NULL)

.. _`write_ipc_from_queue.return`:

Return
------

0 for success else failure code

.. _`write_ipc_to_queue`:

write_ipc_to_queue
==================

.. c:function:: int write_ipc_to_queue(struct ishtp_device *dev, void (*ipc_send_compl)(void *), void *ipc_send_compl_prm, unsigned char *msg, int length)

    write ipc msg to Tx queue

    :param dev:
        ishtp device instance
    :type dev: struct ishtp_device \*

    :param void (\*ipc_send_compl)(void \*):
        Send complete callback

    :param ipc_send_compl_prm:
        Parameter to send in complete callback
    :type ipc_send_compl_prm: void \*

    :param msg:
        Pointer to message
    :type msg: unsigned char \*

    :param length:
        Length of message
    :type length: int

.. _`write_ipc_to_queue.description`:

Description
-----------

Recived msg with IPC (and upper protocol) header  and add it to the device
Tx-to-write list then try to send the first IPC waiting msg
(if DRBL is cleared)
This function returns negative value for failure (means free list
is empty, or msg too long) and 0 for success.

.. _`write_ipc_to_queue.return`:

Return
------

0 for success else failure code

.. _`ipc_send_mng_msg`:

ipc_send_mng_msg
================

.. c:function:: int ipc_send_mng_msg(struct ishtp_device *dev, uint32_t msg_code, void *msg, size_t size)

    Send management message

    :param dev:
        ishtp device instance
    :type dev: struct ishtp_device \*

    :param msg_code:
        Message code
    :type msg_code: uint32_t

    :param msg:
        Pointer to message
    :type msg: void \*

    :param size:
        Length of message
    :type size: size_t

.. _`ipc_send_mng_msg.description`:

Description
-----------

Send management message to FW

.. _`ipc_send_mng_msg.return`:

Return
------

0 for success else failure code

.. _`timed_wait_for_timeout`:

timed_wait_for_timeout
======================

.. c:function:: int timed_wait_for_timeout(struct ishtp_device *dev, int condition, unsigned int timeinc, unsigned int timeout)

    wait special event with timeout

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

    :param condition:
        indicate the condition for waiting
    :type condition: int

    :param timeinc:
        time slice for every wait cycle, in ms
    :type timeinc: unsigned int

    :param timeout:
        time in ms for timeout
    :type timeout: unsigned int

.. _`timed_wait_for_timeout.description`:

Description
-----------

This function will check special event to be ready in a loop, the loop
period is specificd in timeinc. Wait timeout will causes failure.

.. _`timed_wait_for_timeout.return`:

Return
------

0 for success else failure code

.. _`ish_fw_reset_handler`:

ish_fw_reset_handler
====================

.. c:function:: int ish_fw_reset_handler(struct ishtp_device *dev)

    FW reset handler

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`ish_fw_reset_handler.description`:

Description
-----------

Handle FW reset

.. _`ish_fw_reset_handler.return`:

Return
------

0 for success else failure code

.. _`fw_reset_work_fn`:

fw_reset_work_fn
================

.. c:function:: void fw_reset_work_fn(struct work_struct *unused)

    FW reset worker function

    :param unused:
        not used
    :type unused: struct work_struct \*

.. _`fw_reset_work_fn.description`:

Description
-----------

Call ish_fw_reset_handler to complete FW reset

.. _`_ish_sync_fw_clock`:

\_ish_sync_fw_clock
===================

.. c:function:: void _ish_sync_fw_clock(struct ishtp_device *dev)

    Sync FW clock with the OS clock

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`_ish_sync_fw_clock.description`:

Description
-----------

Sync FW and OS time

.. _`recv_ipc`:

recv_ipc
========

.. c:function:: void recv_ipc(struct ishtp_device *dev, uint32_t doorbell_val)

    Receive and process IPC management messages

    :param dev:
        ishtp device instance
    :type dev: struct ishtp_device \*

    :param doorbell_val:
        doorbell value
    :type doorbell_val: uint32_t

.. _`recv_ipc.description`:

Description
-----------

This function runs in ISR context.

.. _`recv_ipc.note`:

NOTE
----

Any other mng command than reset_notify and reset_notify_ack
won't wake BH handler

.. _`ish_irq_handler`:

ish_irq_handler
===============

.. c:function:: irqreturn_t ish_irq_handler(int irq, void *dev_id)

    ISH IRQ handler

    :param irq:
        irq number
    :type irq: int

    :param dev_id:
        ishtp device pointer
    :type dev_id: void \*

.. _`ish_irq_handler.description`:

Description
-----------

ISH IRQ handler. If interrupt is generated and is for ISH it will process
the interrupt.

.. _`ish_disable_dma`:

ish_disable_dma
===============

.. c:function:: int ish_disable_dma(struct ishtp_device *dev)

    disable dma communication between host and ISHFW

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`ish_disable_dma.description`:

Description
-----------

Clear the dma enable bit and wait for dma inactive.

.. _`ish_disable_dma.return`:

Return
------

0 for success else error code.

.. _`ish_wakeup`:

ish_wakeup
==========

.. c:function:: void ish_wakeup(struct ishtp_device *dev)

    wakeup ishfw from waiting-for-host state

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`ish_wakeup.description`:

Description
-----------

Set the dma enable bit and send a void message to FW,
it wil wakeup FW from waiting-for-host state.

.. _`_ish_hw_reset`:

\_ish_hw_reset
==============

.. c:function:: int _ish_hw_reset(struct ishtp_device *dev)

    HW reset

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`_ish_hw_reset.description`:

Description
-----------

Reset ISH HW to recover if any error

.. _`_ish_hw_reset.return`:

Return
------

0 for success else error fault code

.. _`_ish_ipc_reset`:

\_ish_ipc_reset
===============

.. c:function:: int _ish_ipc_reset(struct ishtp_device *dev)

    IPC reset

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`_ish_ipc_reset.description`:

Description
-----------

Resets host and fw IPC and upper layers

.. _`_ish_ipc_reset.return`:

Return
------

0 for success else error fault code

.. _`ish_hw_start`:

ish_hw_start
============

.. c:function:: int ish_hw_start(struct ishtp_device *dev)

    Start ISH HW

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

.. _`ish_hw_start.description`:

Description
-----------

Set host to ready state and wait for FW reset

.. _`ish_hw_start.return`:

Return
------

0 for success else error fault code

.. _`ish_ipc_get_header`:

ish_ipc_get_header
==================

.. c:function:: uint32_t ish_ipc_get_header(struct ishtp_device *dev, int length, int busy)

    Get doorbell value

    :param dev:
        ishtp device pointer
    :type dev: struct ishtp_device \*

    :param length:
        length of message
    :type length: int

    :param busy:
        busy status
    :type busy: int

.. _`ish_ipc_get_header.description`:

Description
-----------

Get door bell value from message header

.. _`ish_ipc_get_header.return`:

Return
------

door bell value

.. _`ish_dev_init`:

ish_dev_init
============

.. c:function:: struct ishtp_device *ish_dev_init(struct pci_dev *pdev)

    Initialize ISH devoce

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`ish_dev_init.description`:

Description
-----------

Allocate ISHTP device and initialize IPC processing

.. _`ish_dev_init.return`:

Return
------

ISHTP device instance on success else NULL

.. _`ish_device_disable`:

ish_device_disable
==================

.. c:function:: void ish_device_disable(struct ishtp_device *dev)

    Disable ISH device

    :param dev:
        ISHTP device pointer
    :type dev: struct ishtp_device \*

.. _`ish_device_disable.description`:

Description
-----------

Disable ISH by clearing host ready to inform firmware.

.. This file was automatic generated / don't edit.

