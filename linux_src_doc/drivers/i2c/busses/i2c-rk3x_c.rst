.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-rk3x.c

.. _`i2c_spec_values`:

struct i2c_spec_values
======================

.. c:type:: struct i2c_spec_values


.. _`i2c_spec_values.definition`:

Definition
----------

.. code-block:: c

    struct i2c_spec_values {
        unsigned long min_hold_start_ns;
        unsigned long min_low_ns;
        unsigned long min_high_ns;
        unsigned long min_setup_start_ns;
        unsigned long max_data_hold_ns;
        unsigned long min_data_setup_ns;
        unsigned long min_setup_stop_ns;
        unsigned long min_hold_buffer_ns;
    }

.. _`i2c_spec_values.members`:

Members
-------

min_hold_start_ns
    min hold time (repeated) START condition

min_low_ns
    min LOW period of the SCL clock

min_high_ns
    min HIGH period of the SCL cloc

min_setup_start_ns
    min set-up time for a repeated START conditio

max_data_hold_ns
    max data hold time

min_data_setup_ns
    min data set-up time

min_setup_stop_ns
    min set-up time for STOP condition

min_hold_buffer_ns
    min bus free time between a STOP and
    START condition

.. _`rk3x_i2c_calced_timings`:

struct rk3x_i2c_calced_timings
==============================

.. c:type:: struct rk3x_i2c_calced_timings


.. _`rk3x_i2c_calced_timings.definition`:

Definition
----------

.. code-block:: c

    struct rk3x_i2c_calced_timings {
        unsigned long div_low;
        unsigned long div_high;
        unsigned int tuning;
    }

.. _`rk3x_i2c_calced_timings.members`:

Members
-------

div_low
    Divider output for low

div_high
    Divider output for high

tuning
    Used to adjust setup/hold data time,
    setup/hold start time and setup stop time for
    v1's calc_timings, the tuning should all be 0
    for old hardware anyone using v0's calc_timings.

.. _`rk3x_i2c_soc_data`:

struct rk3x_i2c_soc_data
========================

.. c:type:: struct rk3x_i2c_soc_data


.. _`rk3x_i2c_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct rk3x_i2c_soc_data {
        int grf_offset;
        int (*calc_timings)(unsigned long, struct i2c_timings *, struct rk3x_i2c_calced_timings *);
    }

.. _`rk3x_i2c_soc_data.members`:

Members
-------

grf_offset
    offset inside the grf regmap for setting the i2c type

calc_timings
    Callback function for i2c timing information calculated

.. _`rk3x_i2c`:

struct rk3x_i2c
===============

.. c:type:: struct rk3x_i2c

    private data of the controller

.. _`rk3x_i2c.definition`:

Definition
----------

.. code-block:: c

    struct rk3x_i2c {
        struct i2c_adapter adap;
        struct device *dev;
        const struct rk3x_i2c_soc_data *soc_data;
        void __iomem *regs;
        struct clk *clk;
        struct clk *pclk;
        struct notifier_block clk_rate_nb;
        struct i2c_timings t;
        spinlock_t lock;
        wait_queue_head_t wait;
        bool busy;
        struct i2c_msg *msg;
        u8 addr;
        unsigned int mode;
        bool is_last_msg;
        enum rk3x_i2c_state state;
        unsigned int processed;
        int error;
    }

.. _`rk3x_i2c.members`:

Members
-------

adap
    corresponding I2C adapter

dev
    device for this controller

soc_data
    related soc data struct

regs
    virtual memory area

clk
    function clk for rk3399 or function & Bus clks for others

pclk
    Bus clk for rk3399

clk_rate_nb
    i2c clk rate change notify

t
    I2C known timing information

lock
    spinlock for the i2c bus

wait
    the waitqueue to wait for i2c transfer

busy
    the condition for the event to wait for

msg
    current i2c message

addr
    addr of i2c slave device

mode
    mode of i2c transfer

is_last_msg
    flag determines whether it is the last msg in this transfer

state
    state of i2c transfer

processed
    byte length which has been send or received

error
    error code for i2c transfer

.. _`rk3x_i2c_start`:

rk3x_i2c_start
==============

.. c:function:: void rk3x_i2c_start(struct rk3x_i2c *i2c)

    :param struct rk3x_i2c \*i2c:
        *undescribed*

.. _`rk3x_i2c_stop`:

rk3x_i2c_stop
=============

.. c:function:: void rk3x_i2c_stop(struct rk3x_i2c *i2c, int error)

    :param struct rk3x_i2c \*i2c:
        *undescribed*

    :param int error:
        Error code to return in rk3x_i2c_xfer

.. _`rk3x_i2c_prepare_read`:

rk3x_i2c_prepare_read
=====================

.. c:function:: void rk3x_i2c_prepare_read(struct rk3x_i2c *i2c)

    >msg

    :param struct rk3x_i2c \*i2c:
        *undescribed*

.. _`rk3x_i2c_fill_transmit_buf`:

rk3x_i2c_fill_transmit_buf
==========================

.. c:function:: void rk3x_i2c_fill_transmit_buf(struct rk3x_i2c *i2c)

    >msg

    :param struct rk3x_i2c \*i2c:
        *undescribed*

.. _`rk3x_i2c_get_spec`:

rk3x_i2c_get_spec
=================

.. c:function:: const struct i2c_spec_values *rk3x_i2c_get_spec(unsigned int speed)

    :param unsigned int speed:
        Desired SCL frequency

.. _`rk3x_i2c_get_spec.return`:

Return
------

Matched i2c spec values.

.. _`rk3x_i2c_v0_calc_timings`:

rk3x_i2c_v0_calc_timings
========================

.. c:function:: int rk3x_i2c_v0_calc_timings(unsigned long clk_rate, struct i2c_timings *t, struct rk3x_i2c_calced_timings *t_calc)

    :param unsigned long clk_rate:
        I2C input clock rate

    :param struct i2c_timings \*t:
        Known I2C timing information

    :param struct rk3x_i2c_calced_timings \*t_calc:
        Caculated rk3x private timings that would be written into regs

.. _`rk3x_i2c_v0_calc_timings.return`:

Return
------

0 on success, -EINVAL if the goal SCL rate is too slow. In that case
a best-effort divider value is returned in divs. If the target rate is
too high, we silently use the highest possible rate.

.. _`rk3x_i2c_v1_calc_timings`:

rk3x_i2c_v1_calc_timings
========================

.. c:function:: int rk3x_i2c_v1_calc_timings(unsigned long clk_rate, struct i2c_timings *t, struct rk3x_i2c_calced_timings *t_calc)

    :param unsigned long clk_rate:
        I2C input clock rate

    :param struct i2c_timings \*t:
        Known I2C timing information

    :param struct rk3x_i2c_calced_timings \*t_calc:
        Caculated rk3x private timings that would be written into regs

.. _`rk3x_i2c_v1_calc_timings.return`:

Return
------

0 on success, -EINVAL if the goal SCL rate is too slow. In that case
a best-effort divider value is returned in divs. If the target rate is
too high, we silently use the highest possible rate.
The following formulas are v1's method to calculate timings.

l = divl + 1;
h = divh + 1;
s = sda_update_config + 1;
u = start_setup_config + 1;
p = stop_setup_config + 1;
T = Tclk_i2c;

tHigh = 8 \* h \* T;
tLow = 8 \* l \* T;

tHD;sda = (l \* s + 1) \* T;
tSU;sda = [(8 - s) \* l + 1] \* T;
tI2C = 8 \* (l + h) \* T;

tSU;sta = (8h \* u + 1) \* T;
tHD;sta = [8h \* (u + 1) - 1] \* T;
tSU;sto = (8h \* p + 1) \* T;

.. _`rk3x_i2c_clk_notifier_cb`:

rk3x_i2c_clk_notifier_cb
========================

.. c:function:: int rk3x_i2c_clk_notifier_cb(struct notifier_block *nb, unsigned long event, void *data)

    Clock rate change callback

    :param struct notifier_block \*nb:
        Pointer to notifier block

    :param unsigned long event:
        Notification reason

    :param void \*data:
        Pointer to notification data object

.. _`rk3x_i2c_clk_notifier_cb.description`:

Description
-----------

The callback checks whether a valid bus frequency can be generated after the
change. If so, the change is acknowledged, otherwise the change is aborted.
New dividers are written to the HW in the pre- or post change notification
depending on the scaling direction.

Code adapted from i2c-cadence.c.

.. _`rk3x_i2c_clk_notifier_cb.return`:

Return
------

NOTIFY_STOP if the rate change should be aborted, NOTIFY_OK
to acknowledge the change, NOTIFY_DONE if the notification is
considered irrelevant.

.. _`rk3x_i2c_setup`:

rk3x_i2c_setup
==============

.. c:function:: int rk3x_i2c_setup(struct rk3x_i2c *i2c, struct i2c_msg *msgs, int num)

    :param struct rk3x_i2c \*i2c:
        *undescribed*

    :param struct i2c_msg \*msgs:
        I2C msgs to process

    :param int num:
        Number of msgs

.. _`rk3x_i2c_setup.description`:

Description
-----------

Must be called with i2c->lock held.

.. _`rk3x_i2c_setup.return`:

Return
------

Number of I2C msgs processed or negative in case of error

.. This file was automatic generated / don't edit.

