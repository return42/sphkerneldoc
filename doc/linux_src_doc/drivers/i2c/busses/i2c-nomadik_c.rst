.. -*- coding: utf-8; mode: rst -*-

=============
i2c-nomadik.c
=============


.. _`i2c_vendor_data`:

struct i2c_vendor_data
======================

.. c:type:: i2c_vendor_data

    per-vendor variations


.. _`i2c_vendor_data.definition`:

Definition
----------

.. code-block:: c

  struct i2c_vendor_data {
    bool has_mtdws;
    u32 fifodepth;
  };


.. _`i2c_vendor_data.members`:

Members
-------

:``has_mtdws``:
    variant has the MTDWS bit

:``fifodepth``:
    variant FIFO depth




.. _`i2c_nmk_client`:

struct i2c_nmk_client
=====================

.. c:type:: i2c_nmk_client

    client specific data


.. _`i2c_nmk_client.definition`:

Definition
----------

.. code-block:: c

  struct i2c_nmk_client {
    unsigned short slave_adr;
    unsigned long count;
    unsigned char * buffer;
    unsigned long xfer_bytes;
    enum i2c_operation operation;
  };


.. _`i2c_nmk_client.members`:

Members
-------

:``slave_adr``:
    7-bit slave address

:``count``:
    no. bytes to be transferred

:``buffer``:
    client data buffer

:``xfer_bytes``:
    bytes transferred till now

:``operation``:
    current I2C operation




.. _`nmk_i2c_dev`:

struct nmk_i2c_dev
==================

.. c:type:: nmk_i2c_dev

    private data structure of the controller.


.. _`nmk_i2c_dev.definition`:

Definition
----------

.. code-block:: c

  struct nmk_i2c_dev {
    struct i2c_vendor_data * vendor;
    struct amba_device * adev;
    struct i2c_adapter adap;
    int irq;
    void __iomem * virtbase;
    struct clk * clk;
    struct i2c_nmk_client cli;
    u32 clk_freq;
    unsigned char tft;
    unsigned char rft;
    enum i2c_freq_mode sm;
    int stop;
    struct completion xfer_complete;
    int result;
  };


.. _`nmk_i2c_dev.members`:

Members
-------

:``vendor``:
    vendor data for this variant.

:``adev``:
    parent amba device.

:``adap``:
    corresponding I2C adapter.

:``irq``:
    interrupt line for the controller.

:``virtbase``:
    virtual io memory area.

:``clk``:
    hardware i2c block clock.

:``cli``:
    holder of client specific data.

:``clk_freq``:
    clock frequency for the operation mode

:``tft``:
    Tx FIFO Threshold in bytes

:``rft``:
    Rx FIFO Threshold in bytes
    ``timeout`` Slave response timeout (ms)

:``sm``:
    speed mode

:``stop``:
    stop condition.

:``xfer_complete``:
    acknowledge completion for a I2C message.

:``result``:
    controller propogated result.




.. _`flush_i2c_fifo`:

flush_i2c_fifo
==============

.. c:function:: int flush_i2c_fifo (struct nmk_i2c_dev *dev)

    This function flushes the I2C FIFO

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver



.. _`flush_i2c_fifo.description`:

Description
-----------

This function flushes the I2C Tx and Rx FIFOs. It returns
0 on successful flushing of FIFO



.. _`disable_all_interrupts`:

disable_all_interrupts
======================

.. c:function:: void disable_all_interrupts (struct nmk_i2c_dev *dev)

    Disable all interrupts of this I2c Bus

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver



.. _`clear_all_interrupts`:

clear_all_interrupts
====================

.. c:function:: void clear_all_interrupts (struct nmk_i2c_dev *dev)

    Clear all interrupts of I2C Controller

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver



.. _`init_hw`:

init_hw
=======

.. c:function:: int init_hw (struct nmk_i2c_dev *dev)

    initialize the I2C hardware

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver



.. _`load_i2c_mcr_reg`:

load_i2c_mcr_reg
================

.. c:function:: u32 load_i2c_mcr_reg (struct nmk_i2c_dev *dev, u16 flags)

    load the MCR register

    :param struct nmk_i2c_dev \*dev:
        private data of controller

    :param u16 flags:
        message flags



.. _`setup_i2c_controller`:

setup_i2c_controller
====================

.. c:function:: void setup_i2c_controller (struct nmk_i2c_dev *dev)

    setup the controller

    :param struct nmk_i2c_dev \*dev:
        private data of controller



.. _`read_i2c`:

read_i2c
========

.. c:function:: int read_i2c (struct nmk_i2c_dev *dev, u16 flags)

    Read from I2C client device

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver

    :param u16 flags:
        message flags



.. _`read_i2c.description`:

Description
-----------

This function reads from i2c client device when controller is in
master mode. There is a completion timeout. If there is no transfer
before timeout error is returned.



.. _`write_i2c`:

write_i2c
=========

.. c:function:: int write_i2c (struct nmk_i2c_dev *dev, u16 flags)

    Write data to I2C client.

    :param struct nmk_i2c_dev \*dev:
        private data of I2C Driver

    :param u16 flags:
        message flags



.. _`write_i2c.description`:

Description
-----------

This function writes data to I2C client



.. _`nmk_i2c_xfer_one`:

nmk_i2c_xfer_one
================

.. c:function:: int nmk_i2c_xfer_one (struct nmk_i2c_dev *dev, u16 flags)

    transmit a single I2C message

    :param struct nmk_i2c_dev \*dev:
        device with a message encoded into it

    :param u16 flags:
        message flags



.. _`nmk_i2c_xfer`:

nmk_i2c_xfer
============

.. c:function:: int nmk_i2c_xfer (struct i2c_adapter *i2c_adap, struct i2c_msg msgs[], int num_msgs)

    I2C transfer function used by kernel framework

    :param struct i2c_adapter \*i2c_adap:
        Adapter pointer to the controller

    :param struct i2c_msg msgs:
        Pointer to data to be written.

    :param int num_msgs:
        Number of messages to be executed



.. _`nmk_i2c_xfer.description`:

Description
-----------

This is the function called by the generic kernel :c:func:`i2c_transfer`
or i2c_smbus...() API calls. Note that this code is protected by the
semaphore set in the kernel :c:func:`i2c_transfer` function.



.. _`nmk_i2c_xfer.read-transfer`:

READ TRANSFER 
--------------

We impose a restriction of the first message to be the
index message for any read transaction.
- a no index is coded as '0',
- 2byte big endian index is coded as '3'
!!! msg[0].buf holds the actual index.
This is compatible with generic messages of smbus emulator
that send a one byte index.
eg. a I2C transation to read 2 bytes from index 0
idx = 0;
msg[0].addr = client->addr;
msg[0].flags = 0x0;
msg[0].len = 1;
msg[0].buf = :c:type:`struct idx <idx>`;

msg[1].addr = client->addr;
msg[1].flags = I2C_M_RD;
msg[1].len = 2;
msg[1].buf = rd_buff
i2c_transfer(adap, msg, 2);



.. _`nmk_i2c_xfer.write-transfer`:

WRITE TRANSFER 
---------------

The I2C standard interface interprets all data as payload.
If you want to emulate an SMBUS write transaction put the
index as first byte(or first and second) in the payload.
eg. a I2C transation to write 2 bytes from index 1
wr_buff[0] = 0x1;
wr_buff[1] = 0x23;
wr_buff[2] = 0x46;
msg[0].flags = 0x0;
msg[0].len = 3;
msg[0].buf = wr_buff;
i2c_transfer(adap, msg, 1);

To read or write a block of data (multiple bytes) using SMBUS emulation
please use the :c:func:`i2c_smbus_read_i2c_block_data`
or :c:func:`i2c_smbus_write_i2c_block_data` API



.. _`disable_interrupts`:

disable_interrupts
==================

.. c:function:: int disable_interrupts (struct nmk_i2c_dev *dev, u32 irq)

    disable the interrupts

    :param struct nmk_i2c_dev \*dev:
        private data of controller

    :param u32 irq:
        interrupt number



.. _`i2c_irq_handler`:

i2c_irq_handler
===============

.. c:function:: irqreturn_t i2c_irq_handler (int irq, void *arg)

    interrupt routine

    :param int irq:
        interrupt number

    :param void \*arg:
        data passed to the handler



.. _`i2c_irq_handler.description`:

Description
-----------

This is the interrupt handler for the i2c driver. Currently
it handles the major interrupts like Rx & Tx FIFO management
interrupts, master transaction interrupts, arbitration and
bus error interrupts. The rest of the interrupts are treated as
unhandled.

