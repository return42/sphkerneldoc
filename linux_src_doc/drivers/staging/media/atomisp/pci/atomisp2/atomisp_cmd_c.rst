.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/pci/atomisp2/atomisp_cmd.c

.. _`css_input_resolution_changed`:

css_input_resolution_changed
============================

.. c:function:: int css_input_resolution_changed(struct atomisp_sub_device *asd, struct v4l2_mbus_framefmt *ffmt)

    :param struct atomisp_sub_device \*asd:
        *undescribed*

    :param struct v4l2_mbus_framefmt \*ffmt:
        *undescribed*

.. _`css_input_resolution_changed.description`:

Description
-----------

Update params like CSS RAW binning, 2ppc mode and pp_input
which depend on input size, but are not automatically
handled in CSS when the input resolution is changed.

.. This file was automatic generated / don't edit.

