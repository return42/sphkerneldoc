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
        int (*load)(struct drm_device *, unsigned long flags);
        int (*firstopen)(struct drm_device *);
        int (*open)(struct drm_device *, struct drm_file *);
        void (*preclose)(struct drm_device *, struct drm_file *file_priv);
        void (*postclose)(struct drm_device *, struct drm_file *);
        void (*lastclose)(struct drm_device *);
        int (*unload)(struct drm_device *);
        int (*dma_ioctl)(struct drm_device *dev, void *data, struct drm_file *file_priv);
        int (*dma_quiescent)(struct drm_device *);
        int (*context_dtor)(struct drm_device *dev, int context);
        int (*set_busid)(struct drm_device *dev, struct drm_master *master);
        u32 (*get_vblank_counter)(struct drm_device *dev, unsigned int pipe);
        int (*enable_vblank)(struct drm_device *dev, unsigned int pipe);
        void (*disable_vblank)(struct drm_device *dev, unsigned int pipe);
        int (*device_is_agp)(struct drm_device *dev);
        int (*get_scanout_position)(struct drm_device *dev, unsigned int pipe,unsigned int flags, int *vpos, int *hpos,ktime_t *stime, ktime_t *etime,const struct drm_display_mode *mode);
        int (*get_vblank_timestamp)(struct drm_device *dev, unsigned int pipe,int *max_error,struct timeval *vblank_time,unsigned flags);
        irqreturn_t(*irq_handler)(int irq, void *arg);
        void (*irq_preinstall)(struct drm_device *dev);
        int (*irq_postinstall)(struct drm_device *dev);
        void (*irq_uninstall)(struct drm_device *dev);
        int (*master_create)(struct drm_device *dev, struct drm_master *master);
        void (*master_destroy)(struct drm_device *dev, struct drm_master *master);
        int (*master_set)(struct drm_device *dev, struct drm_file *file_priv,bool from_open);
        void (*master_drop)(struct drm_device *dev, struct drm_file *file_priv);
        int (*debugfs_init)(struct drm_minor *minor);
        void (*debugfs_cleanup)(struct drm_minor *minor);
        void (*gem_free_object)(struct drm_gem_object *obj);
        void (*gem_free_object_unlocked)(struct drm_gem_object *obj);
        int (*gem_open_object)(struct drm_gem_object *, struct drm_file *);
        void (*gem_close_object)(struct drm_gem_object *, struct drm_file *);
        struct drm_gem_object *(*gem_create_object)(struct drm_device *dev,size_t size);
        int (*prime_handle_to_fd)(struct drm_device *dev, struct drm_file *file_priv,uint32_t handle, uint32_t flags, int *prime_fd);
        int (*prime_fd_to_handle)(struct drm_device *dev, struct drm_file *file_priv,int prime_fd, uint32_t *handle);
        struct dma_buf * (*gem_prime_export)(struct drm_device *dev,struct drm_gem_object *obj, int flags);
        struct drm_gem_object * (*gem_prime_import)(struct drm_device *dev,struct dma_buf *dma_buf);
        int (*gem_prime_pin)(struct drm_gem_object *obj);
        void (*gem_prime_unpin)(struct drm_gem_object *obj);
        struct reservation_object * (*gem_prime_res_obj)(struct drm_gem_object *obj);
        struct sg_table *(*gem_prime_get_sg_table)(struct drm_gem_object *obj);
        struct drm_gem_object *(*gem_prime_import_sg_table)(struct drm_device *dev,struct dma_buf_attachment *attach,struct sg_table *sgt);
        void *(*gem_prime_vmap)(struct drm_gem_object *obj);
        void (*gem_prime_vunmap)(struct drm_gem_object *obj, void *vaddr);
        int (*gem_prime_mmap)(struct drm_gem_object *obj,struct vm_area_struct *vma);
        void (*vgaarb_irq)(struct drm_device *dev, bool state);
        int (*dumb_create)(struct drm_file *file_priv,struct drm_device *dev,struct drm_mode_create_dumb *args);
        int (*dumb_map_offset)(struct drm_file *file_priv,struct drm_device *dev, uint32_t handle,uint64_t *offset);
        int (*dumb_destroy)(struct drm_file *file_priv,struct drm_device *dev,uint32_t handle);
        const struct vm_operations_struct *gem_vm_ops;
        int major;
        int minor;
        int patchlevel;
        char *name;
        char *desc;
        char *date;
        u32 driver_features;
        int dev_priv_size;
        const struct drm_ioctl_desc *ioctls;
        int num_ioctls;
        const struct file_operations *fops;
        struct list_head legacy_dev_list;
    }

.. _`drm_driver.members`:

Members
-------

load
    *undescribed*

firstopen
    *undescribed*

open
    *undescribed*

preclose
    *undescribed*

postclose
    *undescribed*

lastclose
    *undescribed*

unload
    *undescribed*

dma_ioctl
    *undescribed*

dma_quiescent
    *undescribed*

context_dtor
    *undescribed*

set_busid
    *undescribed*

get_vblank_counter

    Driver callback for fetching a raw hardware vblank counter for the
    CRTC specified with the pipe argument.  If a device doesn't have a
    hardware counter, the driver can simply use
    \ :c:func:`drm_vblank_no_hw_counter`\  function. The DRM core will account for
    missed vblank events while interrupts where disabled based on system
    timestamps.

    Wraparound handling and loss of events due to modesetting is dealt
    with in the DRM core code, as long as drivers call
    \ :c:func:`drm_crtc_vblank_off`\  and \ :c:func:`drm_crtc_vblank_on`\  when disabling or
    enabling a CRTC.

    Returns:

    Raw vblank counter value.

enable_vblank

    Enable vblank interrupts for the CRTC specified with the pipe
    argument.

    Returns:

    Zero on success, appropriate errno if the given \ ``crtc``\ 's vblank
    interrupt cannot be enabled.

disable_vblank

    Disable vblank interrupts for the CRTC specified with the pipe
    argument.

device_is_agp

    Called by \ :c:func:`drm_device_is_agp`\ .  Typically used to determine if a card
    is really attached to AGP or not.

    Returns:

    One of three values is returned depending on whether or not the
    card is absolutely not AGP (return of 0), absolutely is AGP
    (return of 1), or may or may not be AGP (return of 2).

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
    flags:
        Flags from the caller (DRM_CALLED_FROM_VBLIRQ or 0).
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

    Flags, or'ed together as follows:

    DRM_SCANOUTPOS_VALID:
        Query successful.
    DRM_SCANOUTPOS_INVBL:
        Inside vblank.
    DRM_SCANOUTPOS_ACCURATE: Returned position is accurate. A lack of
        this flag means that returned position may be offset by a
        constant but unknown small number of scanlines wrt. real scanout
        position.

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
    flags:
        0 = Defaults, no special treatment needed.
        DRM_CALLED_FROM_VBLIRQ = Function is called from vblank
        irq handler. Some drivers need to apply some workarounds
        for gpu-specific vblank irq quirks if flag is set.

    Returns:

    Zero if timestamping isn't supported in current display mode or a
    negative number on failure. A positive status code on success,
    which describes how the vblank_time timestamp was computed.

irq_handler
    *undescribed*

irq_preinstall
    *undescribed*

irq_postinstall
    *undescribed*

irq_uninstall
    *undescribed*

master_create

    Called whenever a new master is created. Only used by vmwgfx.

master_destroy

    Called whenever a master is destroyed. Only used by vmwgfx.

master_set

    Called whenever the minor master is set. Only used by vmwgfx.

master_drop

    Called whenever the minor master is dropped. Only used by vmwgfx.

debugfs_init
    *undescribed*

debugfs_cleanup
    *undescribed*

gem_free_object
    deconstructor for drm_gem_objects
    This is deprecated and should not be used by new drivers. Use
    \ ``gem_free_object_unlocked``\  instead.

gem_free_object_unlocked
    deconstructor for drm_gem_objects
    This is for drivers which are not encumbered with dev->struct_mutex
    legacy locking schemes. Use this hook instead of \ ``gem_free_object``\ .

gem_open_object
    *undescribed*

gem_close_object
    *undescribed*

gem_create_object
    constructor for gem objects
    Hook for allocating the GEM object struct, for use by core
    helpers.

prime_handle_to_fd
    *undescribed*

prime_fd_to_handle
    *undescribed*

gem_prime_export
    *undescribed*

gem_prime_import
    *undescribed*

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

vgaarb_irq
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
    *undescribed*

major
    *undescribed*

minor
    *undescribed*

patchlevel
    *undescribed*

name
    *undescribed*

desc
    *undescribed*

date
    *undescribed*

driver_features
    *undescribed*

dev_priv_size
    *undescribed*

ioctls
    *undescribed*

num_ioctls
    *undescribed*

fops
    *undescribed*

legacy_dev_list
    *undescribed*

.. _`drm_driver.description`:

Description
-----------

This structure represent the common code for a family of cards. There will
one drm_device for each card present in this family. It contains lots of
vfunc entries, and a pile of those probably should be moved to more
appropriate places like \ :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`\  or into a new operations
structure for GEM drivers.

.. This file was automatic generated / don't edit.

