.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/media-dev.c

.. _`fimc_pipeline_prepare`:

fimc_pipeline_prepare
=====================

.. c:function:: void fimc_pipeline_prepare(struct fimc_pipeline *p, struct media_entity *me)

    update pipeline information with subdevice pointers

    :param struct fimc_pipeline \*p:
        fimc pipeline

    :param struct media_entity \*me:
        media entity terminating the pipeline

.. _`fimc_pipeline_prepare.description`:

Description
-----------

Caller holds the graph mutex.

.. _`__subdev_set_power`:

\__subdev_set_power
===================

.. c:function:: int __subdev_set_power(struct v4l2_subdev *sd, int on)

    change power state of a single subdev

    :param struct v4l2_subdev \*sd:
        subdevice to change power state for

    :param int on:
        1 to enable power or 0 to disable

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

    :param struct fimc_pipeline \*p:
        fimc device terminating the pipeline

    :param bool on:
        true to power on, false to power off

.. _`fimc_pipeline_s_power.description`:

Description
-----------

Needs to be called with the graph mutex held.

.. _`__fimc_pipeline_enable`:

\__fimc_pipeline_enable
=======================

.. c:function:: int __fimc_pipeline_enable(struct exynos_media_pipeline *ep, struct fimc_md *fmd)

    enable power of all pipeline subdevs and the sensor clock

    :param struct exynos_media_pipeline \*ep:
        video pipeline structure

    :param struct fimc_md \*fmd:
        fimc media device

.. _`__fimc_pipeline_enable.description`:

Description
-----------

Called with the graph mutex held.

.. _`__fimc_pipeline_open`:

\__fimc_pipeline_open
=====================

.. c:function:: int __fimc_pipeline_open(struct exynos_media_pipeline *ep, struct media_entity *me, bool prepare)

    update the pipeline information, enable power of all pipeline subdevs and the sensor clock

    :param struct exynos_media_pipeline \*ep:
        fimc device terminating the pipeline

    :param struct media_entity \*me:
        media entity to start graph walk with

    :param bool prepare:
        true to walk the current pipeline and acquire all subdevs

.. _`__fimc_pipeline_open.description`:

Description
-----------

Called with the graph mutex held.

.. _`__fimc_pipeline_close`:

\__fimc_pipeline_close
======================

.. c:function:: int __fimc_pipeline_close(struct exynos_media_pipeline *ep)

    disable the sensor clock and pipeline power

    :param struct exynos_media_pipeline \*ep:
        fimc device terminating the pipeline

.. _`__fimc_pipeline_close.description`:

Description
-----------

Disable power of all subdevs and turn the external sensor clock off.

.. _`__fimc_pipeline_s_stream`:

\__fimc_pipeline_s_stream
=========================

.. c:function:: int __fimc_pipeline_s_stream(struct exynos_media_pipeline *ep, bool on)

    call \ :c:func:`s_stream`\  on pipeline subdevs

    :param struct exynos_media_pipeline \*ep:
        video pipeline structure

    :param bool on:
        passed as the \ :c:func:`s_stream`\  callback argument

.. _`__fimc_md_create_fimc_sink_links`:

\__fimc_md_create_fimc_sink_links
=================================

.. c:function:: int __fimc_md_create_fimc_sink_links(struct fimc_md *fmd, struct media_entity *source, struct v4l2_subdev *sensor, int pad, int link_mask)

    create links to all FIMC entities

    :param struct fimc_md \*fmd:
        fimc media device

    :param struct media_entity \*source:
        the source entity to create links to all fimc entities from

    :param struct v4l2_subdev \*sensor:
        sensor subdev linked to FIMC[fimc_id] entity, may be null

    :param int pad:
        the source entity pad index

    :param int link_mask:
        bitmask of the fimc devices for which link should be enabled

.. _`fimc_md_create_links`:

fimc_md_create_links
====================

.. c:function:: int fimc_md_create_links(struct fimc_md *fmd)

    create default links between registered entities

    :param struct fimc_md \*fmd:
        fimc media device

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

