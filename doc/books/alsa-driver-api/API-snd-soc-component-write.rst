
.. _API-snd-soc-component-write:

=======================
snd_soc_component_write
=======================

*man snd_soc_component_write(9)*

*4.6.0-rc1*

Write register value


Synopsis
========

.. c:function:: int snd_soc_component_write( struct snd_soc_component * component, unsigned int reg, unsigned int val )

Arguments
=========

``component``
    Component to write to

``reg``
    Register to write

``val``
    Value to write to the register


Return
======

0 on success, a negative error code otherwise.
