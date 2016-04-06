
.. _API-media-entity-pipeline-stop:

==========================
media_entity_pipeline_stop
==========================

*man media_entity_pipeline_stop(9)*

*4.6.0-rc1*

Mark a pipeline as not streaming


Synopsis
========

.. c:function:: void media_entity_pipeline_stop( struct media_entity * entity )

Arguments
=========

``entity``
    Starting entity


Description
===========

Mark all entities connected to a given entity through enabled links, either directly or indirectly, as not streaming. The media_entity pipe field is reset to NULL.

If multiple calls to ``media_entity_pipeline_start`` have been made, the same number of calls to this function are required to mark the pipeline as not streaming.
