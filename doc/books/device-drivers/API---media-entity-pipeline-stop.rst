
.. _API---media-entity-pipeline-stop:

============================
__media_entity_pipeline_stop
============================

*man __media_entity_pipeline_stop(9)*

*4.6.0-rc1*

Mark a pipeline as not streaming


Synopsis
========

.. c:function:: void __media_entity_pipeline_stop( struct media_entity * entity )

Arguments
=========

``entity``
    Starting entity


Note
====

This is the non-locking version of ``media_entity_pipeline_stop``
