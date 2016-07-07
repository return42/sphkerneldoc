.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_sa.c

.. _`radeon_sa_event`:

radeon_sa_event
===============

.. c:function:: bool radeon_sa_event(struct radeon_sa_manager *sa_manager, unsigned size, unsigned align)

    Check if we can stop waiting

    :param struct radeon_sa_manager \*sa_manager:
        pointer to the sa_manager

    :param unsigned size:
        number of bytes we want to allocate

    :param unsigned align:
        alignment we need to match

.. _`radeon_sa_event.description`:

Description
-----------

Check if either there is a fence we can wait for or
enough free memory to satisfy the allocation directly

.. This file was automatic generated / don't edit.

