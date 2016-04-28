.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-pipeline-pm-use:

====================
v4l2_pipeline_pm_use
====================

*man v4l2_pipeline_pm_use(9)*

*4.6.0-rc5*

Update the use count of an entity


Synopsis
========

.. c:function:: int v4l2_pipeline_pm_use( struct media_entity * entity, int use )

Arguments
=========

``entity``
    The entity

``use``
    Use (1) or stop using (0) the entity


Description
===========

Update the use count of all entities in the pipeline and power entities
on or off accordingly.

This function is intended to be called in video node open (use == 1) and
release (use == 0). It uses struct media_entity.use_count to track the
power status. The use of this function should be paired with
``v4l2_pipeline_link_notify``.

Return 0 on success or a negative error code on failure. Powering
entities off is assumed to never fail. No failure can occur when the use
parameter is set to 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
