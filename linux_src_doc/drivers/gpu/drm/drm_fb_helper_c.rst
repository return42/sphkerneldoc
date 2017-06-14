.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fb_helper.c

.. _`fbdev-helpers`:

fbdev helpers
=============

The fb helper functions are useful to provide an fbdev on top of a drm kernel
mode setting driver. They can be used mostly independently from the crtc
helper functions used by many drivers to implement the kernel mode setting
interfaces.

Initialization is done as a four-step process with \ :c:func:`drm_fb_helper_prepare`\ ,
\ :c:func:`drm_fb_helper_init`\ , \ :c:func:`drm_fb_helper_single_add_all_connectors`\  and
\ :c:func:`drm_fb_helper_initial_config`\ . Drivers with fancier requirements than the
default behaviour can override the third step with their own code.
Teardown is done with \ :c:func:`drm_fb_helper_fini`\  after the fbdev device is
unregisters using \ :c:func:`drm_fb_helper_unregister_fbi`\ .

At runtime drivers should restore the fbdev console by calling
\ :c:func:`drm_fb_helper_restore_fbdev_mode_unlocked`\  from their \ :c:type:`drm_driver.lastclose <drm_driver>`\ 
callback.  They should also notify the fb helper code from updates to the
output configuration by calling \ :c:func:`drm_fb_helper_hotplug_event`\ . For easier
integration with the output polling code in drm_crtc_helper.c the modeset
code provides a \ :c:type:`drm_mode_config_funcs.output_poll_changed <drm_mode_config_funcs>`\  callback.

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
mmap page writes.

.. _`drm_fb_helper_single_add_all_connectors`:

drm_fb_helper_single_add_all_connectors
=======================================

.. c:function:: int drm_fb_helper_single_add_all_connectors(struct drm_fb_helper *fb_helper)

    add all connectors to fbdev emulation helper

    :param struct drm_fb_helper \*fb_helper:
        fbdev initialized with drm_fb_helper_init

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

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_debug_leave`:

drm_fb_helper_debug_leave
=========================

.. c:function:: int drm_fb_helper_debug_leave(struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_debug_leave <fb_ops>`\ 

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_restore_fbdev_mode_unlocked`:

drm_fb_helper_restore_fbdev_mode_unlocked
=========================================

.. c:function:: int drm_fb_helper_restore_fbdev_mode_unlocked(struct drm_fb_helper *fb_helper)

    restore fbdev configuration

    :param struct drm_fb_helper \*fb_helper:
        fbcon to restore

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

    :param int blank:
        desired blanking state

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_prepare`:

drm_fb_helper_prepare
=====================

.. c:function:: void drm_fb_helper_prepare(struct drm_device *dev, struct drm_fb_helper *helper, const struct drm_fb_helper_funcs *funcs)

    setup a drm_fb_helper structure

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_fb_helper \*helper:
        driver-allocated fbdev helper structure to set up

    :param const struct drm_fb_helper_funcs \*funcs:
        pointer to structure of functions associate with this helper

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

    :param struct drm_device \*dev:
        drm device

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper structure to initialize

    :param int max_conn_count:
        max connector count

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

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

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

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

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

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

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

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

.. _`drm_fb_helper_unlink_fbi.description`:

Description
-----------

A wrapper around unlink_framebuffer implemented by fbdev core

.. _`drm_fb_helper_deferred_io`:

drm_fb_helper_deferred_io
=========================

.. c:function:: void drm_fb_helper_deferred_io(struct fb_info *info, struct list_head *pagelist)

    fbdev deferred_io callback function

    :param struct fb_info \*info:
        fb_info struct pointer

    :param struct list_head \*pagelist:
        list of dirty mmap framebuffer pages

.. _`drm_fb_helper_deferred_io.description`:

Description
-----------

This function is used as the \ :c:type:`fb_deferred_io.deferred_io <fb_deferred_io>`\ 
callback function for flushing the fbdev mmap writes.

.. _`drm_fb_helper_sys_read`:

drm_fb_helper_sys_read
======================

.. c:function:: ssize_t drm_fb_helper_sys_read(struct fb_info *info, char __user *buf, size_t count, loff_t *ppos)

    wrapper around fb_sys_read

    :param struct fb_info \*info:
        fb_info struct pointer

    :param char __user \*buf:
        userspace buffer to read from framebuffer memory

    :param size_t count:
        number of bytes to read from framebuffer memory

    :param loff_t \*ppos:
        read offset within framebuffer memory

.. _`drm_fb_helper_sys_read.description`:

Description
-----------

A wrapper around fb_sys_read implemented by fbdev core

.. _`drm_fb_helper_sys_write`:

drm_fb_helper_sys_write
=======================

.. c:function:: ssize_t drm_fb_helper_sys_write(struct fb_info *info, const char __user *buf, size_t count, loff_t *ppos)

    wrapper around fb_sys_write

    :param struct fb_info \*info:
        fb_info struct pointer

    :param const char __user \*buf:
        userspace buffer to write to framebuffer memory

    :param size_t count:
        number of bytes to write to framebuffer memory

    :param loff_t \*ppos:
        write offset within framebuffer memory

.. _`drm_fb_helper_sys_write.description`:

Description
-----------

A wrapper around fb_sys_write implemented by fbdev core

.. _`drm_fb_helper_sys_fillrect`:

drm_fb_helper_sys_fillrect
==========================

.. c:function:: void drm_fb_helper_sys_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    wrapper around sys_fillrect

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_fillrect \*rect:
        info about rectangle to fill

.. _`drm_fb_helper_sys_fillrect.description`:

Description
-----------

A wrapper around sys_fillrect implemented by fbdev core

.. _`drm_fb_helper_sys_copyarea`:

drm_fb_helper_sys_copyarea
==========================

.. c:function:: void drm_fb_helper_sys_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    wrapper around sys_copyarea

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_copyarea \*area:
        info about area to copy

.. _`drm_fb_helper_sys_copyarea.description`:

Description
-----------

A wrapper around sys_copyarea implemented by fbdev core

.. _`drm_fb_helper_sys_imageblit`:

drm_fb_helper_sys_imageblit
===========================

.. c:function:: void drm_fb_helper_sys_imageblit(struct fb_info *info, const struct fb_image *image)

    wrapper around sys_imageblit

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_image \*image:
        info about image to blit

.. _`drm_fb_helper_sys_imageblit.description`:

Description
-----------

A wrapper around sys_imageblit implemented by fbdev core

.. _`drm_fb_helper_cfb_fillrect`:

drm_fb_helper_cfb_fillrect
==========================

.. c:function:: void drm_fb_helper_cfb_fillrect(struct fb_info *info, const struct fb_fillrect *rect)

    wrapper around cfb_fillrect

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_fillrect \*rect:
        info about rectangle to fill

.. _`drm_fb_helper_cfb_fillrect.description`:

Description
-----------

A wrapper around cfb_imageblit implemented by fbdev core

.. _`drm_fb_helper_cfb_copyarea`:

drm_fb_helper_cfb_copyarea
==========================

.. c:function:: void drm_fb_helper_cfb_copyarea(struct fb_info *info, const struct fb_copyarea *area)

    wrapper around cfb_copyarea

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_copyarea \*area:
        info about area to copy

.. _`drm_fb_helper_cfb_copyarea.description`:

Description
-----------

A wrapper around cfb_copyarea implemented by fbdev core

.. _`drm_fb_helper_cfb_imageblit`:

drm_fb_helper_cfb_imageblit
===========================

.. c:function:: void drm_fb_helper_cfb_imageblit(struct fb_info *info, const struct fb_image *image)

    wrapper around cfb_imageblit

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param const struct fb_image \*image:
        info about image to blit

.. _`drm_fb_helper_cfb_imageblit.description`:

Description
-----------

A wrapper around cfb_imageblit implemented by fbdev core

.. _`drm_fb_helper_set_suspend`:

drm_fb_helper_set_suspend
=========================

.. c:function:: void drm_fb_helper_set_suspend(struct drm_fb_helper *fb_helper, bool suspend)

    wrapper around fb_set_suspend

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

    :param bool suspend:
        whether to suspend or resume

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

    :param struct drm_fb_helper \*fb_helper:
        driver-allocated fbdev helper

    :param bool suspend:
        whether to suspend or resume

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

    :param struct fb_cmap \*cmap:
        cmap to set

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_ioctl`:

drm_fb_helper_ioctl
===================

.. c:function:: int drm_fb_helper_ioctl(struct fb_info *info, unsigned int cmd, unsigned long arg)

    legacy ioctl implementation

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param unsigned int cmd:
        ioctl command

    :param unsigned long arg:
        ioctl argument

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

    :param struct fb_var_screeninfo \*var:
        screeninfo to check

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_set_par`:

drm_fb_helper_set_par
=====================

.. c:function:: int drm_fb_helper_set_par(struct fb_info *info)

    implementation for \ :c:type:`fb_ops.fb_set_par <fb_ops>`\ 

    :param struct fb_info \*info:
        fbdev registered by the helper

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

    :param struct fb_var_screeninfo \*var:
        updated screen information

    :param struct fb_info \*info:
        fbdev registered by the helper

.. _`drm_fb_helper_fill_fix`:

drm_fb_helper_fill_fix
======================

.. c:function:: void drm_fb_helper_fill_fix(struct fb_info *info, uint32_t pitch, uint32_t depth)

    initializes fixed fbdev information

    :param struct fb_info \*info:
        fbdev registered by the helper

    :param uint32_t pitch:
        desired pitch

    :param uint32_t depth:
        desired depth

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

    :param struct fb_info \*info:
        fbdev instance to set up

    :param struct drm_fb_helper \*fb_helper:
        fb helper instance to use as template

    :param uint32_t fb_width:
        desired fb width

    :param uint32_t fb_height:
        desired fb height

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

    :param struct drm_fb_helper \*fb_helper:
        fb_helper device struct

    :param int bpp_sel:
        bpp value to use for the framebuffer configuration

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

    :param struct drm_fb_helper \*fb_helper:
        the drm_fb_helper

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

.. This file was automatic generated / don't edit.

