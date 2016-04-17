.. -*- coding: utf-8; mode: rst -*-

===============
osd_initiator.h
===============


.. _`osd_auto_detect_ver`:

osd_auto_detect_ver
===================

.. c:function:: int osd_auto_detect_ver (struct osd_dev *od, void *caps, struct osd_dev_info *odi)

    Detect the OSD version, return Unique Identification

    :param struct osd_dev \*od:
        OSD target lun handle

    :param void \*caps:
        Capabilities authorizing OSD root read attributes access

    :param struct osd_dev_info \*odi:
        Retrieved information uniquely identifying the osd target lun



.. _`osd_auto_detect_ver.note`:

Note
----

odi->osdname must be kfreed by caller.

Auto detects the OSD version of the OSD target and sets the ``od``
accordingly. Meanwhile also returns the "system id" and "osd name" root
attributes which uniquely identify the OSD target. This member is usually
called by the ULD. ULD users should call :c:func:`osduld_device_info`.
This rutine allocates osd requests and memory at GFP_KERNEL level and might
sleep.



.. _`osd_start_request`:

osd_start_request
=================

.. c:function:: struct osd_request *osd_start_request (struct osd_dev *od, gfp_t gfp)

    Allocate and initialize an osd_request

    :param struct osd_dev \*od:

        *undescribed*

    :param gfp_t gfp:
        The allocation flags to use for request allocation, and all
        subsequent allocations. This will be stored at
        osd_request->alloc_flags, can be changed by user later



.. _`osd_start_request.description`:

Description
-----------

Allocate osd_request and initialize all members to the
default/initial state.



.. _`osd_finalize_request`:

osd_finalize_request
====================

.. c:function:: int osd_finalize_request (struct osd_request *or, u8 options, const void *cap, const u8 *cap_key)

    Sign request and prepare request for execution

    :param struct osd_request \*or:
        osd_request to prepare

    :param u8 options:
        combination of osd_req_options bit flags or 0.

    :param const void \*cap:
        A Pointer to an OSD_CAP_LEN bytes buffer that is received from
        The security manager as capabilities for this cdb.

    :param const u8 \*cap_key:
        The cryptographic key used to sign the cdb/data. Can be null
        if NOSEC is used.



.. _`osd_finalize_request.description`:

Description
-----------

The actual request and bios are only allocated here, so are the get_attr
buffers that will receive the returned attributes. Copy's ``cap`` to cdb.
Sign the cdb/data with ``cap_key``\ .



.. _`osd_execute_request`:

osd_execute_request
===================

.. c:function:: int osd_execute_request (struct osd_request *or)

    Execute the request synchronously through block-layer

    :param struct osd_request \*or:
        osd_request to Executed



.. _`osd_execute_request.description`:

Description
-----------

Calls blk_execute_rq to q the command and waits for completion.



.. _`osd_execute_request_async`:

osd_execute_request_async
=========================

.. c:function:: int osd_execute_request_async (struct osd_request *or, osd_req_done_fn *done, void *private)

    Execute the request without waitting.

    :param struct osd_request \*or:
        - osd_request to Executed

    :param osd_req_done_fn \*done:
        (Optional)         - Called at end of execution

    :param void \*private:
        - Will be passed to ``done`` function



.. _`osd_execute_request_async.description`:

Description
-----------

Calls blk_execute_rq_nowait to queue the command. When execution is done
optionally calls ``done`` with ``private`` as parameter. ``or``\ ->async_error will
have the return code



.. _`osd_end_request`:

osd_end_request
===============

.. c:function:: void osd_end_request (struct osd_request *or)

    return osd_request to free store

    :param struct osd_request \*or:
        osd_request to free



.. _`osd_end_request.description`:

Description
-----------

Deallocate all osd_request resources (struct req's, BIOs, buffers, etc.)

