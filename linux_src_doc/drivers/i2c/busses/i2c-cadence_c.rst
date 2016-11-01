.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-cadence.c

.. _`cdns_i2c`:

struct cdns_i2c
===============

.. c:type:: struct cdns_i2c

    I2C device private data structure

.. _`cdns_i2c.definition`:

Definition
----------

.. code-block:: c

    struct cdns_i2c {
        struct device *dev;
        void __iomem *membase;
        struct i2c_adapter adap;
        struct i2c_msg *p_msg;
        int err_status;
        struct completion xfer_done;
        unsigned char *p_send_buf;
        unsigned char *p_recv_buf;
        unsigned int send_count;
        unsigned int recv_count;
        unsigned int curr_recv_count;
        int irq;
        unsigned long input_clk;
        unsigned int i2c_clk;
        unsigned int bus_hold_flag;
        struct clk *clk;
        struct notifier_block clk_rate_change_nb;
        u32 quirks;
    }

.. _`cdns_i2c.members`:

Members
-------

dev
    Pointer to device structure

membase
    Base address of the I2C device

adap
    I2C adapter instance

p_msg
    Message pointer

err_status
    Error status in Interrupt Status Register

xfer_done
    Transfer complete status

p_send_buf
    Pointer to transmit buffer

p_recv_buf
    Pointer to receive buffer

send_count
    Number of bytes still expected to send

recv_count
    Number of bytes still expected to receive

curr_recv_count
    Number of bytes to be received in current transfer

irq
    IRQ number

input_clk
    Input clock to I2C controller

i2c_clk
    Maximum I2C clock speed

bus_hold_flag
    Flag used in repeated start for clearing HOLD bit

clk
    Pointer to struct clk

clk_rate_change_nb
    Notifier block for clock rate changes

quirks
    flag for broken hold bit usage in r1p10

.. _`cdns_i2c_clear_bus_hold`:

cdns_i2c_clear_bus_hold
=======================

.. c:function:: void cdns_i2c_clear_bus_hold(struct cdns_i2c *id)

    Clear bus hold bit

    :param struct cdns_i2c \*id:
        Pointer to driver data struct

.. _`cdns_i2c_clear_bus_hold.description`:

Description
-----------

Helper to clear the controller's bus hold bit.

.. _`cdns_i2c_isr`:

cdns_i2c_isr
============

.. c:function:: irqreturn_t cdns_i2c_isr(int irq, void *ptr)

    Interrupt handler for the I2C device

    :param int irq:
        irq number for the I2C device

    :param void \*ptr:
        void pointer to cdns_i2c structure

.. _`cdns_i2c_isr.description`:

Description
-----------

This function handles the data interrupt, transfer complete interrupt and
the error interrupts of the I2C device.

.. _`cdns_i2c_isr.return`:

Return
------

IRQ_HANDLED always

.. _`cdns_i2c_mrecv`:

cdns_i2c_mrecv
==============

.. c:function:: void cdns_i2c_mrecv(struct cdns_i2c *id)

    Prepare and start a master receive operation

    :param struct cdns_i2c \*id:
        pointer to the i2c device structure

.. _`cdns_i2c_msend`:

cdns_i2c_msend
==============

.. c:function:: void cdns_i2c_msend(struct cdns_i2c *id)

    Prepare and start a master send operation

    :param struct cdns_i2c \*id:
        pointer to the i2c device

.. _`cdns_i2c_master_reset`:

cdns_i2c_master_reset
=====================

.. c:function:: void cdns_i2c_master_reset(struct i2c_adapter *adap)

    Reset the interface

    :param struct i2c_adapter \*adap:
        pointer to the i2c adapter driver instance

.. _`cdns_i2c_master_reset.description`:

Description
-----------

This function cleanup the fifos, clear the hold bit and status
and disable the interrupts.

.. _`cdns_i2c_master_xfer`:

cdns_i2c_master_xfer
====================

.. c:function:: int cdns_i2c_master_xfer(struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    The main i2c transfer function

    :param struct i2c_adapter \*adap:
        pointer to the i2c adapter driver instance

    :param struct i2c_msg \*msgs:
        pointer to the i2c message structure

    :param int num:
        the number of messages to transfer

.. _`cdns_i2c_master_xfer.description`:

Description
-----------

Initiates the send/recv activity based on the transfer message received.

.. _`cdns_i2c_master_xfer.return`:

Return
------

number of msgs processed on success, negative error otherwise

.. _`cdns_i2c_func`:

cdns_i2c_func
=============

.. c:function:: u32 cdns_i2c_func(struct i2c_adapter *adap)

    Returns the supported features of the I2C driver

    :param struct i2c_adapter \*adap:
        pointer to the i2c adapter structure

.. _`cdns_i2c_func.return`:

Return
------

32 bit value, each bit corresponding to a feature

.. _`cdns_i2c_calc_divs`:

cdns_i2c_calc_divs
==================

.. c:function:: int cdns_i2c_calc_divs(unsigned long *f, unsigned long input_clk, unsigned int *a, unsigned int *b)

    Calculate clock dividers

    :param unsigned long \*f:
        I2C clock frequency

    :param unsigned long input_clk:
        Input clock frequency

    :param unsigned int \*a:
        First divider (return value)

    :param unsigned int \*b:
        Second divider (return value)

.. _`cdns_i2c_calc_divs.description`:

Description
-----------

f is used as input and output variable. As input it is used as target I2C
frequency. On function exit f holds the actually resulting I2C frequency.

.. _`cdns_i2c_calc_divs.return`:

Return
------

0 on success, negative errno otherwise.

.. _`cdns_i2c_setclk`:

cdns_i2c_setclk
===============

.. c:function:: int cdns_i2c_setclk(unsigned long clk_in, struct cdns_i2c *id)

    This function sets the serial clock rate for the I2C device

    :param unsigned long clk_in:
        I2C clock input frequency in Hz

    :param struct cdns_i2c \*id:
        Pointer to the I2C device structure

.. _`cdns_i2c_setclk.description`:

Description
-----------

The device must be idle rather than busy transferring data before setting
these device options.
The data rate is set by values in the control register.
The formula for determining the correct register values is
Fscl = Fpclk/(22 x (divisor_a+1) x (divisor_b+1))
See the hardware data sheet for a full explanation of setting the serial
clock rate. The clock can not be faster than the input clock divide by 22.
The two most common clock rates are 100KHz and 400KHz.

.. _`cdns_i2c_setclk.return`:

Return
------

0 on success, negative error otherwise

.. _`cdns_i2c_clk_notifier_cb`:

cdns_i2c_clk_notifier_cb
========================

.. c:function:: int cdns_i2c_clk_notifier_cb(struct notifier_block *nb, unsigned long event, void *data)

    Clock rate change callback

    :param struct notifier_block \*nb:
        Pointer to notifier block

    :param unsigned long event:
        Notification reason

    :param void \*data:
        Pointer to notification data object

.. _`cdns_i2c_clk_notifier_cb.description`:

Description
-----------

This function is called when the cdns_i2c input clock frequency changes.
The callback checks whether a valid bus frequency can be generated after the
change. If so, the change is acknowledged, otherwise the change is aborted.
New dividers are written to the HW in the pre- or post change notification
depending on the scaling direction.

.. _`cdns_i2c_clk_notifier_cb.return`:

Return
------

NOTIFY_STOP if the rate change should be aborted, NOTIFY_OK
to acknowledge the change, NOTIFY_DONE if the notification is
considered irrelevant.

.. _`cdns_i2c_runtime_suspend`:

cdns_i2c_runtime_suspend
========================

.. c:function:: int __maybe_unused cdns_i2c_runtime_suspend(struct device *dev)

    Runtime suspend method for the driver

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cdns_i2c_runtime_suspend.description`:

Description
-----------

Put the driver into low power mode.

.. _`cdns_i2c_runtime_suspend.return`:

Return
------

0 always

.. _`cdns_i2c_runtime_resume`:

cdns_i2c_runtime_resume
=======================

.. c:function:: int __maybe_unused cdns_i2c_runtime_resume(struct device *dev)

    Runtime resume

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cdns_i2c_runtime_resume.description`:

Description
-----------

Runtime resume callback.

.. _`cdns_i2c_runtime_resume.return`:

Return
------

0 on success and error value on error

.. _`cdns_i2c_probe`:

cdns_i2c_probe
==============

.. c:function:: int cdns_i2c_probe(struct platform_device *pdev)

    Platform registration call

    :param struct platform_device \*pdev:
        Handle to the platform device structure

.. _`cdns_i2c_probe.description`:

Description
-----------

This function does all the memory allocation and registration for the i2c
device. User can modify the address mode to 10 bit address mode using the
ioctl call with option I2C_TENBIT.

.. _`cdns_i2c_probe.return`:

Return
------

0 on success, negative error otherwise

.. _`cdns_i2c_remove`:

cdns_i2c_remove
===============

.. c:function:: int cdns_i2c_remove(struct platform_device *pdev)

    Unregister the device after releasing the resources

    :param struct platform_device \*pdev:
        Handle to the platform device structure

.. _`cdns_i2c_remove.description`:

Description
-----------

This function frees all the resources allocated to the device.

.. _`cdns_i2c_remove.return`:

Return
------

0 always

.. This file was automatic generated / don't edit.

