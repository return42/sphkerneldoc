.. -*- coding: utf-8; mode: rst -*-

=====
otg.c
=====


.. _`hw_read_otgsc`:

hw_read_otgsc
=============

.. c:function:: u32 hw_read_otgsc (struct ci_hdrc *ci, u32 mask)

    :param struct ci_hdrc \*ci:

        *undescribed*

    :param u32 mask:
        bitfield mask



.. _`hw_write_otgsc`:

hw_write_otgsc
==============

.. c:function:: void hw_write_otgsc (struct ci_hdrc *ci, u32 mask, u32 data)

    :param struct ci_hdrc \*ci:

        *undescribed*

    :param u32 mask:
        bitfield mask

    :param u32 data:
        to be written



.. _`ci_otg_role`:

ci_otg_role
===========

.. c:function:: enum ci_role ci_otg_role (struct ci_hdrc *ci)

    pick role based on ID pin state

    :param struct ci_hdrc \*ci:
        the controller



.. _`ci_otg_work`:

ci_otg_work
===========

.. c:function:: void ci_otg_work (struct work_struct *work)

    perform otg (vbus/id) event handle

    :param struct work_struct \*work:
        work struct



.. _`ci_hdrc_otg_init`:

ci_hdrc_otg_init
================

.. c:function:: int ci_hdrc_otg_init (struct ci_hdrc *ci)

    initialize otg struct

    :param struct ci_hdrc \*ci:

        *undescribed*



.. _`ci_hdrc_otg_init.ci`:

ci
--

the controller



.. _`ci_hdrc_otg_destroy`:

ci_hdrc_otg_destroy
===================

.. c:function:: void ci_hdrc_otg_destroy (struct ci_hdrc *ci)

    destroy otg struct

    :param struct ci_hdrc \*ci:

        *undescribed*



.. _`ci_hdrc_otg_destroy.ci`:

ci
--

the controller

