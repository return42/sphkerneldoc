
.. _API-drm-edid-is-valid:

=================
drm_edid_is_valid
=================

*man drm_edid_is_valid(9)*

*4.6.0-rc1*

sanity check EDID data


Synopsis
========

.. c:function:: bool drm_edid_is_valid( struct edid * edid )

Arguments
=========

``edid``
    EDID data


Description
===========

Sanity-check an entire EDID record (including extensions)


Return
======

True if the EDID data is valid, false otherwise.
