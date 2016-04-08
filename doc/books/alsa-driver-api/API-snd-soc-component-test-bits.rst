
.. _API-snd-soc-component-test-bits:

===========================
snd_soc_component_test_bits
===========================

*man snd_soc_component_test_bits(9)*

*4.6.0-rc1*

Test register for change


Synopsis
========

.. c:function:: int snd_soc_component_test_bits( struct snd_soc_component * component, unsigned int reg, unsigned int mask, unsigned int value )

Arguments
=========

``component``
    component

``reg``
    Register to test

``mask``
    Mask that specifies which bits to test

``value``
    Value to test against


Description
===========

Tests a register with a new value and checks if the new value is different from the old value.


Return
======

1 for change, otherwise 0.
