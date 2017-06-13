.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/media-dev.h

.. _`fimc_sensor_info`:

struct fimc_sensor_info
=======================

.. c:type:: struct fimc_sensor_info

    image data source subdev information

.. _`fimc_sensor_info.definition`:

Definition
----------

.. code-block:: c

    struct fimc_sensor_info {
        struct fimc_source_info pdata;
        struct v4l2_async_subdev asd;
        struct v4l2_subdev *subdev;
        struct fimc_dev *host;
    }

.. _`fimc_sensor_info.members`:

Members
-------

pdata
    sensor's atrributes passed as media device's platform data

asd
    asynchronous subdev registration data structure

subdev
    image sensor v4l2 subdev

host
    fimc device the sensor is currently linked to

.. _`fimc_sensor_info.description`:

Description
-----------

This data structure applies to image sensor and the writeback subdevs.

.. _`fimc_md`:

struct fimc_md
==============

.. c:type:: struct fimc_md

    fimc media device information

.. _`fimc_md.definition`:

Definition
----------

.. code-block:: c

    struct fimc_md {
        struct fimc_csis_info csis[CSIS_MAX_ENTITIES];
        struct fimc_sensor_info sensor[FIMC_MAX_SENSORS];
        int num_sensors;
        struct fimc_camclk_info camclk[FIMC_MAX_CAMCLKS];
        struct clk  *wbclk[FIMC_MAX_WBCLKS];
        struct fimc_lite  *fimc_lite[FIMC_LITE_MAX_DEVS];
        struct fimc_dev  *fimc[FIMC_MAX_DEVS];
        struct fimc_is *fimc_is;
        bool use_isp;
        struct device *pmf;
        struct media_device media_dev;
        struct v4l2_device v4l2_dev;
        struct platform_device *pdev;
        struct fimc_pinctrl clk_provider;
        struct v4l2_async_notifier subdev_notifier;
        struct v4l2_async_subdev  *async_subdevs[FIMC_MAX_SENSORS];
        bool user_subdev_api;
        spinlock_t slock;
        struct list_head pipelines;
        struct media_graph link_setup_graph;
    }

.. _`fimc_md.members`:

Members
-------

csis
    MIPI CSIS subdevs data

sensor
    array of registered sensor subdevs

num_sensors
    actual number of registered sensors

camclk
    external sensor clock information

fimc
    array of registered fimc devices

fimc_is
    fimc-is data structure

use_isp
    set to true when FIMC-IS subsystem is used

pmf
    handle to the CAMCLK clock control FIMC helper device

media_dev
    top level media device

v4l2_dev
    top level v4l2_device holding up the subdevs

pdev
    platform device this media device is hooked up into

clk_provider
    *undescribed*

subdev_notifier
    *undescribed*

user_subdev_api
    true if subdevs are not configured by the host driver

slock
    spinlock protecting \ ``sensor``\  array

pipelines
    *undescribed*

link_setup_graph
    *undescribed*

.. This file was automatic generated / don't edit.

