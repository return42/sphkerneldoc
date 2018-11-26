.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fb_helper.c

.. _`fbdev-helpers`:

fbdev helpers
=============

The fb helper functions are useful to provide an fbdev on top of a drm kernel
mode setting driver. They can be used mostly independently from the crtc
helper functions used by many drivers to implement the kernel mode setting
interfaces.

Drivers that support a dumb buffer with a virtual address and mmap support,
should try out the generic fbdev emulation using \ :c:func:`drm_fbdev_generic_setup`\ .

Setup fbdev emulation by calling \ :c:func:`drm_fb_helper_fbdev_setup`\  and tear it
down by calling \ :c:func:`drm_fb_helper_fbdev_teardown`\ .

Drivers that need to handle connector hotplugging (e.g. dp mst) can't use
the setup helper and will need to do the whole four-step setup process with
\ :c:func:`drm_fb_helper_prepare`\ , \ :c:func:`drm_fb_helper_init`\ ,
\ :c:func:`drm_fb_helper_single_add_all_connectors`\ , enable hotplugging and
\ :c:func:`drm_fb_helper_initial_config`\  to avoid a possible race window.

At runtime drivers should restore the fbdev console by using
\ :c:func:`drm_fb_helper_lastclose`\  as their \ :c:type:`drm_driver.lastclose <drm_driver>`\  callback.
They should also notify the fb helper code from updates to the output
configuration by using \ :c:func:`drm_fb_helper_output_poll_changed`\  as their
\ :c:type:`drm_mode_config_funcs.output_poll_changed <drm_mode_config_funcs>`\  callback.

For suspend/resume consider using \ :c:func:`drm_mode_config_helper_suspend`\  and
\ :c:func:`drm_mode_config_helper_resume`\  which takes care of fbdev as well.

All other functions exported by the fb helper library can be used to
implement the fbdev driver interface by the driver.

It is possible, though perhaps somewhat tricky, to implement race-free
hotplug detection using the fbdev helpers. The \ :c:func:`drm_fb_helper_prepare`\ 
helper must be called first to initialize the minimum required to make
hotplug detection work. Drivers also need to make sure to properly set up
the \ :c:type:`drm_mode_config.funcs <drm_mode_config>`\  member. After calling \ :c:func:`drm_kms_helper_poll_init`\ 
it is safe to enable interrupts and start processing hotplug events. At the
same time, drivers should initialize all modeset objects such as CRTCs,
encoders and connectors. To finish up the fbdev helper initialization, the
\ :c:func:`drm_fb_helper_init`\  function is called. To probe for all attached displays
and set up an initial configuration using the detected hardware, drivers
should call \ :c:func:`drm_fb_helper_single_add_all_connectors`\  followed by
\ :c:func:`drm_fb_helper_initial_config`\ .

If \ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\  is set, the
drm_fb_helper_{cfb,sys}_{write,fillrect,copyarea,imageblit} functions will
accumulate changes and schedule \ :c:type:`drm_fb_helper.dirty_work <drm_fb_helper>`\  to run right
away. This worker then calls the \ :c:func:`dirty`\  function ensuring that it will
always run in process context since the fb_*() function could be running in
atomic context. If \ :c:func:`drm_fb_helper_deferred_io`\  is used as the deferred_io
callback it will also schedule dirty_work with the damage collected from the
mmap page writes. Drivers can use \ :c:func:`drm_fb_helper_defio_init`\  to setup
deferred I/O (coupled with \ :c:func:`drm_fb_helper_fbdev_teardown`\ ).

.. _`drm_fb_helper_single_add_all_connectors`:

drm_fb_helper_single_add_all_connectors
=======================================

.. c:function:: int drm_fb_helper_single_add_all_connectors(struct drm_fb_helper *fb_helper)

    add all connectors to fbdev emulation helper

    :param fb_helper:
        fbdev initialized with drm_fb_helper_init, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_single_add_all_connectors.description`:

Description
-----------

This functions adds all the available connectors for use with the given
fb_helper. This is a separate step to allow drivers to freely assign
connectors to the fbdev, e.g. if some are reserved for special purposes or
not adequate to be used for the fbcon.

This function is protected against concurrent connector hotadds/removals
using \ :c:func:`drm_fb_helper_add_one_connector`\  and
\ :c:func:`drm_fb_helper_remove_one_connector`\ .

.. _`drm_fb_helper_debug_enter`:

drm_fb_helper_debug_enter
=========================

.. c:function:: int drm_fb_helper_debug_enter(struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_debug_enter <fb_ops>`\ 

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_debug_leave`:

drm_fb_helper_debug_leave
=========================

.. c:function:: int drm_fb_helper_debug_leave(struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_debug_leave <fb_ops>`\ 

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_restore_fbdev_mode_unlocked`:

drm_fb_helper_restore_fbdev_mode_unlocked
=========================================

.. c:function:: int drm_fb_helper_restore_fbdev_mode_unlocked(struct drm_fb_helper *fb_helper)

    restore fbdev configuration

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_restore_fbdev_mode_unlocked.description`:

Description
-----------

This should be called from driver's drm \ :c:type:`drm_driver.lastclose <drm_driver>`\  callback
when implementing an fbcon on top of kms using this helper. This ensures that
the user isn't greeted with a black screen when e.g. X dies.

.. _`drm_fb_helper_restore_fbdev_mode_unlocked.return`:

Return
------

Zero if everything went ok, negative error code otherwise.

.. _`drm_fb_helper_blank`:

drm_fb_helper_blank
===================

.. c:function:: int drm_fb_helper_blank(int blank, struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_blank <fb_ops>`\ 

    :param blank:
        desired blanking state
    :type blank: int

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_prepare`:

drm_fb_helper_prepare
=====================

.. c:function:: void drm_fb_helper_prepare(struct drm_device *dev, struct drm_fb_helper *helper, const struct drm_fb_helper_funcs *funcs)

    setup a drm_fb_helper structure

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param helper:
        driver-allocated fbdev helper structure to set up
    :type helper: struct drm_fb_helper \*

    :param funcs:
        pointer to structure of functions associate with this helper
    :type funcs: const struct drm_fb_helper_funcs \*

.. _`drm_fb_helper_prepare.description`:

Description
-----------

Sets up the bare minimum to make the framebuffer helper usable. This is
useful to implement race-free initialization of the polling helpers.

.. _`drm_fb_helper_init`:

drm_fb_helper_init
==================

.. c:function:: int drm_fb_helper_init(struct drm_device *dev, struct drm_fb_helper *fb_helper, int max_conn_count)

    initialize a \ :c:type:`struct drm_fb_helper <drm_fb_helper>`\ 

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param fb_helper:
        driver-allocated fbdev helper structure to initialize
    :type fb_helper: struct drm_fb_helper \*

    :param max_conn_count:
        max connector count
    :type max_conn_count: int

.. _`drm_fb_helper_init.description`:

Description
-----------

This allocates the structures for the fbdev helper with the given limits.
Note that this won't yet touch the hardware (through the driver interfaces)
nor register the fbdev. This is only done in \ :c:func:`drm_fb_helper_initial_config`\ 
to allow driver writes more control over the exact init sequence.

Drivers must call \ :c:func:`drm_fb_helper_prepare`\  before calling this function.

.. _`drm_fb_helper_init.return`:

Return
------

Zero if everything went ok, nonzero otherwise.

.. _`drm_fb_helper_alloc_fbi`:

drm_fb_helper_alloc_fbi
=======================

.. c:function:: struct fb_info *drm_fb_helper_alloc_fbi(struct drm_fb_helper *fb_helper)

    allocate fb_info and some of its members

    :param fb_helper:
        driver-allocated fbdev helper
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_alloc_fbi.description`:

Description
-----------

A helper to alloc fb_info and the members cmap and apertures. Called
by the driver within the fb_probe fb_helper callback function. Drivers do not
need to release the allocated fb_info structure themselves, this is
automatically done when calling \ :c:func:`drm_fb_helper_fini`\ .

.. _`drm_fb_helper_alloc_fbi.return`:

Return
------

fb_info pointer if things went okay, pointer containing error code
otherwise

.. _`drm_fb_helper_unregister_fbi`:

drm_fb_helper_unregister_fbi
============================

.. c:function:: void drm_fb_helper_unregister_fbi(struct drm_fb_helper *fb_helper)

    unregister fb_info framebuffer device

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_unregister_fbi.description`:

Description
-----------

A wrapper around unregister_framebuffer, to release the fb_info
framebuffer device. This must be called before releasing all resources for
\ ``fb_helper``\  by calling \ :c:func:`drm_fb_helper_fini`\ .

.. _`drm_fb_helper_fini`:

drm_fb_helper_fini
==================

.. c:function:: void drm_fb_helper_fini(struct drm_fb_helper *fb_helper)

    finialize a \ :c:type:`struct drm_fb_helper <drm_fb_helper>`\ 

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_fini.description`:

Description
-----------

This cleans up all remaining resources associated with \ ``fb_helper``\ . Must be
called after \ :c:func:`drm_fb_helper_unlink_fbi`\  was called.

.. _`drm_fb_helper_unlink_fbi`:

drm_fb_helper_unlink_fbi
========================

.. c:function:: void drm_fb_helper_unlink_fbi(struct drm_fb_helper *fb_helper)

    wrapper around unlink_framebuffer

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_unlink_fbi.description`:

Description
-----------

A wrapper around unlink_framebuffer implemented by fbdev core

.. _`drm_fb_helper_deferred_io`:

drm_fb_helper_deferred_io
=========================

.. c:function:: void drm_fb_helper_deferred_io(struct fb_info *info, struct list_head *pagelist)

    fbdev deferred_io callback function

    :param info:
        fb_info struct pointer
    :type info: struct fb_info \*

    :param pagelist:
        list of dirty mmap framebuffer pages
    :type pagelist: struct list_head \*

.. _`drm_fb_helper_deferred_io.description`:

Description
-----------

This function is used as the \ :c:type:`fb_deferred_io.deferred_io <fb_deferred_io>`\ 
callback function for flushing the fbdev mmap writes.

.. _`drm_fb_helper_defio_init`:

drm_fb_helper_defio_init
========================

.. c:function:: int drm_fb_helper_defio_init(struct drm_fb_helper *fb_helper)

    fbdev deferred I/O initialization

    :param fb_helper:
        driver-allocated fbdev helper
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_defio_init.description`:

Description
-----------

This function allocates \ :c:type:`struct fb_deferred_io <fb_deferred_io>`\ , sets callback to
\ :c:func:`drm_fb_helper_deferred_io`\ , delay to 50ms and calls \ :c:func:`fb_deferred_io_init`\ .
It should be called from the \ :c:type:`drm_fb_helper_funcs->fb_probe <drm_fb_helper_funcs>`\  callback.
\ :c:func:`drm_fb_helper_fbdev_teardown`\  cleans up deferred I/O.

.. _`drm_fb_helper_defio_init.note`:

NOTE
----

A copy of \ :c:type:`struct fb_ops <fb_ops>`\  is made and assigned to \ :c:type:`info->fbops <info>`\ . This is done
because \ :c:func:`fb_deferred_io_cleanup`\  clears \ :c:type:`fbops->fb_mmap <fbops>`\  and would thereby
affect other instances of that \ :c:type:`struct fb_ops <fb_ops>`\ .

.. _`drm_fb_helper_defio_init.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_fb_helper_sys_read`:

drm_fb_helper_sys_read
======================

.. c:function:: ssize_t drm_fb_helper_sys_read(struct fb_info *info, char __user *buf, size_t count, loff_t *ppos)

    wrapper around fb_sys_read

    :param info:
        fb_info struct pointer
    :type info: struct fb_info \*

    :param buf:
        userspace buffer to read from framebuffer memory
    :type buf: char __user \*

    :param count:
        number of bytes to read from framebuffer memory
    :type count: size_t

    :param ppos:
        read offset within framebuffer memory
    :type ppos: loff_t \*

.. _`drm_fb_helper_sys_read.description`:

Description
-----------

A wrapper around fb_sys_read implemented by fbdev core

.. _`drm_fb_helper_sys_write`:

drm_fb_helper_sys_write
=======================

.. c:function:: ssize_t drm_fb_helper_sys_write(struct fb_info *info, const char __user *buf, size_t count, loff_t *ppos)

    wrapper around fb_sys_write

    :param info:
        fb_info struct pointer
    :type info: struct fb_info \*

    :param buf:
        userspace buffer to write to framebuffer memory
    :type buf: const char __user \*

    :param count:
        number of bytes to write to framebuffer memory
    :type count: size_t

    :param ppos:
        write offset within framebuffer memory
    :type ppos: loff_t \*

.. _`drm_fb_helper_sys_write.description`:

Description
-----------

A wrapper around fb_sys_write implemented by fbdev core

.. _`drm_fb_helper_sys_fillrect`:

drm_fb_helper_sys_fillrect
==========================

.. c:function:: void drm_fb_helper_sys_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    wrapper around sys_fillrect

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param rect:
        info about rectangle to fill
    :type rect: const struct fb_fillrect \*

.. _`drm_fb_helper_sys_fillrect.description`:

Description
-----------

A wrapper around sys_fillrect implemented by fbdev core

.. _`drm_fb_helper_sys_copyarea`:

drm_fb_helper_sys_copyarea
==========================

.. c:function:: void drm_fb_helper_sys_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    wrapper around sys_copyarea

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param area:
        info about area to copy
    :type area: const struct fb_copyarea \*

.. _`drm_fb_helper_sys_copyarea.description`:

Description
-----------

A wrapper around sys_copyarea implemented by fbdev core

.. _`drm_fb_helper_sys_imageblit`:

drm_fb_helper_sys_imageblit
===========================

.. c:function:: void drm_fb_helper_sys_imageblit(struct fb_info *info, const struct fb_image *image)

    wrapper around sys_imageblit

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param image:
        info about image to blit
    :type image: const struct fb_image \*

.. _`drm_fb_helper_sys_imageblit.description`:

Description
-----------

A wrapper around sys_imageblit implemented by fbdev core

.. _`drm_fb_helper_cfb_fillrect`:

drm_fb_helper_cfb_fillrect
==========================

.. c:function:: void drm_fb_helper_cfb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    wrapper around cfb_fillrect

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param rect:
        info about rectangle to fill
    :type rect: const struct fb_fillrect \*

.. _`drm_fb_helper_cfb_fillrect.description`:

Description
-----------

A wrapper around cfb_fillrect implemented by fbdev core

.. _`drm_fb_helper_cfb_copyarea`:

drm_fb_helper_cfb_copyarea
==========================

.. c:function:: void drm_fb_helper_cfb_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    wrapper around cfb_copyarea

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param area:
        info about area to copy
    :type area: const struct fb_copyarea \*

.. _`drm_fb_helper_cfb_copyarea.description`:

Description
-----------

A wrapper around cfb_copyarea implemented by fbdev core

.. _`drm_fb_helper_cfb_imageblit`:

drm_fb_helper_cfb_imageblit
===========================

.. c:function:: void drm_fb_helper_cfb_imageblit(struct fb_info *info, const struct fb_image *image)

    wrapper around cfb_imageblit

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param image:
        info about image to blit
    :type image: const struct fb_image \*

.. _`drm_fb_helper_cfb_imageblit.description`:

Description
-----------

A wrapper around cfb_imageblit implemented by fbdev core

.. _`drm_fb_helper_set_suspend`:

drm_fb_helper_set_suspend
=========================

.. c:function:: void drm_fb_helper_set_suspend(struct drm_fb_helper *fb_helper, bool suspend)

    wrapper around fb_set_suspend

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

    :param suspend:
        whether to suspend or resume
    :type suspend: bool

.. _`drm_fb_helper_set_suspend.description`:

Description
-----------

A wrapper around fb_set_suspend implemented by fbdev core.
Use \ :c:func:`drm_fb_helper_set_suspend_unlocked`\  if you don't need to take
the lock yourself

.. _`drm_fb_helper_set_suspend_unlocked`:

drm_fb_helper_set_suspend_unlocked
==================================

.. c:function:: void drm_fb_helper_set_suspend_unlocked(struct drm_fb_helper *fb_helper, bool suspend)

    wrapper around fb_set_suspend that also takes the console lock

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

    :param suspend:
        whether to suspend or resume
    :type suspend: bool

.. _`drm_fb_helper_set_suspend_unlocked.description`:

Description
-----------

A wrapper around \ :c:func:`fb_set_suspend`\  that takes the console lock. If the lock
isn't available on resume, a worker is tasked with waiting for the lock
to become available. The console lock can be pretty contented on resume
due to all the printk activity.

This function can be called multiple times with the same state since
\ :c:type:`fb_info.state <fb_info>`\  is checked to see if fbdev is running or not before locking.

Use \ :c:func:`drm_fb_helper_set_suspend`\  if you need to take the lock yourself.

.. _`drm_fb_helper_setcmap`:

drm_fb_helper_setcmap
=====================

.. c:function:: int drm_fb_helper_setcmap(struct fb_cmap *cmap, struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_setcmap <fb_ops>`\ 

    :param cmap:
        cmap to set
    :type cmap: struct fb_cmap \*

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_ioctl`:

drm_fb_helper_ioctl
===================

.. c:function:: int drm_fb_helper_ioctl(struct fb_info *info, unsigned int cmd, unsigned long arg)

    legacy ioctl implementation

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param cmd:
        ioctl command
    :type cmd: unsigned int

    :param arg:
        ioctl argument
    :type arg: unsigned long

.. _`drm_fb_helper_ioctl.description`:

Description
-----------

A helper to implement the standard fbdev ioctl. Only
FBIO_WAITFORVSYNC is implemented for now.

.. _`drm_fb_helper_check_var`:

drm_fb_helper_check_var
=======================

.. c:function:: int drm_fb_helper_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_check_var <fb_ops>`\ 

    :param var:
        screeninfo to check
    :type var: struct fb_var_screeninfo \*

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_set_par`:

drm_fb_helper_set_par
=====================

.. c:function:: int drm_fb_helper_set_par(struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_set_par <fb_ops>`\ 

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_set_par.description`:

Description
-----------

This will let fbcon do the mode init and is called at initialization time by
the fbdev core when registering the driver, and later on through the hotplug
callback.

.. _`drm_fb_helper_pan_display`:

drm_fb_helper_pan_display
=========================

.. c:function:: int drm_fb_helper_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_pan_display <fb_ops>`\ 

    :param var:
        updated screen information
    :type var: struct fb_var_screeninfo \*

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

.. _`drm_fb_helper_fill_fix`:

drm_fb_helper_fill_fix
======================

.. c:function:: void drm_fb_helper_fill_fix(struct fb_info *info, uint32_t pitch, uint32_t depth)

    initializes fixed fbdev information

    :param info:
        fbdev registered by the helper
    :type info: struct fb_info \*

    :param pitch:
        desired pitch
    :type pitch: uint32_t

    :param depth:
        desired depth
    :type depth: uint32_t

.. _`drm_fb_helper_fill_fix.description`:

Description
-----------

Helper to fill in the fixed fbdev information useful for a non-accelerated
fbdev emulations. Drivers which support acceleration methods which impose
additional constraints need to set up their own limits.

Drivers should call this (or their equivalent setup code) from their
\ :c:type:`drm_fb_helper_funcs.fb_probe <drm_fb_helper_funcs>`\  callback.

.. _`drm_fb_helper_fill_var`:

drm_fb_helper_fill_var
======================

.. c:function:: void drm_fb_helper_fill_var(struct fb_info *info, struct drm_fb_helper *fb_helper, uint32_t fb_width, uint32_t fb_height)

    initalizes variable fbdev information

    :param info:
        fbdev instance to set up
    :type info: struct fb_info \*

    :param fb_helper:
        fb helper instance to use as template
    :type fb_helper: struct drm_fb_helper \*

    :param fb_width:
        desired fb width
    :type fb_width: uint32_t

    :param fb_height:
        desired fb height
    :type fb_height: uint32_t

.. _`drm_fb_helper_fill_var.description`:

Description
-----------

Sets up the variable fbdev metainformation from the given fb helper instance
and the drm framebuffer allocated in \ :c:type:`drm_fb_helper.fb <drm_fb_helper>`\ .

Drivers should call this (or their equivalent setup code) from their
\ :c:type:`drm_fb_helper_funcs.fb_probe <drm_fb_helper_funcs>`\  callback after having allocated the fbdev
backing storage framebuffer.

.. _`drm_fb_helper_initial_config`:

drm_fb_helper_initial_config
============================

.. c:function:: int drm_fb_helper_initial_config(struct drm_fb_helper *fb_helper, int bpp_sel)

    setup a sane initial connector configuration

    :param fb_helper:
        fb_helper device struct
    :type fb_helper: struct drm_fb_helper \*

    :param bpp_sel:
        bpp value to use for the framebuffer configuration
    :type bpp_sel: int

.. _`drm_fb_helper_initial_config.description`:

Description
-----------

Scans the CRTCs and connectors and tries to put together an initial setup.
At the moment, this is a cloned configuration across all heads with
a new framebuffer object as the backing store.

Note that this also registers the fbdev and so allows userspace to call into
the driver through the fbdev interfaces.

This function will call down into the \ :c:type:`drm_fb_helper_funcs.fb_probe <drm_fb_helper_funcs>`\  callback
to let the driver allocate and initialize the fbdev info structure and the
drm framebuffer used to back the fbdev. \ :c:func:`drm_fb_helper_fill_var`\  and
\ :c:func:`drm_fb_helper_fill_fix`\  are provided as helpers to setup simple default
values for the fbdev info structure.

.. _`drm_fb_helper_initial_config.hang-debugging`:

HANG DEBUGGING
--------------


When you have fbcon support built-in or already loaded, this function will do
a full modeset to setup the fbdev console. Due to locking misdesign in the
VT/fbdev subsystem that entire modeset sequence has to be done while holding
console_lock. Until console_unlock is called no dmesg lines will be sent out
to consoles, not even serial console. This means when your driver crashes,
you will see absolutely nothing else but a system stuck in this function,
with no further output. Any kind of \ :c:func:`printk`\  you place within your own driver
or in the drm core modeset code will also never show up.

Standard debug practice is to run the fbcon setup without taking the
console_lock as a hack, to be able to see backtraces and crashes on the
serial line. This can be done by setting the fb.lockless_register_fb=1 kernel
cmdline option.

The other option is to just disable fbdev emulation since very likely the
first modeset from userspace will crash in the same way, and is even easier
to debug. This can be done by setting the drm_kms_helper.fbdev_emulation=0
kernel cmdline option.

.. _`drm_fb_helper_initial_config.return`:

Return
------

Zero if everything went ok, nonzero otherwise.

.. _`drm_fb_helper_hotplug_event`:

drm_fb_helper_hotplug_event
===========================

.. c:function:: int drm_fb_helper_hotplug_event(struct drm_fb_helper *fb_helper)

    respond to a hotplug notification by probing all the outputs attached to the fb

    :param fb_helper:
        driver-allocated fbdev helper, can be NULL
    :type fb_helper: struct drm_fb_helper \*

.. _`drm_fb_helper_hotplug_event.description`:

Description
-----------

Scan the connectors attached to the fb_helper and try to put together a
setup after notification of a change in output configuration.

Called at runtime, takes the mode config locks to be able to check/change the
modeset configuration. Must be run from process context (which usually means
either the output polling work or a work item launched from the driver's
hotplug interrupt).

Note that drivers may call this even before calling
drm_fb_helper_initial_config but only after drm_fb_helper_init. This allows
for a race-free fbcon setup and will make sure that the fbdev emulation will
not miss any hotplug events.

.. _`drm_fb_helper_hotplug_event.return`:

Return
------

0 on success and a non-zero error code otherwise.

.. _`drm_fb_helper_fbdev_setup`:

drm_fb_helper_fbdev_setup
=========================

.. c:function:: int drm_fb_helper_fbdev_setup(struct drm_device *dev, struct drm_fb_helper *fb_helper, const struct drm_fb_helper_funcs *funcs, unsigned int preferred_bpp, unsigned int max_conn_count)

    Setup fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param fb_helper:
        fbdev helper structure to set up
    :type fb_helper: struct drm_fb_helper \*

    :param funcs:
        fbdev helper functions
    :type funcs: const struct drm_fb_helper_funcs \*

    :param preferred_bpp:
        Preferred bits per pixel for the device.
        \ ``dev->mode_config.preferred_depth``\  is used if this is zero.
    :type preferred_bpp: unsigned int

    :param max_conn_count:
        Maximum number of connectors.
        \ ``dev->mode_config.num_connector``\  is used if this is zero.
    :type max_conn_count: unsigned int

.. _`drm_fb_helper_fbdev_setup.description`:

Description
-----------

This function sets up fbdev emulation and registers fbdev for access by
userspace. If all connectors are disconnected, setup is deferred to the next
time \ :c:func:`drm_fb_helper_hotplug_event`\  is called.
The caller must to provide a \ :c:type:`drm_fb_helper_funcs->fb_probe <drm_fb_helper_funcs>`\  callback
function.

Use \ :c:func:`drm_fb_helper_fbdev_teardown`\  to destroy the fbdev.

See also: \ :c:func:`drm_fb_helper_initial_config`\ , \ :c:func:`drm_fbdev_generic_setup`\ .

.. _`drm_fb_helper_fbdev_setup.return`:

Return
------

Zero on success or negative error code on failure.

.. _`drm_fb_helper_fbdev_teardown`:

drm_fb_helper_fbdev_teardown
============================

.. c:function:: void drm_fb_helper_fbdev_teardown(struct drm_device *dev)

    Tear down fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_fb_helper_fbdev_teardown.description`:

Description
-----------

This function unregisters fbdev if not already done and cleans up the
associated resources including the \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .
The driver is responsible for freeing the \ :c:type:`struct drm_fb_helper <drm_fb_helper>`\  structure which is
stored in \ :c:type:`drm_device->fb_helper <drm_device>`\ . Do note that this pointer has been cleared
when this function returns.

In order to support device removal/unplug while file handles are still open,
\ :c:func:`drm_fb_helper_unregister_fbi`\  should be called on device removal and
\ :c:func:`drm_fb_helper_fbdev_teardown`\  in the \ :c:type:`drm_driver->release <drm_driver>`\  callback when
file handles are closed.

.. _`drm_fb_helper_lastclose`:

drm_fb_helper_lastclose
=======================

.. c:function:: void drm_fb_helper_lastclose(struct drm_device *dev)

    DRM driver lastclose helper for fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_fb_helper_lastclose.description`:

Description
-----------

This function can be used as the \ :c:type:`drm_driver->lastclose <drm_driver>`\  callback for drivers
that only need to call \ :c:func:`drm_fb_helper_restore_fbdev_mode_unlocked`\ .

.. _`drm_fb_helper_output_poll_changed`:

drm_fb_helper_output_poll_changed
=================================

.. c:function:: void drm_fb_helper_output_poll_changed(struct drm_device *dev)

    DRM mode config \.output_poll_changed helper for fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_fb_helper_output_poll_changed.description`:

Description
-----------

This function can be used as the
\ :c:type:`drm_mode_config_funcs.output_poll_changed <drm_mode_config_funcs>`\  callback for drivers that only
need to call \ :c:func:`drm_fb_helper_hotplug_event`\ .

.. _`drm_fb_helper_generic_probe`:

drm_fb_helper_generic_probe
===========================

.. c:function:: int drm_fb_helper_generic_probe(struct drm_fb_helper *fb_helper, struct drm_fb_helper_surface_size *sizes)

    Generic fbdev emulation probe helper

    :param fb_helper:
        fbdev helper structure
    :type fb_helper: struct drm_fb_helper \*

    :param sizes:
        describes fbdev size and scanout surface size
    :type sizes: struct drm_fb_helper_surface_size \*

.. _`drm_fb_helper_generic_probe.description`:

Description
-----------

This function uses the client API to create a framebuffer backed by a dumb buffer.

The _sys_ versions are used for \ :c:type:`fb_ops.fb_read <fb_ops>`\ , fb_write, fb_fillrect,
fb_copyarea, fb_imageblit.

.. _`drm_fb_helper_generic_probe.return`:

Return
------

Zero on success or negative error code on failure.

.. _`drm_fbdev_generic_setup`:

drm_fbdev_generic_setup
=======================

.. c:function:: int drm_fbdev_generic_setup(struct drm_device *dev, unsigned int preferred_bpp)

    Setup generic fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param preferred_bpp:
        Preferred bits per pixel for the device.
        \ ``dev->mode_config.preferred_depth``\  is used if this is zero.
    :type preferred_bpp: unsigned int

.. _`drm_fbdev_generic_setup.description`:

Description
-----------

This function sets up generic fbdev emulation for drivers that supports
dumb buffers with a virtual address and that can be mmap'ed. If the driver
does not support these functions, it could use \ :c:func:`drm_fb_helper_fbdev_setup`\ .

Restore, hotplug events and teardown are all taken care of. Drivers that do
suspend/resume need to call \ :c:func:`drm_fb_helper_set_suspend_unlocked`\  themselves.
Simple drivers might use \ :c:func:`drm_mode_config_helper_suspend`\ .

Drivers that set the dirty callback on their framebuffer will get a shadow
fbdev buffer that is blitted onto the real buffer. This is done in order to
make deferred I/O work with all kinds of buffers.

This function is safe to call even when there are no connectors present.
Setup will be retried on the next hotplug event.

The fbdev is destroyed by \ :c:func:`drm_dev_unregister`\ .

.. _`drm_fbdev_generic_setup.return`:

Return
------

Zero on success or negative error code on failure.

.. This file was automatic generated / don't edit.

