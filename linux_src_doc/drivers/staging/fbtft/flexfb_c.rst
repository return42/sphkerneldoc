.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fbtft/flexfb.c

.. _`flexfb_lcd_controller`:

struct flexfb_lcd_controller
============================

.. c:type:: struct flexfb_lcd_controller

    Describes the LCD controller properties

.. _`flexfb_lcd_controller.definition`:

Definition
----------

.. code-block:: c

    struct flexfb_lcd_controller {
        const char *name;
        unsigned int width;
        unsigned int height;
        unsigned int setaddrwin;
        unsigned int regwidth;
        s16 *init_seq;
        int init_seq_sz;
    }

.. _`flexfb_lcd_controller.members`:

Members
-------

name
    Model name of the chip

width
    Width of display in pixels

height
    Height of display in pixels

setaddrwin
    Which \ :c:func:`set_addr_win`\  implementation to use

regwidth
    LCD Controller Register width in bits

init_seq
    LCD initialization sequence

init_seq_sz
    Size of LCD initialization sequence

.. This file was automatic generated / don't edit.

