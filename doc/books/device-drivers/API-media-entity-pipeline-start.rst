.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-pipeline-start:

===========================
media_entity_pipeline_start
===========================

*man media_entity_pipeline_start(9)*

*4.6.0-rc5*

Mark a pipeline as streaming


Synopsis
========

.. c:function:: int media_entity_pipeline_start( struct media_entity * entity, struct media_pipeline * pipe )

Arguments
=========

``entity``
    Starting entity

``pipe``
    Media pipeline to be assigned to all entities in the pipeline.


Description
===========

Mark all entities connected to a given entity through enabled links,
either directly or indirectly, as streaming. The given pipeline object
is assigned to every entity in the pipeline and stored in the
media_entity pipe field.

Calls to this function can be nested, in which case the same number of
``media_entity_pipeline_stop`` calls will be required to stop streaming.
The pipeline pointer must be identical for all nested calls to
``media_entity_pipeline_start``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
