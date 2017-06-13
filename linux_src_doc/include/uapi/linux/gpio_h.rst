.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/gpio.h

.. _`gpiochip_info`:

struct gpiochip_info
====================

.. c:type:: struct gpiochip_info

    Information about a certain GPIO chip

.. _`gpiochip_info.definition`:

Definition
----------

.. code-block:: c

    struct gpiochip_info {
        char name;
        char label;
        __u32 lines;
    }

.. _`gpiochip_info.members`:

Members
-------

name
    the Linux kernel name of this GPIO chip

label
    a functional name for this GPIO chip, such as a product
    number, may be NULL

lines
    number of GPIO lines on this chip

.. _`gpioline_info`:

struct gpioline_info
====================

.. c:type:: struct gpioline_info

    Information about a certain GPIO line

.. _`gpioline_info.definition`:

Definition
----------

.. code-block:: c

    struct gpioline_info {
        __u32 line_offset;
        __u32 flags;
        char name;
        char consumer;
    }

.. _`gpioline_info.members`:

Members
-------

line_offset
    the local offset on this GPIO device, fill this in when
    requesting the line information from the kernel

flags
    various flags for this line

name
    the name of this GPIO line, such as the output pin of the line on the
    chip, a rail or a pin header name on a board, as specified by the gpio
    chip, may be NULL

consumer
    a functional name for the consumer of this GPIO line as set by
    whatever is using it, will be NULL if there is no current user but may
    also be NULL if the consumer doesn't set this up

.. _`gpiohandle_request`:

struct gpiohandle_request
=========================

.. c:type:: struct gpiohandle_request

    Information about a GPIO handle request

.. _`gpiohandle_request.definition`:

Definition
----------

.. code-block:: c

    struct gpiohandle_request {
        __u32 lineoffsets;
        __u32 flags;
        __u8 default_values;
        char consumer_label;
        __u32 lines;
        int fd;
    }

.. _`gpiohandle_request.members`:

Members
-------

lineoffsets
    an array desired lines, specified by offset index for the
    associated GPIO device

flags
    desired flags for the desired GPIO lines, such as
    GPIOHANDLE_REQUEST_OUTPUT, GPIOHANDLE_REQUEST_ACTIVE_LOW etc, OR:ed
    together. Note that even if multiple lines are requested, the same flags
    must be applicable to all of them, if you want lines with individual
    flags set, request them one by one. It is possible to select
    a batch of input or output lines, but they must all have the same
    characteristics, i.e. all inputs or all outputs, all active low etc

default_values
    if the GPIOHANDLE_REQUEST_OUTPUT is set for a requested
    line, this specifies the default output value, should be 0 (low) or
    1 (high), anything else than 0 or 1 will be interpreted as 1 (high)

consumer_label
    a desired consumer label for the selected GPIO line(s)
    such as "my-bitbanged-relay"

lines
    number of lines requested in this request, i.e. the number of
    valid fields in the above arrays, set to 1 to request a single line

fd
    if successful this field will contain a valid anonymous file handle
    after a GPIO_GET_LINEHANDLE_IOCTL operation, zero or negative value
    means error

.. _`gpiohandle_data`:

struct gpiohandle_data
======================

.. c:type:: struct gpiohandle_data

    Information of values on a GPIO handle

.. _`gpiohandle_data.definition`:

Definition
----------

.. code-block:: c

    struct gpiohandle_data {
        __u8 values;
    }

.. _`gpiohandle_data.members`:

Members
-------

values
    when getting the state of lines this contains the current
    state of a line, when setting the state of lines these should contain
    the desired target state

.. _`gpioevent_request`:

struct gpioevent_request
========================

.. c:type:: struct gpioevent_request

    Information about a GPIO event request

.. _`gpioevent_request.definition`:

Definition
----------

.. code-block:: c

    struct gpioevent_request {
        __u32 lineoffset;
        __u32 handleflags;
        __u32 eventflags;
        char consumer_label;
        int fd;
    }

.. _`gpioevent_request.members`:

Members
-------

lineoffset
    the desired line to subscribe to events from, specified by
    offset index for the associated GPIO device

handleflags
    desired handle flags for the desired GPIO line, such as
    GPIOHANDLE_REQUEST_ACTIVE_LOW or GPIOHANDLE_REQUEST_OPEN_DRAIN

eventflags
    desired flags for the desired GPIO event line, such as
    GPIOEVENT_REQUEST_RISING_EDGE or GPIOEVENT_REQUEST_FALLING_EDGE

consumer_label
    a desired consumer label for the selected GPIO line(s)
    such as "my-listener"

fd
    if successful this field will contain a valid anonymous file handle
    after a GPIO_GET_LINEEVENT_IOCTL operation, zero or negative value
    means error

.. _`gpioevent_event_rising_edge`:

GPIOEVENT_EVENT_RISING_EDGE
===========================

.. c:function::  GPIOEVENT_EVENT_RISING_EDGE()

.. _`gpioevent_data`:

struct gpioevent_data
=====================

.. c:type:: struct gpioevent_data

    The actual event being pushed to userspace

.. _`gpioevent_data.definition`:

Definition
----------

.. code-block:: c

    struct gpioevent_data {
        __u64 timestamp;
        __u32 id;
    }

.. _`gpioevent_data.members`:

Members
-------

timestamp
    best estimate of time of event occurrence, in nanoseconds

id
    event identifier

.. This file was automatic generated / don't edit.

