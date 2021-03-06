.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-cros-ec-tunnel.c

.. _`ec_i2c_device`:

struct ec_i2c_device
====================

.. c:type:: struct ec_i2c_device

    Driver data for I2C tunnel

.. _`ec_i2c_device.definition`:

Definition
----------

.. code-block:: c

    struct ec_i2c_device {
        struct device *dev;
        struct i2c_adapter adap;
        struct cros_ec_device *ec;
        u16 remote_bus;
        u8 request_buf[256];
        u8 response_buf[256];
    }

.. _`ec_i2c_device.members`:

Members
-------

dev
    Device node

adap
    I2C adapter

ec
    Pointer to EC device

remote_bus
    The EC bus number we tunnel to on the other side.

request_buf
    Buffer for transmitting data; we expect most transfers to fit.

response_buf
    Buffer for receiving data; we expect most transfers to fit.

.. _`ec_i2c_count_message`:

ec_i2c_count_message
====================

.. c:function:: int ec_i2c_count_message(const struct i2c_msg i2c_msgs, int num)

    Count bytes needed for ec_i2c_construct_message

    :param i2c_msgs:
        The i2c messages to read
    :type i2c_msgs: const struct i2c_msg

    :param num:
        The number of i2c messages.
    :type num: int

.. _`ec_i2c_count_message.description`:

Description
-----------

Returns the number of bytes the messages will take up.

.. _`ec_i2c_construct_message`:

ec_i2c_construct_message
========================

.. c:function:: int ec_i2c_construct_message(u8 *buf, const struct i2c_msg i2c_msgs, int num, u16 bus_num)

    construct a message to go to the EC

    :param buf:
        The buffer to fill.  We assume that the buffer is big enough.
    :type buf: u8 \*

    :param i2c_msgs:
        The i2c messages to read.
    :type i2c_msgs: const struct i2c_msg

    :param num:
        The number of i2c messages.
    :type num: int

    :param bus_num:
        The remote bus number we want to talk to.
    :type bus_num: u16

.. _`ec_i2c_construct_message.description`:

Description
-----------

This function effectively stuffs the standard i2c_msg format of Linux into
a format that the EC understands.

Returns 0 or a negative error number.

.. _`ec_i2c_count_response`:

ec_i2c_count_response
=====================

.. c:function:: int ec_i2c_count_response(struct i2c_msg i2c_msgs, int num)

    Count bytes needed for ec_i2c_parse_response

    :param i2c_msgs:
        The i2c messages to to fill up.
    :type i2c_msgs: struct i2c_msg

    :param num:
        The number of i2c messages expected.
    :type num: int

.. _`ec_i2c_count_response.description`:

Description
-----------

Returns the number of response bytes expeced.

.. _`ec_i2c_parse_response`:

ec_i2c_parse_response
=====================

.. c:function:: int ec_i2c_parse_response(const u8 *buf, struct i2c_msg i2c_msgs, int *num)

    Parse a response from the EC

    :param buf:
        The buffer to parse.
    :type buf: const u8 \*

    :param i2c_msgs:
        The i2c messages to to fill up.
    :type i2c_msgs: struct i2c_msg

    :param num:
        The number of i2c messages; will be modified to include the actual
        number received.
    :type num: int \*

.. _`ec_i2c_parse_response.description`:

Description
-----------

We'll take the EC's response and copy it back into msgs.

Returns 0 or a negative error number.

.. This file was automatic generated / don't edit.

