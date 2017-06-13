.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-stm32f4.c

.. _`stm32f4_i2c_msg`:

struct stm32f4_i2c_msg
======================

.. c:type:: struct stm32f4_i2c_msg

    client specific data

.. _`stm32f4_i2c_msg.definition`:

Definition
----------

.. code-block:: c

    struct stm32f4_i2c_msg {
        u8 addr;
        u32 count;
        u8 *buf;
        int result;
        bool stop;
    }

.. _`stm32f4_i2c_msg.members`:

Members
-------

addr
    8-bit slave addr, including r/w bit

count
    number of bytes to be transferred

buf
    data buffer

result
    result of the transfer

stop
    last I2C msg to be sent, i.e. STOP to be generated

.. _`stm32f4_i2c_dev`:

struct stm32f4_i2c_dev
======================

.. c:type:: struct stm32f4_i2c_dev

    private data of the controller

.. _`stm32f4_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct stm32f4_i2c_dev {
        struct i2c_adapter adap;
        struct device *dev;
        void __iomem *base;
        struct completion complete;
        struct clk *clk;
        int speed;
        int parent_rate;
        struct stm32f4_i2c_msg msg;
    }

.. _`stm32f4_i2c_dev.members`:

Members
-------

adap
    I2C adapter for this controller

dev
    device for this controller

base
    virtual memory area

complete
    completion of I2C message

clk
    hw i2c clock

speed
    I2C clock frequency of the controller. Standard or Fast are supported

parent_rate
    I2C clock parent rate in MHz

msg
    I2C transfer information

.. _`stm32f4_i2c_hw_config`:

stm32f4_i2c_hw_config
=====================

.. c:function:: int stm32f4_i2c_hw_config(struct stm32f4_i2c_dev *i2c_dev)

    Prepare I2C block

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_write_byte`:

stm32f4_i2c_write_byte
======================

.. c:function:: void stm32f4_i2c_write_byte(struct stm32f4_i2c_dev *i2c_dev, u8 byte)

    Write a byte in the data register

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

    :param u8 byte:
        Data to write in the register

.. _`stm32f4_i2c_write_msg`:

stm32f4_i2c_write_msg
=====================

.. c:function:: void stm32f4_i2c_write_msg(struct stm32f4_i2c_dev *i2c_dev)

    Fill the data register in write mode

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_write_msg.description`:

Description
-----------

This function fills the data register with I2C transfer buffer

.. _`stm32f4_i2c_handle_write`:

stm32f4_i2c_handle_write
========================

.. c:function:: void stm32f4_i2c_handle_write(struct stm32f4_i2c_dev *i2c_dev)

    Handle FIFO empty interrupt in case of write

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_handle_read`:

stm32f4_i2c_handle_read
=======================

.. c:function:: void stm32f4_i2c_handle_read(struct stm32f4_i2c_dev *i2c_dev)

    Handle FIFO empty interrupt in case of read

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_handle_read.description`:

Description
-----------

This function is called when a new data is received in data register

.. _`stm32f4_i2c_handle_rx_done`:

stm32f4_i2c_handle_rx_done
==========================

.. c:function:: void stm32f4_i2c_handle_rx_done(struct stm32f4_i2c_dev *i2c_dev)

    Handle byte transfer finished interrupt in case of read

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_handle_rx_done.description`:

Description
-----------

This function is called when a new data is received in the shift register
but data register has not been read yet.

.. _`stm32f4_i2c_handle_rx_addr`:

stm32f4_i2c_handle_rx_addr
==========================

.. c:function:: void stm32f4_i2c_handle_rx_addr(struct stm32f4_i2c_dev *i2c_dev)

    Handle address matched interrupt in case of master receiver

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

.. _`stm32f4_i2c_isr_event`:

stm32f4_i2c_isr_event
=====================

.. c:function:: irqreturn_t stm32f4_i2c_isr_event(int irq, void *data)

    Interrupt routine for I2C bus event

    :param int irq:
        interrupt number

    :param void \*data:
        Controller's private data

.. _`stm32f4_i2c_isr_error`:

stm32f4_i2c_isr_error
=====================

.. c:function:: irqreturn_t stm32f4_i2c_isr_error(int irq, void *data)

    Interrupt routine for I2C bus error

    :param int irq:
        interrupt number

    :param void \*data:
        Controller's private data

.. _`stm32f4_i2c_xfer_msg`:

stm32f4_i2c_xfer_msg
====================

.. c:function:: int stm32f4_i2c_xfer_msg(struct stm32f4_i2c_dev *i2c_dev, struct i2c_msg *msg, bool is_first, bool is_last)

    Transfer a single I2C message

    :param struct stm32f4_i2c_dev \*i2c_dev:
        Controller's private data

    :param struct i2c_msg \*msg:
        I2C message to transfer

    :param bool is_first:
        first message of the sequence

    :param bool is_last:
        last message of the sequence

.. _`stm32f4_i2c_xfer`:

stm32f4_i2c_xfer
================

.. c:function:: int stm32f4_i2c_xfer(struct i2c_adapter *i2c_adap, struct i2c_msg msgs[], int num)

    Transfer combined I2C message

    :param struct i2c_adapter \*i2c_adap:
        Adapter pointer to the controller

    :param struct i2c_msg msgs:
        Pointer to data to be written.

    :param int num:
        Number of messages to be executed

.. This file was automatic generated / don't edit.

