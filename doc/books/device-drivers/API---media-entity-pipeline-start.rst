.. -*- coding: utf-8; mode: rst -*-

.. _API---media-entity-pipeline-start:

=============================
__media_entity_pipeline_start
=============================

*man __media_entity_pipeline_start(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
