.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ti/wkup_m3_ipc.c

.. _`wkup_m3_set_mem_type`:

wkup_m3_set_mem_type
====================

.. c:function:: void wkup_m3_set_mem_type(struct wkup_m3_ipc *m3_ipc, int mem_type)

    Pass wkup_m3 which type of memory is in use

    :param struct wkup_m3_ipc \*m3_ipc:
        *undescribed*

    :param int mem_type:
        memory type value read directly from emif

.. _`wkup_m3_set_mem_type.description`:

Description
-----------

wkup_m3 must know what memory type is in use to properly suspend
and resume.

.. _`wkup_m3_set_resume_address`:

wkup_m3_set_resume_address
==========================

.. c:function:: void wkup_m3_set_resume_address(struct wkup_m3_ipc *m3_ipc, void *addr)

    Pass wkup_m3 resume address

    :param struct wkup_m3_ipc \*m3_ipc:
        *undescribed*

    :param void \*addr:
        Physical address from which resume code should execute

.. _`wkup_m3_request_pm_status`:

wkup_m3_request_pm_status
=========================

.. c:function:: int wkup_m3_request_pm_status(struct wkup_m3_ipc *m3_ipc)

    Retrieve wkup_m3 status code after suspend

    :param struct wkup_m3_ipc \*m3_ipc:
        *undescribed*

.. _`wkup_m3_request_pm_status.description`:

Description
-----------

Returns code representing the status of a low power mode transition.
0 - Successful transition
1 - Failure to transition to low power state

.. _`wkup_m3_prepare_low_power`:

wkup_m3_prepare_low_power
=========================

.. c:function:: int wkup_m3_prepare_low_power(struct wkup_m3_ipc *m3_ipc, int state)

    Request preparation for transition to low power state

    :param struct wkup_m3_ipc \*m3_ipc:
        *undescribed*

    :param int state:
        A kernel suspend state to enter, either MEM or STANDBY

.. _`wkup_m3_prepare_low_power.description`:

Description
-----------

Returns 0 if preparation was successful, otherwise returns error code

.. _`wkup_m3_finish_low_power`:

wkup_m3_finish_low_power
========================

.. c:function:: int wkup_m3_finish_low_power(struct wkup_m3_ipc *m3_ipc)

    Return m3 to reset state

    :param struct wkup_m3_ipc \*m3_ipc:
        *undescribed*

.. _`wkup_m3_finish_low_power.description`:

Description
-----------

Returns 0 if reset was successful, otherwise returns error code

.. _`wkup_m3_ipc_get`:

wkup_m3_ipc_get
===============

.. c:function:: struct wkup_m3_ipc *wkup_m3_ipc_get( void)

    Return handle to wkup_m3_ipc

    :param  void:
        no arguments

.. _`wkup_m3_ipc_get.description`:

Description
-----------

Returns NULL if the wkup_m3 is not yet available, otherwise returns
pointer to wkup_m3_ipc struct.

.. _`wkup_m3_ipc_put`:

wkup_m3_ipc_put
===============

.. c:function:: void wkup_m3_ipc_put(struct wkup_m3_ipc *m3_ipc)

    Free handle to wkup_m3_ipc returned from wkup_m3_ipc_get

    :param struct wkup_m3_ipc \*m3_ipc:
        A pointer to wkup_m3_ipc struct returned by wkup_m3_ipc_get

.. This file was automatic generated / don't edit.

