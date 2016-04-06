
.. _API-struct-lirc-driver:

==================
struct lirc_driver
==================

*man struct lirc_driver(9)*

*4.6.0-rc1*

Defines the parameters on a LIRC driver


Synopsis
========

.. code-block:: c

    struct lirc_driver {
      char name[40];
      int minor;
      __u32 code_length;
      unsigned int buffer_size;
      int sample_rate;
      __u32 features;
      unsigned int chunk_size;
      void * data;
      int min_timeout;
      int max_timeout;
      int (* add_to_buf) (void *data, struct lirc_buffer *buf);
      struct lirc_buffer * rbuf;
      int (* set_use_inc) (void *data);
      void (* set_use_dec) (void *data);
      struct rc_dev * rdev;
      const struct file_operations * fops;
      struct device * dev;
      struct module * owner;
    };


Members
=======

name[40]
    this string will be used for logs

minor
    indicates minor device (/dev/lirc) number for registered driver if caller fills it with negative value, then the first free minor number will be used (if available).

code_length
    length of the remote control key code expressed in bits.

buffer_size
    Number of FIFO buffers with ``chunk_size`` size. If zero, creates a buffer with BUFLEN size (16 bytes).

sample_rate
    if zero, the device will wait for an event with a new code to be parsed. Otherwise, specifies the sample rate for polling. Value should be between 0 and HZ. If equal to HZ, it
    would mean one polling per second.

features
    lirc compatible hardware features, like LIRC_MODE_RAW, LIRC_CAN_⋆, as defined at include/media/lirc.h.

chunk_size
    Size of each FIFO buffer.

data
    it may point to any driver data and this pointer will be passed to all callback functions.

min_timeout
    Minimum timeout for record. Valid only if LIRC_CAN_SET_REC_TIMEOUT is defined.

max_timeout
    Maximum timeout for record. Valid only if LIRC_CAN_SET_REC_TIMEOUT is defined.

add_to_buf
    add_to_buf will be called after specified period of the time or triggered by the external event, this behavior depends on value of the sample_rate this function will be
    called in user context. This routine should return 0 if data was added to the buffer and -ENODATA if none was available. This should add some number of bits evenly divisible by
    code_length to the buffer.

rbuf
    if not NULL, it will be used as a read buffer, you will have to write to the buffer by other means, like irq's (see also lirc_serial.c).

set_use_inc
    set_use_inc will be called after device is opened

set_use_dec
    set_use_dec will be called after device is closed

rdev
    Pointed to struct rc_dev associated with the LIRC device.

fops
    file_operations for drivers which don't fit the current driver model. Some ioctl's can be directly handled by lirc_dev if the driver's ioctl function is NULL or if it returns
    -ENOIOCTLCMD (see also lirc_serial.c).

dev
    pointer to the struct device associated with the LIRC device.

owner
    the module owning this struct
