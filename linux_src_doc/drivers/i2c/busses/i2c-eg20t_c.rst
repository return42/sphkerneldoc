.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-eg20t.c

.. _`i2c_algo_pch_data`:

struct i2c_algo_pch_data
========================

.. c:type:: struct i2c_algo_pch_data

    for I2C driver functionalities

.. _`i2c_algo_pch_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_algo_pch_data {
        struct i2c_adapter pch_adapter;
        struct adapter_info *p_adapter_info;
        void __iomem *pch_base_address;
        int pch_buff_mode_en;
        u32 pch_event_flag;
        bool pch_i2c_xfer_in_progress;
    }

.. _`i2c_algo_pch_data.members`:

Members
-------

pch_adapter
    stores the reference to i2c_adapter structure

p_adapter_info
    stores the reference to adapter_info structure

pch_base_address
    specifies the remapped base address

pch_buff_mode_en
    specifies if buffer mode is enabled

pch_event_flag
    specifies occurrence of interrupt events

pch_i2c_xfer_in_progress
    specifies whether the transfer is completed

.. _`adapter_info`:

struct adapter_info
===================

.. c:type:: struct adapter_info

    This structure holds the adapter information for the

.. _`adapter_info.definition`:

Definition
----------

.. code-block:: c

    struct adapter_info {
        struct i2c_algo_pch_data pch_data;
        bool pch_i2c_suspended;
        int ch_num;
    }

.. _`adapter_info.members`:

Members
-------

pch_data
    stores a list of i2c_algo_pch_data

pch_i2c_suspended
    specifies whether the system is suspended or not
    perhaps with more lines and words.

ch_num
    specifies the number of i2c instance

.. _`adapter_info.description`:

Description
-----------

pch_data has as many elements as maximum I2C channels

.. _`pch_i2c_init`:

pch_i2c_init
============

.. c:function:: void pch_i2c_init(struct i2c_algo_pch_data *adap)

    hardware initialization of I2C module

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_wait_for_bus_idle`:

pch_i2c_wait_for_bus_idle
=========================

.. c:function:: s32 pch_i2c_wait_for_bus_idle(struct i2c_algo_pch_data *adap, s32 timeout)

    check the status of bus.

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

    :param s32 timeout:
        waiting time counter (ms).

.. _`pch_i2c_start`:

pch_i2c_start
=============

.. c:function:: void pch_i2c_start(struct i2c_algo_pch_data *adap)

    Generate I2C start condition in normal mode.

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_start.description`:

Description
-----------

Generate I2C start condition in normal mode by setting I2CCTL.I2CMSTA to 1.

.. _`pch_i2c_stop`:

pch_i2c_stop
============

.. c:function:: void pch_i2c_stop(struct i2c_algo_pch_data *adap)

    generate stop condition in normal mode.

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_repstart`:

pch_i2c_repstart
================

.. c:function:: void pch_i2c_repstart(struct i2c_algo_pch_data *adap)

    generate repeated start condition in normal mode

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_writebytes`:

pch_i2c_writebytes
==================

.. c:function:: s32 pch_i2c_writebytes(struct i2c_adapter *i2c_adap, struct i2c_msg *msgs, u32 last, u32 first)

    write data to I2C bus in normal mode

    :param struct i2c_adapter \*i2c_adap:
        Pointer to the struct i2c_adapter.

    :param struct i2c_msg \*msgs:
        *undescribed*

    :param u32 last:
        specifies whether last message or not.
        In the case of compound mode it will be 1 for last message,
        otherwise 0.

    :param u32 first:
        specifies whether first message or not.
        1 for first message otherwise 0.

.. _`pch_i2c_sendack`:

pch_i2c_sendack
===============

.. c:function:: void pch_i2c_sendack(struct i2c_algo_pch_data *adap)

    send ACK

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_sendnack`:

pch_i2c_sendnack
================

.. c:function:: void pch_i2c_sendnack(struct i2c_algo_pch_data *adap)

    send NACK

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_restart`:

pch_i2c_restart
===============

.. c:function:: void pch_i2c_restart(struct i2c_algo_pch_data *adap)

    Generate I2C restart condition in normal mode.

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_restart.description`:

Description
-----------

Generate I2C restart condition in normal mode by setting I2CCTL.I2CRSTA.

.. _`pch_i2c_readbytes`:

pch_i2c_readbytes
=================

.. c:function:: s32 pch_i2c_readbytes(struct i2c_adapter *i2c_adap, struct i2c_msg *msgs, u32 last, u32 first)

    read data  from I2C bus in normal mode.

    :param struct i2c_adapter \*i2c_adap:
        Pointer to the struct i2c_adapter.

    :param struct i2c_msg \*msgs:
        Pointer to i2c_msg structure.

    :param u32 last:
        specifies whether last message or not.

    :param u32 first:
        specifies whether first message or not.

.. _`pch_i2c_cb`:

pch_i2c_cb
==========

.. c:function:: void pch_i2c_cb(struct i2c_algo_pch_data *adap)

    Interrupt handler Call back function

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_handler`:

pch_i2c_handler
===============

.. c:function:: irqreturn_t pch_i2c_handler(int irq, void *pData)

    interrupt handler for the PCH I2C controller

    :param int irq:
        irq number.

    :param void \*pData:
        cookie passed back to the handler function.

.. _`pch_i2c_xfer`:

pch_i2c_xfer
============

.. c:function:: s32 pch_i2c_xfer(struct i2c_adapter *i2c_adap, struct i2c_msg *msgs, s32 num)

    Reading adnd writing data through I2C bus

    :param struct i2c_adapter \*i2c_adap:
        Pointer to the struct i2c_adapter.

    :param struct i2c_msg \*msgs:
        Pointer to i2c_msg structure.

    :param s32 num:
        number of messages.

.. _`pch_i2c_func`:

pch_i2c_func
============

.. c:function:: u32 pch_i2c_func(struct i2c_adapter *adap)

    return the functionality of the I2C driver

    :param struct i2c_adapter \*adap:
        Pointer to struct i2c_algo_pch_data.

.. _`pch_i2c_disbl_int`:

pch_i2c_disbl_int
=================

.. c:function:: void pch_i2c_disbl_int(struct i2c_algo_pch_data *adap)

    Disable PCH I2C interrupts

    :param struct i2c_algo_pch_data \*adap:
        Pointer to struct i2c_algo_pch_data.

.. This file was automatic generated / don't edit.

