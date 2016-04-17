.. -*- coding: utf-8; mode: rst -*-

======================
intel_telemetry_core.c
======================


.. _`telemetry_update_events`:

telemetry_update_events
=======================

.. c:function:: int telemetry_update_events (struct telemetry_evtconfig pss_evtconfig, struct telemetry_evtconfig ioss_evtconfig)

    Update telemetry Configuration

    :param struct telemetry_evtconfig pss_evtconfig:
        IOSS related config. No change if num_evts = 0.

    :param struct telemetry_evtconfig ioss_evtconfig:

        *undescribed*



.. _`telemetry_update_events.description`:

Description
-----------

This API updates the IOSS & PSS Telemetry configuration. Old config
is overwritten. Call telemetry_reset_events when logging is over



.. _`telemetry_update_events.all-sample-period-values-should-be-in-the-form-of`:

All sample period values should be in the form of
-------------------------------------------------

bits[6:3] -> value; bits [0:2]-> Exponent; Period = (Value \*16^Exponent)



.. _`telemetry_update_events.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_set_sampling_period`:

telemetry_set_sampling_period
=============================

.. c:function:: int telemetry_set_sampling_period (u8 pss_period, u8 ioss_period)

    Sets the IOSS & PSS sampling period

    :param u8 pss_period:
        placeholder for PSS Period to be set.
        Set to 0 if not required to be updated

    :param u8 ioss_period:
        placeholder for IOSS Period to be set
        Set to 0 if not required to be updated



.. _`telemetry_set_sampling_period.all-values-should-be-in-the-form-of`:

All values should be in the form of
-----------------------------------

bits[6:3] -> value; bits [0:2]-> Exponent; Period = (Value \*16^Exponent)



.. _`telemetry_set_sampling_period.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_get_sampling_period`:

telemetry_get_sampling_period
=============================

.. c:function:: int telemetry_get_sampling_period (u8 *pss_min_period, u8 *pss_max_period, u8 *ioss_min_period, u8 *ioss_max_period)

    Get IOSS & PSS min & max sampling period

    :param u8 \*pss_min_period:
        placeholder for PSS Min Period supported

    :param u8 \*pss_max_period:
        placeholder for PSS Max Period supported

    :param u8 \*ioss_min_period:
        placeholder for IOSS Min Period supported

    :param u8 \*ioss_max_period:
        placeholder for IOSS Max Period supported



.. _`telemetry_get_sampling_period.all-values-should-be-in-the-form-of`:

All values should be in the form of
-----------------------------------

bits[6:3] -> value; bits [0:2]-> Exponent; Period = (Value \*16^Exponent)



.. _`telemetry_get_sampling_period.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_reset_events`:

telemetry_reset_events
======================

.. c:function:: int telemetry_reset_events ( void)

    Restore the IOSS & PSS configuration to default

    :param void:
        no arguments



.. _`telemetry_reset_events.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_get_eventconfig`:

telemetry_get_eventconfig
=========================

.. c:function:: int telemetry_get_eventconfig (struct telemetry_evtconfig *pss_evtconfig, struct telemetry_evtconfig *ioss_evtconfig, int pss_len, int ioss_len)

    Returns the pss and ioss events enabled

    :param struct telemetry_evtconfig \*pss_evtconfig:
        Pointer to IOSS related configuration.

    :param struct telemetry_evtconfig \*ioss_evtconfig:

        *undescribed*

    :param int pss_len:
        Number of u32 elements allocated for pss_evtconfig array

    :param int ioss_len:
        Number of u32 elements allocated for ioss_evtconfig array



.. _`telemetry_get_eventconfig.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_add_events`:

telemetry_add_events
====================

.. c:function:: int telemetry_add_events (u8 num_pss_evts, u8 num_ioss_evts, u32 *pss_evtmap, u32 *ioss_evtmap)

    Add IOSS & PSS configuration to existing settings.

    :param u8 num_pss_evts:
        Number of PSS Events (<29) in pss_evtmap. Can be 0.

    :param u8 num_ioss_evts:
        Number of IOSS Events (<29) in ioss_evtmap. Can be 0.

    :param u32 \*pss_evtmap:
        Array of PSS Event-IDs to Enable

    :param u32 \*ioss_evtmap:
        Array of PSS Event-IDs to Enable



.. _`telemetry_add_events.description`:

Description
-----------

Events are appended to Old Configuration. In case of total events > 28, it
returns error. Call telemetry_reset_events to reset after eventlog done



.. _`telemetry_add_events.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_read_events`:

telemetry_read_events
=====================

.. c:function:: int telemetry_read_events (enum telemetry_unit telem_unit, struct telemetry_evtlog *evtlog, int len)

    Fetches samples as specified by evtlog.telem_evt_id

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param struct telemetry_evtlog \*evtlog:
        Array of telemetry_evtlog structs to fill data
        evtlog.telem_evt_id specifies the ids to read

    :param int len:
        Length of array of evtlog



.. _`telemetry_read_events.return`:

Return
------

number of eventlogs read for success, < 0 for failure



.. _`telemetry_raw_read_events`:

telemetry_raw_read_events
=========================

.. c:function:: int telemetry_raw_read_events (enum telemetry_unit telem_unit, struct telemetry_evtlog *evtlog, int len)

    Fetch samples specified by evtlog.telem_evt_id

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param struct telemetry_evtlog \*evtlog:
        Array of telemetry_evtlog structs to fill data
        evtlog.telem_evt_id specifies the ids to read

    :param int len:
        Length of array of evtlog



.. _`telemetry_raw_read_events.description`:

Description
-----------

The caller must take care of locking in this case.



.. _`telemetry_raw_read_events.return`:

Return
------

number of eventlogs read for success, < 0 for failure



.. _`telemetry_read_eventlog`:

telemetry_read_eventlog
=======================

.. c:function:: int telemetry_read_eventlog (enum telemetry_unit telem_unit, struct telemetry_evtlog *evtlog, int len)

    Fetch the Telemetry log from PSS or IOSS

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param struct telemetry_evtlog \*evtlog:
        Array of telemetry_evtlog structs to fill data

    :param int len:
        Length of array of evtlog



.. _`telemetry_read_eventlog.return`:

Return
------

number of eventlogs read for success, < 0 for failure



.. _`telemetry_raw_read_eventlog`:

telemetry_raw_read_eventlog
===========================

.. c:function:: int telemetry_raw_read_eventlog (enum telemetry_unit telem_unit, struct telemetry_evtlog *evtlog, int len)

    Fetch the Telemetry log from PSS or IOSS

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param struct telemetry_evtlog \*evtlog:
        Array of telemetry_evtlog structs to fill data

    :param int len:
        Length of array of evtlog



.. _`telemetry_raw_read_eventlog.description`:

Description
-----------

The caller must take care of locking in this case.



.. _`telemetry_raw_read_eventlog.return`:

Return
------

number of eventlogs read for success, < 0 for failure



.. _`telemetry_get_trace_verbosity`:

telemetry_get_trace_verbosity
=============================

.. c:function:: int telemetry_get_trace_verbosity (enum telemetry_unit telem_unit, u32 *verbosity)

    Get the IOSS & PSS Trace verbosity

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param u32 \*verbosity:
        Pointer to return Verbosity



.. _`telemetry_get_trace_verbosity.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_set_trace_verbosity`:

telemetry_set_trace_verbosity
=============================

.. c:function:: int telemetry_set_trace_verbosity (enum telemetry_unit telem_unit, u32 verbosity)

    Update the IOSS & PSS Trace verbosity

    :param enum telemetry_unit telem_unit:
        Specify whether IOSS or PSS Read

    :param u32 verbosity:
        Verbosity to set



.. _`telemetry_set_trace_verbosity.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_set_pltdata`:

telemetry_set_pltdata
=====================

.. c:function:: int telemetry_set_pltdata (struct telemetry_core_ops *ops, struct telemetry_plt_config *pltconfig)

    Set the platform specific Data

    :param struct telemetry_core_ops \*ops:
        Pointer to ops structure

    :param struct telemetry_plt_config \*pltconfig:
        Platform config data



.. _`telemetry_set_pltdata.description`:

Description
-----------

Usage by other than telemetry pltdrv module is invalid



.. _`telemetry_set_pltdata.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_clear_pltdata`:

telemetry_clear_pltdata
=======================

.. c:function:: int telemetry_clear_pltdata ( void)

    Clear the platform specific Data

    :param void:
        no arguments



.. _`telemetry_clear_pltdata.description`:

Description
-----------


Usage by other than telemetry pltdrv module is invalid



.. _`telemetry_clear_pltdata.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_pltconfig_valid`:

telemetry_pltconfig_valid
=========================

.. c:function:: int telemetry_pltconfig_valid ( void)

    Checkif platform config is valid

    :param void:
        no arguments



.. _`telemetry_pltconfig_valid.description`:

Description
-----------


Usage by other than telemetry module is invalid



.. _`telemetry_pltconfig_valid.return`:

Return
------

0 success, < 0 for failure



.. _`telemetry_get_evtname`:

telemetry_get_evtname
=====================

.. c:function:: int telemetry_get_evtname (enum telemetry_unit telem_unit, const char **name, int len)

    Checkif platform config is valid

    :param enum telemetry_unit telem_unit:
        Telemetry Unit to check

    :param const char \*\*name:
        Array of character pointers to contain name

    :param int len:
        length of array name provided by user



.. _`telemetry_get_evtname.description`:

Description
-----------

Usage by other than telemetry debugfs module is invalid



.. _`telemetry_get_evtname.return`:

Return
------

0 success, < 0 for failure

