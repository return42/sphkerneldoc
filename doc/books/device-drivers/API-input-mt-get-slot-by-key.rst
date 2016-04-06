
.. _API-input-mt-get-slot-by-key:

========================
input_mt_get_slot_by_key
========================

*man input_mt_get_slot_by_key(9)*

*4.6.0-rc1*

return slot matching key


Synopsis
========

.. c:function:: int input_mt_get_slot_by_key( struct input_dev * dev, int key )

Arguments
=========

``dev``
    input device with allocated MT slots

``key``
    the key of the sought slot


Description
===========

Returns the slot of the given key, if it exists, otherwise set the key on the first unused slot and return.

If no available slot can be found, -1 is returned. Note that for this function to work properly, ``input_mt_sync_frame`` has to be called at each frame.
