.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/chrome/cros_ec_spi.c

.. _`cros_ec_spi`:

struct cros_ec_spi
==================

.. c:type:: struct cros_ec_spi

    information about a SPI-connected EC

.. _`cros_ec_spi.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_spi {
        struct spi_device *spi;
        s64 last_transfer_ns;
        unsigned int start_of_msg_delay;
        unsigned int end_of_msg_delay;
    }

.. _`cros_ec_spi.members`:

Members
-------

spi
    SPI device we are connected to

last_transfer_ns
    time that we last finished a transfer.

start_of_msg_delay
    used to set the delay_usecs on the spi_transfer that
    is sent when we want to turn on CS at the start of a transaction.

end_of_msg_delay
    used to set the delay_usecs on the spi_transfer that
    is sent when we want to turn off CS at the end of a transaction.

.. _`receive_n_bytes`:

receive_n_bytes
===============

.. c:function:: int receive_n_bytes(struct cros_ec_device *ec_dev, u8 *buf, int n)

    receive n bytes from the EC.

    :param ec_dev:
        *undescribed*
    :type ec_dev: struct cros_ec_device \*

    :param buf:
        *undescribed*
    :type buf: u8 \*

    :param n:
        *undescribed*
    :type n: int

.. _`receive_n_bytes.description`:

Description
-----------

Assumes buf is a pointer into the ec_dev->din buffer

.. _`cros_ec_spi_receive_packet`:

cros_ec_spi_receive_packet
==========================

.. c:function:: int cros_ec_spi_receive_packet(struct cros_ec_device *ec_dev, int need_len)

    Receive a packet from the EC.

    :param ec_dev:
        ChromeOS EC device
    :type ec_dev: struct cros_ec_device \*

    :param need_len:
        Number of message bytes we need to read
    :type need_len: int

.. _`cros_ec_spi_receive_packet.this-function-has-two-phases`:

This function has two phases
----------------------------

reading the preamble bytes (since if we read
data from the EC before it is ready to send, we just get preamble) and
reading the actual message.

The received data is placed into ec_dev->din.

.. _`cros_ec_spi_receive_response`:

cros_ec_spi_receive_response
============================

.. c:function:: int cros_ec_spi_receive_response(struct cros_ec_device *ec_dev, int need_len)

    Receive a response from the EC.

    :param ec_dev:
        ChromeOS EC device
    :type ec_dev: struct cros_ec_device \*

    :param need_len:
        Number of message bytes we need to read
    :type need_len: int

.. _`cros_ec_spi_receive_response.this-function-has-two-phases`:

This function has two phases
----------------------------

reading the preamble bytes (since if we read
data from the EC before it is ready to send, we just get preamble) and
reading the actual message.

The received data is placed into ec_dev->din.

.. _`cros_ec_pkt_xfer_spi`:

cros_ec_pkt_xfer_spi
====================

.. c:function:: int cros_ec_pkt_xfer_spi(struct cros_ec_device *ec_dev, struct cros_ec_command *ec_msg)

    Transfer a packet over SPI and receive the reply

    :param ec_dev:
        ChromeOS EC device
    :type ec_dev: struct cros_ec_device \*

    :param ec_msg:
        Message to transfer
    :type ec_msg: struct cros_ec_command \*

.. _`cros_ec_cmd_xfer_spi`:

cros_ec_cmd_xfer_spi
====================

.. c:function:: int cros_ec_cmd_xfer_spi(struct cros_ec_device *ec_dev, struct cros_ec_command *ec_msg)

    Transfer a message over SPI and receive the reply

    :param ec_dev:
        ChromeOS EC device
    :type ec_dev: struct cros_ec_device \*

    :param ec_msg:
        Message to transfer
    :type ec_msg: struct cros_ec_command \*

.. This file was automatic generated / don't edit.

