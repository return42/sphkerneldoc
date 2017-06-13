.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-fh.h

.. _`v4l2_fh`:

struct v4l2_fh
==============

.. c:type:: struct v4l2_fh

    Describes a V4L2 file handler

.. _`v4l2_fh.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fh {
        struct list_head list;
        struct video_device *vdev;
        struct v4l2_ctrl_handler *ctrl_handler;
        enum v4l2_priority prio;
        wait_queue_head_t wait;
        struct list_head subscribed;
        struct list_head available;
        unsigned int navailable;
        u32 sequence;
    #if IS_ENABLED(CONFIG_V4L2_MEM2MEM_DEV)
        struct v4l2_m2m_ctx *m2m_ctx;
    #endif
    }

.. _`v4l2_fh.members`:

Members
-------

list
    list of file handlers

vdev
    pointer to \ :c:type:`struct video_device <video_device>`\ 

ctrl_handler
    pointer to \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 

prio
    priority of the file handler, as defined by \ :c:type:`enum v4l2_priority <v4l2_priority>`\ 

wait
    event' s wait queue

subscribed
    list of subscribed events

available
    list of events waiting to be dequeued

navailable
    number of available events at \ ``available``\  list

sequence
    event sequence number

m2m_ctx
    pointer to \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_fh_init`:

v4l2_fh_init
============

.. c:function:: void v4l2_fh_init(struct v4l2_fh *fh, struct video_device *vdev)

    Initialise the file handle.

    :param struct v4l2_fh \*fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

    :param struct video_device \*vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 

.. _`v4l2_fh_init.description`:

Description
-----------

Parts of the V4L2 framework using the
file handles should be initialised in this function. Must be called
from driver's v4l2_file_operations->open(\) handler if the driver
uses \ :c:type:`struct v4l2_fh <v4l2_fh>`\ .

.. _`v4l2_fh_add`:

v4l2_fh_add
===========

.. c:function:: void v4l2_fh_add(struct v4l2_fh *fh)

    Add the fh to the list of file handles on a video_device.

    :param struct v4l2_fh \*fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

.. _`v4l2_fh_add.description`:

Description
-----------

.. note::
   The \ ``fh``\  file handle must be initialised first.

.. _`v4l2_fh_open`:

v4l2_fh_open
============

.. c:function:: int v4l2_fh_open(struct file *filp)

    Ancillary routine that can be used as the open(\) op of v4l2_file_operations.

    :param struct file \*filp:
        pointer to struct file

.. _`v4l2_fh_open.description`:

Description
-----------

It allocates a v4l2_fh and inits and adds it to the \ :c:type:`struct video_device <video_device>`\ 
associated with the file pointer.

.. _`v4l2_fh_del`:

v4l2_fh_del
===========

.. c:function:: void v4l2_fh_del(struct v4l2_fh *fh)

    Remove file handle from the list of file handles.

    :param struct v4l2_fh \*fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

.. _`v4l2_fh_del.description`:

Description
-----------

On error filp->private_data will be \ ``NULL``\ , otherwise it will point to
the \ :c:type:`struct v4l2_fh <v4l2_fh>`\ .

.. note::
   Must be called in v4l2_file_operations->release(\) handler if the driver
   uses \ :c:type:`struct v4l2_fh <v4l2_fh>`\ .

.. _`v4l2_fh_exit`:

v4l2_fh_exit
============

.. c:function:: void v4l2_fh_exit(struct v4l2_fh *fh)

    Release resources related to a file handle.

    :param struct v4l2_fh \*fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

.. _`v4l2_fh_exit.description`:

Description
-----------

Parts of the V4L2 framework using the v4l2_fh must release their
resources here, too.

.. note::
   Must be called in v4l2_file_operations->release(\) handler if the
   driver uses \ :c:type:`struct v4l2_fh <v4l2_fh>`\ .

.. _`v4l2_fh_release`:

v4l2_fh_release
===============

.. c:function:: int v4l2_fh_release(struct file *filp)

    Ancillary routine that can be used as the release(\) op of v4l2_file_operations.

    :param struct file \*filp:
        pointer to struct file

.. _`v4l2_fh_release.description`:

Description
-----------

It deletes and exits the v4l2_fh associated with the file pointer and
frees it. It will do nothing if filp->private_data (the pointer to the
v4l2_fh struct) is \ ``NULL``\ .

This function always returns 0.

.. _`v4l2_fh_is_singular`:

v4l2_fh_is_singular
===================

.. c:function:: int v4l2_fh_is_singular(struct v4l2_fh *fh)

    Returns 1 if this filehandle is the only filehandle opened for the associated video_device.

    :param struct v4l2_fh \*fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 

.. _`v4l2_fh_is_singular.description`:

Description
-----------

If \ ``fh``\  is NULL, then it returns 0.

.. _`v4l2_fh_is_singular_file`:

v4l2_fh_is_singular_file
========================

.. c:function:: int v4l2_fh_is_singular_file(struct file *filp)

    Returns 1 if this filehandle is the only filehandle opened for the associated video_device.

    :param struct file \*filp:
        pointer to struct file

.. _`v4l2_fh_is_singular_file.description`:

Description
-----------

This is a helper function variant of \ :c:func:`v4l2_fh_is_singular`\  with uses
struct file as argument.

If filp->private_data is \ ``NULL``\ , then it will return 0.

.. This file was automatic generated / don't edit.

