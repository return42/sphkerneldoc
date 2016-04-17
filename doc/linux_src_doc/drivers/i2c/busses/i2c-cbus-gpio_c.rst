.. -*- coding: utf-8; mode: rst -*-

===============
i2c-cbus-gpio.c
===============


.. _`cbus_send_bit`:

cbus_send_bit
=============

.. c:function:: void cbus_send_bit (struct cbus_host *host, unsigned bit)

    sends one bit over the bus

    :param struct cbus_host \*host:
        the host we're using

    :param unsigned bit:
        one bit of information to send



.. _`cbus_send_data`:

cbus_send_data
==============

.. c:function:: void cbus_send_data (struct cbus_host *host, unsigned data, unsigned len)

    sends @len amount of data over the bus

    :param struct cbus_host \*host:
        the host we're using

    :param unsigned data:
        the data to send

    :param unsigned len:
        size of the transfer



.. _`cbus_receive_bit`:

cbus_receive_bit
================

.. c:function:: int cbus_receive_bit (struct cbus_host *host)

    receives one bit from the bus

    :param struct cbus_host \*host:
        the host we're using



.. _`cbus_receive_word`:

cbus_receive_word
=================

.. c:function:: int cbus_receive_word (struct cbus_host *host)

    receives 16-bit word from the bus

    :param struct cbus_host \*host:
        the host we're using



.. _`cbus_transfer`:

cbus_transfer
=============

.. c:function:: int cbus_transfer (struct cbus_host *host, char rw, unsigned dev, unsigned reg, unsigned data)

    transfers data over the bus

    :param struct cbus_host \*host:
        the host we're using

    :param char rw:
        read/write flag

    :param unsigned dev:
        device address

    :param unsigned reg:
        register address

    :param unsigned data:
        if ``rw`` == I2C_SBUS_WRITE data to send otherwise 0

