.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fb_cmdline.c

.. _`fb_get_options`:

fb_get_options
==============

.. c:function:: int fb_get_options(const char *name, char **option)

    get kernel boot parameters

    :param const char \*name:
        framebuffer name as it would appear in
        the boot parameter line
        (video=<name>:<options>)

    :param char \*\*option:
        the option will be stored here

.. _`fb_get_options.note`:

NOTE
----

Needed to maintain backwards compatibility

.. _`video_setup`:

video_setup
===========

.. c:function:: int video_setup(char *options)

    process command line options

    :param char \*options:
        string of options

.. _`video_setup.description`:

Description
-----------

Process command line options for frame buffer subsystem.

.. _`video_setup.note`:

NOTE
----

This function is a \__setup and \__init function.
It only stores the options.  Drivers have to call
\ :c:func:`fb_get_options`\  as necessary.

Returns zero.

.. This file was automatic generated / don't edit.

