
.. _API---media-entity-pipeline-start:

=============================
__media_entity_pipeline_start
=============================

*man __media_entity_pipeline_start(9)*

*4.6.0-rc1*

Mark a pipeline as streaming


Synopsis
========

.. c:function:: int __media_entity_pipeline_start( struct media_entity * entity, struct media_pipeline * pipe )

Arguments
=========

``entity``
    Starting entity

``pipe``
    Media pipeline to be assigned to all entities in the pipeline.


Note
====

This is the non-locking version of ``media_entity_pipeline_start``
