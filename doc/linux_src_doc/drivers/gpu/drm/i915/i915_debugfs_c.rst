.. -*- coding: utf-8; mode: rst -*-

==============
i915_debugfs.c
==============


.. _`i915_debugfs_connector_add`:

i915_debugfs_connector_add
==========================

.. c:function:: int i915_debugfs_connector_add (struct drm_connector *connector)

    add i915 specific connector debugfs files

    :param struct drm_connector \*connector:
        pointer to a registered drm_connector



.. _`i915_debugfs_connector_add.description`:

Description
-----------

Cleanup will be done by :c:func:`drm_connector_unregister` through a call to
:c:func:`drm_debugfs_connector_remove`.

Returns 0 on success, negative error codes on error.

