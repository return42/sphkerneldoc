.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/chsc.c

.. _`chsc_error_from_response`:

chsc_error_from_response
========================

.. c:function:: int chsc_error_from_response(int response)

    convert a chsc response to an error

    :param response:
        chsc response code
    :type response: int

.. _`chsc_error_from_response.description`:

Description
-----------

Returns an appropriate Linux error code for \ ``response``\ .

.. _`chsc_ssqd`:

chsc_ssqd
=========

.. c:function:: int chsc_ssqd(struct subchannel_id schid, struct chsc_ssqd_area *ssqd)

    store subchannel QDIO data (SSQD)

    :param schid:
        id of the subchannel on which SSQD is performed
    :type schid: struct subchannel_id

    :param ssqd:
        request and response block for SSQD
    :type ssqd: struct chsc_ssqd_area \*

.. _`chsc_ssqd.description`:

Description
-----------

Returns 0 on success.

.. _`chsc_sadc`:

chsc_sadc
=========

.. c:function:: int chsc_sadc(struct subchannel_id schid, struct chsc_scssc_area *scssc, u64 summary_indicator_addr, u64 subchannel_indicator_addr)

    set adapter device controls (SADC)

    :param schid:
        id of the subchannel on which SADC is performed
    :type schid: struct subchannel_id

    :param scssc:
        request and response block for SADC
    :type scssc: struct chsc_scssc_area \*

    :param summary_indicator_addr:
        summary indicator address
    :type summary_indicator_addr: u64

    :param subchannel_indicator_addr:
        subchannel indicator address
    :type subchannel_indicator_addr: u64

.. _`chsc_sadc.description`:

Description
-----------

Returns 0 on success.

.. _`chsc_chp_vary`:

chsc_chp_vary
=============

.. c:function:: int chsc_chp_vary(struct chp_id chpid, int on)

    propagate channel-path vary operation to subchannels

    :param chpid:
        channl-path ID
    :type chpid: struct chp_id

    :param on:
        non-zero for vary online, zero for vary offline
    :type on: int

.. _`chsc_scm_info`:

chsc_scm_info
=============

.. c:function:: int chsc_scm_info(struct chsc_scm_info *scm_area, u64 token)

    store SCM information (SSI)

    :param scm_area:
        request and response block for SSI
    :type scm_area: struct chsc_scm_info \*

    :param token:
        continuation token
    :type token: u64

.. _`chsc_scm_info.description`:

Description
-----------

Returns 0 on success.

.. _`chsc_pnso_brinfo`:

chsc_pnso_brinfo
================

.. c:function:: int chsc_pnso_brinfo(struct subchannel_id schid, struct chsc_pnso_area *brinfo_area, struct chsc_brinfo_resume_token resume_token, int cnc)

    Perform Network-Subchannel Operation, Bridge Info.

    :param schid:
        id of the subchannel on which PNSO is performed
    :type schid: struct subchannel_id

    :param brinfo_area:
        request and response block for the operation
    :type brinfo_area: struct chsc_pnso_area \*

    :param resume_token:
        resume token for multiblock response
    :type resume_token: struct chsc_brinfo_resume_token

    :param cnc:
        Boolean change-notification control
    :type cnc: int

.. _`chsc_pnso_brinfo.description`:

Description
-----------

brinfo_area must be allocated by the caller with get_zeroed_page(GFP_KERNEL)

Returns 0 on success.

.. This file was automatic generated / don't edit.

