.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/chp.c

.. _`chp_get_sch_opm`:

chp_get_sch_opm
===============

.. c:function:: u8 chp_get_sch_opm(struct subchannel *sch)

    return opm for subchannel

    :param struct subchannel \*sch:
        subchannel

.. _`chp_get_sch_opm.description`:

Description
-----------

Calculate and return the operational path mask (opm) based on the chpids
used by the subchannel and the status of the associated channel-paths.

.. _`chp_is_registered`:

chp_is_registered
=================

.. c:function:: int chp_is_registered(struct chp_id chpid)

    check if a channel-path is registered

    :param struct chp_id chpid:
        channel-path ID

.. _`chp_is_registered.description`:

Description
-----------

Return non-zero if a channel-path with the given chpid is registered,
zero otherwise.

.. _`chp_update_desc`:

chp_update_desc
===============

.. c:function:: int chp_update_desc(struct channel_path *chp)

    update channel-path description

    :param struct channel_path \*chp:
        channel-path

.. _`chp_update_desc.description`:

Description
-----------

Update the channel-path description of the specified channel-path
including channel measurement related information.
Return zero on success, non-zero otherwise.

.. _`chp_new`:

chp_new
=======

.. c:function:: int chp_new(struct chp_id chpid)

    register a new channel-path

    :param struct chp_id chpid:
        channel-path ID

.. _`chp_new.description`:

Description
-----------

Create and register data structure representing new channel-path. Return
zero on success, non-zero otherwise.

.. _`chp_get_chp_desc`:

chp_get_chp_desc
================

.. c:function:: struct channel_path_desc *chp_get_chp_desc(struct chp_id chpid)

    return newly allocated channel-path description

    :param struct chp_id chpid:
        channel-path ID

.. _`chp_get_chp_desc.description`:

Description
-----------

On success return a newly allocated copy of the channel-path description
data associated with the given channel-path ID. Return \ ``NULL``\  on error.

.. _`chp_process_crw`:

chp_process_crw
===============

.. c:function:: void chp_process_crw(struct crw *crw0, struct crw *crw1, int overflow)

    process channel-path status change

    :param struct crw \*crw0:
        channel report-word to handler

    :param struct crw \*crw1:
        second channel-report word (always NULL)

    :param int overflow:
        crw overflow indication

.. _`chp_process_crw.description`:

Description
-----------

Handle channel-report-words indicating that the status of a channel-path
has changed.

.. _`chp_info_get_status`:

chp_info_get_status
===================

.. c:function:: int chp_info_get_status(struct chp_id chpid)

    retrieve configure status of a channel-path

    :param struct chp_id chpid:
        channel-path ID

.. _`chp_info_get_status.description`:

Description
-----------

On success, return 0 for standby, 1 for configured, 2 for reserved,
3 for not recognized. Return negative error code on error.

.. _`chp_cfg_schedule`:

chp_cfg_schedule
================

.. c:function:: void chp_cfg_schedule(struct chp_id chpid, int configure)

    schedule chpid configuration request

    :param struct chp_id chpid:
        channel-path ID

    :param int configure:
        Non-zero for configure, zero for deconfigure

.. _`chp_cfg_schedule.description`:

Description
-----------

Schedule a channel-path configuration/deconfiguration request.

.. _`chp_cfg_cancel_deconfigure`:

chp_cfg_cancel_deconfigure
==========================

.. c:function:: void chp_cfg_cancel_deconfigure(struct chp_id chpid)

    cancel chpid deconfiguration request

    :param struct chp_id chpid:
        channel-path ID

.. _`chp_cfg_cancel_deconfigure.description`:

Description
-----------

Cancel an active channel-path deconfiguration request if it has not yet
been performed.

.. This file was automatic generated / don't edit.

