.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_drv.h

.. _`drm_driver`:

struct drm_driver
=================

.. c:type:: struct drm_driver

    DRM driver structure

.. _`drm_driver.definition`:

Definition
----------

.. code-block:: c

    struct drm_driver {
        int (*load) (struct drm_device *, unsigned long flags);
        int (*open) (struct drm_device *, struct drm_file *);
        void (*postclose) (struct drm_device *, struct drm_file *);
        void (*lastclose) (struct drm_device *);
        void (*unload) (struct drm_device *);
        void (*release) (struct drm_device *);
        u32 (*get_vblank_counter) (struct drm_device *dev, unsigned int pipe);
        int (*enable_vblank) (struct drm_device *dev, unsigned int pipe);
        void (*disable_vblank) (struct drm_device *dev, unsigned int pipe);
        bool (*get_scanout_position) (struct drm_device *dev, unsigned int pipe,bool in_vblank_irq, int *vpos, int *hpos,ktime_t *stime, ktime_t *etime, const struct drm_display_mode *mode);
        bool (*get_vblank_timestamp) (struct drm_device *dev, unsigned int pipe,int *max_error,struct timeval *vblank_time, bool in_vblank_irq);
        irqreturn_t(*irq_handler) (int irq, void *arg);
        void (*irq_preinstall) (struct drm_device *dev);
        int (*irq_postinstall) (struct drm_device *dev);
        void (*irq_uninstall) (struct drm_device *dev);
        int (*master_create)(struct drm_device *dev, struct drm_master *master);
        void (*master_destroy)(struct drm_device *dev, struct drm_master *master);
        int (*master_set)(struct drm_device *dev, struct drm_file *file_priv, bool from_open);
        void (*master_drop)(struct drm_device *dev, struct drm_file *file_priv);
        int (*debugfs_init)(struct drm_minor *minor);
        void (*gem_free_object) (struct drm_gem_object *obj);
        void (*gem_free_object_unlocked) (struct drm_gem_object *obj);
        int (*gem_open_object) (struct drm_gem_object *, struct drm_file *);
        void (*gem_close_object) (struct drm_gem_object *, struct drm_file *);
        struct drm_gem_object *(*gem_create_object)(struct drm_device *dev, size_t size);
        int (*prime_handle_to_fd)(struct drm_device *dev, struct drm_file *file_priv, uint32_t handle, uint32_t flags, int *prime_fd);
        int (*prime_fd_to_handle)(struct drm_device *dev, struct drm_file *file_priv, int prime_fd, uint32_t *handle);
        struct dma_buf * (*gem_prime_export)(struct drm_device *dev, struct drm_gem_object *obj, int flags);
        struct drm_gem_object * (*gem_prime_import)(struct drm_device *dev, struct dma_buf *dma_buf);
        int (*gem_prime_pin)(struct drm_gem_object *obj);
        void (*gem_prime_unpin)(struct drm_gem_object *obj);
        struct reservation_object * (*gem_prime_res_obj)( struct drm_gem_object *obj);
        struct sg_table *(*gem_prime_get_sg_table)(struct drm_gem_object *obj);
        struct drm_gem_object *(*gem_prime_import_sg_table)(struct drm_device *dev,struct dma_buf_attachment *attach, struct sg_table *sgt);
        void *(*gem_prime_vmap)(struct drm_gem_object *obj);
        void (*gem_prime_vunmap)(struct drm_gem_object *obj, void *vaddr);
        int (*gem_prime_mmap)(struct drm_gem_object *obj, struct vm_area_struct *vma);
        int (*dumb_create)(struct drm_file *file_priv,struct drm_device *dev, struct drm_mode_create_dumb *args);
        int (*dumb_map_offset)(struct drm_file *file_priv,struct drm_device *dev, uint32_t handle, uint64_t *offset);
        int (*dumb_destroy)(struct drm_file *file_priv,struct drm_device *dev, uint32_t handle);
        const struct vm_operations_struct *gem_vm_ops;
        int major;
        int minor;
        int patchlevel;
        char *name;
        char *desc;
        char *date;
        u32 driver_features;
        const struct drm_ioctl_desc *ioctls;
        int num_ioctls;
        const struct file_operations *fops;
        struct list_head legacy_dev_list;
        int (*firstopen) (struct drm_device *);
        void (*preclose) (struct drm_device *, struct drm_file *file_priv);
        int (*dma_ioctl) (struct drm_device *dev, void *data, struct drm_file *file_priv);
        int (*dma_quiescent) (struct drm_device *);
        int (*context_dtor) (struct drm_device *dev, int context);
        int dev_priv_size;
    }

.. _`drm_driver.members`:

Members
-------

load

    Backward-compatible driver callback to complete
    initialization steps after the driver is registered.  For
    this reason, may suffer from race conditions and its use is
    deprecated for new drivers.  It is therefore only supported
    for existing drivers not yet converted to the new scheme.
    See \ :c:func:`drm_dev_init`\  and \ :c:func:`drm_dev_register`\  for proper and
    race-free way to set up a \ :c:type:`struct drm_device <drm_device>`\ .

    This is deprecated, do not use!

    Returns:

    Zero on success, non-zero value on failure.

open

    Driver callback when a new \ :c:type:`struct drm_file <drm_file>`\  is opened. Useful for
    setting up driver-private data structures like buffer allocators,
    execution contexts or similar things. Such driver-private resources
    must be released again in \ ``postclose``\ .

    Since the display/modeset side of DRM can only be owned by exactly
    one \ :c:type:`struct drm_file <drm_file>`\  (see \ :c:type:`drm_file.is_master <drm_file>`\  and \ :c:type:`drm_device.master <drm_device>`\ )
    there should never be a need to set up any modeset related resources
    in this callback. Doing so would be a driver design bug.

    Returns:

    0 on success, a negative error code on failure, which will be
    promoted to userspace as the result of the \ :c:func:`open`\  system call.

postclose

    One of the driver callbacks when a new \ :c:type:`struct drm_file <drm_file>`\  is closed.
    Useful for tearing down driver-private data structures allocated in
    \ ``open``\  like buffer allocators, execution contexts or similar things.

    Since the display/modeset side of DRM can only be owned by exactly
    one \ :c:type:`struct drm_file <drm_file>`\  (see \ :c:type:`drm_file.is_master <drm_file>`\  and \ :c:type:`drm_device.master <drm_device>`\ )
    there should never be a need to tear down any modeset related
    resources in this callback. Doing so would be a driver design bug.

lastclose

    Called when the last \ :c:type:`struct drm_file <drm_file>`\  has been closed and there's
    currently no userspace client for the \ :c:type:`struct drm_device <drm_device>`\ .

    Modern drivers should only use this to force-restore the fbdev
    framebuffer using \ :c:func:`drm_fb_helper_restore_fbdev_mode_unlocked`\ .
    Anything else would indicate there's something seriously wrong.
    Modern drivers can also use this to execute delayed power switching
    state changes, e.g. in conjunction with the :ref:`vga_switcheroo`
    infrastructure.

    This is called after \ ``postclose``\  hook has been called.

    NOTE:

    All legacy drivers use this callback to de-initialize the hardware.
    This is purely because of the shadow-attach model, where the DRM
    kernel driver does not really own the hardware. Instead ownershipe is
    handled with the help of userspace through an inheritedly racy dance
    to set/unset the VT into raw mode.

    Legacy drivers initialize the hardware in the \ ``firstopen``\  callback,
    which isn't even called for modern drivers.

unload

    Reverse the effects of the driver load callback.  Ideally,
    the clean up performed by the driver should happen in the
    reverse order of the initialization.  Similarly to the load
    hook, this handler is deprecated and its usage should be
    dropped in favor of an open-coded teardown function at the
    driver layer.  See \ :c:func:`drm_dev_unregister`\  and \ :c:func:`drm_dev_unref`\ 
    for the proper way to remove a \ :c:type:`struct drm_device <drm_device>`\ .

    The \ :c:func:`unload`\  hook is called right after unregistering
    the device.

release

    Optional callback for destroying device data after the final
    reference is released, i.e. the device is being destroyed. Drivers
    using this callback are responsible for calling \ :c:func:`drm_dev_fini`\ 
    to finalize the device and then freeing the struct themselves.

get_vblank_counter

    Driver callback for fetching a raw hardware vblank counter for the
    CRTC specified with the pipe argument.  If a device doesn't have a
    hardware counter, the driver can simply leave the hook as NULL.
    The DRM core will account for missed vblank events while interrupts
    where disabled based on system timestamps.

    Wraparound handling and loss of events due to modesetting is dealt
    with in the DRM core code, as long as drivers call
    \ :c:func:`drm_crtc_vblank_off`\  and \ :c:func:`drm_crtc_vblank_on`\  when disabling or
    enabling a CRTC.

    This is deprecated and should not be used by new drivers.
    Use \ :c:type:`drm_crtc_funcs.get_vblank_counter <drm_crtc_funcs>`\  instead.

    Returns:

    Raw vblank counter value.

enable_vblank

    Enable vblank interrupts for the CRTC specified with the pipe
    argument.

    This is deprecated and should not be used by new drivers.
    Use \ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\  instead.

    Returns:

    Zero on success, appropriate errno if the given \ ``crtc``\ 's vblank
    interrupt cannot be enabled.

disable_vblank

    Disable vblank interrupts for the CRTC specified with the pipe
    argument.

    This is deprecated and should not be used by new drivers.
    Use \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\  instead.

get_scanout_position

    Called by vblank timestamping code.

    Returns the current display scanout position from a crtc, and an
    optional accurate \ :c:func:`ktime_get`\  timestamp of when position was
    measured. Note that this is a helper callback which is only used if a
    driver uses \ :c:func:`drm_calc_vbltimestamp_from_scanoutpos`\  for the
    \ ``get_vblank_timestamp``\  callback.

    Parameters:

    dev:
        DRM device.
    pipe:
        Id of the crtc to query.
    in_vblank_irq:
        True when called from \ :c:func:`drm_crtc_handle_vblank`\ .  Some drivers
        need to apply some workarounds for gpu-specific vblank irq quirks
        if flag is set.
    vpos:
        Target location for current vertical scanout position.
    hpos:
        Target location for current horizontal scanout position.
    stime:
        Target location for timestamp taken immediately before
        scanout position query. Can be NULL to skip timestamp.
    etime:
        Target location for timestamp taken immediately after
        scanout position query. Can be NULL to skip timestamp.
    mode:
        Current display timings.

    Returns vpos as a positive number while in active scanout area.
    Returns vpos as a negative number inside vblank, counting the number
    of scanlines to go until end of vblank, e.g., -1 means "one scanline
    until start of active scanout / end of vblank."

    Returns:

    True on success, false if a reliable scanout position counter could
    not be read out.

    FIXME:

    Since this is a helper to implement \ ``get_vblank_timestamp``\ , we should
    move it to \ :c:type:`struct drm_crtc_helper_funcs <drm_crtc_helper_funcs>`\ , like all the other
    helper-internal hooks.

get_vblank_timestamp

    Called by \ :c:func:`drm_get_last_vbltimestamp`\ . Should return a precise
    timestamp when the most recent VBLANK interval ended or will end.

    Specifically, the timestamp in \ ``vblank_time``\  should correspond as
    closely as possible to the time when the first video scanline of
    the video frame after the end of VBLANK will start scanning out,
    the time immediately after end of the VBLANK interval. If the
    \ ``crtc``\  is currently inside VBLANK, this will be a time in the future.
    If the \ ``crtc``\  is currently scanning out a frame, this will be the
    past start time of the current scanout. This is meant to adhere
    to the OpenML OML_sync_control extension specification.

    Paramters:

    dev:
        dev DRM device handle.
    pipe:
        crtc for which timestamp should be returned.
    max_error:
        Maximum allowable timestamp error in nanoseconds.
        Implementation should strive to provide timestamp
        with an error of at most max_error nanoseconds.
        Returns true upper bound on error for timestamp.
    vblank_time:
        Target location for returned vblank timestamp.
    in_vblank_irq:
        True when called from \ :c:func:`drm_crtc_handle_vblank`\ .  Some drivers
        need to apply some workarounds for gpu-specific vblank irq quirks
        if flag is set.

    Returns:

    True on success, false on failure, which means the core should
    fallback to a simple timestamp taken in \ :c:func:`drm_crtc_handle_vblank`\ .

    FIXME:

    We should move this hook to \ :c:type:`struct drm_crtc_funcs <drm_crtc_funcs>`\  like all the other
    vblank hooks.

irq_handler

    Interrupt handler called when using \ :c:func:`drm_irq_install`\ . Not used by
    drivers which implement their own interrupt handling.

irq_preinstall

    Optional callback used by \ :c:func:`drm_irq_install`\  which is called before
    the interrupt handler is registered. This should be used to clear out
    any pending interrupts (from e.g. firmware based drives) and reset
    the interrupt handling registers.

irq_postinstall

    Optional callback used by \ :c:func:`drm_irq_install`\  which is called after
    the interrupt handler is registered. This should be used to enable
    interrupt generation in the hardware.

irq_uninstall

    Optional callback used by \ :c:func:`drm_irq_uninstall`\  which is called before
    the interrupt handler is unregistered. This should be used to disable
    interrupt generation in the hardware.

master_create

    Called whenever a new master is created. Only used by vmwgfx.

master_destroy

    Called whenever a master is destroyed. Only used by vmwgfx.

master_set

    Called whenever the minor master is set. Only used by vmwgfx.

master_drop

    Called whenever the minor master is dropped. Only used by vmwgfx.

debugfs_init

    Allows drivers to create driver-specific debugfs files.

gem_free_object
    deconstructor for drm_gem_objects
    This is deprecated and should not be used by new drivers. Use
    \ ``gem_free_object_unlocked``\  instead.

gem_free_object_unlocked
    deconstructor for drm_gem_objects
    This is for drivers which are not encumbered with \ :c:type:`drm_device.struct_mutex <drm_device>`\ 
    legacy locking schemes. Use this hook instead of \ ``gem_free_object``\ .

gem_open_object

    Driver hook called upon gem handle creation

gem_close_object

    Driver hook called upon gem handle release

gem_create_object
    constructor for gem objects
    Hook for allocating the GEM object struct, for use by core
    helpers.

prime_handle_to_fd

    export handle -> fd (see \ :c:func:`drm_gem_prime_handle_to_fd`\  helper)

prime_fd_to_handle

    import fd -> handle (see \ :c:func:`drm_gem_prime_fd_to_handle`\  helper)

gem_prime_export

    export GEM -> dmabuf

gem_prime_import

    import dmabuf -> GEM

gem_prime_pin
    *undescribed*

gem_prime_unpin
    *undescribed*

gem_prime_res_obj
    *undescribed*

gem_prime_get_sg_table
    *undescribed*

gem_prime_import_sg_table
    *undescribed*

gem_prime_vmap
    *undescribed*

gem_prime_vunmap
    *undescribed*

gem_prime_mmap
    *undescribed*

dumb_create

    This creates a new dumb buffer in the driver's backing storage manager (GEM,
    TTM or something else entirely) and returns the resulting buffer handle. This
    handle can then be wrapped up into a framebuffer modeset object.

    Note that userspace is not allowed to use such objects for render
    acceleration - drivers must create their own private ioctls for such a use
    case.

    Width, height and depth are specified in the \ :c:type:`struct drm_mode_create_dumb <drm_mode_create_dumb>`\ 
    argument. The callback needs to fill the handle, pitch and size for
    the created buffer.

    Called by the user via ioctl.

    Returns:

    Zero on success, negative errno on failure.

dumb_map_offset

    Allocate an offset in the drm device node's address space to be able to
    memory map a dumb buffer. GEM-based drivers must use
    \ :c:func:`drm_gem_create_mmap_offset`\  to implement this.

    Called by the user via ioctl.

    Returns:

    Zero on success, negative errno on failure.

dumb_destroy

    This destroys the userspace handle for the given dumb backing storage buffer.
    Since buffer objects must be reference counted in the kernel a buffer object
    won't be immediately freed if a framebuffer modeset object still uses it.

    Called by the user via ioctl.

    Returns:

    Zero on success, negative errno on failure.

gem_vm_ops
    Driver private ops for this object

major
    driver major number

minor
    driver minor number

patchlevel
    driver patch level

name
    driver name

desc
    driver description

date
    driver date

driver_features
    driver features

ioctls

    Array of driver-private IOCTL description entries. See the chapter on
    :ref:`IOCTL support in the userland interfaces
    chapter<drm_driver_ioctl>` for the full details.

num_ioctls
    Number of entries in \ ``ioctls``\ .

fops

    File operations for the DRM device node. See the discussion in
    :ref:`file operations<drm_driver_fops>` for in-depth coverage and
    some examples.

legacy_dev_list
    *undescribed*

firstopen
    *undescribed*

preclose
    *undescribed*

dma_ioctl
    *undescribed*

dma_quiescent
    *undescribed*

context_dtor
    *undescribed*

dev_priv_size
    *undescribed*

.. _`drm_driver.description`:

Description
-----------

This structure represent the common code for a family of cards. There will
one drm_device for each card present in this family. It contains lots of
vfunc entries, and a pile of those probably should be moved to more
appropriate places like \ :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`\  or into a new operations
structure for GEM drivers.

.. _`drm_dev_is_unplugged`:

drm_dev_is_unplugged
====================

.. c:function:: int drm_dev_is_unplugged(struct drm_device *dev)

    is a DRM device unplugged

    :param struct drm_device \*dev:
        DRM device

.. _`drm_dev_is_unplugged.description`:

Description
-----------

This function can be called to check whether a hotpluggable is unplugged.
Unplugging itself is singalled through \ :c:func:`drm_dev_unplug`\ . If a device is
unplugged, these two functions guarantee that any store before calling
\ :c:func:`drm_dev_unplug`\  is visible to callers of this function after it completes

.. This file was automatic generated / don't edit.

