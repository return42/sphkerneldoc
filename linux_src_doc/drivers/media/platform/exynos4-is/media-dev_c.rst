.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/media-dev.c

.. _`fimc_pipeline_prepare`:

fimc_pipeline_prepare
=====================

.. c:function:: void fimc_pipeline_prepare(struct fimc_pipeline *p, struct media_entity *me)

    update pipeline information with subdevice pointers

    :param p:
        fimc pipeline
    :type p: struct fimc_pipeline \*

    :param me:
        media entity terminating the pipeline
    :type me: struct media_entity \*

.. _`fimc_pipeline_prepare.description`:

Description
-----------

Caller holds the graph mutex.

.. _`__subdev_set_power`:

\__subdev_set_power
===================

.. c:function:: int __subdev_set_power(struct v4l2_subdev *sd, int on)

    change power state of a single subdev

    :param sd:
        subdevice to change power state for
    :type sd: struct v4l2_subdev \*

    :param on:
        1 to enable power or 0 to disable
    :type on: int

.. _`__subdev_set_power.description`:

Description
-----------

Return result of s_power subdev operation or -ENXIO if sd argument
is NULL. Return 0 if the subdevice does not implement s_power.

.. _`fimc_pipeline_s_power`:

fimc_pipeline_s_power
=====================

.. c:function:: int fimc_pipeline_s_power(struct fimc_pipeline *p, bool on)

    change power state of all pipeline subdevs

    :param p:
        fimc device terminating the pipeline
    :type p: struct fimc_pipeline \*

    :param on:
        true to power on, false to power off
    :type on: bool

.. _`fimc_pipeline_s_power.description`:

Description
-----------

Needs to be called with the graph mutex held.

.. _`__fimc_pipeline_enable`:

\__fimc_pipeline_enable
=======================

.. c:function:: int __fimc_pipeline_enable(struct exynos_media_pipeline *ep, struct fimc_md *fmd)

    enable power of all pipeline subdevs and the sensor clock

    :param ep:
        video pipeline structure
    :type ep: struct exynos_media_pipeline \*

    :param fmd:
        fimc media device
    :type fmd: struct fimc_md \*

.. _`__fimc_pipeline_enable.description`:

Description
-----------

Called with the graph mutex held.

.. _`__fimc_pipeline_open`:

\__fimc_pipeline_open
=====================

.. c:function:: int __fimc_pipeline_open(struct exynos_media_pipeline *ep, struct media_entity *me, bool prepare)

    update the pipeline information, enable power of all pipeline subdevs and the sensor clock

    :param ep:
        fimc device terminating the pipeline
    :type ep: struct exynos_media_pipeline \*

    :param me:
        media entity to start graph walk with
    :type me: struct media_entity \*

    :param prepare:
        true to walk the current pipeline and acquire all subdevs
    :type prepare: bool

.. _`__fimc_pipeline_open.description`:

Description
-----------

Called with the graph mutex held.

.. _`__fimc_pipeline_close`:

\__fimc_pipeline_close
======================

.. c:function:: int __fimc_pipeline_close(struct exynos_media_pipeline *ep)

    disable the sensor clock and pipeline power

    :param ep:
        fimc device terminating the pipeline
    :type ep: struct exynos_media_pipeline \*

.. _`__fimc_pipeline_close.description`:

Description
-----------

Disable power of all subdevs and turn the external sensor clock off.

.. _`__fimc_pipeline_s_stream`:

\__fimc_pipeline_s_stream
=========================

.. c:function:: int __fimc_pipeline_s_stream(struct exynos_media_pipeline *ep, bool on)

    call \ :c:func:`s_stream`\  on pipeline subdevs

    :param ep:
        video pipeline structure
    :type ep: struct exynos_media_pipeline \*

    :param on:
        passed as the \ :c:func:`s_stream`\  callback argument
    :type on: bool

.. _`__fimc_md_create_fimc_sink_links`:

\__fimc_md_create_fimc_sink_links
=================================

.. c:function:: int __fimc_md_create_fimc_sink_links(struct fimc_md *fmd, struct media_entity *source, struct v4l2_subdev *sensor, int pad, int link_mask)

    create links to all FIMC entities

    :param fmd:
        fimc media device
    :type fmd: struct fimc_md \*

    :param source:
        the source entity to create links to all fimc entities from
    :type source: struct media_entity \*

    :param sensor:
        sensor subdev linked to FIMC[fimc_id] entity, may be null
    :type sensor: struct v4l2_subdev \*

    :param pad:
        the source entity pad index
    :type pad: int

    :param link_mask:
        bitmask of the fimc devices for which link should be enabled
    :type link_mask: int

.. _`fimc_md_create_links`:

fimc_md_create_links
====================

.. c:function:: int fimc_md_create_links(struct fimc_md *fmd)

    create default links between registered entities

    :param fmd:
        fimc media device
    :type fmd: struct fimc_md \*

.. _`fimc_md_create_links.description`:

Description
-----------

Parallel interface sensor entities are connected directly to FIMC capture
entities. The sensors using MIPI CSIS bus are connected through immutable
link with CSI receiver entity specified by mux_id. Any registered CSIS
entity has a link to each registered FIMC capture entity. Enabled links
are created by default between each subsequent registered sensor and
subsequent FIMC capture entity. The number of default active links is
determined by the number of available sensors or FIMC entities,
whichever is less.

.. This file was automatic generated / don't edit.

