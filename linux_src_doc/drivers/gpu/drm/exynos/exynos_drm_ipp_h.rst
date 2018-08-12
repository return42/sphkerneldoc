.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos_drm_ipp.h

.. _`exynos_drm_ipp_funcs`:

struct exynos_drm_ipp_funcs
===========================

.. c:type:: struct exynos_drm_ipp_funcs

    exynos_drm_ipp control functions

.. _`exynos_drm_ipp_funcs.definition`:

Definition
----------

.. code-block:: c

    struct exynos_drm_ipp_funcs {
        int (*commit)(struct exynos_drm_ipp *ipp, struct exynos_drm_ipp_task *task);
        void (*abort)(struct exynos_drm_ipp *ipp, struct exynos_drm_ipp_task *task);
    }

.. _`exynos_drm_ipp_funcs.members`:

Members
-------

commit

    This is the main entry point to start framebuffer processing
    in the hardware. The exynos_drm_ipp_task has been already validated.
    This function must not wait until the device finishes processing.
    When the driver finishes processing, it has to call
    \ :c:func:`exynos_exynos_drm_ipp_task_done`\  function.

    RETURNS:

    0 on success or negative error codes in case of failure.

abort

    Informs the driver that it has to abort the currently running
    task as soon as possible (i.e. as soon as it can stop the device
    safely), even if the task would not have been finished by then.
    After the driver performs the necessary steps, it has to call
    \ :c:func:`exynos_drm_ipp_task_done`\  (as if the task ended normally).
    This function does not have to (and will usually not) wait
    until the device enters a state when it can be stopped.

.. _`exynos_drm_ipp`:

struct exynos_drm_ipp
=====================

.. c:type:: struct exynos_drm_ipp

    central picture processor module structure

.. _`exynos_drm_ipp.definition`:

Definition
----------

.. code-block:: c

    struct exynos_drm_ipp {
        struct drm_device *dev;
        struct list_head head;
        unsigned int id;
        const char *name;
        const struct exynos_drm_ipp_funcs *funcs;
        unsigned int capabilities;
        const struct exynos_drm_ipp_formats *formats;
        unsigned int num_formats;
        atomic_t sequence;
        spinlock_t lock;
        struct exynos_drm_ipp_task *task;
        struct list_head todo_list;
        wait_queue_head_t done_wq;
    }

.. _`exynos_drm_ipp.members`:

Members
-------

dev
    *undescribed*

head
    *undescribed*

id
    *undescribed*

name
    *undescribed*

funcs
    *undescribed*

capabilities
    *undescribed*

formats
    *undescribed*

num_formats
    *undescribed*

sequence
    *undescribed*

lock
    *undescribed*

task
    *undescribed*

todo_list
    *undescribed*

done_wq
    *undescribed*

.. _`exynos_drm_ipp_task`:

struct exynos_drm_ipp_task
==========================

.. c:type:: struct exynos_drm_ipp_task

    a structure describing transformation that has to be performed by the picture processor hardware module

.. _`exynos_drm_ipp_task.definition`:

Definition
----------

.. code-block:: c

    struct exynos_drm_ipp_task {
        struct drm_device *dev;
        struct exynos_drm_ipp *ipp;
        struct list_head head;
        struct exynos_drm_ipp_buffer src;
        struct exynos_drm_ipp_buffer dst;
        struct drm_exynos_ipp_task_transform transform;
        struct drm_exynos_ipp_task_alpha alpha;
        struct work_struct cleanup_work;
        unsigned int flags;
        int ret;
        struct drm_pending_exynos_ipp_event *event;
    }

.. _`exynos_drm_ipp_task.members`:

Members
-------

dev
    *undescribed*

ipp
    *undescribed*

head
    *undescribed*

src
    *undescribed*

dst
    *undescribed*

transform
    *undescribed*

alpha
    *undescribed*

cleanup_work
    *undescribed*

flags
    *undescribed*

ret
    *undescribed*

event
    *undescribed*

.. This file was automatic generated / don't edit.

