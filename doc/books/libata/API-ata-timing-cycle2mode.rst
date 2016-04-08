
.. _API-ata-timing-cycle2mode:

=====================
ata_timing_cycle2mode
=====================

*man ata_timing_cycle2mode(9)*

*4.6.0-rc1*

find xfer mode for the specified cycle duration


Synopsis
========

.. c:function:: u8 ata_timing_cycle2mode( unsigned int xfer_shift, int cycle )

Arguments
=========

``xfer_shift``
    ATA_SHIFT_⋆ value for transfer type to examine.

``cycle``
    cycle duration in ns


Description
===========

Return matching xfer mode for ``cycle``. The returned mode is of the transfer type specified by ``xfer_shift``. If ``cycle`` is too slow for ``xfer_shift``, 0xff is returned. If
``cycle`` is faster than the fastest known mode, the fasted mode is returned.


LOCKING
=======

None.


RETURNS
=======

Matching xfer_mode, 0xff if no match found.
