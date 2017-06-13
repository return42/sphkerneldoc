.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fbtft/fbtft.h

.. _`fbtft_gpio`:

struct fbtft_gpio
=================

.. c:type:: struct fbtft_gpio

    Structure that holds one pinname to gpio mapping

.. _`fbtft_gpio.definition`:

Definition
----------

.. code-block:: c

    struct fbtft_gpio {
        char name;
        unsigned int gpio;
    }

.. _`fbtft_gpio.members`:

Members
-------

name
    pinname (reset, dc, etc.)

gpio
    GPIO number

.. _`fbtft_ops`:

struct fbtft_ops
================

.. c:type:: struct fbtft_ops

    FBTFT operations structure

.. _`fbtft_ops.definition`:

Definition
----------

.. code-block:: c

    struct fbtft_ops {
        int (*write)(struct fbtft_par *par, void *buf, size_t len);
        int (*read)(struct fbtft_par *par, void *buf, size_t len);
        int (*write_vmem)(struct fbtft_par *par, size_t offset, size_t len);
        void (*write_register)(struct fbtft_par *par, int len, ...);
        void (*set_addr_win)(struct fbtft_par *par, int xs, int ys, int xe, int ye);
        void (*reset)(struct fbtft_par *par);
        void (*mkdirty)(struct fb_info *info, int from, int to);
        void (*update_display)(struct fbtft_par *par, unsigned int start_line, unsigned int end_line);
        int (*init_display)(struct fbtft_par *par);
        int (*blank)(struct fbtft_par *par, bool on);
        unsigned long (*request_gpios_match)(struct fbtft_par *par, const struct fbtft_gpio *gpio);
        int (*request_gpios)(struct fbtft_par *par);
        int (*verify_gpios)(struct fbtft_par *par);
        void (*register_backlight)(struct fbtft_par *par);
        void (*unregister_backlight)(struct fbtft_par *par);
        int (*set_var)(struct fbtft_par *par);
        int (*set_gamma)(struct fbtft_par *par, u32 *curves);
    }

.. _`fbtft_ops.members`:

Members
-------

write
    Writes to interface bus

read
    Reads from interface bus

write_vmem
    Writes video memory to display

write_register
    *undescribed*

set_addr_win
    Set the GRAM update window

reset
    Reset the LCD controller

mkdirty
    Marks display lines for update

update_display
    Updates the display

init_display
    Initializes the display

blank
    Blank the display (optional)

request_gpios_match
    Do pinname to gpio matching

request_gpios
    Request gpios from the kernel

verify_gpios
    Verify that necessary gpios is present (optional)

register_backlight
    Used to register backlight device (optional)

unregister_backlight
    Unregister backlight device (optional)

set_var
    Configure LCD with values from variables like \ ``rotate``\  and \ ``bgr``\ 
    (optional)

set_gamma
    Set Gamma curve (optional)

.. _`fbtft_ops.description`:

Description
-----------

Most of these operations have default functions assigned to them in
\ :c:func:`fbtft_framebuffer_alloc`\ 

.. _`fbtft_display`:

struct fbtft_display
====================

.. c:type:: struct fbtft_display

    Describes the display properties

.. _`fbtft_display.definition`:

Definition
----------

.. code-block:: c

    struct fbtft_display {
        unsigned int width;
        unsigned int height;
        unsigned int regwidth;
        unsigned int buswidth;
        unsigned int backlight;
        struct fbtft_ops fbtftops;
        unsigned int bpp;
        unsigned int fps;
        int txbuflen;
        const s16 *init_sequence;
        char *gamma;
        int gamma_num;
        int gamma_len;
        unsigned long debug;
    }

.. _`fbtft_display.members`:

Members
-------

width
    Width of display in pixels

height
    Height of display in pixels

regwidth
    LCD Controller Register width in bits

buswidth
    Display interface bus width in bits

backlight
    Backlight type.

fbtftops
    FBTFT operations provided by driver or device (platform_data)

bpp
    Bits per pixel

fps
    Frames per second

txbuflen
    Size of transmit buffer

init_sequence
    Pointer to LCD initialization array

gamma
    String representation of Gamma curve(s)

gamma_num
    Number of Gamma curves

gamma_len
    Number of values per Gamma curve

debug
    Initial debug value

.. _`fbtft_display.description`:

Description
-----------

This structure is not stored by FBTFT except for init_sequence.

.. _`fbtft_platform_data`:

struct fbtft_platform_data
==========================

.. c:type:: struct fbtft_platform_data

    Passes display specific data to the driver

.. _`fbtft_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct fbtft_platform_data {
        struct fbtft_display display;
        const struct fbtft_gpio *gpios;
        unsigned int rotate;
        bool bgr;
        unsigned int fps;
        int txbuflen;
        u8 startbyte;
        char *gamma;
        void *extra;
    }

.. _`fbtft_platform_data.members`:

Members
-------

display
    Display properties

gpios
    Pointer to an array of pinname to gpio mappings

rotate
    Display rotation angle

bgr
    LCD Controller BGR bit

fps
    Frames per second (this will go away, use \ ``fps``\  in \ ``fbtft_display``\ )

txbuflen
    Size of transmit buffer

startbyte
    When set, enables use of Startbyte in transfers

gamma
    String representation of Gamma curve(s)

extra
    A way to pass extra info

.. This file was automatic generated / don't edit.

