
.. _API-drm-get-connector-status-name:

=============================
drm_get_connector_status_name
=============================

*man drm_get_connector_status_name(9)*

*4.6.0-rc1*

return a string for connector status


Synopsis
========

.. c:function:: const char ⋆ drm_get_connector_status_name( enum drm_connector_status status )

Arguments
=========

``status``
    connector status to compute name of


Description
===========

In contrast to the other drm_get_⋆_name functions this one here returns a const pointer and hence is threadsafe.
