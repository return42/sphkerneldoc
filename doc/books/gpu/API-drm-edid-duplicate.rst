
.. _API-drm-edid-duplicate:

==================
drm_edid_duplicate
==================

*man drm_edid_duplicate(9)*

*4.6.0-rc1*

duplicate an EDID and the extensions


Synopsis
========

.. c:function:: struct edid ⋆ drm_edid_duplicate( const struct edid * edid )

Arguments
=========

``edid``
    EDID to duplicate


Return
======

Pointer to duplicated EDID or NULL on allocation failure.
