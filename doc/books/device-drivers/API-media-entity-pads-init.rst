
.. _API-media-entity-pads-init:

======================
media_entity_pads_init
======================

*man media_entity_pads_init(9)*

*4.6.0-rc1*

Initialize the entity pads


Synopsis
========

.. c:function:: int media_entity_pads_init( struct media_entity * entity, u16 num_pads, struct media_pad * pads )

Arguments
=========

``entity``
    entity where the pads belong

``num_pads``
    total number of sink and source pads

``pads``
    Array of ``num_pads`` pads.


Description
===========

The pads array is managed by the entity driver and passed to ``media_entity_pads_init`` where its pointer will be stored in the entity structure.

If no pads are needed, drivers could either directly fill ``media_entity``->``num_pads`` with 0 and ``media_entity``->``pads`` with NULL or call this function that will do the
same.

As the number of pads is known in advance, the pads array is not allocated dynamically but is managed by the entity driver. Most drivers will embed the pads array in a
driver-specific structure, avoiding dynamic allocation.

Drivers must set the direction of every pad in the pads array before calling ``media_entity_pads_init``. The function will initialize the other pads fields.
