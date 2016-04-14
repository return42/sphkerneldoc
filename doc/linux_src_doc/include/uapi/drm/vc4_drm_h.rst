.. -*- coding: utf-8; mode: rst -*-

=========
vc4_drm.h
=========

.. _`drm_vc4_submit_cl`:

struct drm_vc4_submit_cl
========================

.. c:type:: struct drm_vc4_submit_cl

    ioctl argument for submitting commands to the 3D engine.



Definition
----------

.. code-block:: c

  struct drm_vc4_submit_cl {
    #define VC4_SUBMIT_CL_USE_CLEAR_COLOR			(1 \\\lt;\\\lt; 0)
  };



Members
-------



Description
-----------


Drivers typically use GPU BOs to store batchbuffers / command lists and
their associated state.  However, because the VC4 lacks an MMU, we have to
do validation of memory accesses by the GPU commands.  If we were to store
our commands in BOs, we'd need to do uncached readback from them to do the
validation process, which is too expensive.  Instead, userspace accumulates
commands and associated state in plain memory, then the kernel copies the
data to its own address space, and then validates and stores it in a GPU
BO.


.. _`drm_vc4_wait_seqno`:

struct drm_vc4_wait_seqno
=========================

.. c:type:: struct drm_vc4_wait_seqno

    ioctl argument for waiting for DRM_VC4_SUBMIT_CL completion using its returned seqno.



Definition
----------

.. code-block:: c

  struct drm_vc4_wait_seqno {
  };



Members
-------



Description
-----------


timeout_ns is the timeout in nanoseconds, where "0" means "don't
block, just return the status."


.. _`drm_vc4_wait_bo`:

struct drm_vc4_wait_bo
======================

.. c:type:: struct drm_vc4_wait_bo

    ioctl argument for waiting for completion of the last DRM_VC4_SUBMIT_CL on a BO.



Definition
----------

.. code-block:: c

  struct drm_vc4_wait_bo {
  };



Members
-------



Description
-----------


This is useful for cases where multiple processes might be
rendering to a BO and you want to wait for all rendering to be
completed.


.. _`drm_vc4_create_bo`:

struct drm_vc4_create_bo
========================

.. c:type:: struct drm_vc4_create_bo

    ioctl argument for creating VC4 BOs.



Definition
----------

.. code-block:: c

  struct drm_vc4_create_bo {
  };



Members
-------



Description
-----------


There are currently no values for the flags argument, but it may be
used in a future extension.


.. _`drm_vc4_mmap_bo`:

struct drm_vc4_mmap_bo
======================

.. c:type:: struct drm_vc4_mmap_bo

    ioctl argument for mapping VC4 BOs.



Definition
----------

.. code-block:: c

  struct drm_vc4_mmap_bo {
  };



Members
-------



Description
-----------


This doesn't actually perform an mmap.  Instead, it returns the
offset you need to use in an mmap on the DRM device node.  This
means that tools like valgrind end up knowing about the mapped
memory.

There are currently no values for the flags argument, but it may be
used in a future extension.


.. _`drm_vc4_create_shader_bo`:

struct drm_vc4_create_shader_bo
===============================

.. c:type:: struct drm_vc4_create_shader_bo

    ioctl argument for creating VC4 shader BOs.



Definition
----------

.. code-block:: c

  struct drm_vc4_create_shader_bo {
  };



Members
-------



Description
-----------


Since allowing a shader to be overwritten while it's also being
executed from would allow privlege escalation, shaders must be
created using this ioctl, and they can't be mmapped later.


.. _`drm_vc4_get_hang_state`:

struct drm_vc4_get_hang_state
=============================

.. c:type:: struct drm_vc4_get_hang_state

    ioctl argument for collecting state from a GPU hang for analysis.



Definition
----------

.. code-block:: c

  struct drm_vc4_get_hang_state {
  };



Members
-------


