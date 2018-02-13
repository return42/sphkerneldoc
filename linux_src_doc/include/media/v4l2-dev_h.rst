.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-dev.h

.. _`vfl_devnode_type`:

enum vfl_devnode_type
=====================

.. c:type:: enum vfl_devnode_type

    type of V4L2 device node

.. _`vfl_devnode_type.definition`:

Definition
----------

.. code-block:: c

    enum vfl_devnode_type {
        VFL_TYPE_GRABBER,
        VFL_TYPE_VBI,
        VFL_TYPE_RADIO,
        VFL_TYPE_SUBDEV,
        VFL_TYPE_SDR,
        VFL_TYPE_TOUCH
    };

.. _`vfl_devnode_type.constants`:

Constants
---------

VFL_TYPE_GRABBER
    for video input/output devices

VFL_TYPE_VBI
    for vertical blank data (i.e. closed captions, teletext)

VFL_TYPE_RADIO
    for radio tuners

VFL_TYPE_SUBDEV
    for V4L2 subdevices

VFL_TYPE_SDR
    for Software Defined Radio tuners

VFL_TYPE_TOUCH
    for touch sensors

.. _`vfl_devnode_direction`:

enum vfl_devnode_direction
==========================

.. c:type:: enum vfl_devnode_direction

    Identifies if a \ :c:type:`struct video_device <video_device>`\  corresponds to a receiver, a transmitter or a mem-to-mem device.

.. _`vfl_devnode_direction.definition`:

Definition
----------

.. code-block:: c

    enum vfl_devnode_direction {
        VFL_DIR_RX,
        VFL_DIR_TX,
        VFL_DIR_M2M
    };

.. _`vfl_devnode_direction.constants`:

Constants
---------

VFL_DIR_RX
    device is a receiver.

VFL_DIR_TX
    device is a transmitter.

VFL_DIR_M2M
    device is a memory to memory device.

.. _`vfl_devnode_direction.note`:

Note
----

Ignored if \ :c:type:`enum vfl_devnode_type <vfl_devnode_type>`\  is \ ``VFL_TYPE_SUBDEV``\ .

.. _`v4l2_video_device_flags`:

enum v4l2_video_device_flags
============================

.. c:type:: enum v4l2_video_device_flags

    Flags used by \ :c:type:`struct video_device <video_device>`\ 

.. _`v4l2_video_device_flags.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_video_device_flags {
        V4L2_FL_REGISTERED,
        V4L2_FL_USES_V4L2_FH
    };

.. _`v4l2_video_device_flags.constants`:

Constants
---------

V4L2_FL_REGISTERED
    indicates that a \ :c:type:`struct video_device <video_device>`\  is registered.
    Drivers can clear this flag if they want to block all future
    device access. It is cleared by video_unregister_device.

V4L2_FL_USES_V4L2_FH
    indicates that file->private_data points to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ .
    This flag is set by the core when \ :c:func:`v4l2_fh_init`\  is called.
    All new drivers should use it.

.. _`v4l2_prio_state`:

struct v4l2_prio_state
======================

.. c:type:: struct v4l2_prio_state

    stores the priority states

.. _`v4l2_prio_state.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_prio_state {
        atomic_t prios[4];
    }

.. _`v4l2_prio_state.members`:

Members
-------

prios
    array with elements to store the array priorities

.. _`v4l2_prio_state.description`:

Description
-----------


.. note::
   The size of \ ``prios``\  array matches the number of priority types defined
   by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\ .

.. _`v4l2_prio_init`:

v4l2_prio_init
==============

.. c:function:: void v4l2_prio_init(struct v4l2_prio_state *global)

    initializes a struct v4l2_prio_state

    :param struct v4l2_prio_state \*global:
        pointer to \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\ 

.. _`v4l2_prio_change`:

v4l2_prio_change
================

.. c:function:: int v4l2_prio_change(struct v4l2_prio_state *global, enum v4l2_priority *local, enum v4l2_priority new)

    changes the v4l2 file handler priority

    :param struct v4l2_prio_state \*global:
        pointer to the \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  of the device node.

    :param enum v4l2_priority \*local:
        pointer to the desired priority, as defined by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\ 

    :param enum v4l2_priority new:
        Priority type requested, as defined by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\ .

.. _`v4l2_prio_change.description`:

Description
-----------

.. note::
     This function should be used only by the V4L2 core.

.. _`v4l2_prio_open`:

v4l2_prio_open
==============

.. c:function:: void v4l2_prio_open(struct v4l2_prio_state *global, enum v4l2_priority *local)

    Implements the priority logic for a file handler open

    :param struct v4l2_prio_state \*global:
        pointer to the \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  of the device node.

    :param enum v4l2_priority \*local:
        pointer to the desired priority, as defined by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\ 

.. _`v4l2_prio_open.description`:

Description
-----------

.. note::
     This function should be used only by the V4L2 core.

.. _`v4l2_prio_close`:

v4l2_prio_close
===============

.. c:function:: void v4l2_prio_close(struct v4l2_prio_state *global, enum v4l2_priority local)

    Implements the priority logic for a file handler close

    :param struct v4l2_prio_state \*global:
        pointer to the \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  of the device node.

    :param enum v4l2_priority local:
        priority to be released, as defined by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\ 

.. _`v4l2_prio_close.description`:

Description
-----------

.. note::
     This function should be used only by the V4L2 core.

.. _`v4l2_prio_max`:

v4l2_prio_max
=============

.. c:function:: enum v4l2_priority v4l2_prio_max(struct v4l2_prio_state *global)

    Return the maximum priority, as stored at the \ ``global``\  array.

    :param struct v4l2_prio_state \*global:
        pointer to the \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  of the device node.

.. _`v4l2_prio_max.description`:

Description
-----------

.. note::
     This function should be used only by the V4L2 core.

.. _`v4l2_prio_check`:

v4l2_prio_check
===============

.. c:function:: int v4l2_prio_check(struct v4l2_prio_state *global, enum v4l2_priority local)

    Implements the priority logic for a file handler close

    :param struct v4l2_prio_state \*global:
        pointer to the \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  of the device node.

    :param enum v4l2_priority local:
        desired priority, as defined by enum \ :c:type:`struct v4l2_priority <v4l2_priority>`\  local

.. _`v4l2_prio_check.description`:

Description
-----------

.. note::
     This function should be used only by the V4L2 core.

.. _`v4l2_file_operations`:

struct v4l2_file_operations
===========================

.. c:type:: struct v4l2_file_operations

    fs operations used by a V4L2 device

.. _`v4l2_file_operations.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_file_operations {
        struct module *owner;
        ssize_t (*read) (struct file *, char __user *, size_t, loff_t *);
        ssize_t (*write) (struct file *, const char __user *, size_t, loff_t *);
        __poll_t (*poll) (struct file *, struct poll_table_struct *);
        long (*unlocked_ioctl) (struct file *, unsigned int, unsigned long);
    #ifdef CONFIG_COMPAT
        long (*compat_ioctl32) (struct file *, unsigned int, unsigned long);
    #endif
        unsigned long (*get_unmapped_area) (struct file *, unsigned long, unsigned long, unsigned long, unsigned long);
        int (*mmap) (struct file *, struct vm_area_struct *);
        int (*open) (struct file *);
        int (*release) (struct file *);
    }

.. _`v4l2_file_operations.members`:

Members
-------

owner
    pointer to struct module

read
    operations needed to implement the \ :c:func:`read`\  syscall

write
    operations needed to implement the \ :c:func:`write`\  syscall

poll
    operations needed to implement the \ :c:func:`poll`\  syscall

unlocked_ioctl
    operations needed to implement the \ :c:func:`ioctl`\  syscall

compat_ioctl32
    operations needed to implement the \ :c:func:`ioctl`\  syscall for
    the special case where the Kernel uses 64 bits instructions, but
    the userspace uses 32 bits.

get_unmapped_area
    called by the \ :c:func:`mmap`\  syscall, used when %!CONFIG_MMU

mmap
    operations needed to implement the \ :c:func:`mmap`\  syscall

open
    operations needed to implement the \ :c:func:`open`\  syscall

release
    operations needed to implement the \ :c:func:`release`\  syscall

.. _`v4l2_file_operations.description`:

Description
-----------

.. note::

     Those operations are used to implemente the fs struct file_operations
     at the V4L2 drivers. The V4L2 core overrides the fs ops with some
     extra logic needed by the subsystem.

.. _`video_device`:

struct video_device
===================

.. c:type:: struct video_device

    Structure used to create and manage the V4L2 device nodes.

.. _`video_device.definition`:

Definition
----------

.. code-block:: c

    struct video_device {
    #if defined(CONFIG_MEDIA_CONTROLLER)
        struct media_entity entity;
        struct media_intf_devnode *intf_devnode;
        struct media_pipeline pipe;
    #endif
        const struct v4l2_file_operations *fops;
        u32 device_caps;
        struct device dev;
        struct cdev *cdev;
        struct v4l2_device *v4l2_dev;
        struct device *dev_parent;
        struct v4l2_ctrl_handler *ctrl_handler;
        struct vb2_queue *queue;
        struct v4l2_prio_state *prio;
        char name[32];
        enum vfl_devnode_type vfl_type;
        enum vfl_devnode_direction vfl_dir;
        int minor;
        u16 num;
        unsigned long flags;
        int index;
        spinlock_t fh_lock;
        struct list_head fh_list;
        int dev_debug;
        v4l2_std_id tvnorms;
        void (*release)(struct video_device *vdev);
        const struct v4l2_ioctl_ops *ioctl_ops;
        DECLARE_BITMAP(valid_ioctls, BASE_VIDIOC_PRIVATE);
        DECLARE_BITMAP(disable_locking, BASE_VIDIOC_PRIVATE);
        struct mutex *lock;
    }

.. _`video_device.members`:

Members
-------

entity
    &struct media_entity

intf_devnode
    pointer to \ :c:type:`struct media_intf_devnode <media_intf_devnode>`\ 

pipe
    &struct media_pipeline

fops
    pointer to \ :c:type:`struct v4l2_file_operations <v4l2_file_operations>`\  for the video device

device_caps
    device capabilities as used in v4l2_capabilities

dev
    &struct device for the video device

cdev
    character device

v4l2_dev
    pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\  parent

dev_parent
    pointer to \ :c:type:`struct device <device>`\  parent

ctrl_handler
    Control handler associated with this device node.
    May be NULL.

queue
    &struct vb2_queue associated with this device node. May be NULL.

prio
    pointer to \ :c:type:`struct v4l2_prio_state <v4l2_prio_state>`\  with device's Priority state.
    If NULL, then v4l2_dev->prio will be used.

name
    video device name

vfl_type
    V4L device type, as defined by \ :c:type:`enum vfl_devnode_type <vfl_devnode_type>`\ 

vfl_dir
    V4L receiver, transmitter or m2m

minor
    device node 'minor'. It is set to -1 if the registration failed

num
    number of the video device node

flags
    video device flags. Use bitops to set/clear/test flags.
    Contains a set of \ :c:type:`enum v4l2_video_device_flags <v4l2_video_device_flags>`\ .

index
    attribute to differentiate multiple indices on one physical device

fh_lock
    Lock for all v4l2_fhs

fh_list
    List of \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

dev_debug
    Internal device debug flags, not for use by drivers

tvnorms
    Supported tv norms

release
    video device \ :c:func:`release`\  callback

ioctl_ops
    pointer to \ :c:type:`struct v4l2_ioctl_ops <v4l2_ioctl_ops>`\  with ioctl callbacks

valid_ioctls
    bitmap with the valid ioctls for this device

disable_locking
    bitmap with the ioctls that don't require locking

lock
    pointer to \ :c:type:`struct mutex <mutex>`\  serialization lock

.. _`video_device.description`:

Description
-----------

.. note::
     Only set \ ``dev_parent``\  if that can't be deduced from \ ``v4l2_dev``\ .

.. _`media_entity_to_video_device`:

media_entity_to_video_device
============================

.. c:function::  media_entity_to_video_device( entity)

    Returns a \ :c:type:`struct video_device <video_device>`\  from the \ :c:type:`struct media_entity <media_entity>`\  embedded on it.

    :param  entity:
        pointer to \ :c:type:`struct media_entity <media_entity>`\ 

.. _`to_video_device`:

to_video_device
===============

.. c:function::  to_video_device( cd)

    Returns a \ :c:type:`struct video_device <video_device>`\  from the \ :c:type:`struct device <device>`\  embedded on it.

    :param  cd:
        pointer to \ :c:type:`struct device <device>`\ 

.. _`__video_register_device`:

__video_register_device
=======================

.. c:function:: int __video_register_device(struct video_device *vdev, enum vfl_devnode_type type, int nr, int warn_if_nr_in_use, struct module *owner)

    register video4linux devices

    :param struct video_device \*vdev:
        struct video_device to register

    :param enum vfl_devnode_type type:
        type of device to register, as defined by \ :c:type:`enum vfl_devnode_type <vfl_devnode_type>`\ 

    :param int nr:
        which device node number is desired:
        (0 == /dev/video0, 1 == /dev/video1, ..., -1 == first free)

    :param int warn_if_nr_in_use:
        warn if the desired device node number
        was already in use and another number was chosen instead.

    :param struct module \*owner:
        module that owns the video device node

.. _`__video_register_device.description`:

Description
-----------

The registration code assigns minor numbers and device node numbers
based on the requested type and registers the new device node with
the kernel.

This function assumes that struct video_device was zeroed when it
was allocated and does not contain any stale date.

An error is returned if no free minor or device node number could be
found, or if the registration of the device node failed.

Returns 0 on success.

.. note::

     This function is meant to be used only inside the V4L2 core.
     Drivers should use \ :c:func:`video_register_device`\  or
     \ :c:func:`video_register_device_no_warn`\ .

.. _`video_register_device`:

video_register_device
=====================

.. c:function:: int video_register_device(struct video_device *vdev, enum vfl_devnode_type type, int nr)

    register video4linux devices

    :param struct video_device \*vdev:
        struct video_device to register

    :param enum vfl_devnode_type type:
        type of device to register, as defined by \ :c:type:`enum vfl_devnode_type <vfl_devnode_type>`\ 

    :param int nr:
        which device node number is desired:
        (0 == /dev/video0, 1 == /dev/video1, ..., -1 == first free)

.. _`video_register_device.description`:

Description
-----------

Internally, it calls \ :c:func:`__video_register_device`\ . Please see its
documentation for more details.

.. note::
     if video_register_device fails, the \ :c:func:`release`\  callback of
     \ :c:type:`struct video_device <video_device>`\  structure is *not* called, so the caller
     is responsible for freeing any data. Usually that means that
     you \ :c:func:`video_device_release`\  should be called on failure.

.. _`video_register_device_no_warn`:

video_register_device_no_warn
=============================

.. c:function:: int video_register_device_no_warn(struct video_device *vdev, enum vfl_devnode_type type, int nr)

    register video4linux devices

    :param struct video_device \*vdev:
        struct video_device to register

    :param enum vfl_devnode_type type:
        type of device to register, as defined by \ :c:type:`enum vfl_devnode_type <vfl_devnode_type>`\ 

    :param int nr:
        which device node number is desired:
        (0 == /dev/video0, 1 == /dev/video1, ..., -1 == first free)

.. _`video_register_device_no_warn.description`:

Description
-----------

This function is identical to \ :c:func:`video_register_device`\  except that no
warning is issued if the desired device node number was already in use.

Internally, it calls \ :c:func:`__video_register_device`\ . Please see its
documentation for more details.

.. note::
     if video_register_device fails, the \ :c:func:`release`\  callback of
     \ :c:type:`struct video_device <video_device>`\  structure is *not* called, so the caller
     is responsible for freeing any data. Usually that means that
     you \ :c:func:`video_device_release`\  should be called on failure.

.. _`video_unregister_device`:

video_unregister_device
=======================

.. c:function:: void video_unregister_device(struct video_device *vdev)

    Unregister video devices.

    :param struct video_device \*vdev:
        &struct video_device to register

.. _`video_unregister_device.description`:

Description
-----------

Does nothing if vdev == NULL or if \ :c:func:`video_is_registered`\  returns false.

.. _`video_device_alloc`:

video_device_alloc
==================

.. c:function:: struct video_device *video_device_alloc( void)

    helper function to alloc \ :c:type:`struct video_device <video_device>`\ 

    :param  void:
        no arguments

.. _`video_device_alloc.description`:

Description
-----------

Returns NULL if \ ``-ENOMEM``\  or a \ :c:type:`struct video_device <video_device>`\  on success.

.. _`video_device_release`:

video_device_release
====================

.. c:function:: void video_device_release(struct video_device *vdev)

    helper function to release \ :c:type:`struct video_device <video_device>`\ 

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. _`video_device_release.description`:

Description
-----------

Can also be used for video_device->release(\).

.. _`video_device_release_empty`:

video_device_release_empty
==========================

.. c:function:: void video_device_release_empty(struct video_device *vdev)

    helper function to implement the video_device->release(\) callback.

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. _`video_device_release_empty.description`:

Description
-----------

This release function does nothing.

It should be used when the video_device is a static global struct.

.. note::
     Having a static video_device is a dubious construction at best.

.. _`v4l2_is_known_ioctl`:

v4l2_is_known_ioctl
===================

.. c:function:: bool v4l2_is_known_ioctl(unsigned int cmd)

    Checks if a given cmd is a known V4L ioctl

    :param unsigned int cmd:
        ioctl command

.. _`v4l2_is_known_ioctl.description`:

Description
-----------

returns true if cmd is a known V4L2 ioctl

.. _`v4l2_disable_ioctl`:

v4l2_disable_ioctl
==================

.. c:function:: void v4l2_disable_ioctl(struct video_device *vdev, unsigned int cmd)

    mark that a given command isn't implemented. shouldn't use core locking

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

    :param unsigned int cmd:
        ioctl command

.. _`v4l2_disable_ioctl.description`:

Description
-----------

This function allows drivers to provide just one v4l2_ioctl_ops struct, but
disable ioctls based on the specific card that is actually found.

.. note::

   This must be called before video_register_device.
   See also the comments for \ :c:func:`determine_valid_ioctls`\ .

.. _`video_get_drvdata`:

video_get_drvdata
=================

.. c:function:: void *video_get_drvdata(struct video_device *vdev)

    gets private data from \ :c:type:`struct video_device <video_device>`\ .

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. _`video_get_drvdata.description`:

Description
-----------

returns a pointer to the private data

.. _`video_set_drvdata`:

video_set_drvdata
=================

.. c:function:: void video_set_drvdata(struct video_device *vdev, void *data)

    sets private data from \ :c:type:`struct video_device <video_device>`\ .

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

    :param void \*data:
        private data pointer

.. _`video_devdata`:

video_devdata
=============

.. c:function:: struct video_device *video_devdata(struct file *file)

    gets \ :c:type:`struct video_device <video_device>`\  from struct file.

    :param struct file \*file:
        pointer to struct file

.. _`video_drvdata`:

video_drvdata
=============

.. c:function:: void *video_drvdata(struct file *file)

    gets private data from \ :c:type:`struct video_device <video_device>`\  using the struct file.

    :param struct file \*file:
        pointer to struct file

.. _`video_drvdata.description`:

Description
-----------

This is function combines both \ :c:func:`video_get_drvdata`\  and \ :c:func:`video_devdata`\ 
as this is used very often.

.. _`video_device_node_name`:

video_device_node_name
======================

.. c:function:: const char *video_device_node_name(struct video_device *vdev)

    returns the video device name

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. _`video_device_node_name.description`:

Description
-----------

Returns the device name string

.. _`video_is_registered`:

video_is_registered
===================

.. c:function:: int video_is_registered(struct video_device *vdev)

    returns true if the \ :c:type:`struct video_device <video_device>`\  is registered.

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. This file was automatic generated / don't edit.

