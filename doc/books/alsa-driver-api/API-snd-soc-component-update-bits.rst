
.. _API-snd-soc-component-update-bits:

=============================
snd_soc_component_update_bits
=============================

*man snd_soc_component_update_bits(9)*

*4.6.0-rc1*

Perform read/modify/write cycle


Synopsis
========

.. c:function:: int snd_soc_component_update_bits( struct snd_soc_component * component, unsigned int reg, unsigned int mask, unsigned int val )

Arguments
=========

``component``
    Component to update

``reg``
    Register to update

``mask``
    Mask that specifies which bits to update

``val``
    New value for the bits specified by mask


Return
======

1 if the operation was successful and the value of the register changed, 0 if the operation was successful, but the value did not change. Returns a negative error code otherwise.
