.. -*- coding: utf-8; mode: rst -*-

===============
drm_fb_helper.c
===============



.. _xref_drm_fb_helper_single_add_all_connectors:

drm_fb_helper_single_add_all_connectors
=======================================

.. c:function:: int drm_fb_helper_single_add_all_connectors (struct drm_fb_helper * fb_helper)

    add all connectors to fbdev emulation helper

    :param struct drm_fb_helper * fb_helper:
        fbdev initialized with drm_fb_helper_init



Description
-----------

This functions adds all the available connectors for use with the given
fb_helper. This is a separate step to allow drivers to freely assign
connectors to the fbdev, e.g. if some are reserved for special purposes or
not adequate to be used for the fbcon.


This function is protected against concurrent connector hotadds/removals
using :c:func:`drm_fb_helper_add_one_connector` and
:c:func:`drm_fb_helper_remove_one_connector`.




.. _xref_drm_fb_helper_debug_enter:

drm_fb_helper_debug_enter
=========================

.. c:function:: int drm_fb_helper_debug_enter (struct fb_info * info)

    implementation for -\\\gt;fb_debug_enter

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_debug_leave:

drm_fb_helper_debug_leave
=========================

.. c:function:: int drm_fb_helper_debug_leave (struct fb_info * info)

    implementation for -\\\gt;fb_debug_leave

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_restore_fbdev_mode_unlocked:

drm_fb_helper_restore_fbdev_mode_unlocked
=========================================

.. c:function:: int drm_fb_helper_restore_fbdev_mode_unlocked (struct drm_fb_helper * fb_helper)

    restore fbdev configuration

    :param struct drm_fb_helper * fb_helper:
        fbcon to restore



Description
-----------

This should be called from driver's drm ->lastclose callback
when implementing an fbcon on top of kms using this helper. This ensures that
the user isn't greeted with a black screen when e.g. X dies.



RETURNS
-------

Zero if everything went ok, negative error code otherwise.




.. _xref_drm_fb_helper_blank:

drm_fb_helper_blank
===================

.. c:function:: int drm_fb_helper_blank (int blank, struct fb_info * info)

    implementation for -\\\gt;fb_blank

    :param int blank:
        desired blanking state

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_prepare:

drm_fb_helper_prepare
=====================

.. c:function:: void drm_fb_helper_prepare (struct drm_device * dev, struct drm_fb_helper * helper, const struct drm_fb_helper_funcs * funcs)

    setup a drm_fb_helper structure

    :param struct drm_device * dev:
        DRM device

    :param struct drm_fb_helper * helper:
        driver-allocated fbdev helper structure to set up

    :param const struct drm_fb_helper_funcs * funcs:
        pointer to structure of functions associate with this helper



Description
-----------

Sets up the bare minimum to make the framebuffer helper usable. This is
useful to implement race-free initialization of the polling helpers.




.. _xref_drm_fb_helper_init:

drm_fb_helper_init
==================

.. c:function:: int drm_fb_helper_init (struct drm_device * dev, struct drm_fb_helper * fb_helper, int crtc_count, int max_conn_count)

    initialize a drm_fb_helper structure

    :param struct drm_device * dev:
        drm device

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper structure to initialize

    :param int crtc_count:
        maximum number of crtcs to support in this fbdev emulation

    :param int max_conn_count:
        max connector count



Description
-----------

This allocates the structures for the fbdev helper with the given limits.
Note that this won't yet touch the hardware (through the driver interfaces)
nor register the fbdev. This is only done in :c:func:`drm_fb_helper_initial_config`
to allow driver writes more control over the exact init sequence.


Drivers must call :c:func:`drm_fb_helper_prepare` before calling this function.



RETURNS
-------

Zero if everything went ok, nonzero otherwise.




.. _xref_drm_fb_helper_alloc_fbi:

drm_fb_helper_alloc_fbi
=======================

.. c:function:: struct fb_info * drm_fb_helper_alloc_fbi (struct drm_fb_helper * fb_helper)

    allocate fb_info and some of its members

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper



Description
-----------

A helper to alloc fb_info and the members cmap and apertures. Called
by the driver within the fb_probe fb_helper callback function.



RETURNS
-------

fb_info pointer if things went okay, pointer containing error code
otherwise




.. _xref_drm_fb_helper_unregister_fbi:

drm_fb_helper_unregister_fbi
============================

.. c:function:: void drm_fb_helper_unregister_fbi (struct drm_fb_helper * fb_helper)

    unregister fb_info framebuffer device

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper



Description
-----------

A wrapper around unregister_framebuffer, to release the fb_info
framebuffer device




.. _xref_drm_fb_helper_release_fbi:

drm_fb_helper_release_fbi
=========================

.. c:function:: void drm_fb_helper_release_fbi (struct drm_fb_helper * fb_helper)

    dealloc fb_info and its members

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper



Description
-----------

A helper to free memory taken by fb_info and the members cmap and
apertures




.. _xref_drm_fb_helper_unlink_fbi:

drm_fb_helper_unlink_fbi
========================

.. c:function:: void drm_fb_helper_unlink_fbi (struct drm_fb_helper * fb_helper)

    wrapper around unlink_framebuffer

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper



Description
-----------

A wrapper around unlink_framebuffer implemented by fbdev core




.. _xref_drm_fb_helper_sys_read:

drm_fb_helper_sys_read
======================

.. c:function:: ssize_t drm_fb_helper_sys_read (struct fb_info * info, char __user * buf, size_t count, loff_t * ppos)

    wrapper around fb_sys_read

    :param struct fb_info * info:
        fb_info struct pointer

    :param char __user * buf:
        userspace buffer to read from framebuffer memory

    :param size_t count:
        number of bytes to read from framebuffer memory

    :param loff_t * ppos:
        read offset within framebuffer memory



Description
-----------

A wrapper around fb_sys_read implemented by fbdev core




.. _xref_drm_fb_helper_sys_write:

drm_fb_helper_sys_write
=======================

.. c:function:: ssize_t drm_fb_helper_sys_write (struct fb_info * info, const char __user * buf, size_t count, loff_t * ppos)

    wrapper around fb_sys_write

    :param struct fb_info * info:
        fb_info struct pointer

    :param const char __user * buf:
        userspace buffer to write to framebuffer memory

    :param size_t count:
        number of bytes to write to framebuffer memory

    :param loff_t * ppos:
        write offset within framebuffer memory



Description
-----------

A wrapper around fb_sys_write implemented by fbdev core




.. _xref_drm_fb_helper_sys_fillrect:

drm_fb_helper_sys_fillrect
==========================

.. c:function:: void drm_fb_helper_sys_fillrect (struct fb_info * info, const struct fb_fillrect * rect)

    wrapper around sys_fillrect

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_fillrect * rect:
        info about rectangle to fill



Description
-----------

A wrapper around sys_fillrect implemented by fbdev core




.. _xref_drm_fb_helper_sys_copyarea:

drm_fb_helper_sys_copyarea
==========================

.. c:function:: void drm_fb_helper_sys_copyarea (struct fb_info * info, const struct fb_copyarea * area)

    wrapper around sys_copyarea

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_copyarea * area:
        info about area to copy



Description
-----------

A wrapper around sys_copyarea implemented by fbdev core




.. _xref_drm_fb_helper_sys_imageblit:

drm_fb_helper_sys_imageblit
===========================

.. c:function:: void drm_fb_helper_sys_imageblit (struct fb_info * info, const struct fb_image * image)

    wrapper around sys_imageblit

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_image * image:
        info about image to blit



Description
-----------

A wrapper around sys_imageblit implemented by fbdev core




.. _xref_drm_fb_helper_cfb_fillrect:

drm_fb_helper_cfb_fillrect
==========================

.. c:function:: void drm_fb_helper_cfb_fillrect (struct fb_info * info, const struct fb_fillrect * rect)

    wrapper around cfb_fillrect

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_fillrect * rect:
        info about rectangle to fill



Description
-----------

A wrapper around cfb_imageblit implemented by fbdev core




.. _xref_drm_fb_helper_cfb_copyarea:

drm_fb_helper_cfb_copyarea
==========================

.. c:function:: void drm_fb_helper_cfb_copyarea (struct fb_info * info, const struct fb_copyarea * area)

    wrapper around cfb_copyarea

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_copyarea * area:
        info about area to copy



Description
-----------

A wrapper around cfb_copyarea implemented by fbdev core




.. _xref_drm_fb_helper_cfb_imageblit:

drm_fb_helper_cfb_imageblit
===========================

.. c:function:: void drm_fb_helper_cfb_imageblit (struct fb_info * info, const struct fb_image * image)

    wrapper around cfb_imageblit

    :param struct fb_info * info:
        fbdev registered by the helper

    :param const struct fb_image * image:
        info about image to blit



Description
-----------

A wrapper around cfb_imageblit implemented by fbdev core




.. _xref_drm_fb_helper_set_suspend:

drm_fb_helper_set_suspend
=========================

.. c:function:: void drm_fb_helper_set_suspend (struct drm_fb_helper * fb_helper, int state)

    wrapper around fb_set_suspend

    :param struct drm_fb_helper * fb_helper:
        driver-allocated fbdev helper

    :param int state:
        desired state, zero to resume, non-zero to suspend



Description
-----------

A wrapper around fb_set_suspend implemented by fbdev core




.. _xref_drm_fb_helper_setcmap:

drm_fb_helper_setcmap
=====================

.. c:function:: int drm_fb_helper_setcmap (struct fb_cmap * cmap, struct fb_info * info)

    implementation for -\\\gt;fb_setcmap

    :param struct fb_cmap * cmap:
        cmap to set

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_check_var:

drm_fb_helper_check_var
=======================

.. c:function:: int drm_fb_helper_check_var (struct fb_var_screeninfo * var, struct fb_info * info)

    implementation for -\\\gt;fb_check_var

    :param struct fb_var_screeninfo * var:
        screeninfo to check

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_set_par:

drm_fb_helper_set_par
=====================

.. c:function:: int drm_fb_helper_set_par (struct fb_info * info)

    implementation for -\\\gt;fb_set_par

    :param struct fb_info * info:
        fbdev registered by the helper



Description
-----------

This will let fbcon do the mode init and is called at initialization time by
the fbdev core when registering the driver, and later on through the hotplug
callback.




.. _xref_drm_fb_helper_pan_display:

drm_fb_helper_pan_display
=========================

.. c:function:: int drm_fb_helper_pan_display (struct fb_var_screeninfo * var, struct fb_info * info)

    implementation for -\\\gt;fb_pan_display

    :param struct fb_var_screeninfo * var:
        updated screen information

    :param struct fb_info * info:
        fbdev registered by the helper




.. _xref_drm_fb_helper_fill_fix:

drm_fb_helper_fill_fix
======================

.. c:function:: void drm_fb_helper_fill_fix (struct fb_info * info, uint32_t pitch, uint32_t depth)

    initializes fixed fbdev information

    :param struct fb_info * info:
        fbdev registered by the helper

    :param uint32_t pitch:
        desired pitch

    :param uint32_t depth:
        desired depth



Description
-----------

Helper to fill in the fixed fbdev information useful for a non-accelerated
fbdev emulations. Drivers which support acceleration methods which impose
additional constraints need to set up their own limits.


Drivers should call this (or their equivalent setup code) from their
->fb_probe callback.




.. _xref_drm_fb_helper_fill_var:

drm_fb_helper_fill_var
======================

.. c:function:: void drm_fb_helper_fill_var (struct fb_info * info, struct drm_fb_helper * fb_helper, uint32_t fb_width, uint32_t fb_height)

    initalizes variable fbdev information

    :param struct fb_info * info:
        fbdev instance to set up

    :param struct drm_fb_helper * fb_helper:
        fb helper instance to use as template

    :param uint32_t fb_width:
        desired fb width

    :param uint32_t fb_height:
        desired fb height



Description
-----------

Sets up the variable fbdev metainformation from the given fb helper instance
and the drm framebuffer allocated in fb_helper->fb.


Drivers should call this (or their equivalent setup code) from their
->fb_probe callback after having allocated the fbdev backing
storage framebuffer.




.. _xref_drm_fb_helper_initial_config:

drm_fb_helper_initial_config
============================

.. c:function:: int drm_fb_helper_initial_config (struct drm_fb_helper * fb_helper, int bpp_sel)

    setup a sane initial connector configuration

    :param struct drm_fb_helper * fb_helper:
        fb_helper device struct

    :param int bpp_sel:
        bpp value to use for the framebuffer configuration



Description
-----------

Scans the CRTCs and connectors and tries to put together an initial setup.
At the moment, this is a cloned configuration across all heads with
a new framebuffer object as the backing store.


Note that this also registers the fbdev and so allows userspace to call into
the driver through the fbdev interfaces.


This function will call down into the ->fb_probe callback to let
the driver allocate and initialize the fbdev info structure and the drm
framebuffer used to back the fbdev. :c:func:`drm_fb_helper_fill_var` and
:c:func:`drm_fb_helper_fill_fix` are provided as helpers to setup simple default
values for the fbdev info structure.



HANG DEBUGGING
--------------



When you have fbcon support built-in or already loaded, this function will do
a full modeset to setup the fbdev console. Due to locking misdesign in the
VT/fbdev subsystem that entire modeset sequence has to be done while holding
console_lock. Until console_unlock is called no dmesg lines will be sent out
to consoles, not even serial console. This means when your driver crashes,
you will see absolutely nothing else but a system stuck in this function,
with no further output. Any kind of :c:func:`printk` you place within your own driver
or in the drm core modeset code will also never show up.


Standard debug practice is to run the fbcon setup without taking the
console_lock as a hack, to be able to see backtraces and crashes on the
serial line. This can be done by setting the fb.lockless_register_fb=1 kernel
cmdline option.


The other option is to just disable fbdev emulation since very likely the
first modest from userspace will crash in the same way, and is even easier to
debug. This can be done by setting the drm_kms_helper.fbdev_emulation=0
kernel cmdline option.



RETURNS
-------

Zero if everything went ok, nonzero otherwise.




.. _xref_drm_fb_helper_hotplug_event:

drm_fb_helper_hotplug_event
===========================

.. c:function:: int drm_fb_helper_hotplug_event (struct drm_fb_helper * fb_helper)

    respond to a hotplug notification by probing all the outputs attached to the fb

    :param struct drm_fb_helper * fb_helper:
        the drm_fb_helper



Description
-----------

Scan the connectors attached to the fb_helper and try to put together a
setup after *notification of a change in output configuration.


Called at runtime, takes the mode config locks to be able to check/change the
modeset configuration. Must be run from process context (which usually means
either the output polling work or a work item launched from the driver's
hotplug interrupt).


Note that drivers may call this even before calling
drm_fb_helper_initial_config but only aftert drm_fb_helper_init. This allows
for a race-free fbcon setup and will make sure that the fbdev emulation will
not miss any hotplug events.



RETURNS
-------

0 on success and a non-zero error code otherwise.


