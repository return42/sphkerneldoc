
.. _API-drm-atomic-clean-old-fb:

=======================
drm_atomic_clean_old_fb
=======================

*man drm_atomic_clean_old_fb(9)*

*4.6.0-rc1*

- Unset old_fb pointers and set plane->fb pointers.


Synopsis
========

.. c:function:: void drm_atomic_clean_old_fb( struct drm_device * dev, unsigned plane_mask, int ret )

Arguments
=========

``dev``
    drm device to check.

``plane_mask``
    plane mask for planes that were updated.

``ret``
    return value, can be -EDEADLK for a retry.


Description
===========

Before doing an update plane->old_fb is set to plane->fb, but before dropping the locks old_fb needs to be set to NULL and plane->fb updated. This is a common operation for each
atomic update, so this call is split off as a helper.
