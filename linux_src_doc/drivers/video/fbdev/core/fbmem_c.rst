.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbmem.c

.. _`remove_conflicting_framebuffers`:

remove_conflicting_framebuffers
===============================

.. c:function:: int remove_conflicting_framebuffers(struct apertures_struct *a, const char *name, bool primary)

    remove firmware-configured framebuffers

    :param a:
        memory range, users of which are to be removed
    :type a: struct apertures_struct \*

    :param name:
        requesting driver name
    :type name: const char \*

    :param primary:
        also kick vga16fb if present
    :type primary: bool

.. _`remove_conflicting_framebuffers.description`:

Description
-----------

This function removes framebuffer devices (initialized by firmware/bootloader)
which use memory range described by \ ``a``\ . If \ ``a``\  is NULL all such devices are
removed.

.. _`remove_conflicting_pci_framebuffers`:

remove_conflicting_pci_framebuffers
===================================

.. c:function:: int remove_conflicting_pci_framebuffers(struct pci_dev *pdev, int res_id, const char *name)

    remove firmware-configured framebuffers for PCI devices

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param res_id:
        index of PCI BAR configuring framebuffer memory
    :type res_id: int

    :param name:
        requesting driver name
    :type name: const char \*

.. _`remove_conflicting_pci_framebuffers.description`:

Description
-----------

This function removes framebuffer devices (eg. initialized by firmware)
using memory range configured for \ ``pdev``\ 's BAR \ ``res_id``\ .

The function assumes that PCI device with shadowed ROM drives a primary
display and so kicks out vga16fb.

.. _`register_framebuffer`:

register_framebuffer
====================

.. c:function:: int register_framebuffer(struct fb_info *fb_info)

    registers a frame buffer device

    :param fb_info:
        frame buffer info structure
    :type fb_info: struct fb_info \*

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

    :param fb_info:
        frame buffer info structure
    :type fb_info: struct fb_info \*

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

    :param info:
        framebuffer affected
    :type info: struct fb_info \*

    :param state:
        0 = resuming, !=0 = suspending
    :type state: int

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

    :param void:
        no arguments
    :type void: 

.. _`fbmem_init.description`:

Description
-----------

     Initialize the frame buffer subsystem.

.. _`fbmem_init.note`:

NOTE
----

This function is _only_ to be called by drivers/char/mem.c.

.. This file was automatic generated / don't edit.

