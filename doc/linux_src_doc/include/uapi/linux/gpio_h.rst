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
        char name[32];
        char label[32];
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
        char name[32];
        char consumer[32];
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

.. This file was automatic generated / don't edit.

