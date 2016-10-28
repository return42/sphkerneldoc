.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-st.c

.. _`st_i2c_timings`:

struct st_i2c_timings
=====================

.. c:type:: struct st_i2c_timings

    per-Mode tuning parameters

.. _`st_i2c_timings.definition`:

Definition
----------

.. code-block:: c

    struct st_i2c_timings {
        u32 rate;
        u32 rep_start_hold;
        u32 rep_start_setup;
        u32 start_hold;
        u32 data_setup_time;
        u32 stop_setup_time;
        u32 bus_free_time;
        u32 sda_pulse_min_limit;
    }

.. _`st_i2c_timings.members`:

Members
-------

rate
    I2C bus rate

rep_start_hold
    I2C repeated start hold time requirement

rep_start_setup
    I2C repeated start set up time requirement

start_hold
    I2C start hold time requirement

data_setup_time
    I2C data set up time requirement

stop_setup_time
    I2C stop set up time requirement

bus_free_time
    I2C bus free time requirement

sda_pulse_min_limit
    I2C SDA pulse mini width limit

.. _`st_i2c_client`:

struct st_i2c_client
====================

.. c:type:: struct st_i2c_client

    client specific data

.. _`st_i2c_client.definition`:

Definition
----------

.. code-block:: c

    struct st_i2c_client {
        u8 addr;
        u32 count;
        u32 xfered;
        u8 *buf;
        int result;
        bool stop;
    }

.. _`st_i2c_client.members`:

Members
-------

addr
    8-bit slave addr, including r/w bit

count
    number of bytes to be transfered

xfered
    number of bytes already transferred

buf
    data buffer

result
    result of the transfer

stop
    last I2C msg to be sent, i.e. STOP to be generated

.. _`st_i2c_dev`:

struct st_i2c_dev
=================

.. c:type:: struct st_i2c_dev

    private data of the controller

.. _`st_i2c_dev.definition`:

Definition
----------

.. code-block:: c

    struct st_i2c_dev {
        struct i2c_adapter adap;
        struct device *dev;
        void __iomem *base;
        struct completion complete;
        int irq;
        struct clk *clk;
        int mode;
        u32 scl_min_width_us;
        u32 sda_min_width_us;
        struct st_i2c_client client;
        bool busy;
    }

.. _`st_i2c_dev.members`:

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

irq
    interrupt line for th controller

clk
    hw ssc block clock

mode
    I2C mode of the controller. Standard or Fast only supported

scl_min_width_us
    SCL line minimum pulse width in us

sda_min_width_us
    SDA line minimum pulse width in us

client
    I2C transfert information

busy
    I2C transfer on-going

.. _`st_i2c_hw_config`:

st_i2c_hw_config
================

.. c:function:: void st_i2c_hw_config(struct st_i2c_dev *i2c_dev)

    Prepare SSC block, calculate and apply tuning timings

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

.. _`st_i2c_write_tx_fifo`:

st_i2c_write_tx_fifo
====================

.. c:function:: void st_i2c_write_tx_fifo(struct st_i2c_dev *i2c_dev, u8 byte)

    Write a byte in the Tx FIFO

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

    :param u8 byte:
        Data to write in the Tx FIFO

.. _`st_i2c_wr_fill_tx_fifo`:

st_i2c_wr_fill_tx_fifo
======================

.. c:function:: void st_i2c_wr_fill_tx_fifo(struct st_i2c_dev *i2c_dev)

    Fill the Tx FIFO in write mode

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

.. _`st_i2c_wr_fill_tx_fifo.description`:

Description
-----------

This functions fills the Tx FIFO with I2C transfert buffer when
in write mode.

.. _`st_i2c_rd_fill_tx_fifo`:

st_i2c_rd_fill_tx_fifo
======================

.. c:function:: void st_i2c_rd_fill_tx_fifo(struct st_i2c_dev *i2c_dev, int max)

    Fill the Tx FIFO in read mode

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

    :param int max:
        *undescribed*

.. _`st_i2c_rd_fill_tx_fifo.description`:

Description
-----------

This functions fills the Tx FIFO with fixed pattern when
in read mode to trigger clock.

.. _`st_i2c_terminate_xfer`:

st_i2c_terminate_xfer
=====================

.. c:function:: void st_i2c_terminate_xfer(struct st_i2c_dev *i2c_dev)

    Send either STOP or REPSTART condition

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

.. _`st_i2c_handle_write`:

st_i2c_handle_write
===================

.. c:function:: void st_i2c_handle_write(struct st_i2c_dev *i2c_dev)

    Handle FIFO empty interrupt in case of write

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

.. _`st_i2c_handle_read`:

st_i2c_handle_read
==================

.. c:function:: void st_i2c_handle_read(struct st_i2c_dev *i2c_dev)

    Handle FIFO enmpty interrupt in case of read

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

.. _`st_i2c_isr_thread`:

st_i2c_isr_thread
=================

.. c:function:: irqreturn_t st_i2c_isr_thread(int irq, void *data)

    Interrupt routine

    :param int irq:
        interrupt number

    :param void \*data:
        Controller's private data

.. _`st_i2c_xfer_msg`:

st_i2c_xfer_msg
===============

.. c:function:: int st_i2c_xfer_msg(struct st_i2c_dev *i2c_dev, struct i2c_msg *msg, bool is_first, bool is_last)

    Transfer a single I2C message

    :param struct st_i2c_dev \*i2c_dev:
        Controller's private data

    :param struct i2c_msg \*msg:
        I2C message to transfer

    :param bool is_first:
        first message of the sequence

    :param bool is_last:
        last message of the sequence

.. _`st_i2c_xfer`:

st_i2c_xfer
===========

.. c:function:: int st_i2c_xfer(struct i2c_adapter *i2c_adap, struct i2c_msg msgs[], int num)

    Transfer a single I2C message

    :param struct i2c_adapter \*i2c_adap:
        Adapter pointer to the controller

    :param struct i2c_msg msgs:
        Pointer to data to be written.

    :param int num:
        Number of messages to be executed

.. This file was automatic generated / don't edit.

