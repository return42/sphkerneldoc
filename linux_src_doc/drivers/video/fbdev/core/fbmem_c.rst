.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbmem.c

.. _`register_framebuffer`:

register_framebuffer
====================

.. c:function:: int register_framebuffer(struct fb_info *fb_info)

    registers a frame buffer device

    :param struct fb_info \*fb_info:
        frame buffer info structure

.. _`register_framebuffer.description`:

Description
-----------

Registers a frame buffer device \ ``fb_info``\ .

Returns negative errno on error, or zero for success.

.. _`unregister_framebuffer`:

unregister_framebuffer
======================

.. c:function:: int unregister_framebuffer(struct fb_info *fb_info)

    releases a frame buffer device

    :param struct fb_info \*fb_info:
        frame buffer info structure

.. _`unregister_framebuffer.description`:

Description
-----------

Unregisters a frame buffer device \ ``fb_info``\ .

Returns negative errno on error, or zero for success.

This function will also notify the framebuffer console
to release the driver.

This is meant to be called within a driver's \ :c:func:`module_exit`\ 
function. If this is called outside \ :c:func:`module_exit`\ , ensure
that the driver implements \ :c:func:`fb_open`\  and \ :c:func:`fb_release`\  to
check that no processes are using the device.

.. _`fb_set_suspend`:

fb_set_suspend
==============

.. c:function:: void fb_set_suspend(struct fb_info *info, int state)

    low level driver signals suspend

    :param struct fb_info \*info:
        framebuffer affected

    :param int state:
        0 = resuming, !=0 = suspending

.. _`fb_set_suspend.description`:

Description
-----------

This is meant to be used by low level drivers to
signal suspend/resume to the core & clients.
It must be called with the console semaphore held

.. _`fbmem_init`:

fbmem_init
==========

.. c:function:: int fbmem_init( void)

    init frame buffer subsystem

    :param  void:
        no arguments

.. _`fbmem_init.description`:

Description
-----------

Initialize the frame buffer subsystem.

.. _`fbmem_init.note`:

NOTE
----

This function is \_only\_ to be called by drivers/char/mem.c.

.. This file was automatic generated / don't edit.

