.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbcmap.c

.. _`fb_alloc_cmap_gfp`:

fb_alloc_cmap_gfp
=================

.. c:function:: int fb_alloc_cmap_gfp(struct fb_cmap *cmap, int len, int transp, gfp_t flags)

    allocate a colormap

    :param cmap:
        frame buffer colormap structure
    :type cmap: struct fb_cmap \*

    :param len:
        length of \ ``cmap``\ 
    :type len: int

    :param transp:
        boolean, 1 if there is transparency, 0 otherwise
    :type transp: int

    :param flags:
        flags for kmalloc memory allocation
    :type flags: gfp_t

.. _`fb_alloc_cmap_gfp.description`:

Description
-----------

     Allocates memory for a colormap \ ``cmap``\ .  \ ``len``\  is the
     number of entries in the palette.

     Returns negative errno on error, or zero on success.

.. _`fb_dealloc_cmap`:

fb_dealloc_cmap
===============

.. c:function:: void fb_dealloc_cmap(struct fb_cmap *cmap)

    deallocate a colormap

    :param cmap:
        frame buffer colormap structure
    :type cmap: struct fb_cmap \*

.. _`fb_dealloc_cmap.description`:

Description
-----------

     Deallocates a colormap that was previously allocated with
     \ :c:func:`fb_alloc_cmap`\ .

.. _`fb_copy_cmap`:

fb_copy_cmap
============

.. c:function:: int fb_copy_cmap(const struct fb_cmap *from, struct fb_cmap *to)

    copy a colormap

    :param from:
        frame buffer colormap structure
    :type from: const struct fb_cmap \*

    :param to:
        frame buffer colormap structure
    :type to: struct fb_cmap \*

.. _`fb_copy_cmap.description`:

Description
-----------

     Copy contents of colormap from \ ``from``\  to \ ``to``\ .

.. _`fb_set_cmap`:

fb_set_cmap
===========

.. c:function:: int fb_set_cmap(struct fb_cmap *cmap, struct fb_info *info)

    set the colormap

    :param cmap:
        frame buffer colormap structure
    :type cmap: struct fb_cmap \*

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`fb_set_cmap.description`:

Description
-----------

     Sets the colormap \ ``cmap``\  for a screen of device \ ``info``\ .

     Returns negative errno on error, or zero on success.

.. _`fb_default_cmap`:

fb_default_cmap
===============

.. c:function:: const struct fb_cmap *fb_default_cmap(int len)

    get default colormap

    :param len:
        size of palette for a depth
    :type len: int

.. _`fb_default_cmap.description`:

Description
-----------

     Gets the default colormap for a specific screen depth.  \ ``len``\ 
     is the size of the palette for a particular screen depth.

     Returns pointer to a frame buffer colormap structure.

.. _`fb_invert_cmaps`:

fb_invert_cmaps
===============

.. c:function:: void fb_invert_cmaps( void)

    invert all defaults colormaps

    :param void:
        no arguments
    :type void: 

.. _`fb_invert_cmaps.description`:

Description
-----------

     Invert all default colormaps.

.. This file was automatic generated / don't edit.

