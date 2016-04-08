
.. _API-snd-soc-add-component-controls:

==============================
snd_soc_add_component_controls
==============================

*man snd_soc_add_component_controls(9)*

*4.6.0-rc1*

Add an array of controls to a component.


Synopsis
========

.. c:function:: int snd_soc_add_component_controls( struct snd_soc_component * component, const struct snd_kcontrol_new * controls, unsigned int num_controls )

Arguments
=========

``component``
    Component to add controls to

``controls``
    Array of controls to add

``num_controls``
    Number of elements in the array


Return
======

0 for success, else error.
