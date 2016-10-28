.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/davinci_vpfe/vpfe_video.c

.. _`vpfe_video_validate_pipeline`:

vpfe_video_validate_pipeline
============================

.. c:function:: int vpfe_video_validate_pipeline(struct vpfe_pipeline *pipe)

    discrepancies.

    :param struct vpfe_pipeline \*pipe:
        *undescribed*

.. _`vpfe_video_validate_pipeline.description`:

Description
-----------

Return 0 if all formats match, or -EPIPE if at least one link is found with
different formats on its two ends.

.. This file was automatic generated / don't edit.

