.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/auxdisplay/img-ascii-lcd.c

.. _`img_ascii_lcd_config`:

struct img_ascii_lcd_config
===========================

.. c:type:: struct img_ascii_lcd_config

    Configuration information about an LCD model

.. _`img_ascii_lcd_config.definition`:

Definition
----------

.. code-block:: c

    struct img_ascii_lcd_config {
        unsigned int num_chars;
        bool external_regmap;
        void (*update)(struct img_ascii_lcd_ctx *ctx);
    }

.. _`img_ascii_lcd_config.members`:

Members
-------

num_chars
    the number of characters the LCD can display

external_regmap
    true if registers are in a system controller, else false

update
    function called to update the LCD

.. _`img_ascii_lcd_ctx`:

struct img_ascii_lcd_ctx
========================

.. c:type:: struct img_ascii_lcd_ctx

    Private data structure

.. _`img_ascii_lcd_ctx.definition`:

Definition
----------

.. code-block:: c

    struct img_ascii_lcd_ctx {
        struct platform_device *pdev;
        union {
            void __iomem *base;
            struct regmap *regmap;
        } ;
        u32 offset;
        const struct img_ascii_lcd_config *cfg;
        char *message;
        unsigned int message_len;
        unsigned int scroll_pos;
        unsigned int scroll_rate;
        struct timer_list timer;
        char curr[] __aligned(8);
    }

.. _`img_ascii_lcd_ctx.members`:

Members
-------

pdev
    the ASCII LCD platform device

{unnamed_union}
    anonymous

base
    the base address of the LCD registers

regmap
    the regmap through which LCD registers are accessed

offset
    the offset within regmap to the start of the LCD registers

cfg
    pointer to the LCD model configuration

message
    the full message to display or scroll on the LCD

message_len
    the length of the \ ``message``\  string

scroll_pos
    index of the first character of \ ``message``\  currently displayed

scroll_rate
    scroll interval in jiffies

timer
    timer used to implement scrolling

curr
    the string currently displayed on the LCD

.. _`img_ascii_lcd_scroll`:

img_ascii_lcd_scroll
====================

.. c:function:: void img_ascii_lcd_scroll(struct timer_list *t)

    scroll the display by a character

    :param t:
        really a pointer to the private data structure
    :type t: struct timer_list \*

.. _`img_ascii_lcd_scroll.description`:

Description
-----------

Scroll the current message along the LCD by one character, rearming the
timer if required.

.. _`img_ascii_lcd_display`:

img_ascii_lcd_display
=====================

.. c:function:: int img_ascii_lcd_display(struct img_ascii_lcd_ctx *ctx, const char *msg, ssize_t count)

    set the message to be displayed

    :param ctx:
        pointer to the private data structure
    :type ctx: struct img_ascii_lcd_ctx \*

    :param msg:
        the message to display
    :type msg: const char \*

    :param count:
        length of msg, or -1
    :type count: ssize_t

.. _`img_ascii_lcd_display.description`:

Description
-----------

Display a new message \ ``msg``\  on the LCD. \ ``msg``\  can be longer than the number of
characters the LCD can display, in which case it will begin scrolling across
the LCD display.

.. _`img_ascii_lcd_display.return`:

Return
------

0 on success, -ENOMEM on memory allocation failure

.. _`message_show`:

message_show
============

.. c:function:: ssize_t message_show(struct device *dev, struct device_attribute *attr, char *buf)

    read message via sysfs

    :param dev:
        the LCD device
    :type dev: struct device \*

    :param attr:
        the LCD message attribute
    :type attr: struct device_attribute \*

    :param buf:
        the buffer to read the message into
    :type buf: char \*

.. _`message_show.description`:

Description
-----------

Read the current message being displayed or scrolled across the LCD display
into \ ``buf``\ , for reads from sysfs.

.. _`message_show.return`:

Return
------

the number of characters written to \ ``buf``\ 

.. _`message_store`:

message_store
=============

.. c:function:: ssize_t message_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    write a new message via sysfs

    :param dev:
        the LCD device
    :type dev: struct device \*

    :param attr:
        the LCD message attribute
    :type attr: struct device_attribute \*

    :param buf:
        the buffer containing the new message
    :type buf: const char \*

    :param count:
        the size of the message in \ ``buf``\ 
    :type count: size_t

.. _`message_store.description`:

Description
-----------

Write a new message to display or scroll across the LCD display from sysfs.

.. _`message_store.return`:

Return
------

the size of the message on success, else -ERRNO

.. _`img_ascii_lcd_probe`:

img_ascii_lcd_probe
===================

.. c:function:: int img_ascii_lcd_probe(struct platform_device *pdev)

    probe an LCD display device

    :param pdev:
        the LCD platform device
    :type pdev: struct platform_device \*

.. _`img_ascii_lcd_probe.description`:

Description
-----------

Probe an LCD display device, ensuring that we have the required resources in
order to access the LCD & setting up private data as well as sysfs files.

.. _`img_ascii_lcd_probe.return`:

Return
------

0 on success, else -ERRNO

.. _`img_ascii_lcd_remove`:

img_ascii_lcd_remove
====================

.. c:function:: int img_ascii_lcd_remove(struct platform_device *pdev)

    remove an LCD display device

    :param pdev:
        the LCD platform device
    :type pdev: struct platform_device \*

.. _`img_ascii_lcd_remove.description`:

Description
-----------

Remove an LCD display device, freeing private resources & ensuring that the
driver stops using the LCD display registers.

.. _`img_ascii_lcd_remove.return`:

Return
------

0

.. This file was automatic generated / don't edit.

