.. -*- coding: utf-8; mode: rst -*-

===========
media-dev.h
===========



.. _xref_struct_fimc_sensor_info:

struct fimc_sensor_info
=======================

.. c:type:: struct fimc_sensor_info

    image data source subdev information



Definition
----------

.. code-block:: c

  struct fimc_sensor_info {
    struct fimc_source_info pdata;
    struct v4l2_async_subdev asd;
    struct v4l2_subdev * subdev;
    struct fimc_dev * host;
  };



Members
-------

:``struct fimc_source_info pdata``:
    sensor's atrributes passed as media device's platform data

:``struct v4l2_async_subdev asd``:
    asynchronous subdev registration data structure

:``struct v4l2_subdev * subdev``:
    image sensor v4l2 subdev

:``struct fimc_dev * host``:
    fimc device the sensor is currently linked to




Description
-----------

This data structure applies to image sensor and the writeback subdevs.




.. _xref_struct_fimc_md:

struct fimc_md
==============

.. c:type:: struct fimc_md

    fimc media device information



Definition
----------

.. code-block:: c

  struct fimc_md {
    struct fimc_csis_info csis[CSIS_MAX_ENTITIES];
    struct fimc_sensor_info sensor[FIMC_MAX_SENSORS];
    int num_sensors;
    struct fimc_camclk_info camclk[FIMC_MAX_CAMCLKS];
    struct fimc_dev * fimc[FIMC_MAX_DEVS];
    struct fimc_is * fimc_is;
    bool use_isp;
    struct device * pmf;
    struct media_device media_dev;
    struct v4l2_device v4l2_dev;
    struct platform_device * pdev;
    bool user_subdev_api;
    spinlock_t slock;
  };



Members
-------

:``struct fimc_csis_info csis[CSIS_MAX_ENTITIES]``:
    MIPI CSIS subdevs data

:``struct fimc_sensor_info sensor[FIMC_MAX_SENSORS]``:
    array of registered sensor subdevs

:``int num_sensors``:
    actual number of registered sensors

:``struct fimc_camclk_info camclk[FIMC_MAX_CAMCLKS]``:
    external sensor clock information

:``struct fimc_dev * fimc[FIMC_MAX_DEVS]``:
    array of registered fimc devices

:``struct fimc_is * fimc_is``:
    fimc-is data structure

:``bool use_isp``:
    set to true when FIMC-IS subsystem is used

:``struct device * pmf``:
    handle to the CAMCLK clock control FIMC helper device

:``struct media_device media_dev``:
    top level media device

:``struct v4l2_device v4l2_dev``:
    top level v4l2_device holding up the subdevs

:``struct platform_device * pdev``:
    platform device this media device is hooked up into

:``bool user_subdev_api``:
    true if subdevs are not configured by the host driver

:``spinlock_t slock``:
    spinlock protecting **sensor** array



