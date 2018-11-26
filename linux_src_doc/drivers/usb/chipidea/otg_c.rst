.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/otg.c

.. _`hw_read_otgsc`:

hw_read_otgsc
=============

.. c:function:: u32 hw_read_otgsc(struct ci_hdrc *ci, u32 mask)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param mask:
        bitfield mask
    :type mask: u32

.. _`hw_write_otgsc`:

hw_write_otgsc
==============

.. c:function:: void hw_write_otgsc(struct ci_hdrc *ci, u32 mask, u32 data)

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

    :param mask:
        bitfield mask
    :type mask: u32

    :param data:
        to be written
    :type data: u32

.. _`ci_otg_role`:

ci_otg_role
===========

.. c:function:: enum ci_role ci_otg_role(struct ci_hdrc *ci)

    pick role based on ID pin state

    :param ci:
        the controller
    :type ci: struct ci_hdrc \*

.. _`hw_wait_vbus_lower_bsv`:

hw_wait_vbus_lower_bsv
======================

.. c:function:: int hw_wait_vbus_lower_bsv(struct ci_hdrc *ci)

    than OTGSC_BSV before connecting to host.

    :param ci:
        the controller
    :type ci: struct ci_hdrc \*

.. _`hw_wait_vbus_lower_bsv.description`:

Description
-----------

This function returns an error code if timeout

.. _`ci_otg_work`:

ci_otg_work
===========

.. c:function:: void ci_otg_work(struct work_struct *work)

    perform otg (vbus/id) event handle

    :param work:
        work struct
    :type work: struct work_struct \*

.. _`ci_hdrc_otg_init`:

ci_hdrc_otg_init
================

.. c:function:: int ci_hdrc_otg_init(struct ci_hdrc *ci)

    initialize otg struct ci: the controller

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. _`ci_hdrc_otg_destroy`:

ci_hdrc_otg_destroy
===================

.. c:function:: void ci_hdrc_otg_destroy(struct ci_hdrc *ci)

    destroy otg struct ci: the controller

    :param ci:
        *undescribed*
    :type ci: struct ci_hdrc \*

.. This file was automatic generated / don't edit.

