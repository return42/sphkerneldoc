
.. _API-struct-i2c-adapter-quirks:

=========================
struct i2c_adapter_quirks
=========================

*man struct i2c_adapter_quirks(9)*

*4.6.0-rc1*

describe flaws of an i2c adapter


Synopsis
========

.. code-block:: c

    struct i2c_adapter_quirks {
      u64 flags;
      int max_num_msgs;
      u16 max_write_len;
      u16 max_read_len;
      u16 max_comb_1st_msg_len;
      u16 max_comb_2nd_msg_len;
    };


Members
=======

flags
    see I2C_AQ_⋆ for possible flags and read below

max_num_msgs
    maximum number of messages per transfer

max_write_len
    maximum length of a write message

max_read_len
    maximum length of a read message

max_comb_1st_msg_len
    maximum length of the first msg in a combined message

max_comb_2nd_msg_len
    maximum length of the second msg in a combined message


Note about combined messages
============================

Some I2C controllers can only send one message per transfer, plus something called combined message or write-then-read. This is (usually) a small write message followed by a read
message and barely enough to access register based devices like EEPROMs. There is a flag to support this mode. It implies max_num_msg = 2 and does the length checks with
max_comb_⋆_len because combined message mode usually has its own limitations. Because of HW implementations, some controllers can actually do write-then-anything or other
variants. To support that, write-then-read has been broken out into smaller bits like write-first and read-second which can be combined as needed.
