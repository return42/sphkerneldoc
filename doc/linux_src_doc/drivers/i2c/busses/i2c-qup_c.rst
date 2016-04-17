.. -*- coding: utf-8; mode: rst -*-

=========
i2c-qup.c
=========


.. _`qup_i2c_wait_ready`:

qup_i2c_wait_ready
==================

.. c:function:: int qup_i2c_wait_ready (struct qup_i2c_dev *qup, int op, bool val, int len)

    wait for a give number of bytes in tx/rx path

    :param struct qup_i2c_dev \*qup:
        The qup_i2c_dev device

    :param int op:
        The bit/event to wait on

    :param bool val:
        value of the bit to wait on, 0 or 1

    :param int len:
        The length the bytes to be transferred

