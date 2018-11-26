.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/can/xilinx_can.c

.. _`xcan_priv`:

struct xcan_priv
================

.. c:type:: struct xcan_priv

    This definition define CAN driver instance

.. _`xcan_priv.definition`:

Definition
----------

.. code-block:: c

    struct xcan_priv {
        struct can_priv can;
        spinlock_t tx_lock;
        unsigned int tx_head;
        unsigned int tx_tail;
        unsigned int tx_max;
        struct napi_struct napi;
        u32 (*read_reg)(const struct xcan_priv *priv, enum xcan_reg reg);
        void (*write_reg)(const struct xcan_priv *priv, enum xcan_reg reg, u32 val);
        struct device *dev;
        void __iomem *reg_base;
        unsigned long irq_flags;
        struct clk *bus_clk;
        struct clk *can_clk;
        struct xcan_devtype_data devtype;
    }

.. _`xcan_priv.members`:

Members
-------

can
    CAN private data structure.

tx_lock
    Lock for synchronizing TX interrupt handling

tx_head
    Tx CAN packets ready to send on the queue

tx_tail
    Tx CAN packets successfully sended on the queue

tx_max
    Maximum number packets the driver can send

napi
    NAPI structure

read_reg
    For reading data from CAN registers

write_reg
    For writing data to CAN registers

dev
    Network device data structure

reg_base
    Ioremapped address to registers

irq_flags
    For \ :c:func:`request_irq`\ 

bus_clk
    Pointer to struct clk

can_clk
    Pointer to struct clk

devtype
    Device type specific constants

.. _`xcan_write_reg_le`:

xcan_write_reg_le
=================

.. c:function:: void xcan_write_reg_le(const struct xcan_priv *priv, enum xcan_reg reg, u32 val)

    Write a value to the device register little endian

    :param priv:
        Driver private data structure
    :type priv: const struct xcan_priv \*

    :param reg:
        Register offset
    :type reg: enum xcan_reg

    :param val:
        Value to write at the Register offset
    :type val: u32

.. _`xcan_write_reg_le.description`:

Description
-----------

Write data to the paricular CAN register

.. _`xcan_read_reg_le`:

xcan_read_reg_le
================

.. c:function:: u32 xcan_read_reg_le(const struct xcan_priv *priv, enum xcan_reg reg)

    Read a value from the device register little endian

    :param priv:
        Driver private data structure
    :type priv: const struct xcan_priv \*

    :param reg:
        Register offset
    :type reg: enum xcan_reg

.. _`xcan_read_reg_le.description`:

Description
-----------

Read data from the particular CAN register

.. _`xcan_read_reg_le.return`:

Return
------

value read from the CAN register

.. _`xcan_write_reg_be`:

xcan_write_reg_be
=================

.. c:function:: void xcan_write_reg_be(const struct xcan_priv *priv, enum xcan_reg reg, u32 val)

    Write a value to the device register big endian

    :param priv:
        Driver private data structure
    :type priv: const struct xcan_priv \*

    :param reg:
        Register offset
    :type reg: enum xcan_reg

    :param val:
        Value to write at the Register offset
    :type val: u32

.. _`xcan_write_reg_be.description`:

Description
-----------

Write data to the paricular CAN register

.. _`xcan_read_reg_be`:

xcan_read_reg_be
================

.. c:function:: u32 xcan_read_reg_be(const struct xcan_priv *priv, enum xcan_reg reg)

    Read a value from the device register big endian

    :param priv:
        Driver private data structure
    :type priv: const struct xcan_priv \*

    :param reg:
        Register offset
    :type reg: enum xcan_reg

.. _`xcan_read_reg_be.description`:

Description
-----------

Read data from the particular CAN register

.. _`xcan_read_reg_be.return`:

Return
------

value read from the CAN register

.. _`xcan_rx_int_mask`:

xcan_rx_int_mask
================

.. c:function:: u32 xcan_rx_int_mask(const struct xcan_priv *priv)

    Get the mask for the receive interrupt

    :param priv:
        Driver private data structure
    :type priv: const struct xcan_priv \*

.. _`xcan_rx_int_mask.return`:

Return
------

The receive interrupt mask used by the driver on this HW

.. _`set_reset_mode`:

set_reset_mode
==============

.. c:function:: int set_reset_mode(struct net_device *ndev)

    Resets the CAN device mode

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`set_reset_mode.description`:

Description
-----------

This is the driver reset mode routine.The driver
enters into configuration mode.

.. _`set_reset_mode.return`:

Return
------

0 on success and failure value on error

.. _`xcan_set_bittiming`:

xcan_set_bittiming
==================

.. c:function:: int xcan_set_bittiming(struct net_device *ndev)

    CAN set bit timing routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_set_bittiming.description`:

Description
-----------

This is the driver set bittiming  routine.

.. _`xcan_set_bittiming.return`:

Return
------

0 on success and failure value on error

.. _`xcan_chip_start`:

xcan_chip_start
===============

.. c:function:: int xcan_chip_start(struct net_device *ndev)

    This the drivers start routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_chip_start.description`:

Description
-----------

This is the drivers start routine.
Based on the State of the CAN device it puts
the CAN device into a proper mode.

.. _`xcan_chip_start.return`:

Return
------

0 on success and failure value on error

.. _`xcan_do_set_mode`:

xcan_do_set_mode
================

.. c:function:: int xcan_do_set_mode(struct net_device *ndev, enum can_mode mode)

    This sets the mode of the driver

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

    :param mode:
        Tells the mode of the driver
    :type mode: enum can_mode

.. _`xcan_do_set_mode.description`:

Description
-----------

This check the drivers state and calls the
the corresponding modes to set.

.. _`xcan_do_set_mode.return`:

Return
------

0 on success and failure value on error

.. _`xcan_write_frame`:

xcan_write_frame
================

.. c:function:: void xcan_write_frame(struct xcan_priv *priv, struct sk_buff *skb, int frame_offset)

    Write a frame to HW

    :param priv:
        *undescribed*
    :type priv: struct xcan_priv \*

    :param skb:
        sk_buff pointer that contains data to be Txed
    :type skb: struct sk_buff \*

    :param frame_offset:
        Register offset to write the frame to
    :type frame_offset: int

.. _`xcan_start_xmit_fifo`:

xcan_start_xmit_fifo
====================

.. c:function:: int xcan_start_xmit_fifo(struct sk_buff *skb, struct net_device *ndev)

    Starts the transmission (FIFO mode)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`xcan_start_xmit_fifo.return`:

Return
------

0 on success, -ENOSPC if FIFO is full.

.. _`xcan_start_xmit_mailbox`:

xcan_start_xmit_mailbox
=======================

.. c:function:: int xcan_start_xmit_mailbox(struct sk_buff *skb, struct net_device *ndev)

    Starts the transmission (mailbox mode)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`xcan_start_xmit_mailbox.return`:

Return
------

0 on success, -ENOSPC if there is no space

.. _`xcan_start_xmit`:

xcan_start_xmit
===============

.. c:function:: int xcan_start_xmit(struct sk_buff *skb, struct net_device *ndev)

    Starts the transmission

    :param skb:
        sk_buff pointer that contains data to be Txed
    :type skb: struct sk_buff \*

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_start_xmit.description`:

Description
-----------

This function is invoked from upper layers to initiate transmission.

.. _`xcan_start_xmit.return`:

Return
------

NETDEV_TX_OK on success and NETDEV_TX_BUSY when the tx queue is full

.. _`xcan_rx`:

xcan_rx
=======

.. c:function:: int xcan_rx(struct net_device *ndev, int frame_base)

    Is called from CAN isr to complete the received frame  processing

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

    :param frame_base:
        Register offset to the frame to be read
    :type frame_base: int

.. _`xcan_rx.description`:

Description
-----------

This function is invoked from the CAN isr(poll) to process the Rx frames. It
does minimal processing and invokes "netif_receive_skb" to complete further
processing.

.. _`xcan_rx.return`:

Return
------

1 on success and 0 on failure.

.. _`xcan_current_error_state`:

xcan_current_error_state
========================

.. c:function:: enum can_state xcan_current_error_state(struct net_device *ndev)

    Get current error state from HW

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_current_error_state.description`:

Description
-----------

Checks the current CAN error state from the HW. Note that this
only checks for ERROR_PASSIVE and ERROR_WARNING.

.. _`xcan_current_error_state.return`:

Return
------

ERROR_PASSIVE or ERROR_WARNING if either is active, ERROR_ACTIVE
otherwise.

.. _`xcan_set_error_state`:

xcan_set_error_state
====================

.. c:function:: void xcan_set_error_state(struct net_device *ndev, enum can_state new_state, struct can_frame *cf)

    Set new CAN error state

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

    :param new_state:
        The new CAN state to be set
    :type new_state: enum can_state

    :param cf:
        Error frame to be populated or NULL
    :type cf: struct can_frame \*

.. _`xcan_set_error_state.description`:

Description
-----------

Set new CAN error state for the device, updating statistics and
populating the error frame if given.

.. _`xcan_update_error_state_after_rxtx`:

xcan_update_error_state_after_rxtx
==================================

.. c:function:: void xcan_update_error_state_after_rxtx(struct net_device *ndev)

    Update CAN error state after RX/TX

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_update_error_state_after_rxtx.description`:

Description
-----------

If the device is in a ERROR-WARNING or ERROR-PASSIVE state, check if
the performed RX/TX has caused it to drop to a lesser state and set
the interface state accordingly.

.. _`xcan_err_interrupt`:

xcan_err_interrupt
==================

.. c:function:: void xcan_err_interrupt(struct net_device *ndev, u32 isr)

    error frame Isr

    :param ndev:
        net_device pointer
    :type ndev: struct net_device \*

    :param isr:
        interrupt status register value
    :type isr: u32

.. _`xcan_err_interrupt.description`:

Description
-----------

This is the CAN error interrupt and it will
check the the type of error and forward the error
frame to upper layers.

.. _`xcan_state_interrupt`:

xcan_state_interrupt
====================

.. c:function:: void xcan_state_interrupt(struct net_device *ndev, u32 isr)

    It will check the state of the CAN device

    :param ndev:
        net_device pointer
    :type ndev: struct net_device \*

    :param isr:
        interrupt status register value
    :type isr: u32

.. _`xcan_state_interrupt.description`:

Description
-----------

This will checks the state of the CAN device
and puts the device into appropriate state.

.. _`xcan_rx_fifo_get_next_frame`:

xcan_rx_fifo_get_next_frame
===========================

.. c:function:: int xcan_rx_fifo_get_next_frame(struct xcan_priv *priv)

    Get register offset of next RX frame

    :param priv:
        *undescribed*
    :type priv: struct xcan_priv \*

.. _`xcan_rx_fifo_get_next_frame.return`:

Return
------

Register offset of the next frame in RX FIFO.

.. _`xcan_rx_poll`:

xcan_rx_poll
============

.. c:function:: int xcan_rx_poll(struct napi_struct *napi, int quota)

    Poll routine for rx packets (NAPI)

    :param napi:
        napi structure pointer
    :type napi: struct napi_struct \*

    :param quota:
        Max number of rx packets to be processed.
    :type quota: int

.. _`xcan_rx_poll.description`:

Description
-----------

This is the poll routine for rx part.
It will process the packets maximux quota value.

.. _`xcan_rx_poll.return`:

Return
------

number of packets received

.. _`xcan_tx_interrupt`:

xcan_tx_interrupt
=================

.. c:function:: void xcan_tx_interrupt(struct net_device *ndev, u32 isr)

    Tx Done Isr

    :param ndev:
        net_device pointer
    :type ndev: struct net_device \*

    :param isr:
        Interrupt status register value
    :type isr: u32

.. _`xcan_interrupt`:

xcan_interrupt
==============

.. c:function:: irqreturn_t xcan_interrupt(int irq, void *dev_id)

    CAN Isr

    :param irq:
        irq number
    :type irq: int

    :param dev_id:
        device id poniter
    :type dev_id: void \*

.. _`xcan_interrupt.description`:

Description
-----------

This is the xilinx CAN Isr. It checks for the type of interrupt
and invokes the corresponding ISR.

.. _`xcan_interrupt.return`:

Return
------

IRQ_NONE - If CAN device is in sleep mode, IRQ_HANDLED otherwise

.. _`xcan_chip_stop`:

xcan_chip_stop
==============

.. c:function:: void xcan_chip_stop(struct net_device *ndev)

    Driver stop routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_chip_stop.description`:

Description
-----------

This is the drivers stop routine. It will disable the
interrupts and put the device into configuration mode.

.. _`xcan_open`:

xcan_open
=========

.. c:function:: int xcan_open(struct net_device *ndev)

    Driver open routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_open.description`:

Description
-----------

This is the driver open routine.

.. _`xcan_open.return`:

Return
------

0 on success and failure value on error

.. _`xcan_close`:

xcan_close
==========

.. c:function:: int xcan_close(struct net_device *ndev)

    Driver close routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: struct net_device \*

.. _`xcan_close.return`:

Return
------

0 always

.. _`xcan_get_berr_counter`:

xcan_get_berr_counter
=====================

.. c:function:: int xcan_get_berr_counter(const struct net_device *ndev, struct can_berr_counter *bec)

    error counter routine

    :param ndev:
        Pointer to net_device structure
    :type ndev: const struct net_device \*

    :param bec:
        Pointer to can_berr_counter structure
    :type bec: struct can_berr_counter \*

.. _`xcan_get_berr_counter.description`:

Description
-----------

This is the driver error counter routine.

.. _`xcan_get_berr_counter.return`:

Return
------

0 on success and failure value on error

.. _`xcan_suspend`:

xcan_suspend
============

.. c:function:: int __maybe_unused xcan_suspend(struct device *dev)

    Suspend method for the driver

    :param dev:
        Address of the device structure
    :type dev: struct device \*

.. _`xcan_suspend.description`:

Description
-----------

Put the driver into low power mode.

.. _`xcan_suspend.return`:

Return
------

0 on success and failure value on error

.. _`xcan_resume`:

xcan_resume
===========

.. c:function:: int __maybe_unused xcan_resume(struct device *dev)

    Resume from suspend

    :param dev:
        Address of the device structure
    :type dev: struct device \*

.. _`xcan_resume.description`:

Description
-----------

Resume operation after suspend.

.. _`xcan_resume.return`:

Return
------

0 on success and failure value on error

.. _`xcan_runtime_suspend`:

xcan_runtime_suspend
====================

.. c:function:: int __maybe_unused xcan_runtime_suspend(struct device *dev)

    Runtime suspend method for the driver

    :param dev:
        Address of the device structure
    :type dev: struct device \*

.. _`xcan_runtime_suspend.description`:

Description
-----------

Put the driver into low power mode.

.. _`xcan_runtime_suspend.return`:

Return
------

0 always

.. _`xcan_runtime_resume`:

xcan_runtime_resume
===================

.. c:function:: int __maybe_unused xcan_runtime_resume(struct device *dev)

    Runtime resume from suspend

    :param dev:
        Address of the device structure
    :type dev: struct device \*

.. _`xcan_runtime_resume.description`:

Description
-----------

Resume operation after suspend.

.. _`xcan_runtime_resume.return`:

Return
------

0 on success and failure value on error

.. _`xcan_probe`:

xcan_probe
==========

.. c:function:: int xcan_probe(struct platform_device *pdev)

    Platform registration call

    :param pdev:
        Handle to the platform device structure
    :type pdev: struct platform_device \*

.. _`xcan_probe.description`:

Description
-----------

This function does all the memory allocation and registration for the CAN
device.

.. _`xcan_probe.return`:

Return
------

0 on success and failure value on error

.. _`xcan_remove`:

xcan_remove
===========

.. c:function:: int xcan_remove(struct platform_device *pdev)

    Unregister the device after releasing the resources

    :param pdev:
        Handle to the platform device structure
    :type pdev: struct platform_device \*

.. _`xcan_remove.description`:

Description
-----------

This function frees all the resources allocated to the device.

.. _`xcan_remove.return`:

Return
------

0 always

.. This file was automatic generated / don't edit.

