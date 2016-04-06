
.. _API-drm-gem-cma-describe:

====================
drm_gem_cma_describe
====================

*man drm_gem_cma_describe(9)*

*4.6.0-rc1*

describe a CMA GEM object for debugfs


Synopsis
========

.. c:function:: void drm_gem_cma_describe( struct drm_gem_cma_object * cma_obj, struct seq_file * m )

Arguments
=========

``cma_obj``
    CMA GEM object

``m``
    debugfs file handle


Description
===========

This function can be used to dump a human-readable representation of the CMA GEM object into a synthetic file.
