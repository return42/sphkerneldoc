.. -*- coding: utf-8; mode: rst -*-

============
i2c-stu300.c
============


.. _`stu300_dev`:

struct stu300_dev
=================

.. c:type:: stu300_dev

    the stu300 driver state holder


.. _`stu300_dev.definition`:

Definition
----------

.. code-block:: c

  struct stu300_dev {
    struct platform_device * pdev;
    struct i2c_adapter adapter;
    struct clk * clk;
    int irq;
    spinlock_t cmd_issue_lock;
    struct completion cmd_complete;
    enum stu300_event cmd_event;
    enum stu300_error cmd_err;
    unsigned int speed;
    int msg_index;
    int msg_len;
  };


.. _`stu300_dev.members`:

Members
-------

:``pdev``:
    parent platform device

:``adapter``:
    corresponding I2C adapter

:``clk``:
    hardware block clock

:``irq``:
    assigned interrupt line

:``cmd_issue_lock``:
    this locks the following cmd_ variables

:``cmd_complete``:
    acknowledge completion for an I2C command

:``cmd_event``:
    expected event coming in as a response to a command

:``cmd_err``:
    error code as response to a command

:``speed``:
    current bus speed in Hz

:``msg_index``:
    index of current message

:``msg_len``:
    length of current message


