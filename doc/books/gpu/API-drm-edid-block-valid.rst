
.. _API-drm-edid-block-valid:

====================
drm_edid_block_valid
====================

*man drm_edid_block_valid(9)*

*4.6.0-rc1*

Sanity check the EDID block (base or extension)


Synopsis
========

.. c:function:: bool drm_edid_block_valid( u8 * raw_edid, int block, bool print_bad_edid, bool * edid_corrupt )

Arguments
=========

``raw_edid``
    pointer to raw EDID block

``block``
    type of block to validate (0 for base, extension otherwise)

``print_bad_edid``
    if true, dump bad EDID blocks to the console

``edid_corrupt``
    if true, the header or checksum is invalid


Description
===========

Validate a base or extension EDID block and optionally dump bad blocks to the console.


Return
======

True if the block is valid, false otherwise.
