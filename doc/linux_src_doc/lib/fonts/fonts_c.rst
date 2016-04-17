.. -*- coding: utf-8; mode: rst -*-

=======
fonts.c
=======


.. _`find_font`:

find_font
=========

.. c:function:: const struct font_desc *find_font (const char *name)

    find a font

    :param const char \*name:
        string name of a font



.. _`find_font.description`:

Description
-----------

Find a specified font with string name ``name``\ .

Returns ``NULL`` if no font found, or a pointer to the
specified font.



.. _`get_default_font`:

get_default_font
================

.. c:function:: const struct font_desc *get_default_font (int xres, int yres, u32 font_w, u32 font_h)

    get default font

    :param int xres:
        screen size of X

    :param int yres:
        screen size of Y

    :param u32 font_w:
        bit array of supported widths (1 - 32)

    :param u32 font_h:
        bit array of supported heights (1 - 32)



.. _`get_default_font.description`:

Description
-----------

Get the default font for a specified screen size.
Dimensions are in pixels.

Returns ``NULL`` if no font is found, or a pointer to the
chosen font.

