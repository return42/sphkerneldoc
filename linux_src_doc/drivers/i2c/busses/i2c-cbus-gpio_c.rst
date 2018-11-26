.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-cbus-gpio.c

.. _`cbus_send_bit`:

cbus_send_bit
=============

.. c:function:: void cbus_send_bit(struct cbus_host *host, unsigned bit)

    sends one bit over the bus

    :param host:
        the host we're using
    :type host: struct cbus_host \*

    :param bit:
        one bit of information to send
    :type bit: unsigned

.. _`cbus_send_data`:

cbus_send_data
==============

.. c:function:: void cbus_send_data(struct cbus_host *host, unsigned data, unsigned len)

    sends \ ``len``\  amount of data over the bus

    :param host:
        the host we're using
    :type host: struct cbus_host \*

    :param data:
        the data to send
    :type data: unsigned

    :param len:
        size of the transfer
    :type len: unsigned

.. _`cbus_receive_bit`:

cbus_receive_bit
================

.. c:function:: int cbus_receive_bit(struct cbus_host *host)

    receives one bit from the bus

    :param host:
        the host we're using
    :type host: struct cbus_host \*

.. _`cbus_receive_word`:

cbus_receive_word
=================

.. c:function:: int cbus_receive_word(struct cbus_host *host)

    receives 16-bit word from the bus

    :param host:
        the host we're using
    :type host: struct cbus_host \*

.. _`cbus_transfer`:

cbus_transfer
=============

.. c:function:: int cbus_transfer(struct cbus_host *host, char rw, unsigned dev, unsigned reg, unsigned data)

    transfers data over the bus

    :param host:
        the host we're using
    :type host: struct cbus_host \*

    :param rw:
        read/write flag
    :type rw: char

    :param dev:
        device address
    :type dev: unsigned

    :param reg:
        register address
    :type reg: unsigned

    :param data:
        if \ ``rw``\  == I2C_SBUS_WRITE data to send otherwise 0
    :type data: unsigned

.. This file was automatic generated / don't edit.

