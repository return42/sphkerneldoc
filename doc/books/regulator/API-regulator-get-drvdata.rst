
.. _API-regulator-get-drvdata:

=====================
regulator_get_drvdata
=====================

*man regulator_get_drvdata(9)*

*4.6.0-rc1*

get regulator driver data


Synopsis
========

.. c:function:: void ⋆ regulator_get_drvdata( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator


Description
===========

Get regulator driver private data. This call can be used in the consumer driver context when non API regulator specific functions need to be called.
