
.. _API-input-mt-sync-frame:

===================
input_mt_sync_frame
===================

*man input_mt_sync_frame(9)*

*4.6.0-rc1*

synchronize mt frame


Synopsis
========

.. c:function:: void input_mt_sync_frame( struct input_dev * dev )

Arguments
=========

``dev``
    input device with allocated MT slots


Description
===========

Close the frame and prepare the internal state for a new one. Depending on the flags, marks unused slots as inactive and performs pointer emulation.
