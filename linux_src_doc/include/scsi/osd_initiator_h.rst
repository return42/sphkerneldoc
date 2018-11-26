.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/osd_initiator.h

.. _`osd_auto_detect_ver`:

osd_auto_detect_ver
===================

.. c:function:: int osd_auto_detect_ver(struct osd_dev *od, void *caps, struct osd_dev_info *odi)

    Detect the OSD version, return Unique Identification

    :param od:
        OSD target lun handle
    :type od: struct osd_dev \*

    :param caps:
        Capabilities authorizing OSD root read attributes access
    :type caps: void \*

    :param odi:
        Retrieved information uniquely identifying the osd target lun
        Note: odi->osdname must be kfreed by caller.
    :type odi: struct osd_dev_info \*

.. _`osd_auto_detect_ver.description`:

Description
-----------

Auto detects the OSD version of the OSD target and sets the \ ``od``\ 
accordingly. Meanwhile also returns the "system id" and "osd name" root
attributes which uniquely identify the OSD target. This member is usually
called by the ULD. ULD users should call \ :c:func:`osduld_device_info`\ .
This rutine allocates osd requests and memory at GFP_KERNEL level and might
sleep.

.. _`osd_start_request`:

osd_start_request
=================

.. c:function:: struct osd_request *osd_start_request(struct osd_dev *od)

    Allocate and initialize an osd_request

    :param od:
        *undescribed*
    :type od: struct osd_dev \*

.. _`osd_start_request.description`:

Description
-----------

Allocate osd_request and initialize all members to the
default/initial state.

.. _`osd_finalize_request`:

osd_finalize_request
====================

.. c:function:: int osd_finalize_request(struct osd_request *or, u8 options, const void *cap, const u8 *cap_key)

    Sign request and prepare request for execution

    :param or:
        osd_request to prepare
    :type or: struct osd_request \*

    :param options:
        combination of osd_req_options bit flags or 0.
    :type options: u8

    :param cap:
        A Pointer to an OSD_CAP_LEN bytes buffer that is received from
        The security manager as capabilities for this cdb.
    :type cap: const void \*

    :param cap_key:
        The cryptographic key used to sign the cdb/data. Can be null
        if NOSEC is used.
    :type cap_key: const u8 \*

.. _`osd_finalize_request.description`:

Description
-----------

The actual request and bios are only allocated here, so are the get_attr
buffers that will receive the returned attributes. Copy's \ ``cap``\  to cdb.
Sign the cdb/data with \ ``cap_key``\ .

.. _`osd_execute_request`:

osd_execute_request
===================

.. c:function:: int osd_execute_request(struct osd_request *or)

    Execute the request synchronously through block-layer

    :param or:
        osd_request to Executed
    :type or: struct osd_request \*

.. _`osd_execute_request.description`:

Description
-----------

Calls blk_execute_rq to q the command and waits for completion.

.. _`osd_execute_request_async`:

osd_execute_request_async
=========================

.. c:function:: int osd_execute_request_async(struct osd_request *or, osd_req_done_fn *done, void *private)

    Execute the request without waitting.

    :param or:
        - osd_request to Executed
    :type or: struct osd_request \*

    :param done:
        (Optional)         - Called at end of execution
    :type done: osd_req_done_fn \*

    :param private:
        - Will be passed to \ ``done``\  function
    :type private: void \*

.. _`osd_execute_request_async.description`:

Description
-----------

Calls blk_execute_rq_nowait to queue the command. When execution is done
optionally calls \ ``done``\  with \ ``private``\  as parameter. \ ``or->async_error``\  will
have the return code

.. _`osd_end_request`:

osd_end_request
===============

.. c:function:: void osd_end_request(struct osd_request *or)

    return osd_request to free store

    :param or:
        osd_request to free
    :type or: struct osd_request \*

.. _`osd_end_request.description`:

Description
-----------

Deallocate all osd_request resources (struct req's, BIOs, buffers, etc.)

.. This file was automatic generated / don't edit.

