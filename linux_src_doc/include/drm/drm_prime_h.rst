.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_prime.h

.. _`drm_prime_file_private`:

struct drm_prime_file_private
=============================

.. c:type:: struct drm_prime_file_private

    per-file tracking for PRIME

.. _`drm_prime_file_private.definition`:

Definition
----------

.. code-block:: c

    struct drm_prime_file_private {
         void;
    }

.. _`drm_prime_file_private.members`:

Members
-------

void
    no arguments

.. _`drm_prime_file_private.description`:

Description
-----------

This just contains the internal \ :c:type:`struct dma_buf <dma_buf>`\  and handle caches for each
\ :c:type:`struct drm_file <drm_file>`\  used by the PRIME core code.

.. This file was automatic generated / don't edit.

